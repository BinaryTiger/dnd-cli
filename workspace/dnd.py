import argparse

parser = argparse.ArgumentParser()

parser.add_argument("command", help="main command used by the tool", choices=["build", "show"])
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

if args.verbose:
    print(args.command)
    print("Verbose turned on");
else:
    print(args)