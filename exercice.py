#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import math


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(start=-1.3, stop=3.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return [(math.sqrt(coord[0]**2 + coord[1]**2), math.atan2(coord[1]. coord[0])) for coord in cartesian_coordinates]


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.argmin(np.absolute(values - float))


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    pass
