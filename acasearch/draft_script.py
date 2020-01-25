"""Test file to read bibs in a bibtex file and output 5 referencesTo and 5 referencesFrom for each bib.
"""
import requests, json 
from pybtex import database

# Example bib file
bibs = database.parse_file('sample.bib')
for bib_title, bib_entry in bibs.entries.items():
    query = {
        'title': '',
        'abstract': '',
        'authors': ,'',
        
        }
    for key, value in bib_entry.fields.items():
        query[key] = value
    
    print(query)