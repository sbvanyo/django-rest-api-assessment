import unittest
import pytest
from rest_framework.test import APITestCase
from faker import Faker
from rest_framework import status
from tunaapi.models import Artist

class TestArtists(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker()
        cls.artist_1 = Artist.objects.create(
            name=cls.faker.name(),
            age=cls.faker.pyint(min_value=18, max_value=100),
            bio=cls.faker.sentence()
        )

    def setUp(self):
        self.artist_1.refresh_from_db()


    def test_create(self):
        # new_artist = {
        #     "name": self.faker.name(),
        #     "age": self.faker.pyint(min_value=18, max_value=100),
        #     "bio": self.faker.sentence(nb_words=3)
        # }
        # response = self.client.post("/artists", new_artist)

        print(Artist.objects.all(), "******************")
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # data = response.data
        # self.assertTrue("id" in data)
        # self.assertEqual(data.name, new_artist.name)
        # self.assertEqual(data.age, new_artist.age)
        # self.assertEqual(data.bio, new_artist.bio)


    # def test_delete(self):
    #     response = self.client.get("")

    # def test_update(self):
    #     response = self.client.get("")

    # def test_list(self):
    #     response = self.client.get("")

    # def test_details(self):
    #     response = self.client.get("")

    # def test_stretch_filter_by_genre(self):
    #     response = self.client.get("")

    # def test_stretch_filter_artists_with_related_genres(self):
    #     response = self.client.get("")