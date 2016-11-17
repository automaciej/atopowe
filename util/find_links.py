#!/usr/bin/env python
"""Find links in a Markdown file. Output in JSON."""

import argparse
import markdown
import json

class LinkExtractorExtension(markdown.extensions.Extension):

    def extendMarkdown(self, md, md_globals):
        treeprocessor = LinkExtractorProcessor(md)
        treeprocessor.ext = self
        md.treeprocessors['links'] = treeprocessor


class LinkExtractorProcessor(markdown.treeprocessors.Treeprocessor):
    """Process the content while in the tree format."""
    
    def run(self, root):
        self.markdown.links = []
        for link in root.findall('.//a'):
            self.markdown.links.append(link.get('href'))


def GetLinksFromMarkdown(content):
    m = markdown.Markdown(extensions=[LinkExtractorExtension()])
    # We ignore the returned HTML
    html = m.convert(content)
    return m.links


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Extract links from a Markdown page')
    parser.add_argument('input')
    args = parser.parse_args()

    with open(args.input) as fp:
        content = fp.read()

    links = GetLinksFromMarkdown(content)
    print(json.dumps(links, indent=4))
