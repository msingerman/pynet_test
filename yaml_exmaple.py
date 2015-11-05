#!~/applied_python/bin/python

import yaml
import json

my_list = range(3)
my_list.append('burrito')
my_list.append({})
my_list[-1]['ip'] = '10.10.10.10'
my_list[-1]['attrib'] = 'office'

with open("my_file.yml", "w") as f:
  yaml.dump(my_list, f, default_flow_style=True)

with open("my_file.json", "w") as f:
  json.dump(my_list, f)
