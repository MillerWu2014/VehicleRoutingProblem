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

from vrp import PROJECT_ROOT, DataTransformItem


_json_file = os.path.join(PROJECT_ROOT, "data/data.json")
json_parse = DataTransformItem(_json_file)
json_parse.transform()

print(json_parse.get_vehicle_capacity())
for loc in json_parse.get_node_demand():
    print(loc)
