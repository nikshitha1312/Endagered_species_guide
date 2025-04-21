def get_animal_data(animal_name):
    """Return habitat and other information for detected animals."""
    animal_database = {
        "monkey": {
            "animal_class": "Mammal",
            "population": "Various species, total unknown",
            "weight": "1.5-36 kg",
            "length": "0.14-1 m",
            "height": "0.15-1 m",
            "habitats": ["Tropical forests", "Rainforests", "Mountains", "Savannas"],
            "status": "Varies by species",
            "country": "Africa, Asia, Central and South America",
            "places": ["Amazon Rainforest", "Congo Basin", "Indonesian Islands", "Indian Subcontinent"],
            "factor": "Habitat loss and illegal wildlife trade",
            "measures_taken": ["Protected areas", "Anti-poaching efforts", "Conservation programs"]
        },
        "hamster": {
            "animal_class": "Mammal",
            "population": "Stable in captivity, declining in wild",
            "weight": "0.03-0.5 kg",
            "length": "5-15 cm",
            "height": "2-4 cm",
            "habitats": ["Deserts", "Steppes", "Pine forests", "Dunes"],
            "status": "Least Concern (domestic), Some wild species Vulnerable",
            "country": "Syria, Greece, Romania, Belgium",
            "places": ["Northern Syria", "Southern Turkey", "Romania", "Belgium"],
            "factor": "Habitat loss and agricultural expansion",
            "measures_taken": ["Breeding programs", "Habitat protection", "Research studies"]
        },
        "cheetah": {
            "animal_class": "Mammal",
            "population": "Around 7,100",
            "weight": "21-72 kg",
            "length": "1.1-1.5 m",
            "height": "70-90 cm",
            "habitats": ["Savannas", "Grasslands", "Open woodlands"],
            "status": "Vulnerable",
            "country": "Africa",
            "places": ["Namibia", "Botswana", "Kenya", "Tanzania"],
            "factor": "Habitat loss and human conflict",
            "measures_taken": ["Protected areas", "Conservation programs", "Anti-poaching efforts"]
        },
        "leopard": {
            "animal_class": "Mammal",
            "population": "Around 250,000",
            "weight": "17-90 kg",
            "length": "0.9-1.9 m",
            "height": "60-70 cm",
            "habitats": ["Forests", "Grasslands", "Mountains", "Deserts"],
            "status": "Vulnerable",
            "country": "Africa and Asia",
            "places": ["Sub-Saharan Africa", "India", "Sri Lanka", "Southeast Asia"],
            "factor": "Habitat loss and poaching",
            "measures_taken": ["Protected reserves", "Anti-poaching units", "Habitat conservation"]
        },
        "tiger": {
            "animal_class": "Mammal",
            "population": "3,900",
            "weight": "180-300 kg",
            "length": "2.7-3.3 m",
            "height": "0.9-1.1 m",
            "habitats": ["Tropical forests", "Grasslands", "Mangrove swamps"],
            "status": "Endangered",
            "country": "India and Southeast Asia",
            "places": ["Sundarbans", "Ranthambore", "Kaziranga", "Corbett"],
            "factor": "Habitat loss and poaching",
            "measures_taken": ["Tiger reserves", "Anti-poaching patrols", "Habitat conservation"]
        },
        "lion": {
            "animal_class": "Mammal",
            "population": "Around 20,000",
            "weight": "130-190 kg (male), 110-140 kg (female)",
            "length": "1.7-2.5 m",
            "height": "1.2 m",
            "habitats": ["Savannas", "Grasslands", "Open woodlands"],
            "status": "Vulnerable",
            "country": "Africa",
            "places": ["Tanzania", "South Africa", "Kenya", "Botswana"],
            "factor": "Habitat loss and human conflict",
            "measures_taken": ["Protected areas", "Anti-poaching efforts", "Community conservation"]
        },
        "jaguar": {
            "animal_class": "Mammal",
            "population": "Around 173,000",
            "weight": "56-96 kg",
            "length": "1.12-1.85 m",
            "height": "63-75 cm",
            "habitats": ["Rainforests", "Wetlands", "Grasslands"],
            "status": "Near Threatened",
            "country": "Central and South America",
            "places": ["Amazon Basin", "Pantanal", "Mexico", "Argentina"],
            "factor": "Habitat fragmentation and hunting",
            "measures_taken": ["Protected corridors", "Anti-poaching measures", "Habitat preservation"]
        },
        "elephant": {
            "animal_class": "Mammal",
            "population": "415,000 (African), 40,000-50,000 (Asian)",
            "weight": "2,700-6,000 kg",
            "length": "5.5-6.5 m",
            "height": "2.4-3.7 m",
            "habitats": ["Savannas", "Forests", "Deserts", "Marshes"],
            "status": "Vulnerable",
            "country": "Africa and Asia",
            "places": ["Botswana", "Tanzania", "Zimbabwe", "Kenya", "India", "Sri Lanka"],
            "factor": "Habitat loss and poaching",
            "measures_taken": ["Anti-poaching efforts", "Protected areas", "Conservation programs"]
        },
        "zebra": {
            "animal_class": "Mammal",
            "population": "Around 750,000",
            "weight": "220-450 kg",
            "length": "2-2.5 m",
            "height": "1.1-1.5 m",
            "habitats": ["Savannas", "Grasslands", "Woodlands"],
            "status": "Least Concern",
            "country": "Africa",
            "places": ["Kenya", "Tanzania", "South Africa", "Ethiopia"],
            "factor": "Habitat loss and hunting",
            "measures_taken": ["National parks", "Protected reserves", "Conservation efforts"]
        },
        "giraffe": {
            "animal_class": "Mammal",
            "population": "Around 117,000",
            "weight": "800-1,900 kg",
            "length": "4.3-5.7 m",
            "height": "4.3-5.7 m",
            "habitats": ["Savannas", "Grasslands", "Woodlands"],
            "status": "Vulnerable",
            "country": "Africa",
            "places": ["Tanzania", "Kenya", "Uganda", "Namibia"],
            "factor": "Habitat fragmentation and hunting",
            "measures_taken": ["Protected areas", "Anti-poaching measures", "Breeding programs"]
        },
        "hippopotamus": {
            "animal_class": "Mammal",
            "population": "115,000-130,000",
            "weight": "1,500-1,800 kg",
            "length": "3.3-3.5 m",
            "height": "1.5 m",
            "habitats": ["Rivers", "Lakes", "Wetlands"],
            "status": "Vulnerable",
            "country": "Africa",
            "places": ["Tanzania", "Zambia", "South Africa", "Uganda"],
            "factor": "Habitat loss and hunting",
            "measures_taken": ["Protected waterways", "Anti-poaching efforts", "Habitat protection"]
        },
        "rhinoceros": {
            "animal_class": "Mammal",
            "population": "27,000 (all species combined)",
            "weight": "500-2,300 kg",
            "length": "3.5-4.6 m",
            "height": "1.5-1.8 m",
            "habitats": ["Savannas", "Grasslands", "Forests"],
            "status": "Critically Endangered",
            "country": "Africa and Asia",
            "places": ["South Africa", "Namibia", "Kenya", "India"],
            "factor": "Poaching and habitat loss",
            "measures_taken": ["Anti-poaching units", "Protected areas", "Breeding programs"]
        },
        "kangaroo": {
            "animal_class": "Mammal",
            "population": "Around 50 million",
            "weight": "20-90 kg",
            "length": "1.2-2.4 m",
            "height": "1-3 m when standing",
            "habitats": ["Grasslands", "Forests", "Plains"],
            "status": "Least Concern",
            "country": "Australia",
            "places": ["Eastern Australia", "Western Australia", "Tasmania"],
            "factor": "Habitat modification and hunting",
            "measures_taken": ["Protected areas", "Population management", "Habitat conservation"]
        },
        "koala": {
            "animal_class": "Mammal",
            "population": "Around 300,000",
            "weight": "4-14 kg",
            "length": "60-85 cm",
            "height": "20-25 cm when sitting",
            "habitats": ["Eucalyptus forests", "Coastal areas", "Inland regions"],
            "status": "Vulnerable",
            "country": "Australia",
            "places": ["Queensland", "New South Wales", "Victoria", "South Australia"],
            "factor": "Habitat loss and disease",
            "measures_taken": ["Habitat protection", "Disease management", "Rescue programs"]
        }
    }
    
    # Convert animal name to lowercase for case-insensitive matching
    animal_name = animal_name.lower()
    
    # Return data if animal exists in database, otherwise return default data
    return animal_database.get(animal_name, {
        "animal_class": "Unknown",
        "population": "Unknown",
        "weight": "Unknown",
        "length": "Unknown",
        "height": "Unknown",
        "habitats": ["Unknown"],
        "status": "Unknown",
        "country": "Unknown",
        "places": [],
        "factor": "Unknown",
        "measures_taken": []
    }) 