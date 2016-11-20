#!/bin/bash

set -e
set -u

readonly f=$1
isodate=$(git log --pretty=%cI -n1 -- "${f}")
util/set_in_front_matter.py --write "${f}" lastmod "${isodate}"
