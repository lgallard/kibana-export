# kibana-export

Collection of scripts for exporting Kibana dashboards, visualizations and searches

# Scripts:

## kibana-export 

This scripts export all dashboards, visualizations and searches from localhost to the /tmp/kibana directory

*Usage:*

```
python kibana-export.py
```

## kibana-dashboards-export 

This scripts export all dashboards from localhost to the /tmp/kibana/dashboards directory. You can also export just a dashboard if the dashboard name is given.

*Usage:*

```
python kibana-dashboards-export.py
```
or

```
python kibana-dashboards-export.py dashboard-name
```
## kibana-visualizations-export 

This scripts export all visualizations from localhost to the /tmp/kibana/visualizations directory. You can also export just a visualization if the visualization name is given.

*Usage:*

```
python kibana-visualizations-export.py
```

or

```
python kibana-visualizations-export.py visualization-name
```

## kibana-searches-export 

This scripts export all searches from localhost to the /tmp/kibana/searches directory. You can also export just a search if the searches name is given.

*Usage:*

```
python kibana-searches-export.py
```

or

```
python kibana-searches-export.py search-name
```
