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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method."""
        # Define the payload and expected repos list
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        expected_repos = ["repo1", "repo2", "repo3"]

        # Mock get_json to return the payload
        mock_get_json.return_value = payload

        # Mock _public_repos_url to return a dummy URL
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
            client_instance = GithubOrgClient("test_org")
            result = client_instance.public_repos()

            # Assert that the result matches expected repo names
            self.assertEqual(result, expected_repos)

            # Verify both mocks were called exactly once
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
