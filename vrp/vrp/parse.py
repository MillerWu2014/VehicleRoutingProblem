# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# file      :parse.py
# target    :
# 
# output    :
# author    :Miller
# date      :18.7.2 16:27
# log       :包含修改时间、修改人、修改line及原因
# --------------------------------------------------------------------------------
import os
import json
import typing


class DataTransformItem(object):
    """ Parsing the json data, transform to format python object
    argument
    --------
        json_file: str, the json file full path.
    """
    def __init__(self, json_file: str) -> None:
        self.file_path = json_file
        self._keys = ["vehicleCapacity", "depot", "nodes"]
        self._network_dict = dict()

    def _exists(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("The json file is not exist in path: %s" % self.file_path)

    def _parse(self) -> dict:
        with open(self.file_path, "r") as handler:
            try:
                json_to_dict = json.load(handler)
                return json_to_dict
            except Exception as error:
                print("The json data transform to dictionary failed. error:", error)
                exit(1)

    def transform(self) -> object:
        self._exists()  # checking the file whether or not.
        self._network_dict = self._parse()
        for _key in self._keys:
            if _key not in self._network_dict:
                print("The key('%s') is not in json data. The json data must has this key('%s')."
                      % (_key, _key))
                raise KeyError("The json data has not the '%s' item." % _key)
        return self

    def get_vehicle_capacity(self) -> dict:
        """Fetch vehicle capacity from json data"""
        _vehicle_capacity = self._network_dict.get('vehicleCapacity')
        return dict([list(d.items())[0] for d in _vehicle_capacity])

    def get_depot(self):
        return tuple(self._network_dict.get("depot").values())

    def _nodes_index_value(self) -> typing.Iterator:
        node_items = self._network_dict.get("nodes")
        return enumerate(node_items, start=1)

    def get_node_locations(self) -> typing.Iterator:
        for _index, _node in self._nodes_index_value():
            yield _index, (_node.get("x"), _node.get("y"))

    def get_node_demand(self) -> typing.Iterator:
        for _index, _node in self._nodes_index_value():
            yield _index, _node.get("demand")



