"""This module take care of everything city related """


import json
from random_table import RandomTable


class City(object):
    """City class for building the object representation"""
    
    CALAMITY_PATH = "calamity"
    KNOWN_FOR_PATH = "known_for"
    RACE_RELATION_PATH = "race_relation"
    RULER_STATUS_PATH = "ruler_status"
    TRAITS_PATH = "traits"
    
    FILE_EXTENSION = ".json"
    CITY_CONFIG_PATH = "../config/city/"
    OUTPUT_PATH = "../output/city/"

    def __init__(self, name, population):
        self.data = []
        self.name = name
        self.population = population
        self.race_relation = ""
        self.ruler_status = ""
        self.notable_trait = ""
        self.known_for = ""
        self.calamity = ""
        self.buildings = []


    def build_random(self):
        self.race_relation = RandomTable.roll(self.build_config_path(propertie=self.RACE_RELATION_PATH))
        self.ruler_status = RandomTable.roll(self.build_config_path(propertie=self.RULER_STATUS_PATH))
        self.notable_trait = RandomTable.roll(self.build_config_path(propertie=self.TRAITS_PATH))
        self.known_for = RandomTable.roll(self.build_config_path(propertie=self.KNOWN_FOR_PATH))
        self.calamity = RandomTable.roll(self.build_config_path(propertie=self.CALAMITY_PATH))
        
        self.save_to_file(self.OUTPUT_PATH + self.name + self.FILE_EXTENSION) 

    def save_to_file(self, path):
        city = self.build_dictionary()
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
        
    def build_config_path(self, propertie=""):
        return self.CITY_CONFIG_PATH + propertie + self.FILE_EXTENSION
