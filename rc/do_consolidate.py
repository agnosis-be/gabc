#!/usr/bin/python3
#
# This file:
# - /rc/do_consolidate.py (UTF-8/LF/4 SP)
#
# By: agnosis.be
# Repo: gabc
# File version: 1.0
#
# Purpose:
# Consolidate all harvested files stored by Harvester
# into a single CSV file using a format optimized for analysis

import sys
from datetime import date

sys.path.append('../inc')

from consolidate import Consolidator

current_year = date.today().year
input_year_list = list(range(2020, current_year+1))

c = Consolidator(input_year_list)
c.run()