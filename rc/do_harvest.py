#!/usr/bin/python3
#
# This file:
# - /rc/do_harvest.py (UTF-8/LF/4 SP)
#
# By: agnosis.be
# Repo: gabc
# File version: 1.0
#
# Purpose:
# Get and save the top-10 words suggested by Google's search box for every letter from a to z.
# Do this once a day for all web interface languages (hl) in Harvester.hl_enc_map.
#
# Usage:
# For this script to run once a day, you may want to invoke it using crontab or the like.
#

import sys
sys.path.append('../inc')
sys.path.append('../config')

from harvest import Harvester
from my_client_id import CLIENT_ID

h = Harvester(CLIENT_ID)
h.run()