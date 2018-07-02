# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# file      :parse_test.py
# target    :
# 
# output    :
# author    :Miller
# date      :18.7.2 17:36
# log       :包含修改时间、修改人、修改line及原因
# --------------------------------------------------------------------------------
import os

from vrp import PROJECT_ROOT, ParseJsonFormat


_json_file = os.path.join(PROJECT_ROOT, "data/data.json")
json_parse = ParseJsonFormat(_json_file)
json_parse.transform()
for loc in json_parse.get_node_demand():
    print(loc)
