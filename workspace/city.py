"""This module take care of everything city related """


import json
import pprint
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
        self.name = name
        self.population = population
        self.race_relation = ""
        self.ruler_status = ""
        self.notable_trait = ""
        self.known_for = ""
        self.calamity = ""


    def build_random(self, overwrite=False):
        self.race_relation = RandomTable.roll(self.build_config_path(propertie=self.RACE_RELATION_PATH))
        self.ruler_status = RandomTable.roll(self.build_config_path(propertie=self.RULER_STATUS_PATH))
        self.notable_trait = RandomTable.roll(self.build_config_path(propertie=self.TRAITS_PATH))
        self.known_for = RandomTable.roll(self.build_config_path(propertie=self.KNOWN_FOR_PATH))
        self.calamity = RandomTable.roll(self.build_config_path(propertie=self.CALAMITY_PATH))
        
        self.save_to_file(self.OUTPUT_PATH + self.name + self.FILE_EXTENSION, overwrite) 

    def save_to_file(self, path, overwrite=False):
        city = self.build_dictionary()
        
        if overwrite:
            write_mode = "w"
        else:
            write_mode = "x"
            
        with open(path, write_mode) as outfile:
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
        }

        return city_dictionary
        
    def build_config_path(self, propertie=""):
        return self.CITY_CONFIG_PATH + propertie + self.FILE_EXTENSION
    
    @staticmethod    
    def show_city(name):
        path = City.OUTPUT_PATH + name + City.FILE_EXTENSION
        print(path)
        with open(path, 'r') as outfile:
            pprint.pprint(json.load(outfile))
        
