#!/usr/bin/env python3
'''Module containing unittests for client module'''
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''Test access_nested_map function'''
    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a", "b"], 2),
            ({"a": {"b": 2}}, ["a"], {"b": 2})
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


class TestGetJson(unittest.TestCase):
    "Class to test get_json method"

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(self, url, expected_payload):
        """Test get_json method for success"""
        mock_requests = Mock()
        mock_requests.return_value.json.return_value = expected_payload

        with patch('requests.get', mock_requests):
            self.assertEqual(get_json(url), expected_payload)
            mock_requests.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    '''Test memoize function'''
    def test_memoize(self):
        '''Test memoize function'''
        class TestClass:
            '''Test class'''
            def a_method(self):
                '''Method to test'''
                return 42

            @memoize
            def a_property(self):
                '''Property to test'''
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock_method.assert_called_once()
