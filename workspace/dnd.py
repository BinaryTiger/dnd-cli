"""This module is the core dnd app. Use dnd -h for help"""


import argparse
import json
from city import City

parser = argparse.ArgumentParser(prog='dnd')

# Constants
VERSION = "0.0.1"
OUTPUT_PATH_FOR_TESTING = "../output/"
MOCK_CITY = {"name": "MOCK CITY2", "population": 10000}
MOCK_NPC = {"name": "MOCK NPC", "age": 19}


# Arguments
parser.add_argument("command", help="main command used by the tool", choices=["build", "show"])
parser.add_argument("object", help="specify which kind of object the tool have to manipulate", choices=["city", "npc"])
parser.add_argument("name", help="specify the name of the object")

# Flags
parser.add_argument("--overwrite", help="ignores the file exist exception and overwrite it",
                    action="store_true")
parser.add_argument("--random", help="ignores parameters and generate the object randomly",
                    action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-V", "--version", action='version', version="%(prog)s " + VERSION)


args = parser.parse_args()
is_verbose = False
is_random = False
is_overwrite = False
file_path = OUTPUT_PATH_FOR_TESTING + args.object + "/" + args.name + ".json"

# Maybe I can loop the parameters and set the corresponding flags accordingly
if args.verbose:
    is_verbose = True

if args.random:
    is_random = True

if args.overwrite:
    is_overwrite = True
# End of flags settings

if args.command == "build":
    print("We are building a " + args.object)

    if args.object == "city":
        city = City()
        city.name = args.name
        city.population = 10000

        city.save_to_file(file_path)

elif args.command == "show":
    with open(file_path, 'r') as infile:
        data = json.load(infile)
        print(json.dumps(data, indent=4, separators=(',', ': ')))
