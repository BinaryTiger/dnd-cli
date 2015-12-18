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

    def build_random(self, overwrite=False, verbose=False):
        if verbose:
            print("Randomizing the city race relations")
        self.race_relation = RandomTable.roll(self.build_config_path(propertie=self.RACE_RELATION_PATH))
        if verbose:
            print("-> " + self.race_relation)
            print("Randomizing the city ruler status")
        self.ruler_status = RandomTable.roll(self.build_config_path(propertie=self.RULER_STATUS_PATH))
        if verbose:
            print("-> " + self.ruler_status)
            print("Randomizing the city notable trait")
        self.notable_trait = RandomTable.roll(self.build_config_path(propertie=self.TRAITS_PATH))
        if verbose:
            print("-> " + self.notable_trait)
            print("Randomizing what the city is known for")
        self.known_for = RandomTable.roll(self.build_config_path(propertie=self.KNOWN_FOR_PATH))
        if verbose:
            print("-> " + self.known_for)
            print("Randomizing the city impending calamity")
        self.calamity = RandomTable.roll(self.build_config_path(propertie=self.CALAMITY_PATH))
        if verbose:
            print("-> " + self.calamity)
            print("Saving the city to file")

        save_path = self.OUTPUT_PATH + self.name + self.FILE_EXTENSION
        self.save_to_file(save_path, overwrite, verbose)

        if verbose:
            print("City saved under: " + save_path)

    def save_to_file(self, path, overwrite=False, verbose=False):
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

        with open(path, write_mode) as outfile:
            json.dump(city, outfile, indent=4, separators=(',', ': '))

        if verbose:
            print("-> File saved")

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

    def build_config_path(self, propertie):
        return self.CITY_CONFIG_PATH + propertie + self.FILE_EXTENSION

    @staticmethod
    def show_city(name):
        path = City.OUTPUT_PATH + name + City.FILE_EXTENSION
        print(path)
        with open(path, 'r') as outfile:
            pprint.pprint(json.load(outfile))

