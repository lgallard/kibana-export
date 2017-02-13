#!/usr/bin/python

import requests
import json
import sys
import os

tmpdir = '/tmp/kibana/visualizations/'

if not os.path.exists(tmpdir):
    os.makedirs(tmpdir)

if len(sys.argv) == 2:
    visualization = requests.get('http://localhost:9200/.kibana/visualization/'+ sys.argv[1] + '?pretty')
    json_visualization = visualization.json()

    del json_visualization['_index']
    del json_visualization['_version']
    del json_visualization['found']
    visualizations_exported = []
    visualizations_exported.append(json_visualization)

    #print json.dumps(visualizations_exported, indent=2, sort_keys=True)

    with open(tmpdir+sys.argv[1]+'.json', 'w') as outfile:
        json.dump(visualizations_exported, outfile, indent=2, sort_keys=True)
else:

    visualizations = requests.get('http://localhost:9200/.kibana/visualization/_search?pretty')

    json_visualizations = visualizations.json()

    for h in json_visualizations['hits']['hits']:
      print "%s" %h['_id']

      visualization = requests.get('http://localhost:9200/.kibana/visualization/'+ h['_id'] + '?pretty')
      json_visualization = visualization.json()

      del json_visualization['_index']
      del json_visualization['_version']
      del json_visualization['found']
      visualizations_exported = []
      visualizations_exported.append(json_visualization)

      #print json.dumps(visualizations_exported, indent=2, sort_keys=True)

      with open(tmpdir+h['_id']+'.json', 'w') as outfile:
          json.dump(visualizations_exported, outfile, indent=2, sort_keys=True)

