import unittest
import pytest

from rest_framework.test import APIRequestFactory

@pytest.mark.skip()
class TestSongs(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = APIRequestFactory()

    def test_create(self):
        response = self.client.get("")
    def test_delete(self):
        response = self.client.get("")
    def test_update(self):
        response = self.client.get("")
    def test_list(self):
        response = self.client.get("")
    def test_details(self):
        response = self.client.get("")

    # def test_stretch_filter_by_genre(self):
    #     response = self.client.get("")