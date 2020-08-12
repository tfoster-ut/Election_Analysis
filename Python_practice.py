
        # counties = ["Arapahoe", "Denver", "Jefferson"]

        # if "Arapahoe" in counties and "El Paso" not in counties:
        #     print('Only Arapahoe is in the list of counties')
        # else:
        #     print('Arapahoe is in the list of counties and El Paso is not in the list of counties')

#Skill Drill
#Print each county and registered voter from the dictionary.

        # counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}

        # for county, votes in counties_dict.items():
        #     print(f'{county} county has {votes} registered voters')

#Skill Drill 2
#Print each county and registered voter from the dictionary

counties_dict = {'Arapahoe': 369237, 'Denver': 413229, 'Jefferson': 390222}

for county, votes in counties_dict.items():
    print(f'{county} has {votes:,} registered voters')