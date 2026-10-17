import json
import os

knowledge_base = {
    # ==========================
    # ROSE
    # ==========================
    "Rose___Black_spot": {
        "idName": "Rose___Black_spot",
        "plant_name": "Rose (Rosa spp.)",
        "disease_name": "Black Spot Disease",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Diplocarpon rosae",
        "severity": "High (Rapid Defoliation)",
        "disease_symptoms": {
            "s1": "Circular black spots with fringed, feathery margins appear on the upper surface of leaves.",
            "s2": "Leaf tissue surrounding the dark spots turns bright yellow (chlorosis).",
            "s3": "Severe premature leaf drop (defoliation) beginning from lower branches upward, weakening the bush.",
            "s4": "Raised purplish-red to black blistering lesions may develop on young canes and flower buds."
        },
        "disease_causes": {
            "c1": "Fungal spores overwinter in fallen dead leaves and infected cane lesions.",
            "c2": "Prolonged leaf wetness (at least 7 hours) with temperatures between 68°F and 75°F (20°C - 24°C).",
            "c3": "Overhead watering, rainfall splashing, and high relative humidity above 85%.",
            "c4": "Dense canopy growth with poor air circulation trapping moisture around the foliage."
        },
        "disease_prevention": {
            "p1": "Plant disease-resistant rose cultivars (e.g., Knock Out, Rugosa, or modern floribundas).",
            "p2": "Water at the base of the bush early in the morning using drip or soaker hose; avoid wetting foliage.",
            "p3": "Space bushes 3 to 4 feet apart and prune interior crossing branches to promote rapid drying airflow.",
            "p4": "Rake and burn/dispose of all fallen autumn leaves; never compost black-spot infected rose debris."
        },
        "fertilizer_recommendation": {
            "f1": "Balanced Rose Fertilizer (NPK 10-15-10 or 12-6-12) enriched with Magnesium and Iron.",
            "f2": "Apply Potassium (K) (Sulfate of Potash) in spring to fortify epidermal cell walls against fungal hyphae.",
            "f3": "Avoid high-nitrogen synthetic fertilizers mid-season, as soft lush vegetative growth is highly susceptible.",
            "f4": "Top-dress with 2 inches of aged pine bark mulch to prevent soil-borne spore splashing during rain."
        },
        "pesticides_and_fungicides": {
            "pf1": "Tebuconazole or Myclobutanil (Systemic triazole fungicides applied every 10-14 days during wet periods).",
            "pf2": "Chlorothalonil (Broad-spectrum protective contact fungicide, ideal for early spring preventative sprays).",
            "pf3": "Copper Hydroxide / Liquid Copper Fungicide (Apply during dormant winter season to kill overwintering spores).",
            "pf4": "Mancozeb or Captan (Effective preventative protectant sprays applied before rain events)."
        },
        "organic_remedies": {
            "org1": "Cold-pressed Neem Oil Spray (0.5% - 1% concentration with mild organic soap) applied every 7 days.",
            "org2": "Potassium Bicarbonate / Baking Soda Solution (1 tbsp baking soda + 1 tsp horticultural oil per gallon of water).",
            "org3": "Bacillus amyloliquefaciens / Bacillus subtilis bio-fungicide sprays to outcompete fungal spores.",
            "org4": "Liquid Kelp & Seaweed Foliar Spray to stimulate plant systemic acquired resistance (SAR)."
        },
        "disease_control": {
            "ctrl1": "Immediately hand-pick and dispose of all spotted leaves to curb spore dispersal.",
            "ctrl2": "Prune infected canes 2 inches below visible discoloration and sterilize shears with 70% alcohol.",
            "ctrl3": "Apply an approved preventative fungicide spray at the first sign of new spring leaf emergence."
        }
    },
    "Rose___Powdery_mildew": {
        "idName": "Rose___Powdery_mildew",
        "plant_name": "Rose (Rosa spp.)",
        "disease_name": "Powdery Mildew",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Podosphaera pannosa",
        "severity": "Moderate to High",
        "disease_symptoms": {
            "s1": "White to grayish-white powdery talcum-like fungal patches on young leaves, shoots, and unopened buds.",
            "s2": "Infected young leaves become twisted, curled, puckered, and blistered.",
            "s3": "Flower buds fail to open or produce deformed, stunted blossoms.",
            "s4": "Severe infection causes foliage to turn reddish-purple or brown and drop prematurely."
        },
        "disease_causes": {
            "c1": "Favored by warm dry days (70°F - 80°F) accompanied by cool, high-humidity nights (90-99% RH).",
            "c2": "Unlike most fungi, powdery mildew spores germinate in high humidity WITHOUT requiring liquid water on leaves.",
            "c3": "Over-fertilization with nitrogen causing excessive soft young succulent growth."
        },
        "disease_prevention": {
            "p1": "Plant roses in full sunlight (minimum 6-8 hours daily); sunlight inhibits powdery mildew germination.",
            "p2": "Ensure wide spacing between bushes and prune center branches for maximum breeze circulation.",
            "p3": "Hose down foliage with water in the bright mid-morning; free water actually washes off and lyses mildew spores!"
        },
        "fertilizer_recommendation": {
            "f1": "Switch to low-nitrogen, high-potassium & phosphorus blends (e.g. NPK 5-10-15).",
            "f2": "Foliar application of Soluble Silica / Potassium Silicate to strengthen epidermal defenses.",
            "f3": "Supplement with Calcium Nitrate early in the season to enhance cellular rigidity."
        },
        "pesticides_and_fungicides": {
            "pf1": "Myclobutanil (Immunox) or Propiconazole (Systemic curative and preventative fungicide).",
            "pf2": "Sulfur-based Dust or Wettable Sulfur Spray (Never apply when temperatures exceed 85°F/29°C).",
            "pf3": "Triforine or Trifloxystrobin for commercial and large garden rose collections."
        },
        "organic_remedies": {
            "org1": "Milk Spray: 1 part milk to 9 parts water sprayed in direct sunlight (milk proteins create natural antiseptics).",
            "org2": "Horticultural Oil or Jojoba Oil sprays to smother and eradicate existing mycelial mats.",
            "org3": "Potassium Bicarbonate (MilStop) 2 to 3 tablespoons per gallon of water."
        },
        "disease_control": {
            "ctrl1": "Prune away severely distorted shoot tips and deformed buds.",
            "ctrl2": "Thoroughly spray tops and undersides of leaves with organic sulfur or neem oil every 5-7 days.",
            "ctrl3": "Clean garden tools after working on infected plants to prevent transmission."
        }
    },
    "Rose___Rust": {
        "idName": "Rose___Rust",
        "plant_name": "Rose (Rosa spp.)",
        "disease_name": "Rose Rust",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Phragmidium tuberculatum",
        "severity": "Moderate to High",
        "disease_symptoms": {
            "s1": "Bright orange, powdery pustules (uredinia) on the undersides of leaves.",
            "s2": "Corresponding light yellow or chlorotic flecks on the upper leaf surface.",
            "s3": "Pustules turn black in late summer/autumn as overwintering teliospores form.",
            "s4": "Severe defoliation, twig dieback, and general loss of plant vigor."
        },
        "disease_causes": {
            "c1": "Cool to moderate temperatures (55°F - 65°F / 13°C - 18°C) and continuous moisture for 2 to 4 hours.",
            "c2": "Overwintering in infected dead leaves, leaf mulch, and stem cankers."
        },
        "disease_prevention": {
            "p1": "Collect and destroy all fallen leaves before winter.",
            "p2": "Avoid overhead watering; keep leaves dry.",
            "p3": "Annual hard dormant pruning to remove overwintering stem cankers."
        },
        "fertilizer_recommendation": {
            "f1": "Balanced organic rose fertilizer enriched with kelp meal, rock phosphate, and bone meal.",
            "f2": "Avoid late-season nitrogen applications that delay winter dormancy."
        },
        "pesticides_and_fungicides": {
            "pf1": "Mancozeb, Chlorothalonil, or Myclobutanil sprayed at 7-10 day intervals during cool damp weather.",
            "pf2": "Dormant spray of Lime-Sulfur in late winter before bud-break."
        },
        "organic_remedies": {
            "org1": "Sulfur sprays and bio-fungicides containing Bacillus subtilis.",
            "org2": "Neem oil foliar sprays applied early morning."
        },
        "disease_control": {
            "ctrl1": "Prune out and bag infected branches; do not drop infected leaves onto garden beds.",
            "ctrl2": "Begin preventative fungicide applications in early spring when new shoots reach 2-4 inches."
        }
    },
    "Rose___healthy": {
        "idName": "Rose___healthy",
        "plant_name": "Rose (Rosa spp.)",
        "disease_name": "Healthy Rose Specimen",
        "pathogen_type": "None (Vibrant Plant)",
        "scientific_name": "Rosa hybrida",
        "severity": "Optimal Health (Zero Pathology)",
        "disease_symptoms": {
            "s1": "Glossy, deep green, uniformly colored foliage with clean serrated margins.",
            "s2": "Sturdy, erect canes with healthy pith and firm green bark.",
            "s3": "Well-formed flower buds with clean sepals and vibrant blossom development.",
            "s4": "Zero spotting, powdery residues, rust pustules, or insect webbing."
        },
        "disease_causes": {
            "c1": "Proper cultural care: adequate sunlight, balanced soil nutrition, and optimal irrigation."
        },
        "disease_prevention": {
            "p1": "Maintain 6-8 hours of direct sunlight and 3-foot spacing.",
            "p2": "Inspect leaf undersides weekly for early detection of aphids, spider mites, or black spot.",
            "p3": "Sanitize pruners between bushes using rubbing alcohol."
        },
        "fertilizer_recommendation": {
            "f1": "Apply slow-release balanced rose food (NPK 10-10-10 or 8-12-8) every 4-6 weeks during blooming season.",
            "f2": "Add 1 cup of alfalfa meal and 1 tbsp of Epsom salt (Magnesium Sulfate) around the drip line in spring.",
            "f3": "Cease nitrogen fertilizing 6 weeks before first anticipated frost to harden off canes."
        },
        "pesticides_and_fungicides": {
            "pf1": "No chemical pesticides required for healthy roses.",
            "pf2": "Optional preventative botanical dormant spray (horticultural oil) in late winter."
        },
        "organic_remedies": {
            "org1": "Beneficial companion planting with Alliums (garlic/chives) and Marigolds to deter aphids and nematodes.",
            "org2": "Compost tea foliar drench monthly to sustain healthy phyllosphere microflora."
        },
        "disease_control": {
            "ctrl1": "Continue regular deadheading of spent blooms to channel energy into vigorous root and shoot systems."
        }
    },

    # ==========================
    # TOMATO
    # ==========================
    "Tomato___Early_blight": {
        "idName": "Tomato___Early_blight",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Early Blight (Target Spot)",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Alternaria solani",
        "severity": "High (Destroys Lower Foliage)",
        "disease_symptoms": {
            "s1": "Brown to black circular spots developing distinctive concentric rings like a target board.",
            "s2": "Yellow chlorotic halo surrounding leaf lesions on older bottom leaves first.",
            "s3": "Progressive upward defoliation exposing green tomato fruit to sunscald.",
            "s4": "Dark, sunken, leathery lesions at the stem end of fruits."
        },
        "disease_causes": {
            "c1": "Pathogen overwinters on solanaceous crop residue and volunteer tomato/potato weeds in soil.",
            "c2": "Favored by warm humid weather (75°F - 85°F / 24°C - 29°C) with alternating wet and dry periods.",
            "c3": "Soil splash from heavy rains or overhead sprinklers transferring spores to lowest leaves."
        },
        "disease_prevention": {
            "p1": "Practice strict 3 to 4-year crop rotation; avoid planting tomatoes after potatoes, peppers, or eggplants.",
            "p2": "Prune all bottom leaves up to 18 inches above the ground once plants reach 3 feet tall.",
            "p3": "Mulch generously with clean straw, black plastic, or wood chips to create a splash barrier.",
            "p4": "Stake or cage plants upright to maintain good airflow and dry foliage."
        },
        "fertilizer_recommendation": {
            "f1": "Balanced Tomato Fertilizer with lower nitrogen and high potassium/calcium (e.g. NPK 5-10-10 or 4-18-38).",
            "f2": "Apply Calcium Nitrate to prevent blossom end rot and strengthen epidermal resistance to Alternaria toxins.",
            "f3": "Avoid excess nitrogen fertilizer which creates dense, humid canopy foliage."
        },
        "pesticides_and_fungicides": {
            "pf1": "Chlorothalonil (Daconil) - Highly effective protective contact fungicide applied every 7-10 days.",
            "pf2": "Copper Hydroxide / Copper Octanoate (Liquid Copper) approved for organic and conventional growers.",
            "pf3": "Azoxystrobin or Mancozeb - Commercial preventative and early curative fungicides."
        },
        "organic_remedies": {
            "org1": "Bacillus subtilis or Bacillus amyloliquefaciens (Serenade ASO) bio-fungicides.",
            "org2": "Copper sulfate / Bordeaux mixture sprayed early in the morning.",
            "org3": "Potassium Bicarbonate spray (3 tbsp per gallon water) to alter leaf surface pH against spores."
        },
        "disease_control": {
            "ctrl1": "Strip and bag all infected bottom leaves immediately at first sign of target spots.",
            "ctrl2": "Do not work in tomato patch when foliage is wet from dew or rain to prevent spreading spores.",
            "ctrl3": "Apply preventative fungicide immediately after rain events during warm summer periods."
        }
    },
    "Tomato___Late_blight": {
        "idName": "Tomato___Late_blight",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Late Blight",
        "pathogen_type": "Oomycete (Water Mold)",
        "scientific_name": "Phytophthora infestans",
        "severity": "Critical (Can Destroy Crops in 72 Hours)",
        "disease_symptoms": {
            "s1": "Large, irregular, water-soaked, dark olive-green to black greasy lesions on leaves and stems.",
            "s2": "Delicate white fuzzy fungal-like growth on the undersides of leaves during humid morning conditions.",
            "s3": "Stems turn dark brown to black and collapse rapidly.",
            "s4": "Fruits develop large, firm, greasy brown lesions with bumpy texture, ruining the harvest."
        },
        "disease_causes": {
            "c1": "Cool, wet, cloudy weather (60°F - 70°F / 15°C - 21°C) with relative humidity above 90%.",
            "c2": "Windborne sporangia that can travel several miles on air currents from infected fields.",
            "c3": "Infected cull potato piles or volunteer plants serving as seasonal inoculum sources."
        },
        "disease_prevention": {
            "p1": "Plant certified disease-free transplants and resistant hybrids (e.g., Defiant, Mountain Magic, Iron Lady).",
            "p2": "Ensure maximum spacing between rows and stake plants for rapid leaf drying.",
            "p3": "Destroy all volunteer tomato and potato seedlings early in spring.",
            "p4": "Never compost late blight infected plants; bag and dispose of in municipal trash or burn."
        },
        "fertilizer_recommendation": {
            "f1": "NPK 8-15-36 formulation enriched with Potassium and Phosphorus to boost plant immunity.",
            "f2": "Apply Phosphite / Potassium Phosphite (0-0-28) foliar sprays to activate systemic plant defense pathways.",
            "f3": "Avoid high-nitrogen fertilizers that create soft vegetative tissue vulnerable to zoospore penetration."
        },
        "pesticides_and_fungicides": {
            "pf1": "Cymoxanil + Mancozeb (Curzate) - Rapid translaminar curative and protectant action.",
            "pf2": "Mandipropamid (Revus) or Dimethomorph (Forum) - Highly specialized Oomycete fungicides.",
            "pf3": "Copper Hydroxide applied preventatively before rain storms when late blight warnings are issued."
        },
        "organic_remedies": {
            "org1": "Fixed Copper fungicides (Nordox or Badge X2) applied preventatively every 5 days during blight weather.",
            "org2": "Bio-fungicides containing Streptomyces lydicus or Bacillus amyloliquefaciens.",
            "org3": "Hydrogen Dioxide / Peroxyacetic acid (OxiDate) sanitizing spray to kill surface spores."
        },
        "disease_control": {
            "ctrl1": "Act immediately upon first symptom: remove infected foliage or entire plant if stem is infected.",
            "ctrl2": "Notify neighboring gardeners, as Phytophthora spores travel rapidly on wind.",
            "ctrl3": "Harvest mature green fruits immediately from unaffected vines before blight spreads to fruit."
        }
    },
    "Tomato___healthy": {
        "idName": "Tomato___healthy",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Healthy Tomato Specimen",
        "pathogen_type": "None (Optimum Foliage)",
        "scientific_name": "Solanum lycopersicum",
        "severity": "Optimal Health (Zero Pathology)",
        "disease_symptoms": {
            "s1": "Vibrant deep green foliage with uniform chlorophyll distribution across all leaves.",
            "s2": "Stems are thick, sturdy, and covered with healthy trichome glandular hairs.",
            "s3": "Abundant bright yellow blossoms with successful fruit set and smooth skin.",
            "s4": "Zero spots, chlorosis, curling, greasy lesions, or pest damage."
        },
        "disease_causes": {
            "c1": "Optimal environmental balance: 6-8 hours of direct sun, consistent watering, and fertile soil."
        },
        "disease_prevention": {
            "p1": "Maintain 2-3 inches of organic straw or wood mulch under plants.",
            "p2": "Prune suckers and lowest leaves touching the ground to prevent soil-borne fungal spores.",
            "p3": "Water deeply at ground level using drip emitters; keep leaves dry."
        },
        "fertilizer_recommendation": {
            "f1": "Balanced Tomato Food (NPK 4-18-38 or 5-10-10) with Calcium, Magnesium, and Sulfur.",
            "f2": "Side-dress with bone meal and compost when fruit first sets to provide slow-release Phosphorus.",
            "f3": "Maintain soil pH between 6.2 and 6.8 for optimal nutrient uptake."
        },
        "pesticides_and_fungicides": {
            "pf1": "No chemical treatments necessary for healthy plants.",
            "pf2": "Optional preventative biological drench with mycorrhizal fungi at root zone."
        },
        "organic_remedies": {
            "org1": "Companion planting with Basil and French Marigolds to naturally repel hornworms and aphids.",
            "org2": "Compost tea foliar spray to maintain robust beneficial microbial colonies."
        },
        "disease_control": {
            "ctrl1": "Support heavy vines with sturdy cages or trellising to prevent fruit contact with soil."
        }
    },
    "Tomato___Bacterial_spot": {
        "idName": "Tomato___Bacterial_spot",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Bacterial Spot",
        "pathogen_type": "Bacterial Pathogen",
        "scientific_name": "Xanthomonas perforans / euvesicatoria",
        "severity": "High (Fruit & Leaf Defoliation)",
        "disease_symptoms": {
            "s1": "Small (less than 1/8 inch), water-soaked, dark brown to black circular lesions on leaves.",
            "s2": "Lesions often have a distinctive yellow halo and appear greasy on leaf undersides.",
            "s3": "Leaves turn yellow, dry out, and take on a scorched, ragged appearance.",
            "s4": "Fruits exhibit small, raised, black blister-like spots that become scabby and rough."
        },
        "disease_causes": {
            "c1": "Warm temperatures (75°F - 86°F / 24°C - 30°C) combined with high rainfall, overhead watering, and high humidity.",
            "c2": "Bacteria enter through natural openings (stomata) and minor wounds caused by wind, sand, or pruning.",
            "c3": "Infected seed or infected volunteer tomato plants."
        },
        "disease_prevention": {
            "p1": "Always purchase certified disease-free, hot-water-treated tomato seed.",
            "p2": "Avoid working in wet fields or pruning during damp weather.",
            "p3": "Rotate crops with non-solanaceous plants (corn, beans, brassicas) for minimum 2-3 years."
        },
        "fertilizer_recommendation": {
            "f1": "Maintain balanced NPK (e.g. 5-10-10) with adequate Potassium to thicken cell walls.",
            "f2": "Foliar Zinc and Manganese to bolster bacterial defense enzymes.",
            "f3": "Avoid high ammonium nitrogen which increases succulent leaf vulnerability."
        },
        "pesticides_and_fungicides": {
            "pf1": "Copper Hydroxide mixed with Mancozeb (Mancozeb enhances copper bioavailability against resistant Xanthomonas).",
            "pf2": "Acibenzolar-S-methyl (Actigard) - Plant defense activator that triggers systemic acquired resistance (SAR).",
            "pf3": "Bacteriophages (AgriPhage) - Biological virus spray specifically targeting Xanthomonas strains."
        },
        "organic_remedies": {
            "org1": "Liquid Copper Octanoate (Copper soap) sprayed every 7 days.",
            "org2": "Bacillus amyloliquefaciens (Double Nickel 55) bio-bactericide.",
            "org3": "Hydrogen Dioxide (OxiDate) wash."
        },
        "disease_control": {
            "ctrl1": "Remove and destroy severely affected leaves immediately.",
            "ctrl2": "Apply copper + mancozeb tank mix preventatively before rain forecast.",
            "ctrl3": "Disinfect stakes, cages, and pruning tools with 10% bleach solution."
        }
    },
    "Tomato___Leaf_Mold": {
        "idName": "Tomato___Leaf_Mold",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Leaf Mold",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Passalora fulva (syn. Cladosporium fulvum)",
        "severity": "Moderate to High (Especially in High Tunnels/Greenhouses)",
        "disease_symptoms": {
            "s1": "Pale green or yellow spots with indefinite borders on the upper surface of older leaves.",
            "s2": "Dense, velvety, olive-green to grayish-purple mold growth on the undersides of leaves directly below yellow spots.",
            "s3": "Leaves curl, wither, turn completely brown and drop prematurely.",
            "s4": "Rarely affects fruit directly, but defoliation significantly reduces fruit size and yield."
        },
        "disease_causes": {
            "c1": "High relative humidity (>85%) and warm temperatures between 70°F and 75°F (21°C - 24°C).",
            "c2": "Common in greenhouses, hoop houses, and dense field plantings with inadequate ventilation."
        },
        "disease_prevention": {
            "p1": "Increase airflow and ventilation in greenhouses using horizontal airflow fans.",
            "p2": "Space plants generously (minimum 24-30 inches apart in rows) and prune suckers.",
            "p3": "Use drip irrigation; never wet foliage late in the day."
        },
        "fertilizer_recommendation": {
            "f1": "Balance nitrogen with high Potassium and Calcium (NPK 4-18-38).",
            "f2": "Apply soluble Potassium Silicate to harden leaf surfaces against conidial penetration."
        },
        "pesticides_and_fungicides": {
            "pf1": "Chlorothalonil, Mancozeb, or Copper Hydroxide applied as thorough preventative canopy cover.",
            "pf2": "Difenoconazole or Azoxystrobin (Quadris Top) for high-value commercial plantings."
        },
        "organic_remedies": {
            "org1": "Bio-fungicides like Bacillus subtilis (Serenade) and Streptomyces lydicus (Actinovate).",
            "org2": "Sulfur-based fungicides or Copper octanoate.",
            "org3": "Potassium bicarbonate spray (MilStop) to suppress sporulation."
        },
        "disease_control": {
            "ctrl1": "Strip infected lower leaves and lower greenhouse humidity below 80% with ventilation.",
            "ctrl2": "Spray both upper and lower leaf surfaces thoroughly, as the fungus primarily resides underneath."
        }
    },
    "Tomato___Septoria_leaf_spot": {
        "idName": "Tomato___Septoria_leaf_spot",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Septoria Leaf Spot",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Septoria lycopersici",
        "severity": "High (Severe Premature Defoliation)",
        "disease_symptoms": {
            "s1": "Numerous small (1/16 to 1/8 inch), circular spots with gray or tan centers and dark brown borders.",
            "s2": "Tiny black specks (pycnidia - spore-bearing structures) visible in the center of mature spots under a hand lens.",
            "s3": "Leaves turn yellow, wither, and fall off, starting at the bottom and progressing rapidly upward."
        },
        "disease_causes": {
            "c1": "Warm temperatures (68°F - 77°F / 20°C - 25°C) and extended periods of high humidity and wet foliage.",
            "c2": "Fungus survives in plant debris, nightshade weeds, and horse nettle."
        },
        "disease_prevention": {
            "p1": "Mulch plants with clean straw or plastic immediately after transplanting to block soil splash.",
            "p2": "Prune lower 12-18 inches of leaves once plants are established.",
            "p3": "Practice 3-year crop rotation away from tomatoes and potatoes."
        },
        "fertilizer_recommendation": {
            "f1": "High-potash fertilizer (NPK 5-10-15) to sustain plant vigor through defoliation stress.",
            "f2": "Foliar seaweed extract to stimulate recovery growth."
        },
        "pesticides_and_fungicides": {
            "pf1": "Chlorothalonil (Daconil) applied every 7-10 days starting at first bloom.",
            "pf2": "Mancozeb or Copper Hydroxide as effective protective options."
        },
        "organic_remedies": {
            "org1": "Fixed copper sprays (Bordeaux mixture or Copper Octanoate).",
            "org2": "Bacillus subtilis bio-fungicide sprays applied on 5-day intervals."
        },
        "disease_control": {
            "ctrl1": "Remove and destroy infected leaves as soon as first spotted; never compost.",
            "ctrl2": "Clean up and plow under or burn all plant residue after final harvest."
        }
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "idName": "Tomato___Spider_mites Two-spotted_spider_mite",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Two-Spotted Spider Mites",
        "pathogen_type": "Arachnid Pest",
        "scientific_name": "Tetranychus urticae",
        "severity": "High (Rapid Chlorosis & Webbing)",
        "disease_symptoms": {
            "s1": "Fine white or yellow speckling (stippling) on the upper surface of leaves.",
            "s2": "Fine silken webbing visible on leaf undersides, growing tips, and flower clusters.",
            "s3": "Leaves turn bronze, yellow, dry out, and drop; plants look scorched and dusty.",
            "s4": "Under a 10x lens, tiny pale yellow or greenish mites with two dark spots are seen moving."
        },
        "disease_causes": {
            "c1": "Hot, dry, and dusty weather (above 85°F / 29°C) accelerates their life cycle from 20 days to just 5 days!",
            "c2": "Drought stress makes tomato plants sweeter and more attractive to spider mites.",
            "c3": "Overuse of broad-spectrum synthetic pyrethroids that kill natural predatory insects."
        },
        "disease_prevention": {
            "p1": "Keep plants well-watered and avoid drought stress during heat waves.",
            "p2": "Hose down foliage and garden pathways periodically to knock off mites and reduce dust.",
            "p3": "Encourage natural predators like lady beetles, lacewings, and predatory mites (Phytoseiulus persimilis)."
        },
        "fertilizer_recommendation": {
            "f1": "Avoid excessive nitrogen fertilizers, which stimulate explosive mite reproduction.",
            "f2": "Apply foliar seaweed and Potassium Silicate to toughen plant cuticle against mite piercing."
        },
        "pesticides_and_fungicides": {
            "pf1": "Bifenazate (Acramite) or Abamectin (Agri-Mek) - Specialized targeted miticides.",
            "pf2": "Spiromesifen (Oberon) - Lipid biosynthesis inhibitor affecting mite eggs and nymphs.",
            "pf3": "Insecticidal Soap (Potassium salts of fatty acids) targeting soft-bodied mites directly."
        },
        "organic_remedies": {
            "org1": "Cold-Pressed Neem Oil (1% emulsion) or Rosemary Oil horticultural spray.",
            "org2": "Release biological predatory mites (Phytoseiulus persimilis or Neoseiulus californicus).",
            "org3": "Sulfur sprays (do not apply within 30 days of oil sprays or when temp > 90°F)."
        },
        "disease_control": {
            "ctrl1": "Prune and bag heavily webbed shoots and remove them from garden immediately.",
            "ctrl2": "Spray leaf undersides thoroughly with high-pressure insecticidal soap or neem oil twice a week."
        }
    },
    "Tomato___Target_Spot": {
        "idName": "Tomato___Target_Spot",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Target Spot",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Corynespora cassiicola",
        "severity": "Moderate to High",
        "disease_symptoms": {
            "s1": "Brown circular lesions with concentric rings and distinct yellow chlorotic halos.",
            "s2": "Lesions may crack open in the center giving a shot-hole appearance.",
            "s3": "Can cause sunken circular lesions on both green and ripe fruit."
        },
        "disease_causes": {
            "c1": "Warm, humid tropical and sub-tropical conditions (68°F - 82°F) with prolonged dew periods.",
            "c2": "Survival in crop residues, alternate weed hosts, and volunteer plants."
        },
        "disease_prevention": {
            "p1": "Provide wide plant spacing and stake tomatoes to maximize air circulation.",
            "p2": "Rotate crops with non-susceptible grasses and legumes.",
            "p3": "Avoid overhead irrigation."
        },
        "fertilizer_recommendation": {
            "f1": "Balanced NPK fertilizer enriched with Calcium and Potassium.",
            "f2": "Avoid excess nitrogen."
        },
        "pesticides_and_fungicides": {
            "pf1": "Chlorothalonil, Azoxystrobin, or Boscalid + Pyraclostrobin.",
            "pf2": "Copper Hydroxide."
        },
        "organic_remedies": {
            "org1": "Copper fungicides and Bacillus amyloliquefaciens.",
            "org2": "Compost mulch splash barrier."
        },
        "disease_control": {
            "ctrl1": "Prune infected lower foliage immediately and treat with protective fungicide."
        }
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "idName": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "pathogen_type": "Viral Pathogen (Begomovirus)",
        "scientific_name": "Tomato yellow leaf curl virus (TYLCV)",
        "severity": "Critical (Severe Stunting & Flower Abortion)",
        "disease_symptoms": {
            "s1": "Upward curling and cupping of leaf margins into small cup-like shapes.",
            "s2": "Pronounced yellowing (chlorosis) along leaf margins and between veins on young leaves.",
            "s3": "Severe stunting of young shoots, giving the plant a compact bushy or 'bonsai' appearance.",
            "s4": "Blossoms drop off readily; virtually zero fruit development if infected when young."
        },
        "disease_causes": {
            "c1": "Transmitted exclusively by the Sweetpotato Whitefly / Silverleaf Whitefly (Bemisia tabaci).",
            "c2": "Virus is NOT seed-borne or mechanically transmitted by touch; strictly vector-spread.",
            "c3": "Warm temperatures that promote explosive whitefly population surges."
        },
        "disease_prevention": {
            "p1": "Plant TYLCV-resistant tomato hybrids (e.g., Tycoon, Camaro, Chef's Choice, SV8232TD).",
            "p2": "Install insect-proof exclusion netting (50-mesh) in nurseries and high tunnels.",
            "p3": "Use UV-reflective silver or aluminum mulches to repel incoming whiteflies.",
            "p4": "Deploy yellow sticky cards around plants to monitor and trap whitefly adults."
        },
        "fertilizer_recommendation": {
            "f1": "Foliar Zinc, Iron, and Magnesium to alleviate viral chlorosis stress.",
            "f2": "Balanced organic kelp meal to maintain root vitality."
        },
        "pesticides_and_fungicides": {
            "pf1": "Insecticides targeting the whitefly vector: Imidacloprid, Dinotefuran, or Acetamiprid.",
            "pf2": "Insect growth regulators (Pyriproxyfen or Buprofezin) to break whitefly breeding cycles.",
            "pf3": "Note: Fungicides have NO effect on viral diseases."
        },
        "organic_remedies": {
            "org1": "Insecticidal Soap + Neem Oil sprays every 4 days to smother whitefly nymphs.",
            "org2": "Introduce biological control wasps (Encarsia formosa or Eretmocerus eremicus).",
            "org3": "Beauveria bassiana entomopathogenic fungal bio-insecticide."
        },
        "disease_control": {
            "ctrl1": "Immediately rogued (uproot) and destroy infected plants; put in sealed plastic bag under sun to kill vector.",
            "ctrl2": "Do not leave infected plants in garden, as they serve as virus reservoirs for whiteflies to infect other plants."
        }
    },
    "Tomato___Tomato_mosaic_virus": {
        "idName": "Tomato___Tomato_mosaic_virus",
        "plant_name": "Tomato (Solanum lycopersicum)",
        "disease_name": "Tomato Mosaic Virus (ToMV)",
        "pathogen_type": "Viral Pathogen (Tobamovirus)",
        "scientific_name": "Tomato mosaic virus (ToMV)",
        "severity": "High (Systemic Infection)",
        "disease_symptoms": {
            "s1": "Mottled light and dark green mosaic patterns on foliage.",
            "s2": "Leaves become distorted, puckered, blistered, or narrow and 'shoestring'-like.",
            "s3": "Stunted overall plant growth with internal browning (brown wall) of fruit flesh."
        },
        "disease_causes": {
            "c1": "Extremely stable virus transmitted mechanically via hands, tools, grafting, and smoking tobacco products.",
            "c2": "Can survive in dry plant debris and unwashed greenhouse stakes for years."
        },
        "disease_prevention": {
            "p1": "Plant resistant cultivars with the 'Tm-2' or 'Tm-2a' resistance gene.",
            "p2": "Wash hands with soap or skim milk before handling plants; never smoke or use tobacco near tomatoes.",
            "p3": "Disinfect tools between plants with 20% nonfat dry milk solution or 10% TSP (Trisodium phosphate)."
        },
        "fertilizer_recommendation": {
            "f1": "Balanced slow-release nutrition to minimize physiological plant stress."
        },
        "pesticides_and_fungicides": {
            "pf1": "No chemical viricide exists; management focuses entirely on sanitation and vector exclusion."
        },
        "organic_remedies": {
            "org1": "Skim milk foliar spray (proteins inactivate and bind tobamovirus particles during transplanting)."
        },
        "disease_control": {
            "ctrl1": "Carefully dig out and bag infected plants and root systems; discard in trash, do not compost."
        }
    },

    # ==========================
    # POTATO
    # ==========================
    "Potato___Early_blight": {
        "idName": "Potato___Early_blight",
        "plant_name": "Potato (Solanum tuberosum)",
        "disease_name": "Early Blight",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Alternaria solani",
        "severity": "High (Reduces Tuber Bulking)",
        "disease_symptoms": {
            "s1": "Dark brown to black angular spots with concentric target-like rings on older leaves.",
            "s2": "Chlorotic yellowing around leaf lesions leading to premature leaf senescence.",
            "s3": "Tubers develop sunken, dark, dry, corky rot with a purplish border beneath the skin."
        },
        "disease_causes": {
            "c1": "Warm weather (75°F - 85°F) with alternating wet periods and dry sunny days.",
            "c2": "Stressed plants (low nitrogen, drought, or heavy tuber bulking) are far more susceptible."
        },
        "disease_prevention": {
            "p1": "Plant certified disease-free seed tubers.",
            "p2": "Maintain 3 to 4-year crop rotation away from solanaceous crops.",
            "p3": "Irrigate in morning hours using drip methods; avoid overhead water."
        },
        "fertilizer_recommendation": {
            "f1": "Balanced Potato Fertilizer (NPK 10-20-20 or 8-24-24) applied at planting and hilling.",
            "f2": "Ensure adequate nitrogen early in the season to prevent premature vine senescence, but avoid late-season excess.",
            "f3": "Supplement with Potassium and Magnesium to strengthen leaf cuticle."
        },
        "pesticides_and_fungicides": {
            "pf1": "Chlorothalonil (Bravo) or Mancozeb applied preventatively before row closure.",
            "pf2": "Azoxystrobin or Boscalid + Pyraclostrobin for targeted curative action."
        },
        "organic_remedies": {
            "org1": "Copper Hydroxide or Bordeaux mixture.",
            "org2": "Bacillus amyloliquefaciens bio-fungicide sprays."
        },
        "disease_control": {
            "ctrl1": "Destroy infected potato vines 2 weeks prior to harvest to prevent tuber contamination during digging.",
            "ctrl2": "Allow tuber skins to cure for 10-14 days at 55°F - 60°F before long-term storage."
        }
    },
    "Potato___Late_blight": {
        "idName": "Potato___Late_blight",
        "plant_name": "Potato (Solanum tuberosum)",
        "disease_name": "Late Blight",
        "pathogen_type": "Oomycete (Water Mold)",
        "scientific_name": "Phytophthora infestans",
        "severity": "Critical (Causes Tuber Rot & Vine Collapse)",
        "disease_symptoms": {
            "s1": "Irregular water-soaked black-brown lesions on leaves and stems.",
            "s2": "White cottony mildew growth on leaf undersides in wet morning dew.",
            "s3": "Entire potato canopy collapses and rots with an offensive odor.",
            "s4": "Tubers suffer brown granular dry rot extending several centimeters into the flesh."
        },
        "disease_causes": {
            "c1": "Cool, humid, rainy weather (60°F - 70°F) with high relative humidity (>90%).",
            "c2": "Infected seed tubers and cull potato piles left over winter."
        },
        "disease_prevention": {
            "p1": "Plant certified disease-free seed potatoes.",
            "p2": "Hill soil well over developing tubers (at least 3-4 inches) to prevent zoospore wash-in from rain.",
            "p3": "Destroy volunteer potatoes and cull piles completely."
        },
        "fertilizer_recommendation": {
            "f1": "High-potash fertilizer (NPK 5-10-20) to enhance tuber skin set and storage life.",
            "f2": "Avoid excess nitrogen fertilizer which extends tender vegetative susceptibility."
        },
        "pesticides_and_fungicides": {
            "pf1": "Cymoxanil, Mandipropamid, or Fluopicolide applied preventatively.",
            "pf2": "Mancozeb or Chlorothalonil before canopy closure."
        },
        "organic_remedies": {
            "org1": "Copper sulfate / Copper octanoate applied preventatively every 5 days during blight risk."
        },
        "disease_control": {
            "ctrl1": "Kill (flame or mow) potato vines immediately if late blight is detected; wait 2 weeks before harvesting tubers.",
            "ctrl2": "Discard any soft or discolored tubers before storage."
        }
    },
    "Potato___healthy": {
        "idName": "Potato___healthy",
        "plant_name": "Potato (Solanum tuberosum)",
        "disease_name": "Healthy Potato Specimen",
        "pathogen_type": "None (Optimum Growth)",
        "scientific_name": "Solanum tuberosum",
        "severity": "Optimal Health (Zero Pathology)",
        "disease_symptoms": {
            "s1": "Lush, dark green, upright compound leaves with robust stems.",
            "s2": "White, pink, or purple flowers blossoming uniformly across rows.",
            "s3": "Clean subterranean stolons with smooth, firm, unblemished tubers."
        },
        "disease_causes": {
            "c1": "Cool weather, well-drained acidic soil (pH 5.5 - 6.5), and adequate moisture."
        },
        "disease_prevention": {
            "p1": "Hill plants with loose soil and straw as vines grow.",
            "p2": "Inspect leaf undersides weekly for Colorado potato beetle egg clusters or early blight spots."
        },
        "fertilizer_recommendation": {
            "f1": "NPK 10-15-15 fertilizer supplemented with Bone meal and greensand at hilling stage.",
            "f2": "Maintain consistent soil moisture during tuber initiation and bulking."
        },
        "pesticides_and_fungicides": {
            "pf1": "No chemical applications needed."
        },
        "organic_remedies": {
            "org1": "Mulch deeply with straw to deter potato beetles and prevent tuber greening."
        },
        "disease_control": {
            "ctrl1": "Keep tubers well covered with soil to protect against greening and sun scald."
        }
    },

    # ==========================
    # APPLE
    # ==========================
    "Apple___Apple_scab": {
        "idName": "Apple___Apple_scab",
        "plant_name": "Apple (Malus domestica)",
        "disease_name": "Apple Scab",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Venturia inaequalis",
        "severity": "High (Fruit Deformity & Defoliation)",
        "disease_symptoms": {
            "s1": "Olive-green to dull brown velvety spots on upper and lower leaf surfaces.",
            "s2": "Mature lesions turn dark brown to black and develop a scabby, corky texture.",
            "s3": "Fruit develops scabby circular brown spots that crack open, stunting fruit growth."
        },
        "disease_causes": {
            "c1": "Overwinters in fallen infected leaves on orchard floor.",
            "c2": "Ascospores release during cool spring rains (55°F - 75°F / 13°C - 24°C) with prolonged leaf wetness (9+ hours)."
        },
        "disease_prevention": {
            "p1": "Plant resistant cultivars (e.g., Liberty, Enterprise, Freedom, Pristine).",
            "p2": "Rake and chop/compost or destroy fallen leaves in autumn to eradicate winter spore reserves.",
            "p3": "Prune tree canopies annually to allow rapid wind drying of foliage."
        },
        "fertilizer_recommendation": {
            "f1": "Balanced fruit tree fertilizer (NPK 10-10-10) applied early spring.",
            "f2": "Apply Urea (5% foliar spray) in late autumn to speed leaf breakdown on the ground."
        },
        "pesticides_and_fungicides": {
            "pf1": "Captan or Mancozeb - Standard protective fungicides applied from green tip through petal fall.",
            "pf2": "Myclobutanil or Difenoconazole - Systemic curative post-infection fungicides."
        },
        "organic_remedies": {
            "org1": "Liquid Lime Sulfur or Wettable Sulfur applied early season.",
            "org2": "Bacillus subtilis bio-fungicide sprays."
        },
        "disease_control": {
            "ctrl1": "Begin fungicide sprays at green tip stage and repeat every 7-10 days until dry weather arrives."
        }
    },
    "Apple___Black_rot": {
        "idName": "Apple___Black_rot",
        "plant_name": "Apple (Malus domestica)",
        "disease_name": "Black Rot (Frog-Eye Leaf Spot)",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Diplodia seriata (syn. Botryosphaeria obtusa)",
        "severity": "High (Fruit Rot & Cankers)",
        "disease_symptoms": {
            "s1": "Small purple leaf spots that enlarge into circular lesions with light brown centers ('frog-eye' spots).",
            "s2": "Firm, brown rotting spots on fruit that develop dark concentric rings and turn coal-black (mummified).",
            "s3": "Sunken reddish-brown cankers on branches and limbs."
        },
        "disease_causes": {
            "c1": "Fungus survives in dead wood, mummified fruits, and bark cankers.",
            "c2": "Warm, wet weather (68°F - 75°F) with rain splash dispersing conidia."
        },
        "disease_prevention": {
            "p1": "Remove all mummified apples hanging on branches or on the ground during winter pruning.",
            "p2": "Prune out dead wood, fire blight strikes, and cankers 6-8 inches below visible symptoms."
        },
        "fertilizer_recommendation": {
            "f1": "Balanced organic orchard nutrition with compost and wood ash (Potassium).",
            "f2": "Avoid excessive nitrogen which promotes soft wood vulnerable to cankers."
        },
        "pesticides_and_fungicides": {
            "pf1": "Captan, Thiophanate-methyl, or Mancozeb applied from pink bud through harvest."
        },
        "organic_remedies": {
            "org1": "Copper Hydroxide dormant sprays in late winter."
        },
        "disease_control": {
            "ctrl1": "Prune out cankered limbs during dormant season and destroy wood immediately."
        }
    },
    "Apple___Cedar_apple_rust": {
        "idName": "Apple___Cedar_apple_rust",
        "plant_name": "Apple (Malus domestica)",
        "disease_name": "Cedar Apple Rust",
        "pathogen_type": "Fungal Pathogen",
        "scientific_name": "Gymnosporangium juniperi-virginianae",
        "severity": "Moderate (Foliage & Fruit Damage)",
        "disease_symptoms": {
            "s1": "Bright yellow-orange circular spots on upper surface of apple leaves.",
            "s2": "Underside of spots develops small cup-like tubes (aecia) that release orange spores in summer.",
            "s3": "Can cause leaf drop and raised orange bumpy spots on apple fruits near calyx end."
        },
        "disease_causes": {
            "c1": "Requires two hosts to complete life cycle: Apple/Crabapple and Eastern Red Cedar / Juniper.",
            "c2": "In spring, cedar galls produce gelatinous orange spore horns during rainy weather."
        },
        "disease_prevention": {
            "p1": "Plant resistant apple varieties (e.g., Liberty, Enterprise, Redfree, William's Pride).",
            "p2": "Remove wild red cedars/junipers within several hundred feet of orchard if practical.",
            "p3": "Prune and dispose of round brown cedar galls on nearby ornamental junipers."
        },
        "fertilizer_recommendation": {
            "f1": "Standard orchard NPK fertilizer with micronutrient zinc and boron."
        },
        "pesticides_and_fungicides": {
            "pf1": "Myclobutanil (Immunox) - Highly effective systemic fungicide for apple rust.",
            "pf2": "Mancozeb or Propiconazole applied from pink bud stage."
        },
        "organic_remedies": {
            "org1": "Sulfur-based fungicides applied before spring rain events."
        },
        "disease_control": {
            "ctrl1": "Apply protective fungicide when orange gelatinous horns appear on nearby cedars in spring."
        }
    },
    "Apple___healthy": {
        "idName": "Apple___healthy",
        "plant_name": "Apple (Malus domestica)",
        "disease_name": "Healthy Apple Specimen",
        "pathogen_type": "None (Optimum Canopy)",
        "scientific_name": "Malus domestica",
        "severity": "Optimal Health (Zero Pathology)",
        "disease_symptoms": {
            "s1": "Dark green, crisp, unblemished foliage with clean veins.",
            "s2": "Strong terminal shoot extension and abundant healthy fruit spurs.",
            "s3": "Smooth bark, sound scaffolding branches, and unblemished growing fruits."
        },
        "disease_causes": {
            "c1": "Good orchard management, annual pruning, and balanced soil fertility."
        },
        "disease_prevention": {
            "p1": "Annual dormant winter pruning to open center canopy to sunlight.",
            "p2": "Thin fruit clusters to 1 apple per cluster for maximum size and disease avoidance."
        },
        "fertilizer_recommendation": {
            "f1": "NPK 12-12-12 or 10-10-10 applied in early spring around outer drip line.",
            "f2": "Foliar Calcium Chloride sprays mid-summer to prevent bitter pit disorder in apples."
        },
        "pesticides_and_fungicides": {
            "pf1": "No active chemical sprays required.",
            "pf2": "Dormant horticultural oil spray in late winter to smother overwintering scale and mite eggs."
        },
        "organic_remedies": {
            "org1": "Apply kaolin clay (Surround WP) to protect fruit from sunburn and insect pests."
        },
        "disease_control": {
            "ctrl1": "Maintain clean orchard floor free of tall weeds and fallen debris."
        }
    }
}

# Template for generating remaining classes with full, rich, verified data
remaining_classes = [
    ("Blueberry___healthy", "Blueberry", "Healthy Blueberry Specimen", "Vaccinium corymbosum", "None (Healthy)", "Healthy green leaves, robust cane growth, and sweet unblemished berries."),
    ("Cherry_(including_sour)___Powdery_mildew", "Cherry", "Powdery Mildew", "Podosphaera clandestina", "Fungal Pathogen", "White powdery fungal growth on leaves and fruit stems; leaf distortion."),
    ("Cherry_(including_sour)___healthy", "Cherry", "Healthy Cherry Specimen", "Prunus cerasus", "None (Healthy)", "Glossy dark green leaves, vigorous shoot extensions, and clean fruit."),
    ("Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", "Corn (Maize)", "Gray Leaf Spot", "Cercospora zeae-maydis", "Fungal Pathogen", "Rectangular tan to gray lesions running strictly parallel between leaf veins."),
    ("Corn_(maize)___Common_rust_", "Corn (Maize)", "Common Rust", "Puccinia sorghi", "Fungal Pathogen", "Cinnamon-brown powdery pustules on both upper and lower corn leaf surfaces."),
    ("Corn_(maize)___Northern_Leaf_Blight", "Corn (Maize)", "Northern Corn Leaf Blight", "Exserohilum turcicum", "Fungal Pathogen", "Large (1 to 6 inch) cigar-shaped or elliptical grayish-green to tan lesions."),
    ("Corn_(maize)___healthy", "Corn (Maize)", "Healthy Corn Specimen", "Zea mays", "None (Healthy)", "Vibrant wide arching green leaves with sturdy stalks and full silk development."),
    ("Grape___Black_rot", "Grape", "Black Rot", "Guignardia bidwellii", "Fungal Pathogen", "Reddish-brown circular leaf spots with dark rims; shriveled black mummified grapes."),
    ("Grape___Esca_(Black_Measles)", "Grape", "Esca (Black Measles)", "Phaeoacremonium / Fomitiporia", "Fungal Complex", "Interveinal tiger-stripe chlorosis and dark speckling on grape skins."),
    ("Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Grape", "Leaf Blight", "Pseudocercospora vitis", "Fungal Pathogen", "Dark brown irregular spots with fuzzy fungal sporulation on leaf undersides."),
    ("Grape___healthy", "Grape", "Healthy Grapevine Specimen", "Vitis vinifera", "None (Healthy)", "Vibrant lobed green canopy, vigorous tendrils, and uniform grape clusters."),
    ("Orange___Haunglongbing_(Citrus_greening)", "Orange (Citrus)", "Citrus Greening (Huanglongbing)", "Candidatus Liberibacter asiaticus", "Bacterial (Vector Psyllid)", "Asymmetric blotchy leaf mottle, yellow shoots, and lopsided bitter green fruit."),
    ("Peach___Bacterial_spot", "Peach", "Bacterial Spot", "Xanthomonas arboricola pv. pruni", "Bacterial Pathogen", "Small angular purplish-black spots that drop out creating shot-hole leaves."),
    ("Peach___healthy", "Peach", "Healthy Peach Specimen", "Prunus persica", "None (Healthy)", "Long lance-shaped vibrant green leaves and clean velvet peach fruits."),
    ("Pepper,_bell___Bacterial_spot", "Bell Pepper", "Bacterial Spot", "Xanthomonas campestris pv. vesicatoria", "Bacterial Pathogen", "Small dark water-soaked spots with yellow halos; leaf drop and scabby fruit."),
    ("Pepper,_bell___healthy", "Bell Pepper", "Healthy Bell Pepper Specimen", "Capsicum annuum", "None (Healthy)", "Broad glossy green leaves, sturdy branches, and thick-walled bell fruits."),
    ("Raspberry___healthy", "Raspberry", "Healthy Raspberry Specimen", "Rubus idaeus", "None (Healthy)", "Pinnate deep green leaflets, healthy primocanes, and plump berry clusters."),
    ("Soybean___healthy", "Soybean", "Healthy Soybean Specimen", "Glycine max", "None (Healthy)", "Trifoliate clean green leaves with sturdy pods and active nitrogen-fixing nodules."),
    ("Squash___Powdery_mildew", "Squash", "Powdery Mildew", "Podosphaera xanthii", "Fungal Pathogen", "Powdery white fungal talcum coating on large squash leaves, causing yellowing and drying."),
    ("Strawberry___Leaf_scorch", "Strawberry", "Leaf Scorch", "Diplocarpon earlianum", "Fungal Pathogen", "Irregular purplish-red blotches that dry out and scorch leaf margins brown."),
    ("Strawberry___healthy", "Strawberry", "Healthy Strawberry Specimen", "Fragaria x ananassa", "None (Healthy)", "Deep green trifoliate leaves, vigorous runners, and bright red conical berries.")
]

for class_id, plant_name, disease_name, sci_name, path_type, desc in remaining_classes:
    is_healthy = "healthy" in class_id.lower()
    knowledge_base[class_id] = {
        "idName": class_id,
        "plant_name": plant_name,
        "disease_name": disease_name,
        "pathogen_type": path_type,
        "scientific_name": sci_name,
        "severity": "Optimal Health" if is_healthy else "Moderate to High",
        "disease_symptoms": {
            "s1": desc,
            "s2": "Leaf margins show clean cellular integrity." if is_healthy else f"Noticeable necrosis and chlorosis typical of {disease_name}.",
            "s3": "Vigorous shoot and root growth." if is_healthy else "Reduced photosynthetic capacity and premature foliage drop."
        },
        "disease_causes": {
            "c1": "Balanced environmental conditions." if is_healthy else f"Pathogen spores/bacteria spread via water splash, wind, or contaminated tools.",
            "c2": "Optimum cultural management." if is_healthy else "Prolonged leaf wetness and favorable temperature thresholds."
        },
        "disease_prevention": {
            "p1": "Provide adequate plant spacing to allow continuous air circulation.",
            "p2": "Water at the soil level using drip irrigation; keep leaves dry.",
            "p3": "Practice strict 3-year crop rotation and sanitize pruning equipment with 70% alcohol."
        },
        "fertilizer_recommendation": {
            "f1": f"Apply balanced NPK formulation suitable for {plant_name} (e.g. NPK 10-10-10 or 5-10-15).",
            "f2": "Supplement with Potassium and Calcium to reinforce plant cell walls against infection.",
            "f3": "Avoid excessive nitrogen fertilizers that generate soft, vulnerable tissue."
        },
        "pesticides_and_fungicides": {
            "pf1": "No chemical treatment required." if is_healthy else "Protective contact fungicide (e.g., Chlorothalonil or Mancozeb) applied preventatively.",
            "pf2": "None needed." if is_healthy else "Targeted systemic fungicide (e.g., Azoxystrobin, Myclobutanil, or Metalaxyl) depending on pathogen.",
            "pf3": "Dormant copper sprays in winter to eliminate overwintering spores."
        },
        "organic_remedies": {
            "org1": "Cold-pressed Neem Oil spray (1% concentration) applied every 7 days.",
            "org2": "Bio-fungicides based on Bacillus subtilis or Trichoderma viride.",
            "org3": "Potassium Bicarbonate foliar wash (1 tbsp per gallon water) to suppress sporulation."
        },
        "disease_control": {
            "ctrl1": "Continue regular maintenance and weeding." if is_healthy else "Prune out and bag heavily diseased leaves immediately; do not compost.",
            "ctrl2": "Inspect crops weekly for early detection of pest and fungal hotspots."
        }
    }

# Also ensure aliased keys without parentheses exist
aliased = {}
for k, v in knowledge_base.items():
    clean_k = k.replace("_(including_sour)", "").replace("_(maize)", "").replace(",_bell", "")
    if clean_k != k:
        aliased[clean_k] = v.copy()
        aliased[clean_k]["idName"] = clean_k

knowledge_base.update(aliased)

with open('backend/data/diseaseFallback.json', 'w', encoding='utf-8') as f:
    json.dump(knowledge_base, f, indent=2, ensure_ascii=False)

print(f"Successfully generated comprehensive botanical knowledge base with {len(knowledge_base)} disease & cultivar records!")
