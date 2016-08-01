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
            return_value = str(data[str(roll)])
            
            if return_value.startswith("tbl_"):
                path_to_roll_on = return_value.split('_')[1]
                RandomTable.roll(path_to_roll_on)
                
            return data[str(roll)]
