import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from games.models import Game

class GameTestCase(TestCase):
    def test_true_is_true(self):
            """ Tests if True is equal to True. Should always pass. """
            self.assertEqual(True, True)

    def test_game_slugify_on_save(self):
            """ Tests the slug generated when saving a Game. """
            # Author is a required field in our model.
            # Create a user for this test and save it to the test database.
            user = User()
            user.save()

            # Create and save a new page to the test database.
            game = Game(name="My Test Game", description="test")
            game.save()
