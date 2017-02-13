#!/usr/bin/python

import requests
import json
import sys
import os

tmpdir = '/tmp/kibana/dashboards/'
hostname = 'localhost'
port = '9200'

if not os.path.exists(tmpdir):
    os.makedirs(tmpdir)

if len(sys.argv) == 2:
    dashboard = requests.get('http://' + hostname + ':' + port + '/.kibana/dashboard/'+ sys.argv[1] + '?pretty')
    json_dashboard = dashboard.json()

    del json_dashboard['_index']
    del json_dashboard['_version']
    del json_dashboard['found']
    dashboards_exported = []
    dashboards_exported.append(json_dashboard)

    #print json.dumps(dashboards_exported, indent=2, sort_keys=True)

    with open(tmpdir+sys.argv[1]+'.json', 'w') as outfile:
        json.dump(dashboards_exported, outfile, indent=2, sort_keys=True)
else:

    dashboards = requests.get('http://' + hostname + ':' + port + '/.kibana/dashboard/_search?pretty')

    json_dashboards = dashboards.json()

    for h in json_dashboards['hits']['hits']:
      print "%s" %h['_id']

      dashboard = requests.get('http://' + hostname + ':' + port + '/.kibana/dashboard/'+ h['_id'] + '?pretty')
      json_dashboard = dashboard.json()

      del json_dashboard['_index']
      del json_dashboard['_version']
      del json_dashboard['found']
      dashboards_exported = []
      dashboards_exported.append(json_dashboard)

      #print json.dumps(dashboards_exported, indent=2, sort_keys=True)

      with open(tmpdir+h['_id']+'.json', 'w') as outfile:
          json.dump(dashboards_exported, outfile, indent=2, sort_keys=True)

