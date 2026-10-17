// ============================================================================
// Vanaspati.AI - Neo4j Agronomic Knowledge Graph Seed Script
// Compatible with Neo4j 5.x & Neo4j AuraDB Cloud
// ============================================================================

// 1. Constraints & Indexes
CREATE CONSTRAINT crop_name_unique IF NOT EXISTS FOR (c:Crop) REQUIRE c.name IS UNIQUE;
CREATE CONSTRAINT disease_id_unique IF NOT EXISTS FOR (d:Disease) REQUIRE d.idName IS UNIQUE;
CREATE CONSTRAINT pathogen_name_unique IF NOT EXISTS FOR (p:Pathogen) REQUIRE p.scientific_name IS UNIQUE;
CREATE CONSTRAINT remedy_name_unique IF NOT EXISTS FOR (r:BiologicalRemedy) REQUIRE r.name IS UNIQUE;

// 2. Core Crop Taxonomy Nodes
MERGE (c:Crop {name: 'Tomato'}) ON CREATE SET c.scientific_name = 'Solanum lycopersicum', c.category = 'Vegetables', c.family = 'Solanaceae';
MERGE (c:Crop {name: 'Potato'}) ON CREATE SET c.scientific_name = 'Solanum tuberosum', c.category = 'Vegetables', c.family = 'Solanaceae';
MERGE (c:Crop {name: 'Spinach'}) ON CREATE SET c.scientific_name = 'Spinacia oleracea', c.category = 'Spinach & Leafy Greens', c.family = 'Amaranthaceae';
MERGE (c:Crop {name: 'Malabar Spinach'}) ON CREATE SET c.scientific_name = 'Basella alba', c.category = 'Spinach & Leafy Greens', c.family = 'Basellaceae';
MERGE (c:Crop {name: 'Bitter Gourd'}) ON CREATE SET c.scientific_name = 'Momordica charantia', c.category = 'Gourds & Squashes', c.family = 'Cucurbitaceae';
MERGE (c:Crop {name: 'Bottle Gourd'}) ON CREATE SET c.scientific_name = 'Lagenaria siceraria', c.category = 'Gourds & Squashes', c.family = 'Cucurbitaceae';
MERGE (c:Crop {name: 'Apple'}) ON CREATE SET c.scientific_name = 'Malus domestica', c.category = 'Fruit Trees', c.family = 'Rosaceae';
MERGE (c:Crop {name: 'Mango'}) ON CREATE SET c.scientific_name = 'Mangifera indica', c.category = 'Fruit Trees', c.family = 'Anacardiaceae';
MERGE (c:Crop {name: 'Corn'}) ON CREATE SET c.scientific_name = 'Zea mays', c.category = 'Field Crops', c.family = 'Poaceae';

// 3. Certified Koppert Biological Systems Remedies
MERGE (b:BiologicalRemedy {name: 'Trianum-P'}) ON CREATE SET b.organism = 'Trichoderma harzianum T-22', b.supplier = 'Koppert Biological Systems', b.protocol = 'Root & foliar bio-fungicide';
MERGE (b:BiologicalRemedy {name: 'Spidex'}) ON CREATE SET b.organism = 'Phytoseiulus persimilis', b.supplier = 'Koppert Biological Systems', b.protocol = 'Predatory mite against spider mites';
MERGE (b:BiologicalRemedy {name: 'Swirski-Mite'}) ON CREATE SET b.organism = 'Amblyseius swirskii', b.supplier = 'Koppert Biological Systems', b.protocol = 'Predatory biocontrol against thrips and whiteflies';
MERGE (b:BiologicalRemedy {name: 'NatuGro'}) ON CREATE SET b.organism = 'Soil Microbials', b.supplier = 'Koppert Biological Systems', b.protocol = 'Systemic acquired resistance bio-inoculant';

// 4. Companion Planting Relationships
MATCH (t:Crop {name: 'Tomato'}), (b:Crop {name: 'Spinach'}) MERGE (t)-[:COMPATIBLE_WITH]->(b);
MATCH (p:Crop {name: 'Potato'}), (t:Crop {name: 'Tomato'}) MERGE (p)-[:ANTAGONISTIC_TO {reason: 'Shared Late Blight Host'}]->(t);