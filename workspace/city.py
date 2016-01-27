"""This module take care of everything city related """

import json
import pprint
#from workspace.random_table import RandomTable # Used for testing
from random_table import RandomTable # Used for using


class City(object):
    """City class for building the object representation"""

    CALAMITY_PATH = "calamity"
    KNOWN_FOR_PATH = "known_for"
    RACE_RELATION_PATH = "race_relation"
    RULER_STATUS_PATH = "ruler_status"
    TRAITS_PATH = "traits"
    POPULATION_PATH = "population"
    NAME_PATH = "name"
    
    FILE_EXTENSION = ".json"
    CITY_CONFIG_PATH = "../config/city/"
    OUTPUT_PATH = "../output/city/"

    def __init__(self, name=""):
        self.name = name
        self.population = ""
        self.race_relation = ""
        self.ruler_status = ""
        self.notable_trait = ""
        self.known_for = ""
        self.calamity = ""

    def build_random(self, overwrite=False, verbose=False, random_name=True):
        if random_name:
            if verbose:
                print("Randomizing the city name")
            self.name = RandomTable.roll(
                                self.build_config_path(
                                            propertie=self.NAME_PATH))
            if verbose:
                print("-> " + self.name)
        
        if verbose:
            print("Randomizing the city race relations")
        self.race_relation = RandomTable.roll(
                                    self.build_config_path(
                                            propertie=self.RACE_RELATION_PATH))
        if verbose:
            print("-> " + self.race_relation)
            print("Randomizing the city ruler status")
        self.ruler_status = RandomTable.roll(
                                    self.build_config_path(
                                            propertie=self.RULER_STATUS_PATH))
        if verbose:
            print("-> " + self.ruler_status)
            print("Randomizing the city notable trait")
        self.notable_trait = RandomTable.roll(
                                    self.build_config_path(
                                                    propertie=self.TRAITS_PATH))
        if verbose:
            print("-> " + self.notable_trait)
            print("Randomizing what the city is known for")
        self.known_for = RandomTable.roll(
                                self.build_config_path(
                                                propertie=self.KNOWN_FOR_PATH))
        if verbose:
            print("-> " + self.known_for)
            print("Randomizing the city impending calamity")
        self.calamity = RandomTable.roll(
                                self.build_config_path(
                                                propertie=self.CALAMITY_PATH))
        if verbose:
            print("-> " + self.calamity)
            print("Randomizing the city population")
        self.population = RandomTable.roll(
                                    self.build_config_path(
                                                propertie=self.POPULATION_PATH))
        if verbose:
            print("-> " + self.population)
            print("Saving the city to file")

        
        self.save_to_file(overwrite, verbose)

    def save_to_file(self, overwrite=False, verbose=False):
        if verbose:
            print("Building the city dictionary")

        city = self.build_dictionary()

        if verbose:
            print("-> ")
            pprint.pprint(city)
            print("Checking overwrite status")

        if overwrite:
            write_mode = "w"
            if verbose:
                print("-> Overwriting")
        else:
            write_mode = "x"
            if verbose:
                print("-> Not Overwriting")

        if verbose:
            print("Opening the file")
            
        save_path = City.build_output_path(self.name)
        with open(save_path, write_mode) as outfile:
            json.dump(city, outfile, indent=4, separators=(',', ': '))

        if verbose:
            print("City saved under: " + save_path)

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

    @staticmethod
    def build_config_path(propertie):
        return City.CITY_CONFIG_PATH + propertie + City.FILE_EXTENSION
    
    @staticmethod
    def build_output_path(name):
        return City.OUTPUT_PATH + name + City.FILE_EXTENSION

    @staticmethod
    def get_city_by_name(name):
        path = City.build_output_path(name)
        print("info fetch from " + path)
        with open(path, 'r') as outfile:
            return json.load(outfile)

