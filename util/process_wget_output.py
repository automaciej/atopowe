#!/usr/bin/env python

import sys

prev = None
for line in sys.stdin.readlines():
    if line.startswith('2016'):
        sys.stdout.write(line)
    if line.startswith('Remote file does not exist') and prev is not None:
        sys.stdout.write('%s BROKEN LINK\n' % prev.strip())
    prev = line
