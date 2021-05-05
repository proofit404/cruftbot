"""Tests related to index page."""
from django.test import TestCase


class IndexViewTestCase(TestCase):
    """Index page test cases."""

    def test_index_view(self):
        """Open index page."""
        response = self.client.get("/")
        assert response.status_code == 200
