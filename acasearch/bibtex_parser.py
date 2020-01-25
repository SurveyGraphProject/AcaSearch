"""Test file to read bibs in a bibtex file and output 5 referencesTo and 5 referencesFrom for each bib.
"""
from collections import defaultdict
import re

def parse_bibtex(fname):
    # Open bibtex file
    with open(fname) as f:
        lines = ''.join(f.readlines()).rstrip()
        
    # split bibtex into chunks of individual refs
    chunks = list(filter(None, lines.split('@')))
    
    # list of dicts to store the parsed refs
    bibs = [defaultdict(lambda : '') for _ in chunks]

    # Loop over each chunk
    for idx, chunk in enumerate(chunks):
        
        # Get the first ref 
        match = re.search(r'{(.*?),', chunk)
        if match:
            bib_ref = match.group(1)
            bibs[idx]['ref'] = bib_ref
            bibs[idx]['type'] = chunk[:chunk.index('{')]
            
            i = chunk.index('{') + len(bib_ref)
            while i <= len(chunk):
                # Capture LHS of =
                m = re.search(r'(\w*?)=', chunk[i:])
                
                # Capture RHS of =
                if m:
                    # Make a stack to parse parenthesis
                    stack = []
                    
                    # Push the first element manually.
                    i += chunk[i:].index('{')+1
                    stack.append(0)
                    
                    # Loop and parse
                    while len(stack) > 0:
                        c = chunk[i]
                        if c == '{':
                            stack.append(0)
                        elif c == '}':
                            stack.pop()
                        else:
                            bibs[idx][m.group(1)] += c
                        i += 1
                i += 1
    return bibs

