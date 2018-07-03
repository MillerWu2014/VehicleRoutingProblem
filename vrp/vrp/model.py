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


if __name__ == '__main__':
    d = {1: 10, 2: 50, 3: 40}
    v = Vehicle(d)
    print(v.capacity, v.capacity_by_idx(2))
