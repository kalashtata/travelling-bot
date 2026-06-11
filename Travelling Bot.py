import random

print("🌍Ai travel : Hello! How can i help u today!")

responses = {
                "Greeting":["hello! where You want to travel !!",
                            "hi There ! are you ready to explore the world!",
                            "welcome! which destination you would like to travel today!!"],
                "japan":["1. Mount Fuji – Japan's most iconic mountain."
                         "2. Tokyo Tower – Great city views."
                         "3. Osaka Castle – One of Japan's most famous castles."
                         "4. Arashiyama Bamboo Grove – Beautiful walking paths through towering bamboo."
                         "5. Fushimi Inari Taisha – Famous for thousands of red torii gates."],
                "india":["1. Taj Mahal – One of the Seven Wonders of the World."
                         "2. Goa – Famous for beaches and nightlife."
                         "3. Ladakh – Spectacular mountains and landscapes."
                         "4. Jaipur – Known as the Pink City."
                         "5. Golden Temple – A major spiritual and cultural landmark."],
                "germany":["1. Berlin – History and modern culture"
                           "2.Brandenburg Gate  – One of Germany's most famous landmarks."
                           "3. Rhine Valley – Known for castles, vineyards, and river cruises."
                           "4. Neuschwanstein Castle – Iconic castle"
                           "5. Black Forest – Beautiful forests, villages, and hiking trails."],
                "dubai":[" 1. Burj Khalifa – Amazing city views from the observation decks."
                         " 2. Dubai Mall – One of the world's largest malls."
                         " 3. Dubai Fountain – Free water and light shows in the evening."
                         " 4. Palm Jumeirah – Famous palm-shaped island with beaches and resorts."
                         " 5. Dubai Marina – Great for evening walks and dining."],
                "singapore":["1. Marina Bay Sands – Famous for its rooftop SkyPark and city views"
                             "2. Gardens by the Bay – Known for the giant Supertrees and evening light show"
                             "3. Merlion – One of Singapore's most iconic landmarks."
                             "4. Singapore Botanic Gardens - botanical garden with sculptures, a swan lake & significant collection of tropical trees."
                             "5. Sentosa – Beaches, attractions, and family entertainment"],
                "canada":["1. Niagara Falls – One of the world's most famous waterfalls."
                          "2. Banff National Park – Stunning mountains, lakes, and wildlife."
                          "3. Lake Louise – Famous turquoise-blue lake."
                          "4. Vancouver – Mountains, ocean, and city life together."
                          "5. CN Tower – Amazing views of the city."],
            "new zealand":["1. Milford Sound – Spectacular cliffs, waterfalls, and boat cruises."
                           "2. Hobbiton Movie Set – Famous from The Lord of the Rings and The Hobbit movies."
                           "3. Lake Tekapo – Known for its turquoise water and amazing stargazing."
                           "4. Waitomo Glowworm Caves – Thousands of glowing insects light up the caves."
                           "5. Queenstown – Known as the adventure capital of New Zealand."],        
            "malaysia":["1. Petronas Twin Towers – Malaysia's most famous landmark."
                        "2. George Town – Known for street art, heritage buildings, and food."
                        "3. Perhentian Islands – Crystal-clear water and snorkeling."
                        "4. Batu Caves – Famous Hindu temple with a giant statue of Lord Murugan."
                        "5. Mount Kinabalu – The highest peak in Malaysia."],
            "farewell":["goodbye traveler! have a save journey",
                        "see u  soon ! keep exploring the world",
                        "bye!"]
                }


def get_responses(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input or "welcome" in user_input:
        print(random.choice(responses["Greeting"]))
        return random.choice(responses["Greeting"])
    elif "india" in user_input:
        print(random.choice(responses["india"]))
        return random.choice(responses["india"])
    elif "japan" in user_input:
        print(random.choice(responses["japan"]))
        return random.choice(responses["japan"])
    elif "germany" in user_input:
        print(random.choice(responses["germany"]))
        return random.choice(responses["germany"])
    elif "dubai" in user_input:
        print(random.choice(responses["dubai"]))
        return random.choice(responses["dubai"])
    elif "singapore" in user_input:
        print(random.choice(responses["singapore"]))
        return random.choice(responses["singapore"])
    elif "canada" in user_input:
        print(random.choice(responses["canada"]))
        return random.choice(responses["canada"])
    elif "new zealand" in user_input:
        print(random.choice(responses["new zealand"]))
        return random.choice(responses["new zealand"])
    elif "malaysia" in user_input:
        print(random.choice(responses["malaysia"]))
        return random.choice(responses["malaysia"])  
    elif "bye" in user_input or "goodbye" or "see u soon" in user_input:
        print(random.choice(responses["farewell"]))
        return random.choice(responses["farewell"])

   

while True:
    user_input = input("You : ")
    response=get_responses(user_input)
   
    #print(user_input.lower())
    if "taj mahal" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
              "Taj Mahal, agra fort, Aram Bagh !!")
    elif "goa" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
              "North goa, South goa , Inland Adventure !!")
    elif "ladakh" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
               "Shanti Stupa, Thiksey Monastery, Sangam Point !!")    
    elif "jaipur" in user_input.lower():
         print("In this package u will have 7 Days in which it include :-",
               "Hawa Mahal, Jantar Mantar, Nahargarh Fort !!")        
    elif "mount fuji" in user_input.lower():
         print("In this package u will have 7 Days in which it include :-",
                "Fuji Safari Park, Lake Ashi, Aokigahara Forest & Caves !!")        
    elif "golden temple" in user_input.lower():
         print("In this package u will have 7 Days in which it include :-",
               "Guru Ram Das Langar Hall, Darshni Deori, Akal Takht !!")
    elif "tokyo tower" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
              "Zojoji Temple, Shiba Park, Azabudai Hills !!")        
    elif "osaka castle" in user_input.lower():
         print("In this package u will have 7 Days in which it include :-",
               "The Gozabune Boat, Nishinomaru Garden, Tamatsukuri Inari Shrine !!")                  
    elif "Arashiyama Bamboo Grove" in user_input.lower():
         print("In this package u will have 7 Days in which it include :-",
               "Kimono Forest, Sagano Scenic Railway, Otagi Nenbutsu-ji Temple !!")                    
    elif "Fushimi Inari Taisha" in user_input.lower():
         print("In this package u will have 7 Days in which it include :-",
               "Daigo-ji Temple, Teradaya Inn, Kamibo Shrine !!")  
    elif "Berlin" in user_input.lower():
         print("In this package u will have 7 Days in which it include :-",
                "East Side Gallery, Memorial to the Murdered Jews of Europe, Brandenburg Gate !!")
    elif " Brandenburg Gate" in user_input.lower():
          print("In this package u will have 7 Days in which it include :-",
                 "Reichstag Building, Tiergarten, Hopfingerbräu am Brandenburger Tor !!")
    elif "Rhine Valley" in user_input.lower():
          print("In this package u will have 7 Days in which it include :-",
                 "Marksburg, Rheinfels Castle, Deutsches Eck !!")
    elif "Neuschwanstein Castle" in user_input.lower():
          print("In this package u will have 7 Days in which it include :-",
                 "Pöllat Gorge Trail, Marienbrücke, Füssen Old Town !!")
    elif "Black Forest" in user_input.lower():
          print("In this package u will have 7 Days in which it include :-",
                 "Lake Titisee, Lake Mummelsee, Baden-Baden !!")       
    elif "burj khalifa" in user_input.lower():
              print("In this package u will have 7 Days in which it include :-",
                    "level 124 & 125 with 360 view!!")
    elif "dubai mall" in user_input.lower():
              print("In this package u will have 7 Days in which it include :-",
                     "next to burj khalifa the world biggest mall !!")    
    elif "dubai fountain" in user_input.lower():
               print("In this package u will have 7 Days in which it include :-",
                     "dubai most attractive fountain !!")        
    elif "marina bay sands" in user_input.lower():
               print("In this package u will have 7 Days in which it include :-",
                      "SkyPark, Infinity pool, Spectra Light & Water Show!!")        
    elif "Gardens by the bay" in user_input.lower():
               print("In this package u will have 7 Days in which it include :-",
                     "Supertree Grove, Cloud Forest, Flower Dome, OCBC Skywalk !!")
    elif "merlion" in user_input.lower():
              print("In this package u will have 7 Days in which it include :-",
                    " Home of Singapore's famous Merlion statue!!")        
    elif "sentosa" in user_input.lower():
               print("In this package u will have 7 Days in which it include :-",
                     "Beaches, attaraction, & entertairment !!")                  
    elif "singapore botanic gardens" in user_input.lower():
               print("In this package u will have 7 Days in which it include :-",
                     "Garden By The Bay, Marlina Bay Sands, Merlion Park !!")         
    elif "niagara falls" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
          "Maid of the Mist, Cave of the Winds, Niagara Parks Butterfly Conservatory !!")

    elif "banff national park" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
          "Moraine Lake, Banff Gondola, Bow Falls !!")

    elif "lake louise" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
          "Lake Agnes Tea House, Moraine Lake, Plain of Six Glaciers Trail !!")

    elif "vancouver" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
          "Stanley Park, Capilano Suspension Bridge, Granville Island !!")

    elif "cn tower" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
          "Ripley's Aquarium of Canada, Toronto Islands, Royal Ontario Museum !!")

    elif "milford sound" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
          "Mitre Peak, Bowen Falls, Milford Sound Cruise !!")

    elif "hobbiton movie set" in user_input.lower():
        print("In this package u will have 7 Days in which it include :-",
          "Bag End, Green Dragon Inn, Party Tree !!")  
        
    elif "lake Tekapo" in user_input.lower():
                    print("In this package u will have 7 Days in which it include :-",
                          "Church of the good shephered, tekapo springs, Mount john observation !!")                  
    elif "waitomo Glowworm Caves" in user_input.lower():
                    print("In this package u will have 7 Days in which it include :-",
                          "Waitomo cave, raukuri cave, aranui cave!!")                    
    elif "queenstown" in user_input.lower():
                    print("In this package u will have 7 Days in which it include :-",
                          " Skyline, milofrs sound, shotover jet boat ride!!")  
    elif "petronas Twin Towers " in user_input.lower():
                    print("In this package u will have 7 Days in which it include :-",
                           "KLCC park, aquatic KLCC, skybrige!")
    elif "george Town" in user_input.lower():
                   print("In this package u will have 7 Days in which it include :-",
                            "Pengang Art, Kek lok si temple, clan jetties !!")
    elif "perhentian Islands" in user_input.lower():
                     print("In this package u will have 7 Days in which it include :-",
                            "Long beach, turtle beach, coral bay!!")
    elif "batu Caves " in user_input.lower():
                     print("In this package u will have 7 Days in which it include :-",
                            " Temple cave, Drak cave, Ramayana Cave!!")
    elif "mount kinabalu" in user_input.lower():
                      print("In this package u will have 7 Days in which it include :-",
                            "Mount Kinabalu Summit, Kinabalu park, Poring Hot Sorings !!")   
   
    elif "bye" in user_input.lower():
        break
