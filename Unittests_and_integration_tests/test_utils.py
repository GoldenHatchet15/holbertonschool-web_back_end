#!/usr/bin/env python3
"""Test the access_nested_map function."""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns expected results."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),  # Test empty dict with non-existing key "a"
        ({"a": 1}, ("a", "b")),  # Test with key "a" but missing key "b"
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises a KeyError for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Ensure that the missing key is in the exception message
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Test the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected payload."""
        # Create a mock response object with the json method returning test_payload
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function with the test_url
        result = get_json(test_url)

        # Assert that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the result is equal to the test_payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
