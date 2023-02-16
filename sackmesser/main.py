# Entry points for command line utils

from argparse import ArgumentParser
from pathlib import Path
import ast
from . import renaming

def rename_trimbits():
    parser = ArgumentParser()
    parser.add_argument('path', type=Path)
    parser.add_argument('lookup', type=ast.literal_eval)
    parser.add_argument('-n', '--dry', action='store_true')
    args = parser.parse_args()

    renaming.rename_trimbits(args.path, args.lookup, args.dry)