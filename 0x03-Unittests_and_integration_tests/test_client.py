#!/usr/bin/env python3
'''Module containing unittests for client module'''

import unittest
from unittest.mock import patch, Mock, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    '''TestGithubOrgClient class'''

    @parameterized.expand(
        [
            ("google", {'login': 'google'}),
            ("abc", {'login': 'abc'}),
        ]
    )
    @patch('client.get_json')
    def test_org(self, org, expected_response, mock_get_json):
        '''Test org method'''
        mock_get_json.return_value = MagicMock(return_value=expected_response)
        self.assertEqual(GithubOrgClient(org).org(), expected_response)
        mock_get_json.assert_called_once()
