"""This module take care of everything city related """


import json
import random


class RandomTable(object):
    """Random table to get random city or npc properties"""
    
    @staticmethod
    def roll(table_path):
        """Roll on the table specifed in the path argument"""
        with open(table_path, 'r') as infile:
            data = json.load(infile)
            roll = random.randint(1, len(data))
            return data[str(roll)]