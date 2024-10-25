#!/usr/bin/env python3
"""Test the GithubOrgClient class."""

import unittest
from unittest.mock import patch, PropertyMock, Mock, call
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True}),
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """Test that GithubOrgClient.org returns the correct value."""
        get_patch.return_value = expected
        client_instance = GithubOrgClient(org)
        self.assertEqual(client_instance.org, expected)
        get_patch.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct repos_url."""
        expected_url = "https://api.github.com/orgs/test_org/repos"
        payload = {"repos_url": expected_url}
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
                return_value=payload):
            client_instance = GithubOrgClient("test_org")
            self.assertEqual(client_instance._public_repos_url, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method."""
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        expected_repos = ["repo1", "repo2", "repo3"]
        mock_get_json.return_value = payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = (
                "https://api.github.com/orgs/test_org/repos"
            )
            client_instance = GithubOrgClient("test_org")
            result = client_instance.public_repos()
            self.assertEqual(result, expected_repos)
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license returns
        the correct boolean based on
        license_key.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos method."""

    @classmethod
    def setUpClass(cls):
        """Set up a patch for requests.get before all tests."""
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        # Create a mapping of URL to the appropriate mock response
        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda url: options.get(url, org_mock)

    @classmethod
    def tearDownClass(cls):
        """Stop the requests.get patch after all tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos
        to verify the correct repositories
        are returned.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test GithubOrgClient.public_repos
        with the Apache 2.0 license filter.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
