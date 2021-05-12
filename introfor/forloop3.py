

#!/usr/bin/env python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
    i=0
    print(farm["name"] + " has the following agriculture:")
    for animal in (farm["agriculture"]):
        print("   " + farm["agriculture"][i])
        i += 1
            
    
