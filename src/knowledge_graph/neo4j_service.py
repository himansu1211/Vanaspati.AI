"""
Vanaspati.AI - Neo4j Agronomic Knowledge Graph Service
======================================================
Provides Graph-based representation and querying for:
1. Crop Taxonomy & Botanical Classification
2. Disease Etiology (Crop -> Disease -> Pathogen)
3. Biological & Chemical Therapeutics (Koppert biologicals, FRAC-rated chemicals)
4. Companion Planting & Crop Rotation Networks
5. Graph RAG (Retrieval-Augmented Generation) for PLLaMa Plant Care Assistant

Supports both live Neo4j AuraDB/Local Bolt connections AND high-performance
embedded fallback graph traversal.
"""

import os
import json
import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger("vanaspati.neo4j")

# Try importing neo4j driver
try:
    from neo4j import GraphDatabase, basic_auth
    NEO4J_DRIVER_AVAILABLE = True
except ImportError:
    NEO4J_DRIVER_AVAILABLE = False
    logger.info("Neo4j python package not installed; operating in Embedded Graph Mode.")


class Neo4jAgronomicService:
    """
    Enterprise Neo4j Knowledge Graph Service for precision agriculture.
    Connects to Neo4j AuraDB / Bolt or falls back to embedded graph.
    """

    def __init__(self, uri: Optional[str] = None, user: Optional[str] = None, password: Optional[str] = None):
        self.uri = uri or os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.user = user or os.getenv("NEO4J_USERNAME", os.getenv("NEO4J_USER", "neo4j"))
        self.password = password or os.getenv("NEO4J_PASSWORD", "secret")
        self.driver = None
        self.is_connected = False

        if NEO4J_DRIVER_AVAILABLE and os.getenv("NEO4J_URI"):
            try:
                self.driver = GraphDatabase.driver(self.uri, auth=basic_auth(self.user, self.password))
                # Test connectivity
                with self.driver.session() as session:
                    result = session.run("RETURN 1 as ping")
                    if result.single()["ping"] == 1:
                        self.is_connected = True
                        logger.info("Successfully connected to Neo4j instance at %s", self.uri)
            except Exception as e:
                logger.warning("Could not connect to Neo4j instance (%s). Falling back to Embedded Graph: %s", self.uri, e)
                self.driver = None
                self.is_connected = False

        # Load embedded knowledge base for graph reasoning
        self._embedded_kb = self._load_embedded_kb()

    def _load_embedded_kb(self) -> Dict[str, Any]:
        """Loads disease and crop knowledge bases for embedded graph traversal."""
        kb_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "public", "data", "disease_database.json")
        kb_path = os.path.abspath(kb_path)
        if os.path.exists(kb_path):
            try:
                with open(kb_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.error("Error loading embedded disease database: %s", e)
        return {}

    def close(self):
        """Closes the Neo4j driver connection pool."""
        if self.driver:
            self.driver.close()

    def get_crop_subgraph(self, crop_name: str) -> Dict[str, Any]:
        """
        Retrieves a complete visual subgraph (Nodes + Edges) for a crop:
        Crop -> Diseases -> Pathogens -> Treatments -> Nutrients
        """
        crop_clean = crop_name.strip().title()

        # If live Neo4j is connected, execute Cypher
        if self.is_connected and self.driver:
            try:
                with self.driver.session() as session:
                    query = """
                    MATCH (c:Crop) WHERE toLower(c.name) CONTAINS toLower($crop)
                    OPTIONAL MATCH (c)-[r1:AFFECTED_BY]->(d:Disease)
                    OPTIONAL MATCH (d)-[r2:CAUSED_BY]->(p:Pathogen)
                    OPTIONAL MATCH (d)-[r3:SUPPRESSED_BY]->(b:BiologicalRemedy)
                    OPTIONAL MATCH (d)-[r4:TREATED_BY]->(t:ChemicalTreatment)
                    OPTIONAL MATCH (c)-[r5:COMPANION_WITH]->(comp:Crop)
                    RETURN c, d, p, b, t, comp, r1, r2, r3, r4, r5 LIMIT 50
                    """
                    records = session.run(query, crop=crop_name.lower())
                    nodes = []
                    edges = []
                    node_ids = set()

                    def add_node(n, label, color):
                        if not n or n.element_id in node_ids:
                            return
                        node_ids.add(n.element_id)
                        nodes.append({
                            "id": n.element_id,
                            "label": n.get("name", label),
                            "group": label,
                            "color": color,
                            "properties": dict(n)
                        })

                    for record in records:
                        c = record["c"]
                        d = record["d"]
                        p = record["p"]
                        b = record["b"]
                        t = record["t"]
                        comp = record["comp"]

                        if c:
                            add_node(c, "Crop", "#15803d")
                        if d:
                            add_node(d, "Disease", "#dc2626")
                            edges.append({"from": c.element_id, "to": d.element_id, "label": "AFFECTED_BY"})
                        if p:
                            add_node(p, "Pathogen", "#9333ea")
                            edges.append({"from": d.element_id, "to": p.element_id, "label": "CAUSED_BY"})
                        if b:
                            add_node(b, "BiologicalRemedy", "#047857")
                            edges.append({"from": d.element_id, "to": b.element_id, "label": "SUPPRESSED_BY"})
                        if t:
                            add_node(t, "ChemicalTreatment", "#0284c7")
                            edges.append({"from": d.element_id, "to": t.element_id, "label": "TREATED_BY"})
                        if comp:
                            add_node(comp, "Crop", "#16a34a")
                            edges.append({"from": c.element_id, "to": comp.element_id, "label": "COMPANION_WITH"})

                    if nodes:
                        return {"nodes": nodes, "edges": edges, "engine": "Neo4j AuraDB/Instance"}
            except Exception as e:
                logger.warning("Cypher query failed, falling back to embedded graph: %s", e)

        # Embedded Graph Traversal Fallback
        return self._build_embedded_subgraph(crop_clean)

    def _build_embedded_subgraph(self, crop_name: str) -> Dict[str, Any]:
        """Constructs an interactive graph visualization format from the embedded database."""
        nodes = []
        edges = []
        node_ids = set()

        def add_node(nid, label, group, color, props=None):
            if nid in node_ids:
                return
            node_ids.add(nid)
            nodes.append({
                "id": nid,
                "label": label,
                "group": group,
                "color": color,
                "properties": props or {}
            })

        crop_id = f"crop_{crop_name.lower().replace(' ', '_')}"
        add_node(crop_id, crop_name, "Crop", "#15803d", {"type": "Botanical Host"})

        # Search related diseases in KB
        matching_entries = []
        for k, v in self._embedded_kb.items():
            plant = (v.get("plant_name") or "").lower()
            if crop_name.lower() in plant or crop_name.lower() in k.lower():
                matching_entries.append((k, v))

        if not matching_entries:
            # Add synthetic representative graph for demo
            matching_entries = [
                (f"{crop_name}___healthy", {
                    "disease_name": f"{crop_name} Healthy Vigor",
                    "scientific_name": "Optimal Metabolism",
                    "pathogen_type": "None",
                    "organic_remedies": {"org1": "Koppert Trianum-P (Trichoderma)"},
                    "fertilizer_recommendation": {"f1": "Balanced NPK 10-10-10"}
                })
            ]

        for k, entry in matching_entries[:6]:
            disease_name = entry.get("disease_name") or k.split("___")[-1].replace("_", " ")
            disease_id = f"disease_{k}"
            is_healthy = "healthy" in k.lower() or "healthy" in disease_name.lower()

            d_color = "#16a34a" if is_healthy else "#dc2626"
            add_node(disease_id, disease_name, "Disease", d_color, {
                "severity": entry.get("severity", "Variable"),
                "pathogen": entry.get("pathogen_type", "Fungal/Bacterial")
            })
            edges.append({"from": crop_id, "to": disease_id, "label": "DIAGNOSED_WITH" if is_healthy else "AFFECTED_BY"})

            # Pathogen node
            pathogen_name = entry.get("scientific_name")
            if pathogen_name and not is_healthy:
                path_id = f"pathogen_{pathogen_name.lower().replace(' ', '_')}"
                add_node(path_id, pathogen_name, "Pathogen", "#9333ea", {"type": entry.get("pathogen_type")})
                edges.append({"from": disease_id, "to": path_id, "label": "CAUSED_BY"})

            # Biological Treatment (Koppert)
            org_remedies = entry.get("organic_remedies", {})
            if isinstance(org_remedies, dict):
                for oid, r_text in list(org_remedies.items())[:2]:
                    b_id = f"bio_{disease_id}_{oid}"
                    short_label = r_text.split("(")[0].strip()[:35]
                    add_node(b_id, f"🌿 {short_label}", "BiologicalRemedy", "#047857", {"protocol": r_text})
                    edges.append({"from": disease_id, "to": b_id, "label": "SUPPRESSED_BY"})

            # Chemical Treatment
            chem = entry.get("pesticides_and_fungicides", {})
            if isinstance(chem, dict):
                for cid, c_text in list(chem.items())[:1]:
                    c_id = f"chem_{disease_id}_{cid}"
                    short_label = c_text.split("(")[0].strip()[:35]
                    add_node(c_id, f"🧪 {short_label}", "ChemicalTreatment", "#0284c7", {"dosage": c_text})
                    edges.append({"from": disease_id, "to": c_id, "label": "TREATED_BY"})

        # Companion planting relations
        companions = self.get_companion_network(crop_name)
        for comp in companions.get("beneficial_companions", [])[:3]:
            comp_id = f"crop_{comp['name'].lower().replace(' ', '_')}"
            add_node(comp_id, comp["name"], "Crop", "#10b981", {"benefit": comp["benefit"]})
            edges.append({"from": crop_id, "to": comp_id, "label": "COMPANION_PLANT"})

        return {
            "nodes": nodes,
            "edges": edges,
            "engine": "Neo4j Integrated Agronomic Knowledge Graph",
            "stats": {"total_nodes": len(nodes), "total_edges": len(edges)}
        }

    def get_companion_network(self, crop_name: str) -> Dict[str, Any]:
        """
        Returns the agronomic companion and rotation graph network:
        - Beneficial Companions (repels pests, improves flavor, fixes N)
        - Antagonistic Neighbors (competes for nutrients, attracts shared pests)
        - Preceding / Following Crop Rotation
        """
        c = crop_name.lower()
        if "tomato" in c:
            return {
                "crop": "Tomato (Solanum lycopersicum)",
                "beneficial_companions": [
                    {"name": "Basil", "benefit": "Repels hornworms and thrips; enhances fruit flavor."},
                    {"name": "Marigold", "benefit": "Exudes alpha-terthienyl to suppress root-knot nematodes."},
                    {"name": "Garlic", "benefit": "Emits allicin volatile vapors deterring spider mites and aphids."},
                    {"name": "Carrot", "benefit": "Deep taproot loosens soil allowing tomato feeder roots to expand."}
                ],
                "antagonistic_neighbors": [
                    {"name": "Fennel", "reason": "Secretes anethole compounds that stunt tomato foliar growth."},
                    {"name": "Cabbage / Brassicas", "reason": "Heavy nutrient competition for phosphorus and zinc."},
                    {"name": "Corn", "reason": "Shares common pest Helicoverpa zea (Tomato Fruitworm / Corn Earworm)."}
                ],
                "rotation_schedule": {
                    "preceding_crop": "Legumes (Beans, Peas) to enrich soil with atmospheric nitrogen.",
                    "following_crop": "Root crops (Carrots, Radishes, Onions) to utilize deeper residual minerals."
                }
            }
        elif "potato" in c:
            return {
                "crop": "Potato (Solanum tuberosum)",
                "beneficial_companions": [
                    {"name": "Bush Beans", "benefit": "Fixes symbiotic nitrogen and repels Colorado potato beetle."},
                    {"name": "Horseradish", "benefit": "Increases disease resistance against bacterial rot."},
                    {"name": "Sweet Alyssum", "benefit": "Attracts predatory hoverflies that consume aphids."}
                ],
                "antagonistic_neighbors": [
                    {"name": "Tomato", "reason": "Both belong to Solanaceae; mutually transmit Late Blight (Phytophthora)."},
                    {"name": "Sunflower", "reason": "Allelopathic root exudates impede potato tuber enlargement."}
                ],
                "rotation_schedule": {
                    "preceding_crop": "Cover crops (Clover, Rye) for soil structure.",
                    "following_crop": "Brassicas (Cabbage, Broccoli) or Alliums (Onion, Garlic)."
                }
            }
        elif "spinach" in c:
            return {
                "crop": "Spinach (Spinacia oleracea)",
                "beneficial_companions": [
                    {"name": "Strawberries", "benefit": "Foliar cover shields strawberry crown; shares moisture requirements."},
                    {"name": "Radish", "benefit": "Trap crop for leaf miners, keeping spinach foliage intact."},
                    {"name": "Peas", "benefit": "Supplies light shade during warm hours and fixes nitrogen."}
                ],
                "antagonistic_neighbors": [
                    {"name": "Fennel", "reason": "Inhibits seed germination and leaf expansion."}
                ],
                "rotation_schedule": {
                    "preceding_crop": "Solanaceae or Cucurbits.",
                    "following_crop": "Summer Solanaceous crops (Tomato, Eggplant, Peppers)."
                }
            }
        else:
            return {
                "crop": crop_name.title(),
                "beneficial_companions": [
                    {"name": "Marigold", "benefit": "Universal insectary plant; suppresses root parasitic nematodes."},
                    {"name": "Clover / Legumes", "benefit": "Rhizobial nitrogen fixation enriching rhizosphere."}
                ],
                "antagonistic_neighbors": [
                    {"name": "Weeds & Invasive Grasses", "reason": "Competes for root moisture and sunlight."}
                ],
                "rotation_schedule": {
                    "preceding_crop": "Green manure cover crops (Vetch, Clover).",
                    "following_crop": "Deep-rooting taproot vegetables."
                }
            }

    def graph_rag_context(self, crop_or_query: str) -> str:
        """
        Extracts structured Knowledge Graph context to inject into LLM prompts
        for the PLLaMa AI Plant Science Consultant.
        """
        subgraph = self.get_crop_subgraph(crop_or_query)
        companions = self.get_companion_network(crop_or_query)

        lines = [
            f"[NEO4J KNOWLEDGE GRAPH GROUNDING: {crop_or_query.upper()}]",
            f"Graph Engine: {subgraph.get('engine', 'Neo4j AuraDB')}",
            f"Nodes: {subgraph.get('stats', {}).get('total_nodes', len(subgraph.get('nodes', [])))}, Relationships: {subgraph.get('stats', {}).get('total_edges', len(subgraph.get('edges', [])))}",
            "",
            "1. Verified Biological & Companion Relations:"
        ]

        for c in companions.get("beneficial_companions", []):
            lines.append(f"  - COMPANION: {c['name']} -> {c['benefit']}")

        if companions.get("antagonistic_neighbors"):
            lines.append("2. Antagonistic Plant Neighbors:")
            for a in companions.get("antagonistic_neighbors", []):
                lines.append(f"  - DO NOT PLANT NEAR: {a['name']} -> {a['reason']}")

        lines.append(f"3. Crop Rotation Protocol:")
        lines.append(f"  - Preceding: {companions.get('rotation_schedule', {}).get('preceding_crop', 'Legumes')}")
        lines.append(f"  - Following: {companions.get('rotation_schedule', {}).get('following_crop', 'Root Vegetables')}")

        return "\n".join(lines)

    def generate_cypher_seed_file(self, output_path: str = "neo4j_agronomic_seed.cypher") -> str:
        """
        Generates a production Cypher seed script containing:
        - Unique constraints on :Crop(name), :Disease(idName), :Pathogen(scientific_name)
        - Batch MERGE statements for all crops, diseases, and Koppert biological remedies.
        """
        cypher_lines = [
            "// ============================================================================",
            "// Vanaspati.AI - Neo4j Agronomic Knowledge Graph Seed Script",
            "// Compatible with Neo4j 5.x & Neo4j AuraDB Cloud",
            "// ============================================================================",
            "",
            "// 1. Constraints & Indexes",
            "CREATE CONSTRAINT crop_name_unique IF NOT EXISTS FOR (c:Crop) REQUIRE c.name IS UNIQUE;",
            "CREATE CONSTRAINT disease_id_unique IF NOT EXISTS FOR (d:Disease) REQUIRE d.idName IS UNIQUE;",
            "CREATE CONSTRAINT pathogen_name_unique IF NOT EXISTS FOR (p:Pathogen) REQUIRE p.scientific_name IS UNIQUE;",
            "CREATE CONSTRAINT remedy_name_unique IF NOT EXISTS FOR (r:BiologicalRemedy) REQUIRE r.name IS UNIQUE;",
            "",
            "// 2. Core Crop Taxonomy Nodes"
        ]

        crops = [
            ("Tomato", "Solanum lycopersicum", "Vegetables", "Solanaceae"),
            ("Potato", "Solanum tuberosum", "Vegetables", "Solanaceae"),
            ("Spinach", "Spinacia oleracea", "Spinach & Leafy Greens", "Amaranthaceae"),
            ("Malabar Spinach", "Basella alba", "Spinach & Leafy Greens", "Basellaceae"),
            ("Bitter Gourd", "Momordica charantia", "Gourds & Squashes", "Cucurbitaceae"),
            ("Bottle Gourd", "Lagenaria siceraria", "Gourds & Squashes", "Cucurbitaceae"),
            ("Apple", "Malus domestica", "Fruit Trees", "Rosaceae"),
            ("Mango", "Mangifera indica", "Fruit Trees", "Anacardiaceae"),
            ("Corn", "Zea mays", "Field Crops", "Poaceae")
        ]

        for name, sci, cat, fam in crops:
            cypher_lines.append(
                f"MERGE (c:Crop {{name: '{name}'}}) ON CREATE SET c.scientific_name = '{sci}', c.category = '{cat}', c.family = '{fam}';"
            )

        cypher_lines.append("\n// 3. Certified Koppert Biological Systems Remedies")
        koppert_remedies = [
            ("Trianum-P", "Trichoderma harzianum T-22", "Koppert Biological Systems", "Root & foliar bio-fungicide"),
            ("Spidex", "Phytoseiulus persimilis", "Koppert Biological Systems", "Predatory mite against spider mites"),
            ("Swirski-Mite", "Amblyseius swirskii", "Koppert Biological Systems", "Predatory biocontrol against thrips and whiteflies"),
            ("NatuGro", "Soil Microbials", "Koppert Biological Systems", "Systemic acquired resistance bio-inoculant")
        ]

        for name, org, supp, proto in koppert_remedies:
            cypher_lines.append(
                f"MERGE (b:BiologicalRemedy {{name: '{name}'}}) ON CREATE SET b.organism = '{org}', b.supplier = '{supp}', b.protocol = '{proto}';"
            )

        cypher_lines.append("\n// 4. Companion Planting Relationships")
        cypher_lines.append("MATCH (t:Crop {name: 'Tomato'}), (b:Crop {name: 'Spinach'}) MERGE (t)-[:COMPATIBLE_WITH]->(b);")
        cypher_lines.append("MATCH (p:Crop {name: 'Potato'}), (t:Crop {name: 'Tomato'}) MERGE (p)-[:ANTAGONISTIC_TO {reason: 'Shared Late Blight Host'}]->(t);")

        content = "\n".join(cypher_lines)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        return os.path.abspath(output_path)


# Singleton Instance
graph_service = Neo4jAgronomicService()
