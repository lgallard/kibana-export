#!/usr/bin/python

import requests
import json
import sys
import os

tmpdir = '/tmp/kibana/searches/'
hostname = 'localhost'
port = '9200'

if not os.path.exists(tmpdir):
    os.makedirs(tmpdir)

if len(sys.argv) == 2:
    search = requests.get('http://' + hostname + ':' + port + '/.kibana/search/'+ sys.argv[1] + '?pretty')
    json_search = search.json()

    del json_search['_index']
    del json_search['_version']
    del json_search['found']
    searches_exported = []
    searches_exported.append(json_search)

    #print json.dumps(searches_exported, indent=2, sort_keys=True)

    with open(tmpdir+sys.argv[1]+'.json', 'w') as outfile:
        json.dump(searches_exported, outfile, indent=2, sort_keys=True)
else:

    searches = requests.get('http://' + hostname + ':' + port + '/.kibana/search/_search?pretty')

    json_searches = searches.json()

    for h in json_searches['hits']['hits']:
      print "%s" %h['_id']

      search = requests.get('http://' + hostname + ':' + port + '/.kibana/search/'+ h['_id'] + '?pretty')
      json_search = search.json()

      del json_search['_index']
      del json_search['_version'] 
      del json_search['found'] 
      searches_exported = []
      searches_exported.append(json_search)

      #print json.dumps(searches_exported, indent=2, sort_keys=True)

      with open(tmpdir+h['_id']+'.json', 'w') as outfile:
          json.dump(searches_exported, outfile, indent=2, sort_keys=True)
