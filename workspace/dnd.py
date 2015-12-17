""" This module is the core dnd app. Use dnd -h for help"""


import argparse
import json
from city import City
from random_table import RandomTable

parser = argparse.ArgumentParser(prog='dnd')

# Constants
VERSION = "0.0.1"
MOCK_NPC = {"name": "MOCK NPC", "age": 19}


# Arguments
parser.add_argument("command", help="main command used by the tool", choices=["build", "show"])
parser.add_argument("object", help="specify which kind of object the tool have to manipulate", choices=["city", "npc"])
parser.add_argument("name", help="specify the name of the object")

# Flags
parser.add_argument("--overwrite", help="ignores the file exist exception and overwrite it",
                    action="store_true")
parser.add_argument("--random", help="ignores parameters and generate the object randomly, "
                    "you can also specify how many cities you want by passing an "
                    "optional number with the flag",
                    type=int, const=1, nargs='?')
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-V", "--version", action='version', version="%(prog)s " + VERSION)


args = parser.parse_args()
is_verbose = False
is_random = False
is_overwrite = False

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

    if args.object == "city" and is_random:
        print("building " + str(args.random) + " cities")
        city = City(args.name, 10000)
        city.build_random(overwrite = is_overwrite, verbose=is_verbose);

elif args.command == "show":
    print("Showing " + args.name)
    City.show_city(args.name)
