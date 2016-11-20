#!/bin/bash

find content -type f -exec ./util/update_lastmod.sh {} \;
