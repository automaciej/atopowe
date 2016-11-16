#!/usr/bin/env python3

"""Diagnoses broken links in a hugo website. Useful when you import content 
from other places, for example from a Mediawiki instance.
"""

import argparse
import logging
import re
import os
import os.path
import markdown.inlinepatterns

# MARKDOWN_LINK_RE = r'\[.*\]\((.*)\)'
MARKDOWN_LINK_RE = r'\[[^\]]+\]\(([^)]+)\)'

def ExtractLinks(s):
    """Extract Markdown links."""
    # return re.findall(markdown.inlinepatterns.LINK_RE, s, flags=re.M)
    return re.findall(MARKDOWN_LINK_RE, s, flags=re.M)

def PreprocessData(content_dir, content):
    lowercase_path_by_original = {}
    original_path_by_lowercase = {}
    lowercase_link_by_original = {}
    original_link_by_lowercase = {}
    for d, files in content.items():
        logging.debug("d = %r" % d)
        logging.debug("content_dir = %r" % content_dir)
        if d.startswith(content_dir):
            d = d[len(content_dir):]
        logging.debug("after trimming d = %r" % d)
        for filename in files:
            orig_path = os.path.join(d, filename)
            lower_path = orig_path.lower()
            lowercase_path_by_original[orig_path] = lower_path
            original_path_by_lowercase[lower_path] = orig_path
            links = ExtractLinks(files[filename])
            for link in links:
                lowercase_link = link.lower()
                lowercase_link_by_original[link] = lowercase_link
                original_link_by_lowercase[lowercase_link] = link
    return {
            "lowercase_path_by_original": lowercase_path_by_original,
            "original_path_by_lowercase": original_path_by_lowercase,
            "lowercase_link_by_original": lowercase_link_by_original,
            "original_link_by_lowercase": original_link_by_lowercase,
    }


def diagnose_broken_links(content_dir, content):
    data = PreprocessData(content_dir, content)
    print("content_dir:", content_dir)
    for d, files in content.items():
        if d.startswith(content_dir):
            d = d[len(content_dir):]
        for filename in files:
            markdown_links = ExtractLinks(files[filename])
            logging.debug("%r: %r", filename, markdown_links)
 
def main():
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument('content_dir', type=str)
    args = parser.parse_args()
    content = {}
    for root, dirs, files in os.walk(args.content_dir):
        content.setdefault(root, {})
        for f in files:
            try:
                with open(os.path.join(root, f), 'r', encoding='utf-8') as fd:
                    content[root][f] = fd.read()
            except UnicodeDecodeError as e:
                logging.warning(root, f)
    logging.debug("%r", args.content_dir)
    diagnose_broken_links(args.content_dir, content)

if __name__ == '__main__':
    main()
