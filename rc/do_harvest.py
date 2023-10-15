#!/usr/bin/python3
#
# This file:
# - /rc/do_harvest.py (UTF-8/LF/4 SP)
#
# By: agnosis.be
# Repo: gabc
# File version: 1.1
#
# Purpose:
# Get and save the top-10 words suggested by Google's search box for every letter from a to z.
# Do this once a day for all web interface languages (hl) in Harvester.hl_enc_map.
#
# Usage:
# For this script to run once a day, you may want to invoke it using crontab or the like.
# When published as a CGI script on a web server, making a daily HTTP GET request to it does the same.
# Whatever the method, repetitive runs on the same day do not cause any harm.
#

import sys
import os

sys.path.append('../inc')
sys.path.append('../config')

if 'REQUEST_METHOD' in os.environ:
    # if used as CGI script, send HTTP headers
    print('Content-Type: text/plain; charset=UTF-8\r\n')

from harvest import Harvester
from my_client_id import CLIENT_ID

h = Harvester(CLIENT_ID)
h.run()