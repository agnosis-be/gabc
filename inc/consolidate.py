# This file:
# - /inc/consolidate.py (UTF-8/LF/4 SP)
#
# By: agnosis.be
# Repo: gabc
# File version: 1.0
#
# Provides:
# - class Consolidator

import glob
import os
import time
from datetime import datetime
from string import ascii_lowercase

class Consolidator:
    """
    Aggregator used to create a single CSV file from all harvested files using an output format optimized for analysis.

    Given the following harvested file:
        2023-10-10_client01_de.txt

    with the following data:
        aharvested1|aharvested2|aharvested3|aharvested4|aharvested5|aharvested6|aharvested7|aharvested8|aharvested9|aharvested10
        bharvested1|bsuggest2|bsuggest3|bsuggest4|bsuggest5|bsuggest6|bsuggest7|bsuggest8|bsuggest9|bsuggest10

    this class will create the following consolidated file:
        letter|rank|term|lang|client|date'
        a|1|aharvested1|de|client01|10.10.2023
        a|2|aharvested2|de|client01|10.10.2023
        a|3|aharvested3|de|client01|10.10.2023
        a|4|aharvested4|de|client01|10.10.2023
        a|5|aharvested5|de|client01|10.10.2023
        a|6|aharvested6|de|client01|10.10.2023
        a|7|aharvested7|de|client01|10.10.2023
        a|8|aharvested8|de|client01|10.10.2023
        a|9|aharvested9|de|client01|10.10.2023
        a|10|aharvested10|de|client01|10.10.2023
        b|1|bharvested1|de|client01|10.10.2023
        b|2|bharvested2|de|client01|10.10.2023
        b|3|bharvested3|de|client01|10.10.2023
        b|4|bharvested4|de|client01|10.10.2023
        b|5|bharvested5|de|client01|10.10.2023
        b|6|bharvested6|de|client01|10.10.2023
        b|7|bharvested7|de|client01|10.10.2023
        b|8|bharvested8|de|client01|10.10.2023
        b|9|bharvested9|de|client01|10.10.2023
        b|10|bharvested10|de|client01|10.10.2023

    For usage see:
    - ../rc/do_consolidate.py <-- Caller

    For class Harvester see:
    - ./harvest.py
    """

    input_dir = '../data/harvested'
    input_enc = 'utf-8'
    input_file_pattern = '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]_client[0-9][0-9]_[a-z][a-z].txt'

    output_dir = '../data/consolidated'
    output_enc = 'utf-8'
    output_header = ['letter', 'rank', 'term', 'lang', 'client', 'date']
    output_sep = '|'

    def __init__(self, input_year_list: list[int]):
        self.input_year_list = input_year_list
        self.output_path = "{}/gabc_db_{}.txt".format(self.output_dir, int(time.time()))

    def run(self):
        file_path_list = []
        for input_year in self.input_year_list:
            path = "{}/{}/{}".format(self.input_dir, input_year, self.input_file_pattern)
            file_path_list.extend(glob.glob(path))

        file_path_list.sort()

        with open(self.output_path, 'w', encoding=self.output_enc) as out_fo:
            # print header
            print(*self.output_header, sep=self.output_sep, file=out_fo)
            for file_path in file_path_list:
                try:
                    with open(file_path, mode='r', encoding=self.input_enc) as fp:
                        filename = os.path.basename(file_path)
                        date_string, client, lang = filename.split('.')[0].split('_')
                        for idx, line in enumerate(fp.readlines()):
                            term_list = line.strip().split('|')
                            if len(term_list) == 10:
                                for rank, term in enumerate(term_list):
                                    print(
                                        # letter
                                        ascii_lowercase[idx],
                                        # rank
                                        rank+1,
                                        # term
                                        term,
                                        # lang
                                        lang,
                                        # client
                                        client,
                                        # ... date
                                        datetime.strptime(date_string,"%Y-%m-%d").strftime("%d.%m.%Y"),
                                        sep=self.output_sep,
                                        file=out_fo
                                    )
                            else:
                                print('ERROR: column count', filename)
                                break
                except UnicodeDecodeError:
                    print('ERROR: decode', file_path)
                except UnicodeEncodeError:
                    print('ERROR: encode', file_path)