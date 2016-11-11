#!/bin/bash

set -x
set -e
set -u

umask 022

wget --spider -r -nd -nv -H -l 3 -o run1.01.wget.log -D localhost http://localhost:1313 || true
< run1.01.wget.log python process_wget_output.py > run1.02.links.log
grep -B1 'BROKEN LINK' run1.02.links.log > run1.03.broken-links.log
# grep -B1 'broken link!' run1.log | grep -v 'broken link!!!' | grep -v '^--' \
#   | sed -e 's/:$//' | sed -e 's+http://localhost:1313++' > broken.txt
