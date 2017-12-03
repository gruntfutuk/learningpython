import argparse
parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="Echo the text you see here.")
# args = parser.parse_args()
# print(args.echo)
parser.add_argument("square", help="display a square of a given number",
                    type=int)
parser.add_argument("--verbosity", "-v", "-s", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
print(args.square**2)
