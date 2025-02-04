#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """review test class"""

    def __init__(self, *args, **kwargs):
        """review class init"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """testing review place_id attribute"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """testing review user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """testing review text attribute"""
        new = self.value()
        self.assertEqual(type(new.text), str)
