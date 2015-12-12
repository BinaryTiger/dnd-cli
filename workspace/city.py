import json

class City:
    """City class for building the object representation"""

    def __init__(self):
        self.data = []
        self.name = ""
        self.population = 0
        self.race_relation = ""
        self.ruler_status = ""
        self.notable_trait = ""
        self.known_for = ""
        self.calamity = ""
        self.buildings = []
    
        
    def buildRandom(self):
        #Build random tables DMHB p.112
        return "Randomizing city"
        
    def save_to_file(self, path):
        city = self.build_dictionary();
        with open(path, 'w') as outfile:
            json.dump(city, outfile, indent=4, separators=(',', ': '))
        
    def build_dictionary(self):
        city_dictionary = {
            "name": self.name,
            "population": self.population,
            "race relation": self.race_relation,
            "ruler status": self.ruler_status,
            "notable trait": self.notable_trait,
            "known for": self.known_for,
            "calamity": self.calamity,
            "building": self.buildings
        }
        
        return city_dictionary
    