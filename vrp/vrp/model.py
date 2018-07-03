# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# file      :model.py
# target    :
# 
# output    :
# author    :Miller
# date      :18.7.2 17:43
# log       :包含修改时间、修改人、修改line及原因
# --------------------------------------------------------------------------------
import typing
import numpy as np

from six.moves import xrange
from .parse import DataTransformItem
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2


class Vehicle(object):
    """Stores the property of every vehicles
    argument:
        car_capacity: dict, the car map capacity dictionary.
    """

    def __init__(self, car_capacity: typing.Dict[str or int, int]) -> None:
        self._capacity = car_capacity

    def capacity_by_idx(self, key: int or str) -> int:
        return self._capacity.get(key)

    @property
    def capacity(self) -> float:
        """gets vehicle capacity"""
        return np.average(list(self._capacity.values()))


class DataProblem:
    """init data for vrp problem, vehicle, nodes, locations, demand etc."""
    def __init__(self, json_file_path):
        self._depot_ = 0
        self._json_path = json_file_path
        self.data = DataTransformItem(self._json_path)

    def fit(self):
        self.data.transform()
        return self

    @property
    def _vehicle(self):
        _vehicle_capacity = self.data.get_vehicle_capacity()
        return Vehicle(_vehicle_capacity)

    @property
    def _num_vehicles(self):
        return len(self.data.get_vehicle_capacity())

    def locations(self):
        _depot_location = self.depot()
        node_locations = [(_loc[0], _loc[1]) for _index, _loc in self.data.get_node_locations()]
        node_locations.insert(0, _depot_location)
        return node_locations

    def depot(self):
        return self.data.get_depot()

    def demand(self):
        node_demands = [_demand for _index, _demand in self.data.get_node_demand()]
        node_demands.insert(0, 0)
        return node_demands





if __name__ == '__main__':
    d = {1: 10, 2: 50, 3: 40}
    v = Vehicle(d)
    print(v.capacity, v.capacity_by_idx(2))
