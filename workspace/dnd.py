import argparse
import json

parser = argparse.ArgumentParser(prog='dnd')

#Constants
VERSION = "0.0.1"
OUTPUT_PATH_FOR_TESTING = "../output/"
CITY_FOLDER = "../output/city/"
NPC_FOLDER = "../output/npc/"
MOCK_CITY = {"name": "MOCK CITY", "population": 10000}
MOCK_NPC = {"name": "MOCK NPC", "age": 19}


#Arguments
parser.add_argument("command", help="main command used by the tool", choices=["build", "show"])
parser.add_argument("object", help="specify which kind of object the tool have to manipulate", choices=["city", "npc"])
parser.add_argument("name", help="specify the name of the object")

#Flags

parser.add_argument("--overwrite", help="ignores the file exist exception and overwrite it",
                    action="store_true")
parser.add_argument("--random", help="ignores parameters and generate the object randomly",
                    action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-V", "--version", action='version', version="%(prog)s " + VERSION)



args = parser.parse_args()
isVerbose = False
isRandom = False
isOverwrite = False;

#Maybe I can loop the parameters and set the conresponding flags accordingly
if args.verbose:
    isVerbose = True

if args.random:
    isRandom = True

if args.overwrite:
    isOverwrite = True
#End of flags settings

if args.command == "build":
    print("We are building a " + args.object)
    
    filepath = CITY_FOLDER + args.name + ".json"
    with open(filepath, 'w') as outfile:
        json.dump(MOCK_NPC, outfile, indent=4, separators=(',', ': '))
    
    
elif args.command == "show":
    if args.object == "city":
        file_to_read = CITY_FOLDER + args.name + ".json"
        print(file_to_read)
        
        with open(file_to_read, 'r') as infile:
            data = json.load(infile)
            print(json.dumps(data, indent=4, separators=(',', ': ')))