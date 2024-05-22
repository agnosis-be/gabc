# gabc
G**gle ABC

## Motivation
When you enter a search term into [G\*\*gle's search box](https://www.google.com), G\*\*gle suggests 10 different searches for that term.

The suggested searches depend on:
- entered search term
- date
- client's geolocation
- interface language (hl)
- (possibly other parameters)

Collecting and storing the suggested search terms for a longer period of time, creates an interesting data set. The data set may be analyzed using various questions.

## Ansatz
This repository provides functions to
- harvest,
- consolidate, and
- analyze

data returned by the suggest API.

To keep it simple, as search terms we use single letters, from a to z. In that way, we can create a G\*\*gle ABC over time, hence the name of this repository.

A given client harvests the suggested 10 search terms

- once a day
- for every letter from a to z
- for a given list of interface languages (hl)
- from a given machine

## Participate
If you want to participate in harvesting data

1. Clone this repository
   ```
   $ git clone https://github.com/agnosis-be/gabc.git
   ```
3. Request a unique client_id by sending an email to &#109;&#97;&#114;&#107;&#117;&#115;&#46;&#107;&#108;&#105;&#101;&#64;&#119;&#101;&#98;&#46;&#100;&#101;
4. Upon our reply, copy `config/my_client_id.skel` to `config/my_client_id.py`
5. Update `config/my_client_id.py` with the client_id assigned to you
6. Make sure that `rc/do_harvest.py` runs once a day on the same machine
7. Verify that `data/harvested/<year>/` is populated with files created by you
8. Commit and push files created by you to this repository (e.g. once a year)
   ```
   $ git pull
   $ git add data/harvested/*
   $ git commit -m "Added data harvested by <client_id> in <year>"
   $ git push origin main
   ```


