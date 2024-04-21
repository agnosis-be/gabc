# This file:
# - /inc/harvest.py (UTF-8/LF/4 SP)
#
# By: agnosis.be
# Repo: gabc
# File version: 1.1
#
# Provides:
# - class Harvester

from os import path
from string import ascii_lowercase
from datetime import datetime
from urllib import request
import json

class Harvester:
    """
    Client used to send requests to G**gle's suggest API to collect and store the returned data.

    Collects and stores responses requested ...
    - for a given letter (a..z)
    - for a given interface language (hl)
    - on a given day
    - by a given client

    For usage see:
    - ../rc/do_harvest.py <-- Caller

    The G**ggle suggest API auto-completes keywords entered into G**gle's search box.
    Suggested words heavily depend on the client's geolocation, automatically detected by G**gle.
    Hence different clients will receive a different word list for the same hl on the same day.

    References:
    - web interface language (hl) in: https://sites.google.com/site/tomihasa/google-language-codes
    """

    url_fmt = "http://suggestqueries.google.com/complete/search?client=firefox&q={}&hl={}"

    output_dir = "../data/harvested"
    output_enc = "utf-8"

    hl_enc_map = {
        'de': 'ISO-8859-1',
        'en': 'ISO-8859-1',
        'es': 'ISO-8859-1',
        'fr': 'ISO-8859-1',
        'it': 'ISO-8859-1',
        'nl': 'ISO-8859-1',
        'da': 'ISO-8859-1',
        'sv': 'ISO-8859-1',
        'fi': 'ISO-8859-1',
        'no': 'ISO-8859-1',
        'is': 'ISO-8859-1',
        'pt': 'ISO-8859-1'
    }

    def __init__(self, client_id: str):
        assert(client_id != '')
        assert(client_id[0:6] == 'client')
        assert(client_id[6:8].isnumeric())

        self.client_id = client_id
        self.abc = ascii_lowercase

    def run(self):
        now = datetime.now()
        for hl, enc in self.hl_enc_map.items():
            output_path = "{}/{}/{}_{}_{}.txt".format(
                self.output_dir,
                now.strftime("%Y"),
                now.strftime("%Y-%m-%d"),
                self.client_id,
                hl
            )

            if path.exists(output_path):
                continue

            with open(output_path, mode='wt', encoding=self.output_enc) as out_fo:
                for letter in self.abc:
                    url = self.url_fmt.format(letter, hl)
                    with request.urlopen(url) as url_fp:
                        response_bytes = url_fp.read()
                        response_str = response_bytes.decode(enc)
                        response_json = json.loads(response_str)
                        print("|".join(response_json[1]), file=out_fo)