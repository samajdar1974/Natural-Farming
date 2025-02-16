import streamlit as st


practices = {"Gangetic Plains": {
        "Field Crops": {
            "Jute": {
                "Varieties": "JRO 8432, JRO 204, Bidhan Rupali",
                "Land Preparation": "Fine tilth with 3-4 plowings; apply Jeevamrit (200 liters/acre).",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Maintain proper drainage to prevent waterlogging.",
                "Weed Control": "Manual weeding at 20 and 40 days.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                "Pest and Disease Management": "Use Neem Oil (5 ml/liter) every 15 days.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest at pod maturity stage and dry before storage.",
                "Image": "https://example.com/jute_image.jpg"
            },

            "Rice": {
                "Varieties": "Swarna, MTU-7029, IR-64",
                "Land Preparation": "Level the field and apply 200 liters/acre of Jeevamrit.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Maintain 2-5 cm standing water during tillering and grain filling.",
                "Weed Control": "Manual weeding at 20, 40, and 60 days.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 10 days.",
                "Pest and Disease Management": "Neem Oil (5 ml/liter) every 15 days.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when 80-90% of grains turn golden yellow.",
                "Image": "https://example.com/rice_image.jpg"
            },
            "Wheat": {
                "Varieties": "",
                "Land Preparation": "Plow the field 2-3 times to achieve fine tilth and incorporate organic matter.",
                "Seed Treatment": "Treat seeds with Beejamrit (5 liters solution per acre of seeds) and shade-dry before sowing.",
                "Water Management": "Irrigate during critical stages: crown root initiation, booting, and grain filling.",
                "Weed Control": "Perform hand weeding at 25-30 days after sowing.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15-20 days.",
                "Pest and Disease Management": "Spray Neem Oil (5 ml/liter) every 15 days. Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when grains are hard and moisture content is 12-14%.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Maize": {
                "Varieties": "",
                "Land Preparation": "Plow and harrow the field to ensure fine tilth. Incorporate 2 tons/acre of compost.",
                "Seed Treatment": "Soak seeds in Beejamrit (5 liters solution per acre) for 8 hours before sowing.",
                "Water Management": "Irrigate during key growth stages such as germination, knee-high, and tasseling.",
                "Weed Control": "Perform manual weeding 20 and 40 days after sowing.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                "Pest and Disease Management": "Use Neem Oil (5 ml/liter) weekly to manage pests.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when cobs are fully mature and grains are hard.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Blackgram": {
                "Varieties": "PU 31, T 9, Pant U 30",
                "Land Preparation": "Plow field twice and incorporate compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate during flowering and pod formation.",
                "Weed Control": "Manual weeding at 20 and 35 days.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                "Pest and Disease Management": "Use Neem Oil (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when 80% of pods turn black.",
                "Image": "https://example.com/blackgram_image.jpg"
            },
            "Greengram": {
                "Varieties": "PDM 84, IPM 2-3",
                "Land Preparation": "Prepare fine tilth and incorporate compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate only during flowering and pod filling.",
                "Weed Control": "Hand weeding at 20 and 40 days.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) monthly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when pods turn yellow.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Mustard": {
                "Varieties": "Pusa Bold, Rohini, Kranti",
                "Land Preparation": "Fine tilth and well-drained soil required.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at flowering and pod filling stages.",
                "Weed Control": "Hand weeding at 25 and 50 days.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                "Pest and Disease Management": "Use Neem Oil (5 ml/liter) every 10 days.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when 75% of pods turn yellow.",
                "Image": "https://example.com/mustard_image.jpg"
            },
            "Lentil": {
                "Varieties": "Pant L 406, KLS 218",
                "Land Preparation": "Plow 2-3 times to achieve a fine tilth and apply compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at flowering and pod-filling stages.",
                "Weed Control": "Perform manual weeding at 20 and 40 days.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                "Pest and Disease Management": "Neem Oil (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when pods turn yellow and dry.",
                "Image": "https://example.com/lentil_image.jpg"
            },
            "Sesamum": {
                "Varieties": "TIL 35, Pragati",
                "Land Preparation": "Prepare well-drained sandy loam soil with compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at flowering and capsule formation stages.",
                "Weed Control": "Perform manual weeding at 15 and 30 days.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 20 days.",
                "Pest and Disease Management": "Neem Oil (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when capsules turn yellow and split open.",
                "Image": "https://example.com/sesamum_image.jpg"
            },
            "Sunhemp": {
                "Varieties": "K-12 Yellow, Ankur-9090",
                "Land Preparation": "Fine tilth with 2-3 plowings and compost incorporation.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate only if necessary, as it is drought-tolerant.",
                "Weed Control": "Perform manual weeding as needed.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) monthly.",
                "Pest and Disease Management": "Neem Oil (5 ml/liter) for pest control.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when pods mature and turn brown.",
                "Image": "https://example.com/sunhemp_image.jpg"
            },
            "Flax": {
                "Varieties": "T-397, Giza-8, JLS-9",
                "Land Preparation": "Ensure fine tilth and good drainage.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at flowering and pod-filling stages.",
                "Weed Control": "Manual weeding at 20 and 40 days.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter).Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when capsules turn brown and seeds are dry.",
                "Image": "https://example.com/flax_image.jpg"
            },
            "Millets": {
                "Varieties": "Bajra HHB 67, Ragi GPU 45",
                "Land Preparation": "Ensure fine tilth and incorporate compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at booting and grain filling stages.",
                "Weed Control": "Hand weeding at 20 and 40 days.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                "Pest and Disease Management": "Neem Oil (5 ml/liter) every 15 days.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when grains harden and moisture is below 15%.",
                "Image": "https://example.com/millets_image.jpg"
            },
        },

        "Fruits": {
            "Mango": {
                "Varieties": "Alphonso, Dasheri, Langra",
                "Land Preparation": "Dig pits (1m x 1m x 1m) and fill with compost and soil mix.",
                "Planting": "Plant during monsoon with proper spacing.",
                "Water Management": "Irrigate weekly during dry periods.",
                "Weed Control": "Use mulch to suppress weeds and retain moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every month.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) monthly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits mature and develop color.",
                "Image": "https://example.com/mango_image.jpg"
            },
            "Banana": {
                "Varieties": "",
                "Land Preparation": "Prepare pits (60 cm x 60 cm x 60 cm) and fill with a mix of topsoil and compost.",
                "Planting": "Plant suckers during monsoon. Maintain spacing of 2m x 2m.",
                "Water Management": "Irrigate weekly during dry periods; avoid waterlogging.",
                "Mulching": "Apply dried banana leaves or straw to conserve moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) monthly and compost (5 kg/plant) biannually.",
                "Pest and Disease Management": "Spray fermented cow urine (500 ml/liter) and Neem Oil as needed.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits are three-fourths mature. Handle gently to avoid damage.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Guava": {
                "Varieties": "",
                "Land Preparation": "Prepare pits (60 cm x 60 cm x 60 cm) and fill with compost and soil mixture.",
                "Planting": "Plant during monsoon with 5m x 5m spacing.",
                "Water Management": "Irrigate every 7-10 days during dry spells.",
                "Mulching": "Use dried leaves or straw to conserve moisture and prevent weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every month.",
                "Pest and Disease Management": "Spray Neem Oil (5 ml/liter) monthly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits turn yellow and firm.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Jackfruit": {
                "Varieties": "NS1, Lalbagh, Dang Surya",
                "Land Preparation": "Dig pits (1m x 1m x 1m) and fill with compost and topsoil.",
                "Planting": "Plant during monsoon with 8m spacing.",
                "Water Management": "Irrigate every 10-12 days in dry periods.",
                "Weed Control": "Mulch to prevent weeds and retain moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) quarterly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) monthly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits develop aroma and turn yellowish.",
                "Image": "https://example.com/jackfruit_image.jpg"
            },
            "Dragonfruit": {
                "Varieties": "Pink-fleshed, White-fleshed",
                "Land Preparation": "Build trellises and plant in raised beds with compost.",
                "Planting": "Space 3m apart; plant during early monsoon.",
                "Water Management": "Irrigate twice a week in dry weather.",
                "Weed Control": "Use mulch to retain moisture and suppress weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) quarterly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when skin turns bright pink.",
                "Image": "https://example.com/dragonfruit_image.jpg"
            },
            "Strawberry": {
                "Varieties": "Chandler, Winter Dawn",
                "Land Preparation": "Prepare raised beds with well-drained soil and compost.",
                "Planting": "Plant runners with 30cm spacing.",
                "Water Management": "Irrigate twice a week.",
                "Weed Control": "Mulch to prevent weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) monthly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits turn fully red.",
                "Image": "https://example.com/strawberry_image.jpg"
            },
            "Orange": {
                "Varieties": "Nagpur, Kinnow",
                "Land Preparation": "Dig pits (1m x 1m x 1m) and mix compost with topsoil.",
                "Planting": "Plant with 4m spacing during early monsoon.",
                "Water Management": "Irrigate every 7-10 days in dry weather.",
                "Weed Control": "Mulching helps in weed suppression.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) quarterly.",
                "Pest and Disease Management": "Use Neem Oil (5 ml/liter) monthly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits turn bright orange.",
                "Image": "https://example.com/orange_image.jpg"
            },
            "Apple": {
                "Varieties": "Red Delicious, Golden Delicious",
                "Land Preparation": "Dig pits (1m x 1m x 1m) and mix compost with soil.",
                "Planting": "Plant in winter or early spring with 5m spacing.",
                "Water Management": "Irrigate regularly, especially in dry weather.",
                "Weed Control": "Mulching helps retain moisture and prevent weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) quarterly.",
                "Pest and Disease Management": "Use Neem Oil (5 ml/liter) monthly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits reach desired color and firmness.",
                "Image": "https://example.com/apple_image.jpg"
            },
            "Lemon": {
                "Varieties": "Kagzi, Assam Lemon",
                "Land Preparation": "Dig pits (50cm x 50cm x 50cm) and mix compost with topsoil.",
                "Planting": "Plant with 3m spacing during monsoon.",
                "Water Management": "Irrigate weekly in dry conditions.",
                "Weed Control": "Mulching helps in weed suppression.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) quarterly.",
                "Pest and Disease Management": "Use Neem Oil (5 ml/liter) monthly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits turn fully yellow.",
                "Image": "https://example.com/lemon_image.jpg"
            }
        },
        "Vegetables": {
            "Tomato": {
                "Varieties": "",
                "Land Preparation": "Prepare raised beds with compost (2 tons/acre) and apply Jeevamrit (100 liters/acre).",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre). Shade-dry seeds after treatment.",
                "Water Management": "Irrigate every 5-7 days depending on soil moisture. Avoid waterlogging.",
                "Mulching": "Apply dry grass or straw mulch between rows to suppress weeds and conserve moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 10 days and foliar spray Panchagavya (30 ml/liter) biweekly.",
                "Pest and Disease Management": "Spray Neem Oil (5 ml/liter) weekly to control pests.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest fruits when they turn red and firm. Avoid overripe fruits.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Brinjal": {
                "Varieties": "",
                "Land Preparation": "Incorporate 2 tons/acre of compost into raised beds and apply Jeevamrit (100 liters/acre).",
                "Seed Treatment": "Treat seeds with Beejamrit (5 liters solution per acre) and shade-dry.",
                "Water Management": "Irrigate weekly, ensuring soil remains moist but not waterlogged.",
                "Mulching": "Apply organic mulch to retain soil moisture and suppress weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 10-15 days.",
                "Pest and Disease Management": "Spray Neem Oil (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest fruits when they are shiny and of appropriate size. Handle carefully.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Cauliflower": {
                "Varieties": "Snowball, Pusa Deepali",
                "Land Preparation": "Prepare raised beds with rich organic matter.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at regular intervals to maintain moisture.",
                "Weed Control": "Hand weeding and mulching help suppress weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when curds are compact and white.",
                "Image": "https://example.com/cauliflower_image.jpg"
            },
            "Cabbage": {
                "Varieties": "Golden Acre, Pusa Drumhead",
                "Land Preparation": "Prepare raised beds with compost and well-drained soil.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at regular intervals to maintain soil moisture.",
                "Weed Control": "Hand weeding and mulching recommended.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when heads are firm and well-formed.",
                "Image": "https://example.com/cabbage_image.jpg"
            },
            "Okra": {
                "Varieties": "Pusa Sawani, Arka Anamika",
                "Land Preparation": "Prepare raised beds and add compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate every 3-5 days.",
                "Weed Control": "Mulching and manual weeding recommended.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when pods are tender and green.",
                "Image": "https://example.com/okra_image.jpg"
            },
            "Bottle Gourd": {
                "Varieties": "Pusa Naveen, Arka Bahar",
                "Land Preparation": "Prepare raised beds and add compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate every 3-5 days.",
                "Weed Control": "Mulching and manual weeding recommended.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits are tender and green.",
                "Image": "https://example.com/bottle_gourd_image.jpg"
            },
            "French Beans": {
                "Varieties": "Arka Komal, Contender",
                "Land Preparation": "Prepare raised beds with compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at regular intervals.",
                "Weed Control": "Hand weeding and mulching help suppress weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when pods are tender and green.",
                "Image": "https://example.com/french_beans_image.jpg"
            },
            "Cucumber": {
                "Varieties": "Pusa Uday, Malini",
                "Land Preparation": "Prepare raised beds and add compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate every 3-5 days.",
                "Weed Control": "Mulching and manual weeding recommended.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits reach optimal size.",
                "Image": "https://example.com/cucumber_image.jpg"
            },
            "Watermelon": {
                "Varieties": "Sugar Baby, Arka Jyoti",
                "Land Preparation": "Prepare sandy loam soil with compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate weekly, reducing near harvest.",
                "Weed Control": "Mulching suppresses weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when tendril near fruit dries.",
                "Image": "https://example.com/watermelon_image.jpg"
            },
            "Capsicum": {
                "Varieties": "California Wonder, Arka Gagan",
                "Land Preparation": "Prepare raised beds with compost and well-drained soil.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate every 5-7 days.",
                "Weed Control": "Mulching and manual weeding recommended.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits are firm and fully colored.",
                "Image": "https://example.com/capsicum_image.jpg"
            },
            "Pointed Gourd": {
                "Varieties": "Swarna Alaukik, Rajendra Parwal-1",
                "Land Preparation": "Prepare pits filled with compost and sandy loam soil.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at regular intervals.",
                "Weed Control": "Hand weeding and mulching.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits reach full size but are still tender.",
                "Image": "https://example.com/pointed_gourd_image.jpg"
            },
            "Broccoli": {
                "Varieties": "Green Magic, Palam Samridhi",
                "Land Preparation": "Prepare raised beds with organic matter and well-drained soil.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate every 4-6 days.",
                "Weed Control": "Mulching and periodic weeding.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when heads are firm and compact.",
                "Image": "https://example.com/broccoli_image.jpg"
            },
            "Red Cabbage": {
                "Varieties": "Red Express, Ruby Ball",
                "Land Preparation": "Prepare well-drained, fertile soil with compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate regularly to maintain soil moisture.",
                "Weed Control": "Manual weeding and mulching help suppress weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when heads are firm and reach optimal size.",
                "Image": "https://example.com/red_cabbage_image.jpg"
            },
            "Chili": {
                "Varieties": "",
                "Land Preparation": "Prepare raised beds and apply 2 tons/acre of compost mixed with topsoil.",
                "Seed Treatment": "Soak seeds in Beejamrit (5 liters solution per acre) for 8 hours.",
                "Water Management": "Irrigate every 7-10 days. Avoid waterlogging.",
                "Mulching": "Apply rice straw or grass mulch to conserve moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 10 days.",
                "Pest and Disease Management": "Use Neem Oil (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Pick chilies when they reach the desired size and color.",
                "Image": "https://example.com/greengram_image.jpg"
            },
        },
        "Flowers": {
            "Marigold": {
                "Varieties": "African Marigold, French Marigold",
                "Land Preparation": "Plow field twice and apply compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at regular intervals.",
                "Weed Control": "Hand weeding as needed.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when flowers fully bloom.",
                "Image": "https://example.com/marigold_image.jpg"
            },
            "Chrysanthemum": {
                "Varieties": "White Button, Yellow Reflex",
                "Land Preparation": "Plow and incorporate compost for rich soil.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate at regular intervals.",
                "Weed Control": "Mulch and hand weeding as required.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest flowers at full bloom stage.",
                "Image": "https://example.com/chrysanthemum_image.jpg"
            }
        }
    },
    "Coastal Areas": {
        "Field Crops": {
            "Jute": {
                "Varieties": "JRO 8432, JRO 204, Bidhan Rupali (salt-tolerant variety).",
                "Land Preparation": "Fine tilth with 3-4 plowings; proper leveling to ensure drainage and apply Jeevamrit (200 liters/acre) during the last plowing.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre) and add 200 g of neem leaf paste to counter salinity stress.",
                "Nursery Management": "Prepare raised nursery beds and apply Jeevamrit weekly.",
                "Transplanting": "Ensure raised field boundaries and transplant seedlings at a spacing of 20 cm x 15 cm.",
                "Water Management": "Irrigate with fresh water and maintain 2-5 cm standing water during critical stages.",
                "Weed Control": "Use water hyacinth mulch and perform manual weeding as needed.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 10-15 days and neem-mixed compost during land preparation.",
                "Pest and Disease Management": "Spray coconut water (10% solution) during salinity stress and Neem Oil for pests.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when grains are golden yellow. Store on raised platforms to prevent fungal contamination.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Rice": {
                "Varieties": "Luna Sankhi, Luna Suvarna, CSR-36, Nona Bokra",
                "Land Preparation": "Flood the field with fresh water to leach salts and apply Jeevamrit (200 liters/acre) during the last plowing.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre) and add 200 g of neem leaf paste to counter salinity stress.",
                "Nursery Management": "Prepare raised nursery beds and apply Jeevamrit weekly.",
                "Transplanting": "Ensure raised field boundaries and transplant seedlings at a spacing of 20 cm x 15 cm.",
                "Water Management": "Irrigate with fresh water and maintain 2-5 cm standing water during critical stages.",
                "Weed Control": "Use water hyacinth mulch and perform manual weeding as needed.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 10-15 days and neem-mixed compost during land preparation.",
                "Pest and Disease Management": "Spray coconut water (10% solution) during salinity stress and Neem Oil for pests.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when grains are golden yellow. Store on raised platforms to prevent fungal contamination.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Sugarcane": {
                    "Varieties": "Co 86032, Co 99004",
                    "Land Preparation": "Deep plowing and incorporation of organic compost (2 tons/acre).",
                    "Seed Treatment": "Soak setts in Beejamrit (5 liters solution per acre) before planting.",
                    "Water Management": "Irrigate at early growth stages and during dry spells.",
                    "Weed Control": "Manual weeding and mulching with sugarcane trash.",
                    "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                    "Pest and Disease Management": "Use Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                    "Harvesting": "Harvest at 10-12 months when cane is mature.",
                    "Image": "https://example.com/sugarcane_image.jpg"
            },
            "Groundnut": {
                    "Varieties": "TG 37A, K 6",
                    "Land Preparation": "Fine tilth and well-drained soil with compost incorporation.",
                    "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                    "Water Management": "Irrigate at pod development stage.",
                    "Weed Control": "Manual weeding at 20 and 40 days.",
                    "Fertilization": "Apply Jeevamrit (200 liters/acre) every 20 days.",
                    "Pest and Disease Management": "Neem Oil (5 ml/liter) spray for pest control.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                    "Harvesting": "Harvest when leaves turn yellow and pods are mature.",
                    "Image": "https://example.com/groundnut_image.jpg"
            },
            "Sorghum": {
                    "Varieties": "CSV 15, CSH 16",
                    "Land Preparation": "Plow and harrow to achieve fine tilth and add compost (1 ton/acre).",
                    "Seed Treatment": "Soak seeds in Beejamrit (5 liters solution per acre).",
                    "Water Management": "Irrigate during flowering and grain filling stages.",
                    "Weed Control": "Hand weeding at 20 and 40 days.",
                    "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                    "Pest and Disease Management": "Neem Oil (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                    "Harvesting": "Harvest when grains are hard and dry.",
                    "Image": "https://example.com/sorghum_image.jpg"
            },
            "Pearl Millet": {
                    "Varieties": "HHB 67, RHB 177",
                    "Land Preparation": "Prepare sandy loam soil with good drainage and apply compost (1.5 tons/acre).",
                    "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                    "Water Management": "Irrigate at booting and grain filling stages.",
                    "Weed Control": "Hand weeding at 20 and 40 days.",
                    "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                    "Pest and Disease Management": "Neem Oil (5 ml/liter) every 15 days.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                    "Harvesting": "Harvest when grains harden and moisture is below 15%.",
                    "Image": "https://example.com/pearl_millet_image.jpg"
            },
        },
        "Fruits": {
            "Mango": {
                "Varieties": "Alphonso, Dasheri, Kesar",
                "Land Preparation": "Dig pits (1m x 1m x 1m) and fill with compost and soil mix.",
                "Planting": "Plant during monsoon season with 5m x 5m spacing.",
                "Water Management": "Irrigate weekly during dry periods.",
                "Weed Control": "Mulching helps retain moisture and suppress weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) monthly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) monthly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits mature and develop color.",
                "Image": "https://example.com/mango_image.jpg"
            },
            "Banana": {
                "Varieties": "Robusta, Grand Naine",
                "Land Preparation": "Deep plowing and application of compost.",
                "Planting": "Plant at a spacing of 2m x 2m.",
                "Water Management": "Irrigate every 5-7 days.",
                "Weed Control": "Mulching suppresses weeds and retains moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 20 days.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits turn slightly yellow.",
                "Image": "https://example.com/banana_image.jpg"
            },

            "Jackfruit": {
                "Varieties": "NS1, Lalbagh",
                "Land Preparation": "Dig pits (1m x 1m x 1m) and fill with compost and topsoil.",
                "Planting": "Plant during monsoon with 8m spacing.",
                "Water Management": "Irrigate every 10-12 days in dry periods.",
                "Weed Control": "Mulch to prevent weeds and retain moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) quarterly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) monthly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits develop aroma and turn yellowish.",
                "Image": "https://example.com/jackfruit_image.jpg"
            },
            "Coconut": {
                "Varieties": "",
                "Land Preparation": "Dig pits (1m x 1m x 1m) and fill with a mix of compost and sand to improve drainage.",
                "Planting": "Plant saplings with 7m x 7m spacing. Ensure good root coverage.",
                "Water Management": "Irrigate every 15 days during dry spells.",
                "Mulching": "Apply dry coconut leaves around the base to retain moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) monthly and add 10 kg of compost/pit annually.",
                "Pest and Disease Management": "Spray Neem Oil (5 ml/liter) monthly and use cow dung paste to treat stem wounds.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest mature coconuts when the husk turns brown.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Papaya": {
                "Varieties": "",
                "Land Preparation": "Dig pits (50 cm x 50 cm x 50 cm) and fill with a mix of compost and soil.",
                "Planting": "Plant during monsoon with 2m x 2m spacing.",
                "Water Management": "Irrigate weekly during dry periods.",
                "Mulching": "Use straw or dried leaves to conserve moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) monthly and 5 kg compost per pit annually.",
                "Pest and Disease Management": "Spray Neem Oil (5 ml/liter) and Panchagavya (30 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest fruits when they show a yellow tinge at the blossom end.",
                "Image": "https://example.com/greengram_image.jpg"
            },
            "Cashew Nut": {
                "Varieties": "Vengurla-4, Bhubaneswar-1",
                "Land Preparation": "Dig pits (1m x 1m x 1m) and fill with compost.",
                "Planting": "Plant saplings at 7m x 7m spacing.",
                "Water Management": "Irrigate during dry spells.",
                "Weed Control": "Mulching with dry leaves.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) quarterly.",
                "Pest and Disease Management": "Neem Oil (5 ml/liter) spray monthly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest nuts when they fall naturally.",
                "Image": "https://example.com/cashew_image.jpg"
            },
            "Guava": {
                "Varieties": "Lalit, Allahabad Safeda",
                "Land Preparation": "Dig pits (50cm x 50cm x 50cm) and fill with compost.",
                "Planting": "Plant saplings at 4m x 4m spacing.",
                "Water Management": "Irrigate weekly during dry spells.",
                "Weed Control": "Mulching with dry leaves.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) quarterly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits turn yellow and firm.",
                "Image": "https://example.com/guava_image.jpg"
            },
            "Pineapple": {
                    "Varieties": "Queen, Kew",
                    "Land Preparation": "Ensure sandy loam soil with compost application.",
                    "Planting": "Plant suckers with 30 cm spacing.",
                    "Water Management": "Irrigate weekly.",
                    "Weed Control": "Mulching with coconut leaves.",
                    "Fertilization": "Apply Jeevamrit (200 liters/acre) monthly.",
                    "Pest and Disease Management": "Neem Oil (5 ml/liter) for pest control.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                    "Harvesting": "Harvest when fruits turn golden yellow.",
                    "Image": "https://example.com/pineapple_image.jpg"
            },
            "Jamun": {
                    "Varieties": "Rajamun, Badami",
                    "Land Preparation": "Dig pits (50cm x 50cm x 50cm) and fill with compost.",
                    "Planting": "Plant saplings at 5m x 5m spacing.",
                    "Water Management": "Irrigate weekly in dry weather.",
                    "Weed Control": "Mulching with dried leaves.",
                    "Fertilization": "Apply Jeevamrit (200 liters/acre) quarterly.",
                    "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                    "Harvesting": "Harvest when fruits turn deep purple.",
                    "Image": "https://example.com/jamun_image.jpg"
            }
        },
        "Vegetables": {
            "Tomato": {
                "Varieties": "Pusa Ruby, Arka Rakshak",
                "Land Preparation": "Prepare raised beds with compost and apply Jeevamrit (100 liters/acre).",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate every 5-7 days depending on soil moisture.",
                "Weed Control": "Mulching with dry leaves to suppress weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 10 days.",
                "Pest and Disease Management": "Spray Neem Oil (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits turn red and firm.",
                "Image": "https://example.com/tomato_image.jpg"
            },
            "Brinjal": {
                "Varieties": "Pusa Purple Long, Arka Navneet",
                "Land Preparation": "Incorporate compost into raised beds and apply Jeevamrit (100 liters/acre).",
                "Seed Treatment": "Treat seeds with Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate weekly, ensuring soil remains moist but not waterlogged.",
                "Weed Control": "Apply organic mulch to retain soil moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 10-15 days.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest fruits when they are shiny and of appropriate size.",
                "Image": "https://example.com/brinjal_image.jpg"
            },
            "Okra": {
                "Varieties": "Pusa Sawani, Arka Anamika",
                "Land Preparation": "Prepare raised beds and add compost.",
                "Seed Treatment": "Use Beejamrit (5 liters solution per acre).",
                "Water Management": "Irrigate every 3-5 days.",
                "Weed Control": "Mulching and manual weeding recommended.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) biweekly.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when pods are tender and green.",
                "Image": "https://example.com/okra_image.jpg"
            },
            "Pumpkin": {
                "Varieties": "Pusa Vishwas, Arka Suryamukhi",
                "Land Preparation": "Prepare pits (1m x 1m x 1m) and mix soil with compost (5 kg/pit).",
                "Seed Treatment": "Soak seeds in Beejamrit (5 liters solution per acre) before sowing.",
                "Water Management": "Irrigate weekly during dry spells.",
                "Weed Control": "Mulching with straw helps retain moisture.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 10 days.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when fruits are fully mature with a hard rind.",
                "Image": "https://example.com/pumpkin_image.jpg"
            },
            "Taro (Colocasia)": {
                "Varieties": "Muktakeshi, Kachhu",
                "Land Preparation": "Loose soil with organic compost.",
                "Planting": "Plant corms at 30 cm spacing.",
                "Water Management": "Maintain moisture but avoid waterlogging.",
                "Weed Control": "Manual weeding and mulching.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 20 days.",
                "Pest and Disease Management": "Neem Oil (5 ml/liter) spray biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when leaves start drying.",
                "Image": "https://example.com/taro_image.jpg"
            },
            "Water Spinach": {
                "Varieties": "Local varieties",
                "Land Preparation": "Sandy loam soil with compost incorporation.",
                "Planting": "Direct seeding in raised beds.",
                "Water Management": "Irrigate regularly, keeping soil moist.",
                "Weed Control": "Mulching to suppress weeds.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 15 days.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) weekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest tender shoots every 15 days.",
                "Image": "https://example.com/water_spinach_image.jpg"
            },
        },
        "Flowers": {
            "Hibiscus": {
                "Varieties": "Red Hibiscus, White Hibiscus",
                "Land Preparation": "Well-drained loamy soil with compost incorporation.",
                "Planting": "Plant cuttings with 1m spacing.",
                "Water Management": "Irrigate weekly during dry periods.",
                "Weed Control": "Mulching and hand weeding.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every month.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest flowers at full bloom stage.",
                "Image": "https://example.com/hibiscus_image.jpg"
            },
            "Tuberose": {
                "Varieties": "Rajat Rekha, Prajwal",
                "Land Preparation": "Well-drained soil with compost.",
                "Planting": "Plant bulbs with 20 cm spacing.",
                "Water Management": "Irrigate every 5-7 days.",
                "Weed Control": "Mulching with dry straw.",
                "Fertilization": "Apply Jeevamrit (200 liters/acre) every 20 days.",
                "Pest and Disease Management": "Neem Oil spray (5 ml/liter) biweekly.Use Neemastra (100 liters/acre) to control borers and aphids. Apply Agniastra (3-4 liters/100 liters of water) and Bramhastra (2 liters/100 liters of water) for additional pest control",
                "Harvesting": "Harvest when flowers bloom fully.",
                "Image": "https://example.com/tuberose_image.jpg"
            },
        },
    },
    # ... (your existing practices dictionary)
}

INPUT_PREPARATION = {"Jeevamrut": {
        "Inputs": "Desi cow dung: 10 kg, Desi cow urine: 10 L, Jaggery: 1kg; Besan: 1kg; Forest soil: 200g; Water 200L.",
        "Description": "All the ingredients are added into a mud pot/plastic drum and stirred in clockwise direction and kept overnight for fermentation. Then the mixture is filtered to collect the extract.",
        "Use": "100 kg of seeds are soaked in 20 L beejamruth and shade dried for 30 mins before sowing. ",
        "Image": "Jeevamruth.jpg"
    },
    "Beejamrut": {
        "Inputs": "Desi cow dung: 5 kg, Desi cow urine: 5 L, Lime: 50g; Forest soil: 200g; Water: 20L",
        "Description": "All the ingredients are added into a mud pot/plastic drum and stirred in clockwise direction and kept overnight for fermentation. Then the mixture is filtered to collect the extract.",
        "Use": "100 kg of seeds are soaked in 20 L beejamruth and shade dried for 30 mins before sowing.",
        "Image": "Beejamrut.jpg"  # Replace with the URL of an image for Beejamrit
    },
    "Neem oil garlic emulsion": {
        "Inputs": "Neem oil- 20 ml; Garlic-20g; Bar soap- 6g; Water 1L",
        "Description": "Dissolve bar soap in 50 ml luke warm water. Then Add 20 ml neem oil and mix well. Grind garlic in 50 ml water and and collect the 30 ml extract. Mix neem oil and garlic extract and Add water in to the mixture to make upto 1L",
        "Use": "The 2% solution can be sprayed once in 7-10 days interval mainly to manage lepidopteran pest and mites",
        "Image": "Neem oil garlic emulsion.jpg"
    },
    "Neem seed kernel extract": {
        "Inputs": "Neem seed- 50 g; Water 1L",
        "Description": "Grind the neem seed to fine powder. Tie it in cotton cloth and keep it dipped in 500 ml water for 12 hr. Next day, squeeze the extract and add water to make upto 1L",
        "Use": "The 5% solution can be sprayed once in 7-10 days interval mainly to manage the sucking pests",
        "Image": "Neem seed kernel extract.jpg"
    },
    "Neemastra": {
        "Inputs": "Neem leaves- 5kg; Cow urine-5L, Cowdung- 5kg; Water 100 L.",
        "Description": "Mix all the above contents in plastic vessel/ container. Ferment for 48 hours with intermittent stirring in clockwise direction. Filter the contents and store in a clean container.",
        "Use": "Spray the 100L solution in 1 acre farm land to manage sucking pests.",
        "Image": "Neemastra.jpg"
    },
    "Brahmastra": {
        "Inputs": "Cow’s urine - 10 liters; Neem leaves - 3 kg; Custard apple leaf - 2 kg; Papaya leaf - 2 kg; Pomegranate leaf - 2 kg; Guava leaf - 2 kg",
        "Description": "Mix all the above contents in vessel and boil 5 times and allow the contents to cool. Keep the mixture for fermentation for 48 hours and then filter the extract. It can be stored in clean containers for 3-4 months.",
        "Use": "Dilute 2 liters of extract in 100 liters of water for spraying one acre. It is effective against sucking pests and pod/fruit borers.",
        "Image": "Brahmastra.jpg"
    },
    "Agniastra": {
        "Inputs": ": Cow’s urine - 20 liters; Neem leaves - 5 kg; Green chillies - 2 kg; Garlic - 1 kg; Tobacco leaf - 1 kg",
        "Description": "Mix all the above contents in vessel and boil 5 times and allow the contents to cool. Keep the mixture for fermentation for 48 hours and then filter the extract. It can be stored in clean containers for 3-4 months",
        "Use": "Dilute 3-4 liters of extract in 100 liters of water for spraying one acre. It is effective against sucking pests and pod/fruit borers.",
        "Image": "Agniastra.jpg"
    },

    "Panchagavya": {
        "Inputs": "Cow dung: 5kg; cow urine: 3 L; Milk: 2l; Curd: 2l; Ghee: 1kg.",
        "Description": "Mix fresh cowdung and ghee and cow urine, milk and curd separately in two different containers for fermentation for 3 days. Then mix the both the mixtures and ferment for 7 days in an open container for 7 days with intermittent stirring. Filter the extract and store in closed containers.",
        "Use": "As seed treatment (soak seeds in 3% solution for 30 mins)/ foliar spray (3%) or soil drenching along with irrigation water (50L/Ha).",
        "Image": "Panchagavya.jpg"
    },
    # ... (your existing INPUT_PREPARATION dictionary)
}


def main():
    st.title("Natural Farming App 🌾")

    # Sidebar for navigation
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Agro-Climatic Zone", "Farming Inputs", "Contact", "Developers"])

    if page == "Home":
        st.header("Welcome to the Natural Farming Practices App")
        st.image("https://example.com/home_banner.jpg",
                 use_container_width=True)  # Replace with your home banner image URL
        st.write(
            """
            This application provides information on sustainable, natural farming practices.
            Explore crop-specific practices and natural farming input preparation methods.
            """
        )

        st.subheader("KVK, North 24 Parganas (Additional)")
        st.subheader("ICAR-Central Research Institute for Jute and Allied Fibres")

    elif page == "Agro-Climatic Zone":
        st.header("Agro-climatic Zone ")
        zone = st.selectbox("Select Agro-Climatic Zone", practices.keys())
        crop_type = st.selectbox("Select Crop Type", practices[zone].keys())
        crop = st.selectbox("Select Crop", practices[zone][crop_type].keys())

        st.header(f"Practices for {crop} in {zone} ({crop_type})")

        # Display practices for the selected zone, crop type, and crop
        for practice, details in practices[zone][crop_type][crop].items():
            st.subheader(practice)
            translated_details = translate_text(details)
            st.write(translated_details)
        if "Image" in crop:
            st.image(crop["Image"], caption=crop, use_container_width=True)

    elif page == "Farming Inputs":
        st.header("Farming Inputs")
        input_name = st.selectbox("Select Farming Input", list(INPUT_PREPARATION.keys()))

        # Display input preparation details and image
        st.subheader(f"{input_name}")
        input_details = INPUT_PREPARATION[input_name]
        st.markdown(f"**Inputs:**\n{translate_text(input_details['Inputs'])}")
        st.markdown(f"**Description:**\n{translate_text(input_details['Description'])}")
        st.markdown(f"**Use:**\n{translate_text(input_details['Use'])}")

    elif page == "Contact":
        st.header("Contact")
        st.write("""Head""")
        st.write("""KVK, North 24 Parganas, Additional""")
        st.write("""ICAR-CRIJAF""")
        st.write("""Nilganj, Barrackpore, Nprth 24 Parganas""")
        st.write("""West Bengal-700121""")
        st.write("""Email-kvkn24prg2@gmail.com""")
        st.write("""Ph-8250600511""")
    elif page == "Developers":
        st.header("Developer:")
        st.text("""Dr. Tanmay Samajdar""")
        st.header("Co-Developer:")
        st.text(
            " Dr. Rinku Bharali-\nDr. Debojyoti Borkotoky\nDr. Arvind. T.\nMr. Syam K. R.\nMr. V. Om. Subham Raju\nMs. Bernice Ekhe")


if __name__ == "__main__":
    main()

