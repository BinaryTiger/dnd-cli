""" This module is the core dnd app. Use dnd -h for help"""

import argparse
import pprint
from city import City
from npc import Npc

parser = argparse.ArgumentParser(prog='dnd')

# Constants
VERSION = "0.0.1"
MOCK_NPC = {"name": "MOCK NPC", "age": 19}


# Arguments
parser.add_argument("command", help="main command used by the tool", choices=["build", "show"])
parser.add_argument("object", help="specify which kind of object the tool have to manipulate", choices=["city", "npc"])
parser.add_argument("name", help="specify the name of the object")

# Flags
parser.add_argument("-o", "--overwrite", help="ignores the file exist exception and overwrite it",
                    action="store_true")
parser.add_argument("--random", help="ignores parameters and generate the object randomly, "
                    "you can also specify how many cities you want by passing an "
                    "optional number with the flag",
                    type=int, const=1, nargs='?')
parser.add_argument("--forcename", help="Force the specified name", action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-V", "--version", action='version', version="%(prog)s " + VERSION)


args = parser.parse_args()
is_verbose = args.verbose
is_random = args.random
is_overwrite = args.overwrite
is_random_name = not args.forcename

if args.command == "build":
    if args.object == "city" and is_random:
        print("Building " + str(args.random) + " city")
        city = City(args.name)
        city.build_random(overwrite=is_overwrite, verbose=is_verbose, random_name=is_random_name)
    if args.object == "npc" and is_random:
        print("Building " + str(args.random) + " npc")
        npc = Npc(args.name)
        npc.build_random(overwrite=is_overwrite, verbose=is_verbose)

elif args.command == "show":
    if args.object == "city":
        pprint.pprint(City.get_city_by_name(args.name))
    if args.object == "npc":
        pprint.pprint(Npc.get_npc_by_name(args.name))
