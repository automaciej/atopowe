#!/usr/bin/env python3

import argparse
import collections
import logging
import os
import os.path
import re
import toml
import pprint
import yaml

import hugotools

def main():
    parser = argparse.ArgumentParser(
            description='Add an item to TOML list in a Hugo page')
    parser.add_argument('input', help='A *.md file')
    parser.add_argument('--write', help='Write results back, in-place.',
            default=False, action='store_true')
    parser.add_argument('field_name', help='e.g. "aliases"')
    parser.add_argument('value', help='e.g. "/old/page-location/"')
    args = parser.parse_args()

    metadata = hugotools.GetPageData(args.input)
    print(args)
    front_matter = metadata['front_matter']
    if 'aliases' not in front_matter:
        front_matter['aliases'] = []
    front_matter['aliases'].append(args.value)
    print(metadata['front_matter'])
    new_content = hugotools.ReplaceFrontMatter(metadata['content'], front_matter)

    if args.write:
        with open(args.input, 'w') as fd:
            fd.write(new_content)
    else:
        print('Would have written to {}'.format(args.input))
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
