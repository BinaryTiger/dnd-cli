import argparse

parser = argparse.ArgumentParser(prog='dnd')

#Constants
VERSION = "0.0.1"


#Arguments
parser.add_argument("command", help="main command used by the tool", choices=["build", "show"])

#Flags
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-V", "--version", action='version', version="%(prog)s " + VERSION)
args = parser.parse_args()

if args.verbose:
    print(args.command)
    print("Verbose turned on");
else:
    print(args)