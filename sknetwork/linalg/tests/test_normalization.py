#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on April 2020
@author: Nathan de Lara <ndelara@enst.fr>
"""

import unittest

import numpy as np
from scipy import sparse

from sknetwork.basics import CoNeighbors
from sknetwork.linalg import normalize


class TestNormalization(unittest.TestCase):

    def test_formats(self):
        n = 5
        mat1 = normalize(np.eye(n))
        mat2 = normalize(sparse.eye(n))
        mat3 = normalize(CoNeighbors(mat2))

        x = np.random.randn(n)
        self.assertAlmostEqual(np.linalg.norm(mat1.dot(x) - x), 0)
        self.assertAlmostEqual(np.linalg.norm(mat2.dot(x) - x), 0)
        self.assertAlmostEqual(np.linalg.norm(mat3.dot(x) - x), 0)