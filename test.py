from datetime import datetime
from elasticsearch import Elasticsearch
import ipdb
es = Elasticsearch()

ipdb.set_trace()

doc = {
    'author': 'nirmit',
    'text': 'Hey',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", doc_type='tweet', body=doc)
print res
print(res['created'])

# res = es.get(index="test-index", doc_type='tweet', id=1)
# print res
# print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"multi_match": {"query" : "nirmit", "fields": ["author", "text"]} }})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
