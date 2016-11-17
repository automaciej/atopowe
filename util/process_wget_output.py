#!/usr/bin/env python

import argparse
import io
import logging
import os
import os.path
import re
import requests
import urllib.parse
from bs4 import BeautifulSoup
from fuzzywuzzy import process
import pprint
import json

import hugotools

WHITELIST = set([
        'http://localhost:1313/forum'
])

def Process(inlines):
    out = []
    prev = None
    last_url = None
    lines = []
    for line in inlines:
        if line.startswith('2016'):
            # This is a link. Let's find it.
            parts = re.split('\s+', line)
            last_url = parts[2]
            if last_url == 'URL:':
                last_url = parts[3]
            last_url = re.sub('URL:', '', last_url).strip()
            last_url = re.sub(':$', '', last_url)
        if line.startswith('Remote file does not exist') and prev is not None:
            # This means that in the previous line we had the broken URL.
            broken_url = re.sub(':$', '', prev.strip())
            if broken_url not in WHITELIST:
                out.append((last_url, broken_url))
        prev = line
    return out


def FrontRemove(s, pattern):
    if s.startswith(pattern):
        return s[len(pattern):]
    return s


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(
            description='Extract links from a Markdown page')
    parser.add_argument('input')
    parser.add_argument('content_dir')
    parser.add_argument('--write', default=False, action='store_true')
    args = parser.parse_args()

    with open(args.input, 'r', errors='ignore') as fd:
        broken_links = Process(fd.readlines())

    # Let's make an index of content stuff.
    content_files = []
    for root, dirs, files in os.walk(args.content_dir):
        relroot = root.lstrip(args.content_dir)
        for name in files:
            if name.endswith('.md'):
                content_files.append(os.path.join(relroot, name))

    baseurl = 'http://localhost:1313/'
    # We don't really know which URL has a broken link. So let's try to fix them
    # all.
    fix_candidates = {x.lower(): x for x in content_files}
    fix_ideas = {}
    broken_link_slugs = []
    for url, broken_link in broken_links:
        broken_link_rel = FrontRemove(broken_link, baseurl)
        broken_link_rel_unquoted = urllib.parse.unquote(broken_link_rel)
        broken_link_slugs.append(broken_link_rel_unquoted)
        broken_link_rel_unquoted_lower = broken_link_rel_unquoted.lower()
        print('BROKEN LINK: %s, %r' % (broken_link, broken_link_rel_unquoted))
        fix_idea, match_ratio = process.extractOne(
                broken_link_rel_unquoted,
                fix_candidates.keys())
        print('Fix for %r could be %r with ratio %d' % (broken_link_rel,
            fix_candidates[fix_idea], match_ratio))
        fix_ideas[broken_link] = (fix_candidates[fix_idea],
                broken_link_rel_unquoted, match_ratio)
    print('Writing fix ideas')
    with open('fix-ideas.json', 'w') as fd:
        json.dump(fix_ideas, fd, indent=2)
    with open('broken-link-slugs.json', 'w') as fd:
        json.dump(broken_link_slugs, fd, indent=2)
    with open('broken.txt', 'w') as fd:
        fd.write('\n'.join(broken_link_slugs) + '\n')
