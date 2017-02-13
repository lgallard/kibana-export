#!/usr/bin/python

import requests
import json
import sys
import os

objects = ['dashboard', 'visualization', 'search']

tmpdir='/tmp/kibana/'
hostname = 'localhost'
port = '9200'

for object in objects:

    if object == 'search':
        output_dir = tmpdir + '/' + object + 'es/'
    else:
        output_dir = tmpdir + '/' + object + 's/'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    r = requests.get('http://' + hostname + ':' + port + '/.kibana/' + object + '/_search?pretty')

    json_r = r.json()

    for h in json_r['hits']['hits']:
      #print "%s" %h['_id']

      obj  = requests.get('http://' + hostname + ':' + port + '/.kibana/' + object + '/'+ h['_id'] + '?pretty')
      json_obj = obj.json()

      del json_obj['_index']
      del json_obj['_version']
      del json_obj['found']
      obj_exported = []
      obj_exported.append(json_obj)

      #print json.dumps(obj_exported, indent=2, sort_keys=True)

      with open(output_dir+h['_id']+'.json', 'w') as outfile:
          json.dump(obj_exported, outfile, indent=2, sort_keys=True)

