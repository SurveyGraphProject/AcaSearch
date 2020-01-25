"""Different search tools can be found here.
"""

import arxiv
import requests
import json

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


def get_citation_tree(prophy_id):
    """Not sure but I think if the id is correct, only one article is returned
    """
    url = 'https://www.prophy.science/api/articles/{0}/full'.format(prophy_id)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}

    r = requests.get(url, headers=headers)
    res = json.loads(r.content)
    referencesFrom = res['referencesFrom']
    referencesTo = res['referencesTo']
    return referencesFrom, referencesTo

def get_prophy_id(arxiv_id):
    url = 'https://www.prophy.science/api/graphql/?query='
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}

    query='{{ found: search(query:"{}") {{ hits {{ article {{ id }} }} }} }}'.format(arxiv_id)
    r = requests.get(url+query, headers=headers)
    res = json.loads(r.content)
    return res['data']['found']['hits'][0]['article']['id']

