#!/usr/bin/env python3
"""Test the GithubOrgClient class."""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True}),
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """Test that GithubOrgClient.org returns the correct value."""
        # Set the mocked return value for get_json
        get_patch.return_value = expected
        client_instance = GithubOrgClient(org)
        
        # Assert that org property returns the expected value
        self.assertEqual(client_instance.org, expected)
        
        # Verify that get_json was called with the correct URL
        get_patch.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct repos_url."""
        # Define the expected URL and payload with repos_url
        expected_url = "https://api.github.com/orgs/test_org/repos"
        payload = {"repos_url": expected_url}

        # Patch the org property using PropertyMock to return the payload
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock, return_value=payload):
            client_instance = GithubOrgClient("test_org")
            # Assert that _public_repos_url returns the correct repos_url
            self.assertEqual(client_instance._public_repos_url, expected_url)


if __name__ == "__main__":
    unittest.main()
