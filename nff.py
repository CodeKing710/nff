#!/usr/bin/env python

import argparse
import yaml
import sys
import subprocess
from pathlib import Path

MAIN_CONFIG = Path("/etc/nff.yml")
INCLUDED_CONFIG = Path("/etc/nff.d")
SHARE_PATH = Path("/usr/share/nff")
NFT_CONFIG = Path("/etc/nftables.d/00-nff.nft")
VERBOSE = False

# Verbose logging function
def verbose(*msgs):
    if VERBOSE:
        print(*msgs)


# Configuration functions
def load_file(path):
    if not path.exists():
        print(f"Error finding file {path}", file=sys.stderr)
        sys.exit(1)
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f) or {}
    except yaml.YAMLError as e:
        print(f"Error loading file {path}: {e}", file=sys.stderr)
        sys.exit(1)

def load_cfg():
    config = load_file(MAIN_CONFIG)
    if INCLUDED_CONFIG.is_dir():
        for extra in INCLUDED_CONFIG.glob("*.yml"):
            config.update(load_file(extra))
    return config

# Singletons
def show_version():
    with open(SHARE_PATH / "version", 'r') as f:
        print(f.read().strip())

# Execution flag functions
def show_rules(args, config):
    if args.nfstyle:
        try:
            result = subprocess.run(["nft","list","ruleset"], capture_output=True, text=True)
            print(result.stdout)
        except FileNotFoundError:
            print("Error: nftables is not accessible. Check if it is installed and in the PATH", file=sys.stderr)
    else:
        # Print out the YAML config in a nice way
        print(config)

def apply_rules(args, config):
    if NFT_CONFIG.exists():
        verbose(f"Applying NFF rules...")
        subprocess.run(["nft","-f",str(NFT_CONFIG)], check=True)

    print("NFF rules applied!")

def arg_parser():
    parser = argparse.ArgumentParser(description="nff: A simple nftables firewall tool")
    parser.add_argument('-V', '--verbose', action='store_true')
    parser.add_argument('-v', '--version', action='store_true')
    subparsers = parser.add_subparsers(dest="status | apply")

    # Show rules

    show_p = subparsers.add_parser('status')
    show_p.add_argument('-N', '--nfstyle', action='store_true')
    show_p.set_defaults(func=show_rules)

    # Apply Configs

    apply_p = subparsers.add_parser('apply')
    apply_p.set_defaults(func=apply_rules)

    return parser

def main():
    global VERBOSE
    parser = arg_parser()
    args = parser.parse_args()

    # Check verbosity
    if args.verbose:
        VERBOSE = True
    elif args.version:
        show_version()
        sys.exit(0)

    # Load configs and begin
    config = load_cfg()
    if hasattr(args, 'func'):
        args.func(args, config)
    else:
        with open(SHARE_PATH / "help",'r') as f:
            print(f.read())

if __name__ == "__main__":
    main()
