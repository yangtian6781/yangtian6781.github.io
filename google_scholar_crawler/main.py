print(1, flush=True)
from scholarly import scholarly
print(1)
import jsonpickle
print(1)
import json
print(1)
from datetime import datetime
print(1)
import os

print(1)
print(os.environ['GOOGLE_SCHOLAR_ID'])
author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
print(1)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
print(1)
name = author['name']
print(1)
author['updated'] = str(datetime.now())
print(1)
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
