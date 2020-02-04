"""Different search tools can be found here.
"""

import arxiv
import requests
import json
import pprint

def arxiv_search(title, n=None):
    q = 'ti:{0}'
    query =  q.format(
        title,
    )
    res = arxiv.query(
        query=query,
        max_results=3,
        sort_by="relevance")
    if n is None:
        return res
    elif n == 1:
        return res[0]
    else:
        return res[:n]


def get_citation_tree(prophy_id, depth=1, width=5):
    """Return a citation tree in json format with depth and width.

    example
    -------
from acasearch.search_tools import get_citation_tree
get_citation_tree(403)
    """
    url = 'https://www.prophy.science/api/articles/{0}/full'.format(prophy_id)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}

    r = requests.get(url, headers=headers)
    res = json.loads(r.content) # loads a dictionary

    ret_dict = {
        'title': '',
        'authors': [],
        'year': '',
        'url': '',
        'referencesTo' : [],
        'referencesFrom' : []
    }
    
    article = res['article']

    ret_dict['title'] = article['title']
    ret_dict['authors'] = [author['name'] for author in article['authors']]
    ret_dict['year'] = article['year']
    ret_dict['url'] = article['urls'].pop(0) if article['urls'] else ''
    
    for ref_type in ['referencesFrom', 'referencesTo']:
        for ref in res[ref_type]['references'][:width]:
            obj = {
                'title': ref['title'],
                'authors': [author['name'] for author in ref['authors']],
                'year': ref['year'],
                # 'url': ref['urls'].pop(0) if ref['urls'] else ''
            }
        ret_dict[ref_type].append(obj)

    return json.dumps(ret_dict)

def get_prophy_id(arxiv_id):
    url = 'https://www.prophy.science/api/graphql/?query='
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}

    query='{{ found: search(query:"{}") {{ hits {{ article {{ id }} }} }} }}'.format(arxiv_id)
    r = requests.get(url+query, headers=headers)
    res = json.loads(r.content)
    
    return res['data']['found']['hits'][0]['article']['id']

if __name__ == "__main__":
    print(get_citation_tree(403))