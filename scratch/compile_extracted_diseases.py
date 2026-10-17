import json
import csv
import re

# Load Koppert extracted data
with open('scratch/koppert_extracted.json', 'r', encoding='utf-8') as f:
    koppert_data = json.load(f)

print(f"Loaded {len(koppert_data)} Koppert entries.")

# Britannica Encyclopedia Disease Directory
britannica_diseases = [
    # BACTERIAL DISEASES
    {
        "disease_name": "Aster Yellows",
        "category": "Biotic Disease (Phytoplasma / Bacterial)",
        "pathogen": "Candidatus Phytoplasma asteris (formerly considered a virus/MLO)",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Asters, lettuce, carrots, celery, onions, tomatoes, potatoes, over 300 species of dicotyledonous and monocotyledonous plants.",
        "symptoms": "Severe chlorosis (yellowing) of leaves with veins remaining pale green; stunted growth, proliferation of multiple weak shoots (witches' broom effect), floral virescence (petals turn green and leaf-like), deformed seed production.",
        "disease_cycle": "Transmitted by the aster leafhopper (Macrosteles quadrilineatus) in a persistent, circulative manner. Survives in perennial wild host plants and winter weeds, then spread to annual agricultural crops during early season migrations.",
        "prevention_and_management": "Eradicate susceptible perennial weeds around field borders (dandelions, wild lettuce, plantain). Implement fine insect mesh in nurseries. Rogue out infected plants immediately. Apply row covers.",
        "biological_and_chemical_controls": "Control leafhopper vector using Beauveria bassiana, neem seed kernel extract (NSKE), or pyrethrin sprays. Foliar antibiotic oxytetracycline can temporarily suppress symptoms in high-value ornamentals."
    },
    {
        "disease_name": "Bacterial Wilt (Brown Rot / Stewart's Wilt / Southern Wilt)",
        "category": "Biotic Disease (Bacterial)",
        "pathogen": "Ralstonia solanacearum / Pantoea stewartii / Curtobacterium flaccumfaciens",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Potato, tomato, eggplant, pepper, banana (Moko disease), corn (Stewart's wilt), beans.",
        "symptoms": "Rapid daytime wilting of canopy while foliage remains green; vascular browning in stems; milky bacterial slime oozes when cut stem is placed in clear water (bacterial stream test). In potato tubers, a brown discoloration appears in the vascular ring.",
        "disease_cycle": "Soil-borne pathogen entering through root wounds, nematode punctures, or cultivation injury. Multiplies within xylem vessels, producing extracellular polysaccharides (EPS) that clog water transport.",
        "prevention_and_management": "3-5 year crop rotation with non-solanaceous crops (grasses, maize). Plant certified pathogen-free seeds/seed-pieces. Disinfect pruning knives between rows. Enhance soil drainage.",
        "biological_and_chemical_controls": "Soil bio-inoculants containing Bacillus subtilis, Pseudomonas fluorescens, and Trichoderma harzianum. Copper oxychloride or copper hydroxide drench. Antibiotics such as streptomycin sulfate + tetracycline drench."
    },
    {
        "disease_name": "Fire Blight",
        "category": "Biotic Disease (Bacterial)",
        "pathogen": "Erwinia amylovora",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Apples, pears, quinces, crabapples, hawthorn, cotoneaster, pyracantha.",
        "symptoms": "Blossoms and vegetative shoot tips suddenly wilt, turn black or dark brown as if scorched by fire; shepherd's crook curvature at twig tips; milky to amber-colored bacterial droplet exudate on blighted bark and fruit under humid conditions.",
        "disease_cycle": "Overwinters in canker margins on twigs and trunks. In spring, oozing bacteria are carried by rain splash, bees, and flies to open blossoms. Pathogen travels downward through phloem and xylem into branches.",
        "prevention_and_management": "Prune blighted twigs in dry winter weather 20-30 cm below visible lesion, dipping tools in 70% alcohol or 10% bleach between every cut. Avoid high-nitrogen fertilizers that stimulate soft succulent shoots.",
        "biological_and_chemical_controls": "Apply bio-bactericides containing Bacillus amyloliquefaciens or Pseudomonas fluorescens during bloom. Streptomycin sulfate or kasugamycin sprays during flowering risk periods. Fixed copper sprays applied at silver-tip bud break."
    },
    {
        "disease_name": "Rice Bacterial Blight",
        "category": "Biotic Disease (Bacterial)",
        "pathogen": "Xanthomonas oryzae pv. oryzae",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Paddy Rice (Oryza sativa), wild grasses (Leersia oryzoides).",
        "symptoms": "Water-soaked stripes starting at leaf margins and leaf tips, enlarging into long wavy yellow-to-white blighted lesions running down the leaf blade; bacterial ooze droplets form in morning dew. Kresek phase causes entire young seedling wilting and death.",
        "disease_cycle": "Survives in seed hulls, stubble, and irrigation canals. Enters leaves via hydathodes at leaf margins and mechanical wounds created by typhoon winds or farm tools.",
        "prevention_and_management": "Plant resistant cultivars carrying Xa-gene resistance (e.g., Xa21). Ensure balanced N-P-K fertilization (excess nitrogen increases severity). Drain excess water from fields.",
        "biological_and_chemical_controls": "Seed soaking in streptocycline (100 ppm) + copper oxychloride solution. Foliar spraying with copper hydroxide or validamycin. Bio-inoculants with Pseudomonas fluorescens seed treatment."
    },
    {
        "disease_name": "Bacterial Canker",
        "category": "Biotic Disease (Bacterial)",
        "pathogen": "Clavibacter michiganensis subsp. michiganensis / Xanthomonas citri / Pseudomonas syringae",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Tomato, peppers, stone fruits (peaches, cherries, plums), citrus.",
        "symptoms": "Tomato: lower leaves curl upward and wilt; brown vascular discoloration; stems develop dark streaks that crack open into cankers; fruit displays 'bird's eye' spots (small white spots with dark brown central dots). Citrus: raised corky brown eruptions surrounded by yellow halo.",
        "disease_cycle": "Seed-borne and debris-borne. Enters plants through natural openings (stomata, hydathodes) and pruning wounds. Disseminated by splashing rain, overhead irrigation, and handling.",
        "prevention_and_management": "Hot-water seed treatment (50°C for 25 minutes for tomato seed). Rogue out infected plants. Sterilize stakes, greenhouse benches, and trellising twine.",
        "biological_and_chemical_controls": "Copper hydroxide mixed with mancozeb for preventive bactericidal barrier. Bacillus subtilis foliar spray. In citrus, systemic trunk injection of oxytetracycline in regulated situations."
    },
    {
        "disease_name": "Crown Gall",
        "category": "Biotic Disease (Bacterial)",
        "pathogen": "Agrobacterium tumefaciens (Rhizobium radiobacter)",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Roses, grapevines, walnut, willow, apple, stone fruits, and over 140 genera of dicotyledonous angiosperms.",
        "symptoms": "Rough, abnormal, tumor-like swellings (galls) on roots, crown (ground level), and woody lower stems. Young galls are spongy and flesh-colored; older galls turn hard, woody, dark brown, and fissured.",
        "disease_cycle": "Bacterium enters root or stem wounds caused by grafting, cultivation, root insects, or pruning. It transfers a segment of its Ti-plasmid (T-DNA) into host plant cells, directing host cells to overproduce auxins and cytokinins (causing hyperplasia and hypertrophy).",
        "prevention_and_management": "Plant certified disease-free nursery stock. Avoid wounding stems and crowns during planting and weed cultivation. Sanitize budding knives with alcohol.",
        "biological_and_chemical_controls": "Pre-planting dip of root systems in antagonistic biocontrol agent Agrobacterium radiobacter strain K84 or K1026 (produces agrocin 84 which selectively kills virulent crown gall bacteria)."
    },
    {
        "disease_name": "Bacterial Soft Rot",
        "category": "Biotic Disease (Bacterial)",
        "pathogen": "Pectobacterium carotovorum (formerly Erwinia carotovora) / Dickeya dadantii",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Potato tubers, carrots, onions, cabbage, cauliflower, lettuce, tomato, cucumber, ornamentals.",
        "symptoms": "Water-soaked lesions on storage organs, roots, and succulent stems that rapidly enlarge. Infected tissues disintegrate into a soft, mushy, slimy liquefaction accompanied by a foul, putrid odor caused by secondary rotting bacteria.",
        "disease_cycle": "Pathogen produces copious pectolytic enzymes (pectin lyase, polygalacturonase) that dissolve the middle lamella of host plant cells. Enters through harvest wounds, insect bites, freeze damage, or lenticels under anaerobic waterlogging.",
        "prevention_and_management": "Harvest during dry weather. Avoid bruising and mechanical abrasion of tubers/roots. Cure tubers before storage (promote suberization). Ensure well-ventilated, cold storage conditions (4°C for potatoes).",
        "biological_and_chemical_controls": "Post-harvest wash with chlorinated water (50-100 ppm free chlorine). Biocontrol with Pseudomonas fluorescens or Bacillus amyloliquefaciens dip. Dust seed pieces with mancozeb."
    },
    {
        "disease_name": "Common Scab of Potato",
        "category": "Biotic Disease (Bacterial / Actinomycete)",
        "pathogen": "Streptomyces scabies / Streptomyces acidiscabies",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Potato (Solanum tuberosum), beet, radish, turnip, carrot, parsnip.",
        "symptoms": "Superficial, raised, or deeply pitted rough corky brown lesions on the skin of developing tubers. Lesions may coalesce to cover substantial portions of the tuber surface, severely reducing commercial quality.",
        "disease_cycle": "Soil-dwelling filamentous actinomycete that penetrates young tubers through immature lenticels and stomata. Produces thaxtomin phytotoxins that disrupt plant cellulose synthesis.",
        "prevention_and_management": "Maintain soil pH below 5.2 (scab bacteria are suppressed in acidic soils). Keep soil moisture high (near field capacity) during the 4-6 weeks of tuber initiation. Rotate with alfalfa, rye, or corn.",
        "biological_and_chemical_controls": "Treat seed tubers with fludioxonil or mancozeb. Apply elemental sulfur to lower soil pH in alkaline fields. Inoculate soil with antagonistic Trichoderma spp. and non-pathogenic Streptomyces strains."
    },

    # FUNGAL DISEASES
    {
        "disease_name": "Anthracnose",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Colletotrichum gloeosporioides / Colletotrichum acutatum / Colletotrichum lindemuthianum",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Mango, avocado, banana, beans, tomato, pepper, strawberry, cucurbits, coffee, turfgrass.",
        "symptoms": "Dark brown to black sunken circular necrotic lesions on foliage, stems, flowers, and fruit. Under moist humid conditions, concentric salmon-pink or orange gelatinous spore masses (acervuli) erupt in lesion centers.",
        "disease_cycle": "Survives as dormant mycelium or appressoria on plant debris, seed coats, or infected twigs. Conidia are spread by splashing raindrops and wind-driven mist. Fungi penetrate cuticle directly via specialized melanized appressoria.",
        "prevention_and_management": "Use certified disease-free seeds. Prune dense canopies to promote rapid drying of foliage. Remove fallen leaves and mummified fruits. Avoid overhead sprinkler irrigation.",
        "biological_and_chemical_controls": "Biofungicides: Trichoderma harzianum (Trianum-P), Bacillus subtilis (Veni GoKlean). Chemical fungicides: Azoxystrobin, Difenoconazole, Chlorothalonil, Copper oxychloride, Mancozeb."
    },
    {
        "disease_name": "Black Knot",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Apiosporina morbosa (Dibotryon morbosum)",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Plums, prunes, tart cherries, sweet cherries, wild chokecherries.",
        "symptoms": "Elongated, rough, velvety olive-green swellings on twigs and branches that expand over 1-2 years into hard, coal-black, cracked, brittle, knotty galls that encircle and girdle branches.",
        "disease_cycle": "Ascospores mature in pseudothecia on 2-year-old knots during spring rainy periods and infect succulent green shoots. The fungus stimulates abnormal cell division in xylem and bark parenchymatous tissue.",
        "prevention_and_management": "Prune out galls during dormant season, cutting at least 10-15 cm below the visible knot margin. Destroy or burn prunings immediately. Eradicate wild cherry and plum trees near commercial orchards.",
        "biological_and_chemical_controls": "Dormant spray of lime sulfur or Bordeaux mixture. Apply protective captan, chlorothalonil, or thiophanate-methyl sprays from green tip until terminal growth ceases."
    },
    {
        "disease_name": "Chestnut Blight",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Cryphonectria parasitica (formerly Endothia parasitica)",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "American chestnut (Castanea dentata), European chestnut, chinquapin, scarlet oak.",
        "symptoms": "Sunken or swollen reddish-orange to yellowish-brown cankers on stems and branches; yellow-orange pinhead-sized fruiting pycnidia erupt through bark fissures; foliage above canker wilts, dies, and turns reddish-brown ('flags'); epicormic sprouts emerge below cankers.",
        "disease_cycle": "Airborne ascospores and rain-splashed conidia enter bark cracks and mechanical wounds. Mycelium produces oxalic acid that kills the cambium, vascular cylinder, and phloem, completely girdling mature trunks.",
        "prevention_and_management": "Breeding blight-resistant backcross hybrids (American chestnut crossed with Chinese chestnut Castanea mollissima). Quarantine diseased timber.",
        "biological_and_chemical_controls": "Hypovirulence biocontrol: inoculation of virulent cankers with hypovirus-infected strains of Cryphonectria parasitica containing double-stranded RNA (dsRNA) which diminishes virulence and converts lethal cankers into superficial swelling."
    },
    {
        "disease_name": "Late Blight of Potato and Tomato",
        "category": "Biotic Disease (Oomycete / Fungal)",
        "pathogen": "Phytophthora infestans",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Potato, tomato, eggplant, petunia, bittersweet nightshade.",
        "symptoms": "Water-soaked, pale-to-dark green irregular spots on leaves and stems, turning dark purplish-brown with pale green margins. In cool, wet weather, a delicate white fuzzy mildew appears on the lower leaf surface. Infected tubers develop irregular reddish-brown granular dry rot.",
        "disease_cycle": "Historic cause of the 1845 Irish Potato Famine. Overwinters as mycelium in infected seed tubers, volunteer potatoes, or cull piles. Biflagellate zoospores emerge from sporangia in free water and infect plants rapidly within hours.",
        "prevention_and_management": "Plant certified disease-free seed tubers. Eliminate cull piles and volunteer potatoes. Ensure wide plant spacing. Destroy haulms (vines) 2 weeks before harvest.",
        "biological_and_chemical_controls": "Biological control: Trichoderma asperellum, Bacillus amyloliquefaciens. Chemical fungicides: Metalaxyl/Mefenoxam, Cymoxanil + Mancozeb, Fluopicolide, Dimethomorph, Mandipropamid, Copper hydroxide."
    },
    {
        "disease_name": "Early Blight",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Alternaria solani",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Potato, tomato, eggplant, peppers.",
        "symptoms": "Small brown-black spots on older lower leaves, developing distinct concentric circular rings (concentric target board or bullseye pattern) surrounded by a chlorotic yellow halo; extensive defoliation, stem collar rot, and sunken leathery fruit rots.",
        "disease_cycle": "Survives in solanaceous plant debris and infected seed. Multi-celled beaked conidia are dispersed by wind, rain, and overhead irrigation. Favored by alternating periods of wet dew and warm dry days.",
        "prevention_and_management": "Crop rotation with non-host crops for 2-3 years. Mulch soil to prevent rain splash. Prune lower foliage. Ensure adequate potassium and nitrogen nutrition to avoid early plant senescence.",
        "biological_and_chemical_controls": "Biofungicides: Bacillus subtilis, Trichoderma harzianum. Chemical sprays: Chlorothalonil, Mancozeb, Azoxystrobin, Difenoconazole, Boscalid, Copper oxychloride."
    },
    {
        "disease_name": "Clubroot of Crucifers",
        "category": "Biotic Disease (Plasmodiophorid / Fungal-like)",
        "pathogen": "Plasmodiophora brassicae",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Cabbage, broccoli, cauliflower, Brussels sprouts, turnip, radish, mustard, canola.",
        "symptoms": "Severe swelling, spindle-shaped club-like distortion, and gall formation on main taproots and lateral roots. Above ground: pale yellow foliage, mid-day wilting on warm sunny days, and severe plant stunting.",
        "disease_cycle": "Soil-borne obligate parasite. Resting spores persist in soil for up to 15-20 years. In wet soil, biflagellate primary zoospores hatch, infect root hairs, and stimulate host cells to divide (hyperplasia) and enlarge (hypertrophy).",
        "prevention_and_management": "Raise soil pH above 7.2 by applying hydrated lime or agricultural calcitic lime. Improve field drainage. Practice long rotations (6-8 years) without crucifers or brassica weeds. Clean tractor tires.",
        "biological_and_chemical_controls": "Fungicide drenches: Fluazinam or cyazofamid applied to transplant planting holes. Bio-fungicide Trichoderma harzianum or Streptomyces lydicus incorporated into seedbed soil."
    },
    {
        "disease_name": "Damping-Off",
        "category": "Biotic Disease (Oomycete & Fungal)",
        "pathogen": "Pythium aphanidermatum / Pythium ultimum / Rhizoctonia solani / Fusarium spp.",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Seedlings of virtually all vegetables, flowers, cotton, sugar beets, and cereals.",
        "symptoms": "Pre-emergence damping-off: seeds rot and decay before germinating or shoots rot before breaking the soil line. Post-emergence damping-off: water-soaked constriction and thinning at the soil line (wirestem), causing young seedlings to topple over and die.",
        "disease_cycle": "Soil-inhabiting saprophytes that attack tender non-lignified seedling tissues under cold, wet, poorly drained, compacted soil conditions. Oospores and sclerotia survive indefinitely in substrate.",
        "prevention_and_management": "Use sterile seed-starting potting mix. Avoid overwatering and heavy dense soil. Ensure good air circulation and warm germination temperatures. Sow seeds at proper depth.",
        "biological_and_chemical_controls": "Koppert biological products: Trianum-P / Trianum-G (Trichoderma harzianum Rifai T-22), Prestop (Clonostachys rosea). Chemical seed dressings: Metalaxyl, Thiram, Captan, Fludioxonil."
    },
    {
        "disease_name": "Dutch Elm Disease",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Ophiostoma ulmi / Ophiostoma novo-ulmi",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "American elm (Ulmus americana), English elm, slippery elm, and other Ulmus species.",
        "symptoms": "Foliage on upper branches wilts, turns dull green then bright yellow, dries out, turns brown, and curls up ('flagging'); peeled bark exposes continuous dark brown or purple streaking in outermost sapwood xylem ring; rapid whole-tree mortality.",
        "disease_cycle": "Transmitted by European elm bark beetles (Scolytus multistriatus) and native elm bark beetles (Hylurgopinus rufipes) that carry sticky fungal spores in their galleries; also spreads underground between adjacent trees via root grafts.",
        "prevention_and_management": "Rapid removal and debarking/burning of dead elm timber. Trenching or root-graft disruption between trees with a vibratory plow. Planting tolerant elm cultivars (e.g., 'Valley Forge', 'Princeton').",
        "biological_and_chemical_controls": "Preventive macro-infusion of systemic fungicide propiconazole (Arbotect) into root flares every 3 seasons. Pheromone trapping and insecticidal sprays against vector bark beetles."
    },
    {
        "disease_name": "Ergot of Rye and Cereals",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Claviceps purpurea",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Rye (Secale cereale), wheat, barley, triticale, oats, and various wild pasture grasses.",
        "symptoms": "During flowering, floral parts secrete sweet, sticky yellow droplets ('honeydew') loaded with conidia. Later, normal grain kernels are replaced by hard, elongated, curved, purplish-black resting horn-like bodies (sclerotia or ergots). Sclerotia contain poisonous ergot alkaloids (ergotamine) toxic to humans and livestock (ergotism / St. Anthony's Fire).",
        "disease_cycle": "Overwintering sclerotia on or near soil surface germinate in spring to produce stromatic heads with perithecia. Ejected ascospores infect open grass flowers during damp bloom periods.",
        "prevention_and_management": "Use certified ergot-free seed. Deep plowing (inverts soil and buries sclerotia deeper than 5 cm, preventing germination). Crop rotation with non-grass crops. Mow roadside grasses before blooming.",
        "biological_and_chemical_controls": "Float-separate sclerotia from grain seed in a 20% brine (salt) solution before planting. Seed treatment with triazole fungicides (tebuconazole, difenoconazole)."
    },
    {
        "disease_name": "Fusarium Wilt (including Panama Disease of Banana)",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Fusarium oxysporum (e.g. f. sp. cubense, lycopersici, vasinfectum)",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Banana, tomato, cotton, pea, watermelon, melon, cabbage, date palm, carnation.",
        "symptoms": "Unilateral (one-sided) yellowing of leaves; leaf buckling and wilting from bottom upwards; distinct dark red-brown to chocolate vascular ring discoloration in xylem vessels; stunted growth and death.",
        "disease_cycle": "Soil-borne pathogen producing thick-walled chlamydospores that endure in soil for 20-30+ years. Enters root hairs, colonizes xylem, and releases fusaric acid, causing vascular collapse.",
        "prevention_and_management": "Plant resistant cultivars (e.g., Fusarium-resistant tomato hybrids, Tropical Race 4 quarantine for banana). Strictly disinfect farm machinery and boots. Solarize soil with plastic sheets.",
        "biological_and_chemical_controls": "Koppert biological control: Trianum-P (Trichoderma harzianum Rifai strain T-22), Bacillus subtilis, Streptomyces. Soil drench with carbendazim or thiophanate-methyl in non-food crops."
    },
    {
        "disease_name": "Peach Leaf Curl & Leaf Blister",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Taphrina deformans (peach leaf curl) / Taphrina caerulescens (oak leaf blister)",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Peach, nectarine, almond, oak trees.",
        "symptoms": "In spring, emerging leaves become thickened, puckered, twisted, and severely distorted; color shifts from normal green to reddish, purplish, or chlorotic yellow; leaves develop a velvety gray-white sheen of naked asci before turning brown and dropping.",
        "disease_cycle": "Ascospores and blastoconidia (yeast-like budding spores) overwinter on bark, branch twigs, and bud scales. In cool wet spring weather, rain washes spores into swelling buds, where mycelium invades succulent leaf tissues.",
        "prevention_and_management": "Plant curl-resistant cultivars (e.g., 'Frost', 'Avalon', 'Muir'). Prune infected twigs after premature defoliation and boost tree vigor with nitrogen fertilizer and irrigation.",
        "biological_and_chemical_controls": "Single targeted fungicide spray applied in late autumn after leaf drop or in late winter just prior to bud swell. Effective chemicals: Copper fungicides (Bordeaux mixture, copper hydroxide), chlorothalonil, or ziram."
    },
    {
        "disease_name": "Downy Mildew",
        "category": "Biotic Disease (Oomycete)",
        "pathogen": "Pseudoperonospora cubensis / Plasmopara viticola / Bremia lactucae / Peronospora spp.",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Cucurbits (cucumber, melon, squash), grapevines, lettuce, onions, spinach, brassicas, hops.",
        "symptoms": "Angular, bright yellow chlorotic spots on the upper leaf surface sharply restricted by leaf veins ('mosaic tile effect'). Under high humidity, a dense purplish-gray to brown fuzzy felt of sporangiophores develops on the corresponding lower leaf surface.",
        "disease_cycle": "Obligate biotrophic oomycete favored by cool-to-moderate temperatures (15-22°C) and extended leaf wetness or high relative humidity (>85%). Wind-borne sporangia germinate to release swimming zoospores.",
        "prevention_and_management": "Avoid overhead sprinkler irrigation; water at ground level. Select resistant hybrids. Maintain wide row spacing and trellis vines to ensure maximum sunlight and airflow. Destroy crop residues.",
        "biological_and_chemical_controls": "Koppert biological products: Trianum-P, Veni GoKlean, copper-based bio-enhancers. Chemical fungicides: Fosetyl-aluminum, Metalaxyl-M + Mancozeb, Fluopicolide, Dimethomorph, Cymoxanil, Propamocarb."
    },
    {
        "disease_name": "Powdery Mildew",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Erysiphe spp. / Podosphaera spp. / Blumeria graminis / Leveillula taurica / Oidium spp.",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Cucurbits, grapes, apples, roses, cereals (wheat, barley), tomato, pepper, peas, strawberries, ornamentals.",
        "symptoms": "White to talcum-powder-like circular patches of mycelium and conidia erupting primarily on the upper surface of leaves, shoots, buds, and fruits; infected leaves turn yellow, curl upward, become dry, brittle, and drop prematurely.",
        "disease_cycle": "Obligate biotrophic parasite that does not require liquid free water to germinate (germinates in high relative humidity). Overwinters as dormant mycelium in bud scales or as cleistothecia / chasmothecia.",
        "prevention_and_management": "Plant resistant cultivars. Extra silicon and calcium nutrition to harden epidermal cell walls. Prune dense foliage. Ensure greenhouse morning venting on the lee side.",
        "biological_and_chemical_controls": "Koppert biological products: Veni GoKlean, Bacillus subtilis, Ampelomyces quisqualis (hyperparasite of powdery mildew). Potassium bicarbonate, horticultural mineral oils, sulfur dust, myclobutanil, azoxystrobin, trifloxystrobin."
    },
    {
        "disease_name": "Oak Wilt",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Bretziella fagacearum (formerly Ceratocystis fagacearum)",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Oak species (Quercus spp., especially red oak group: pin oak, red oak, black oak; also white oaks).",
        "symptoms": "Leaves turn dull bronze or water-soaked olive-green starting at leaf margins and tip, progressing inward towards the leaf base; dramatic sudden mid-summer defoliation; sweet, fruity-smelling fungal mats form beneath bark; whole-tree mortality in red oaks within weeks.",
        "disease_cycle": "Transmitted by sap-feeding nitidulid beetles attracted to fresh pruning wounds or tree injuries; spreads rapidly through grafted root systems between nearby trees.",
        "prevention_and_management": "Do NOT prune or wound oak trees during peak beetle activity (April to July). Sever interconnected root systems using vibratory plow line trenches at least 1.5 m deep. Paint any accidental wounds immediately.",
        "biological_and_chemical_controls": "Preventive macro-infusion of systemic fungicide propiconazole (Alamo) into root flares of high-value non-symptomatic or early-symptomatic white oaks."
    },
    {
        "disease_name": "Gray Mold (Botrytis Blight / Noble Rot)",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Botrytis cinerea",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Strawberry, grapevines, tomato, bell pepper, rose, peony, onion, lettuce, and over 200 plant species.",
        "symptoms": "Water-soaked soft brown lesions on petals, leaves, and stems that rapidly become covered with a dense, luxuriant, grayish-brown fuzzy layer of conidiophores and spores; soft watery fruit rots; black flattened sclerotia on old tissues.",
        "disease_cycle": "Necrotrophic facultative parasite that readily colonizes aging flower petals and dying tissue before invading healthy stems and fruit. Favored by cool, humid, damp weather (15-20°C, >90% RH).",
        "prevention_and_management": "Keep greenhouse humidity below 80% with ventilation and heating. Remove spent blossoms and senescent lower leaves. Avoid wetting foliage during irrigation. Handle fruit gently.",
        "biological_and_chemical_controls": "Koppert biological products: Trianum-P, Clonostachys rosea, Aureobasidium pullulans (Botector), Bacillus subtilis. Chemical fungicides: Fenhexamid, Cyprodinil + Fludioxonil, Boscalid, Iprodione."
    },
    {
        "disease_name": "Wood Decays & Heart Rot",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Phellinus igniarius / Ganoderma applanatum / Fomes fomentarius / Trametes versicolor",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Deciduous shade trees (oak, beech, birch, maple) and conifers (pine, spruce, fir).",
        "symptoms": "Presence of woody bracket fungi, shelf conks, or mushroom brackets on trunks and branch stubs; internal hollows, spongy white or brown crumbly wood inside the core trunk (heartwood); branch dieback and windthrow failure.",
        "disease_cycle": "Basidiospores carried by wind infect dead branch stubs, fire scars, or mechanical trunk wounds. Wood-decay enzymes (cellulases, lignin peroxidases) slowly break down structural lignin and cellulose over decades.",
        "prevention_and_management": "Prevent bark gouges and trunk damage from machinery. Make proper pruning cuts outside the branch collar (do not make flush cuts). Avoid topping trees. Hazardous trees should be evaluated and removed.",
        "biological_and_chemical_controls": "No curative chemical treatments once internal wood rot is established; prophylactic sealing and biological wound dressings containing Trichoderma harzianum can protect fresh wound sites."
    },
    {
        "disease_name": "Rust Diseases (Cereal Stem Rust / Cedar-Apple Rust / Coffee Rust / White Pine Blister)",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Puccinia graminis / Gymnosporangium juniperi-virginianae / Hemileia vastatrix / Cronartium ribicola",
        "source": "Encyclopædia Britannica & CSK HPKV Pathology Lecture",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Wheat, barley, oats, coffee, apple, cedar/juniper, white pine, gooseberry/currant, roses, beans.",
        "symptoms": "Eruption of powdery reddish-orange, golden-yellow, or dark brown pustules (uredinia) on leaves, petioles, and stems; chlorotic halos; severe defoliation and lodging; galls with orange gelatinous horns on alternate hosts.",
        "disease_cycle": "Complex macrocyclic heteroecious rust life cycles producing up to 5 distinct spore states (urediniospores, teliospores, basidiospores, pycniospores, aeciospores) requiring two alternate botanical hosts to complete reproduction.",
        "prevention_and_management": "Eradicate alternate hosts (e.g., remove common barberry Berberis vulgaris near wheat fields; remove Ribes near white pines). Plant rust-resistant crop cultivars carrying Sr genes.",
        "biological_and_chemical_controls": "Triazole fungicides: Tebuconazole, Propiconazole, Epoxiconazole, Difenoconazole; Strobilurins (Azoxystrobin, Pyraclostrobin); Mancozeb protective sprays; Biofungicide Bacillus subtilis."
    },
    {
        "disease_name": "Apple Scab",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Venturia inaequalis",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Apple (Malus domestica), crabapple, hawthorn, mountain ash.",
        "symptoms": "Dull olive-green to velvety brown circular spots on leaves that turn dark and puckered; fruit develops sunken, brownish-black corky scabs that crack open, distort fruit development, and lead to early fruit drop.",
        "disease_cycle": "Overwinters in pseudothecia on dead fallen leaf litter. In spring rain, shooting ascospores infect expanding blossom clusters and young leaves. Secondary cycles propagate via conidia (Spilocaea pomi) all season long.",
        "prevention_and_management": "Shred fallen autumn leaves with a flail mower or apply 5% urea spray to hasten leaf decomposition. Plant scab-resistant cultivars (e.g., 'Prima', 'Liberty', 'Freedom', 'GoldRush').",
        "biological_and_chemical_controls": "Koppert biological products: Veni GoKlean, Trichoderma, Bacillus subtilis. Chemical fungicides: Captan, Mancozeb, Difenoconazole, Cyprodinil, Dodine, Kresoxim-methyl, Lime sulfur."
    },
    {
        "disease_name": "Smut Diseases (Corn Smut / Loose Smut / Stinking Bunt)",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Ustilago maydis / Ustilago tritici / Ustilago nuda / Tilletia tritici / Tilletia caries",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Maize, wheat, barley, oats, grasses.",
        "symptoms": "Corn smut: large, glistening, silvery-white swollen galls forming on ears, tassels, and stalks, which rupture to release millions of powdery black teliospores. Loose smut: entire grain spikelet transformed into an olive-black mass of loose teliospores. Stinking bunt: bunted kernels filled with foul fishy-smelling trimethylamine black powder.",
        "disease_cycle": "Loose smut is internally seed-borne (dormant mycelium resides within grain embryo). Bunt and corn smut teliospores survive on seed surfaces or in soil.",
        "prevention_and_management": "Sow certified disease-free seed. Hot-water seed treatment (52-54°C for 10 minutes for loose smut). Avoid excessive mechanical injury during field cultivation.",
        "biological_and_chemical_controls": "Systemic triazole seed treatments: Carboxin + Thiram, Difenoconazole, Tebuconazole, Triticonazole, Fludioxonil. Antagonistic Bacillus velezensis seed dressing."
    },
    {
        "disease_name": "Snow Mold",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Typhula incarnata / Typhula ishikariensis (Gray Snow Mold) / Microdochium nivale (Pink Snow Mold)",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Turfgrasses (golf greens, lawns), winter wheat, winter rye, barley.",
        "symptoms": "Bleached, matted, straw-colored circular patches (20-60 cm) appearing upon winter snowmelt; gray snow mold shows tiny reddish-brown to black seed-like sclerotia embedded in leaves; pink snow mold develops a faint salmon-pink fuzzy mycelium when exposed to daylight.",
        "disease_cycle": "Active under deep, prolonged snow cover on unfrozen turf at temperatures near freezing (0-4°C). Sclerotia survive warm summer months in soil and thatch.",
        "prevention_and_management": "Avoid late-autumn applications of high-nitrogen fertilizer that promote lush succulent growth. Mow grass late into autumn. Aerate compacted turf. Install snow fencing to avoid heavy drifts.",
        "biological_and_chemical_controls": "Preventive autumn fungicide applications before first permanent snowfall: Iprodione, Fludioxonil, Propiconazole, Chlorothalonil, Penthiopyrad. Bio-protection with cold-tolerant Trichoderma strains."
    },
    {
        "disease_name": "Sooty Mold",
        "category": "Biotic Disease (Fungal Saprophyte)",
        "pathogen": "Capnodium spp. / Fumago vagans / Scorias spongiosa / Cladosporium spp.",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Citrus, gardenia, crape myrtle, camellia, mango, ornamentals, shade trees.",
        "symptoms": "Black, charcoal-like, crusty, velvety, or sooty coating covering leaves, twigs, and fruit; easily rubbed off with fingers; does not invade internal plant tissue, but physically blocks sunlight, drastically inhibiting photosynthesis.",
        "disease_cycle": "Non-parasitic superficial epiphytic fungi that live exclusively on honeydew excrement deposited by phloem-feeding insects (aphids, scale insects, whiteflies, mealybugs, psyllids).",
        "prevention_and_management": "Control the underlying honeydew-producing insect population. Wash sooty leaves with mild soap and water spray or insecticidal soap.",
        "biological_and_chemical_controls": "Release Koppert insect biocontrols: Cryptolaemus montrouzieri (ladybird against mealybugs), Encarsia formosa (against whiteflies), Aphidius colemani (against aphids). Spray neem oil, horticultural oil, or acetamiprid."
    },
    {
        "disease_name": "Verticillium Wilt",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Verticillium dahliae / Verticillium albo-atrum",
        "source": "Encyclopædia Britannica & Koppert India",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Cotton, potato, tomato, eggplant, strawberry, olive, maple, avocado, mint, over 300 dicot species.",
        "symptoms": "V-shaped chlorotic and necrotic lesions along leaf margins; one-sided (unilateral) wilting of branches or foliage; vascular discoloration (olive-brown to dark streaks in sapwood); progressive stunting and plant decline.",
        "disease_cycle": "Soil-borne pathogen producing resilient micro-sclerotia that persist in soil for 10-15+ years. Enters roots directly or through nematode wounds, colonizes xylem, and spreads systemic conidia upwards.",
        "prevention_and_management": "Avoid planting susceptible crops in fields with a history of verticillium wilt. Grow non-host monocot crops (corn, sorghum, wheat) in rotation. Soil solarization using clear polyethylene film.",
        "biological_and_chemical_controls": "Koppert biological products: Trianum-P (Trichoderma harzianum T-22), Bacillus amyloliquefaciens. Bio-fumigation with brassica cover crops (mustard meal producing glucosinolates)."
    },

    # VIRAL & VIROID DISEASES
    {
        "disease_name": "Curly Top Disease",
        "category": "Biotic Disease (Viral)",
        "pathogen": "Beet curly top virus (BCTV) / Curtovirus",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Sugar beet, table beet, tomato, pepper, bean, spinach, cantaloupe, cucurbits.",
        "symptoms": "Leaves curl inward and upward with thickened, puckered, brittle blades; veins become swollen, translucent, and develop tiny nipple-like gall outgrowths on leaf undersides; severe plant dwarfing and yellowing.",
        "disease_cycle": "Transmitted by the beet leafhopper (Circulifer tenellus) in a circulative, non-propagative manner. Leafhoppers acquire the virus while feeding on infected wild desert weeds and migrate into cultivated valleys.",
        "prevention_and_management": "Use curly top-resistant sugar beet and bean cultivars. Plant early or use dense plant stands to shade the ground (leafhoppers prefer sunny, sparse stands). Trap crops and border weed management.",
        "biological_and_chemical_controls": "Control leafhopper vector migrations using systemic seed treatments (imidacloprid, thiamethoxam) or entomopathogenic fungi (Beauveria bassiana)."
    },
    {
        "disease_name": "Mosaic Diseases (Tobacco / Cucumber / Tomato / Cauliflower Mosaic)",
        "category": "Biotic Disease (Viral)",
        "pathogen": "Tobacco mosaic virus (TMV) / Cucumber mosaic virus (CMV) / Tomato mosaic virus (ToMV) / Potyviruses",
        "source": "Encyclopædia Britannica & CSK HPKV Pathology Lecture",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Tobacco, tomato, cucumber, melons, squash, peppers, potatoes, brassicas, legumes, ornamentals.",
        "symptoms": "Contrasting light green and dark green mottled 'checkerboard' mosaic pattern on leaves; blistering, leaf curling, 'shoestring' leaf malformation (lamina fails to develop, leaving only the midrib); stunting; fruit marbling and distortion.",
        "disease_cycle": "TMV/ToMV are extremely stable rod-shaped virions spread mechanically on workers' hands, pruning shears, and smokers' tobacco residues. CMV and Potyviruses are stylet-borne non-persistently by aphids (Aphis gossypii, Myzus persicae).",
        "prevention_and_management": "Sanitize tools in 20% non-fat dry milk or 10% TSP (trisodium phosphate) solution. Wash hands with soap before touching plants. Eliminate aphid weed reservoirs. Use certified virus-free seed.",
        "biological_and_chemical_controls": "Control insect vectors using Koppert Aphidius colemani, Chrysoperla carnea (green lacewing), and neem oil. Apply reflective silver mulches to repel alighting aphid vectors."
    },
    {
        "disease_name": "Citrus Psorosis",
        "category": "Biotic Disease (Viral)",
        "pathogen": "Citrus psorosis virus (CPsV) / Ophiovirus",
        "source": "Encyclopædia Britannica",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Sweet orange, grapefruit, mandarin, tangelo.",
        "symptoms": "Bark scaling and flaking on the trunk and primary scaffold limbs; resinous gumming (gummosis); internal wood staining; young leaves exhibit faint translucent flecks, oak-leaf patterns, or ring spots in spring.",
        "disease_cycle": "Disseminated primarily through infected budwood and vegetative propagation. Natural field vector transmission may involve soil-inhabiting Olpidium fungi or unknown airborne vectors.",
        "prevention_and_management": "Use only certified virus-tested, shoot-tip grafted nursery stock. Implement strict citrus budwood certification programs. Remove and replace declining trees.",
        "biological_and_chemical_controls": "Scrape bark lesions on mildly affected trunks down to healthy wood to stimulate healing callus formation. No curative chemical viricide exists."
    },
    {
        "disease_name": "Tomato Spotted Wilt",
        "category": "Biotic Disease (Viral)",
        "pathogen": "Tomato spotted wilt orthotospovirus (TSWV)",
        "source": "Encyclopædia Britannica & CSK HPKV Pathology Lecture",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Tomato, pepper, peanut/groundnut, potato, lettuce, tobacco, over 1000 dicot/monocot species.",
        "symptoms": "Bronzing and purpling of upper leaf surfaces; necrotic ring spots, streaks on terminal shoots; growing tips die back ('spotted wilt'); ripening fruit shows concentric chlorotic and necrotic circular rings with bumpy contours.",
        "disease_cycle": "Transmitted exclusively by thrips (primarily western flower thrips Frankliniella occidentalis and onion thrips Thrips tabaci). Virus is acquired by thrips larvae and transmitted persistently by adults.",
        "prevention_and_management": "Plant TSWV-resistant cultivars possessing the Sw-5 resistance gene. Install fine thrips screening (mesh size < 0.15 mm) on greenhouse vents. Control reservoir weeds.",
        "biological_and_chemical_controls": "Release Koppert predatory thrips mites: Amblyseius swirskii, Neoseiulus cucumeris, or Orius laevigatus (minute pirate bug). Apply spinosad, cyantraniliprole, or Beauveria bassiana."
    },
    {
        "disease_name": "Potato Spindle Tuber Viroid (PSTVd)",
        "category": "Biotic Disease (Viroid)",
        "pathogen": "Potato spindle tuber viroid (PSTVd) - naked circular ssRNA",
        "source": "Encyclopædia Britannica & CSK HPKV Pathology Lecture",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Potato (Solanum tuberosum), tomato, pepino, avocado.",
        "symptoms": "Tubers become abnormally elongated, cylindrical, spindle-shaped or dumb-bell shaped with prominent deep eyes and surface cracking. Foliage becomes erect, stiff, upright, and spindly with darker green leaves; dramatic yield reduction.",
        "disease_cycle": "Smallest known infectious pathogen (approx 359 nucleotides, no protein coat). Extremely stable, mechanically transmitted via cutting knives, tractor tires, machinery, pollen, and true botanical seed.",
        "prevention_and_management": "Plant certified viroid-tested micropropagated seed tubers. Strict phytosanitary quarantine measures. Clean cutting equipment with 2% sodium hypochlorite.",
        "biological_and_chemical_controls": "No viricide or chemical cure available. Eradication of infected lots and seed-piece sterilization are the sole effective controls."
    },

    # SPECIALIZED / LECTURE DISEASES (CSK HPKV & Regional Catalogs)
    {
        "disease_name": "Tikka Disease of Groundnut (Early and Late Leaf Spot)",
        "category": "Biotic Disease (Fungal)",
        "pathogen": "Cercosporidium personatum (Late) / Cercospora arachidicola (Early)",
        "source": "Dr. P.N. Sharma Plant Pathology (CSK HPKV) & Reference CSV",
        "url": "https://www.koppert.in/disease-control/cercospora-leaf-spot",
        "host_plants": "Groundnut / Peanut (Arachis hypogaea).",
        "symptoms": "Early leaf spot (C. arachidicola): larger circular reddish-brown spots (4-10 mm) with distinct yellow halos on upper leaf surface. Late leaf spot (C. personatum): smaller, circular, deep brownish-black spots (1-6 mm) on lower surface with late indistinct halos; severe defoliation up to 50-70% yield loss.",
        "disease_cycle": "Primary infection from soil-borne conidia surviving in crop residue or seeds. Secondary spread by wind-borne conidia during humid conditions (heavy dew, temperatures 25-30°C).",
        "prevention_and_management": "Crop rotation with cereals. Seed soaking in 0.5% copper sulphate or hot water. Deep burial of crop debris. Grow resistant cultivars (e.g., Akra Anamia, Kadiri-3).",
        "biological_and_chemical_controls": "Seed dressing with Trichoderma viride (4 g/kg seed). Foliar spraying with Bordeaux mixture (1%), Mancozeb (0.2%), Chlorothalonil, Carbendazim (0.1%), or Hexaconazole."
    },
    {
        "disease_name": "Yellow Vein Mosaic of Bhendi (Okra)",
        "category": "Biotic Disease (Viral)",
        "pathogen": "Bhendi yellow vein mosaic virus (BYVMV) / Begomovirus",
        "source": "Dr. P.N. Sharma Plant Pathology (CSK HPKV)",
        "url": "https://www.koppert.in/disease-control/",
        "host_plants": "Okra / Bhendi / Lady's Finger (Abelmoschus esculentus), wild malvaceous weeds.",
        "symptoms": "Vein clearing followed by an unmistakable network of brilliant yellow veins enclosing islands of green tissue; complete chlorosis in advanced stages; fruits become dwarfed, malformed, tough, and yellowish-green; up to 80-100% crop loss if infected early.",
        "disease_cycle": "Transmitted by the whitefly (Bemisia tabaci). Population peaks during hot summer months. Virus overwinters on roadside weeds like Croton sparsiflorus and Ageratum.",
        "prevention_and_management": "Destroy weed hosts around okra plots. Grow resistant varieties like 'Arka Anamika', 'Arka Abhay', 'Punjab Padmini', 'Parbhani Kranti'. Rogue out infected plants within 20 days.",
        "biological_and_chemical_controls": "Foliar spray of neem oil (5-10 ml/L) at weekly intervals. Control whitefly vector with yellow sticky traps and bio-agents (Verticillium lecanii / Lecanicillium) or sprays of dimethoate (0.03%) or thiamethoxam."
    },
    {
        "disease_name": "Little Leaf of Brinjal",
        "category": "Biotic Disease (Phytoplasma)",
        "pathogen": "Phytoplasma (Mycoplasma-like organism / MLB)",
        "source": "Dr. P.N. Sharma Plant Pathology (CSK HPKV)",
        "url": "https://www.koppert.in/disease-control/",
        "host_plants": "Eggplant / Brinjal (Solanum melongena), Datura fastuosa, Vinca rosea.",
        "symptoms": "Extreme reduction in leaf size ('little leaf'); petioles shorten and lamina turns soft and pale yellow; internodes contract drastically giving the top branches a dense bushy/witches' broom appearance; flowers turn green (phyllody) and fail to fruit.",
        "disease_cycle": "Transmitted by leafhopper vectors (Cestius phycitis, Empoasca devastans). Pathogen resides in phloem sieve tube cells.",
        "prevention_and_management": "Rogue out and burn infected plants early. Grow tolerant varieties (Pusa Purple Cluster, Black Beauty). Adjust sowing dates to evade major leafhopper flight periods.",
        "biological_and_chemical_controls": "Apply phorate 10G granules to nursery beds. Dip roots of seedlings in 0.05% tetracycline hydrochloride solution prior to transplanting. Spray dimethoate or imidacloprid to control leafhoppers."
    },
    {
        "disease_name": "Red Rust of Tea",
        "category": "Biotic Disease (Algal Parasite)",
        "pathogen": "Cephaleuros parasiticus (Green Algae / Trentepohliales)",
        "source": "Dr. P.N. Sharma Plant Pathology (CSK HPKV)",
        "url": "https://www.koppert.in/disease-control/",
        "host_plants": "Tea (Camellia sinensis), mango, guava, citrus.",
        "symptoms": "Velvety circular orange-red to reddish-brown hairy spots appearing on upper leaf surfaces and young shoots between April and July; causes chlorosis, defoliation, twig dieback, bark cracking, and loss of bush productivity.",
        "disease_cycle": "Unique plant disease caused by a parasitic green alga. Overwinters on infected stems and crop debris. Spreads by swimming biflagellate zoospores and airborne sporangia under hot, humid, sun-drenched conditions.",
        "prevention_and_management": "Improve plantation drainage. Prune affected branches and plucking buds. Maintain adequate shade trees to avoid direct intense scorching sunlight. Apply 2% MOP (potash) and urea to rehabilitate stressed bushes.",
        "biological_and_chemical_controls": "Spray copper fungicides (Copper oxychloride 0.25% or Bordeaux mixture 1%) directly targeting young stems and branches during peak fruiting season (May-June)."
    },
    {
        "disease_name": "Root-Knot Nematode Disease",
        "category": "Biotic Disease (Nematode)",
        "pathogen": "Meloidogyne incognita / Meloidogyne javanica / Meloidogyne arenaria",
        "source": "Encyclopædia Britannica & Reference CSV",
        "url": "https://www.britannica.com/topic/list-of-plant-diseases-2033263",
        "host_plants": "Tomato, potato, cucumber, carrot, cotton, tobacco, soybean, coffee, fruit trees.",
        "symptoms": "Formation of swollen, irregular galls and knots along root systems; root branching is stunted and feeder roots decay; above-ground plants display yellowing, stunting, daytime wilting, and severe nutrient deficiency symptoms.",
        "disease_cycle": "Microscopic second-stage juveniles (J2) penetrate root tips, migrate to the vascular cylinder, and inject esophageal secretions that transform host cells into specialized multinucleate 'giant cells' for feeding.",
        "prevention_and_management": "Crop rotation with non-host crops (marigolds Tagetes spp. produce nematicidal alpha-terthienyl). Soil solarization with plastic sheeting. Deep summer plowing.",
        "biological_and_chemical_controls": "Koppert beneficial nematodes (Steinernema feltiae for pest control) or bionematicides: Paecilomyces lilacinus (Purpureocillium lilacinum), Pochonia chlamydosporia, Bacillus firmus. Chemical nematicides: Fluopyram, Oxamyl."
    }
]

print(f"Total Britannica & Reference diseases prepared: {len(britannica_diseases)}")

# Merge with Koppert diseases
master_catalog = []
all_names = set()

# First add Koppert diseases
for kd in koppert_data:
    name = kd["disease_name"]
    master_catalog.append({
        "disease_name": name,
        "pathogen": kd["pathogen"],
        "category": "Biotic Disease (Fungal / Bacterial / Oomycete)",
        "source": "Koppert India",
        "url": kd["url"],
        "host_plants": "Horticultural & agricultural crops (vegetables, fruits, cereals, ornamentals)",
        "general_overview": kd["general_overview"],
        "damage_symptoms": kd["damage_symptoms"],
        "life_cycle": kd["life_cycle"],
        "prevention_and_management": kd["prevention_and_management"],
        "biological_products": ", ".join(kd["biological_products"]) if kd["biological_products"] else "Koppert biological crop protection products (Trianum-P, Veni GoKlean, Trichoderma, Bacillus)"
    })
    all_names.add(name.lower())

# Now add Britannica & Lecture diseases
for bd in britannica_diseases:
    name = bd["disease_name"]
    master_catalog.append({
        "disease_name": name,
        "pathogen": bd["pathogen"],
        "category": bd["category"],
        "source": bd["source"],
        "url": bd["url"],
        "host_plants": bd["host_plants"],
        "general_overview": f"Documented in {bd['source']} as a major plant disease affecting {bd['host_plants']}.",
        "damage_symptoms": bd["symptoms"],
        "life_cycle": bd["disease_cycle"],
        "prevention_and_management": bd["prevention_and_management"],
        "biological_products": bd["biological_and_chemical_controls"]
    })

print(f"Total entries in master catalog: {len(master_catalog)}")

# Save to JSON
with open('Data-processed/extracted_plant_diseases.json', 'w', encoding='utf-8') as f:
    json.dump(master_catalog, f, indent=2, ensure_ascii=False)

# Save to CSV
fieldnames = [
    "disease_name", "pathogen", "category", "source", "host_plants", 
    "damage_symptoms", "life_cycle", "prevention_and_management", 
    "biological_products", "url"
]

with open('Data-processed/extracted_plant_diseases.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    for row in master_catalog:
        writer.writerow(row)

print("Saved Data-processed/extracted_plant_diseases.json and Data-processed/extracted_plant_diseases.csv successfully!")
