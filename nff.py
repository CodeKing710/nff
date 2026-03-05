#!/bin/env python

import argparse
import yaml
import sys
from pathlib import Path

MAIN_CONFIG = Path("/etc/nff.yml")
INCLUDED_CONFIG = Path("/etc/nff.d")

# Configuration functions
def load_file(path):
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f) or {}
    except yaml.YAMLError as e:
        print(f"Error loading file {path}: {e}", file=sys.stderr)
        sys.exit(1)

def load_cfg(path):
    pass

def merge_cfgs(base, override):
    pass

# Execution flag functions
def show_rules():
    pass

def apply_rules():
    pass

def arg_parser():
    pass

def main():
    parser = arg_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
