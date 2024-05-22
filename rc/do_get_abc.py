#!/usr/bin/python3
#
# This file:
# - /rc/do_get_abc.py (UTF-8/LF/4 SP)
#
# By: agnosis.be
# Repo: gabc
# File version: 1.0
#
# Purpose:
# For every letter from a to z get G**gle's top suggest term for that letter incl. its frequency
#
# Usage:
# 1. Run ./do_consolidate.py and record the filename created in ../data/consolidated
# 2. Copy ../config/my_analysis.skel to ../config/my_analysis.py
# 3. In my_analysis.py: set `input_file' to filename created in step 1;
#    set `user_name' to your user name
# 4. Run ./do_get_abc.py (this file)
# 5. View files created in ../data/analyzed

import sys
sys.path.append('../inc')
sys.path.append('../config')

from analyze import Analyzer, InvalidArguments, OutOfBounds, NoResults, UnknownOutputFormat
from my_analysis import user_name, input_file, dates, clients, langs, ranks

a = Analyzer(input_file=input_file)

try:
    abc_dict = a.get_abc(dates=dates, clients=clients, langs=langs, ranks=ranks)
    a.save_result(
        result_dict=abc_dict,
        output_format='htm',
        user_name=user_name,
        function_used='getabc',
        dates=dates,
        clients=clients,
        langs=langs,
        ranks=ranks
    )

except InvalidArguments as e:
    print('ERR:', e, file=sys.stderr)
except OutOfBounds as e:
    print('ERR:', e, file=sys.stderr)
except KeyError as e:
    print('ERR:', e, file=sys.stderr)
except NoResults as e:
    print('ERR:', e, file=sys.stderr)
except FileExistsError as e:
    print('ERR:', e, file=sys.stderr)
except UnknownOutputFormat as e:
    print('ERR:', e, file=sys.stderr)
