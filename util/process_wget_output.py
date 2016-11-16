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
    # print('\n'.join(str(x) for x in broken_links))

    # Let's make an index of content stuff.
    content_files = []
    
    for root, dirs, files in os.walk(args.content_dir):
        relroot = root.lstrip(args.content_dir)
        for name in files:
            if name.endswith('.md'):
                content_files.append(os.path.join(relroot, name))

    baseurl = 'http://localhost:1313/'
    count = 0
    # We don't really know which URL has a broken link. So let's try to fix them
    # all.
    for url, broken_link in broken_links:
        if re.search(r'\.(png|jpg|JPG)$', url):
            # Graphics take a long time to process and is pointless here.
            continue
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        metatag = soup.find('meta', id='file-source')
        if metatag:
            file_source = metatag.get('content')
        else:
            print('no file source for %r, but it has a broken link %r' % (url,
                broken_link))
            continue
        print('Processing:', url, file_source, broken_link)
        # Now we know to edit file_source and that we have a broken link there.
        file_path = os.path.join(args.content_dir, file_source)
        broken_link_rel = FrontRemove(broken_link, baseurl)
        broken_link_rel_unquoted = urllib.parse.unquote(broken_link_rel)
        broken_link_rel_unquoted_lower = broken_link_rel.lower()
        found = []
        for cf in content_files:
            cf_lower = cf.lower()
            # This is where we're guessing what to use
            if cf_lower.startswith(broken_link_rel_unquoted_lower):
                found.append(cf)
        if found:
            print('We can fix %r by replacing broken link %r (%r?) with one of %r' % (
                    file_source, broken_link, broken_link_rel, found))
        else:
            print('No ideas how to fix %r in %r' % (broken_link_rel_unquoted, file_source))
            continue
        with open(file_path, 'r') as fd:
            md_content = fd.read()
        new_content = md_content.replace('/' + broken_link_rel_unquoted, '{{< relref "%s" >}}' % found[0])
        if new_content == md_content:
            logging.info("Trying to replace %r didn't work", broken_link_rel_unquoted)
        if args.write:
            with open(file_path, 'w') as fd:
                fd.write(new_content)
        else:
            logging.info('Running in dry run mode, not writing to %r.',
                    file_path)
        count += 1
        if count > 10:
            # break
            pass
