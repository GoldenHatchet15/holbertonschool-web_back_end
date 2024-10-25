#!/usr/bin/env python3
"""Test the GithubOrgClient class."""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Instantiate the GithubOrgClient with the given org_name
        client = GithubOrgClient(org_name)

        # Call the org method, which should call get_json
        client.org()

        # The expected URL that should be passed to get_json
        expected_url = f"https://api.github.com/orgs/{org_name}"

        # Assert get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """Test the _public_repos_url property."""
        # Define the repos_url in a mock response
        mock_org_data = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"}

        # Patch the org property to return mock_org_data directly
        with patch.object(GithubOrgClient, 'org', return_value=mock_org_data):
            # Instantiate the client
            client = GithubOrgClient("test_org")

            # Access _public_repos_url and check the result
            result = client._public_repos_url
            expected_url = "https://api.github.com/orgs/test_org/repos"
            self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()
