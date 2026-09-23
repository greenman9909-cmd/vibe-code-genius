from __future__ import annotations

import argparse
from .core import GodTreeCore


def main():
    parser = argparse.ArgumentParser(prog='godtree-os')
    sub = parser.add_subparsers(dest='command')

    init = sub.add_parser('init')
    init.add_argument('path', nargs='?', default='.')

    mission = sub.add_parser('mission')
    mission.add_argument('objective')
    mission.add_argument('--path', default='.')

    args = parser.parse_args()

    if args.command == 'init':
        print(GodTreeCore(args.path).register_project())

    elif args.command == 'mission':
        print(GodTreeCore(args.path).create_mission(args.objective))


if __name__ == '__main__':
    main()
