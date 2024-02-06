#!/usr/bin/env python3
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Test access_nested_map function'''
    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a", "b"], 2)
        ]
    )
    def test_access_nested_map(self, input, path, expected):
        '''Test access_nested_map function'''
        self.assertEqual(access_nested_map(input, path), expected)

    @parameterized.expand(
        [
            ({}, ["a"], KeyError),
            ({"a": 1}, ["a", "b"], KeyError),
            ({"a": 1}, ["b"], KeyError)
        ]
    )
    def test_access_nested_map_exception(self, input, path, expected):
        '''Test access_nested_map function raises exception'''
        with self.assertRaises(expected):
            access_nested_map(input, path)
