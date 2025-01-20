import pytest
from classes.many_to_many import Article, Magazine, Author


class TestAuthor:
    """Author in many_to_many.py"""

    def test_name_is_valid(self):
        """author name is a non-empty string"""
        with pytest.raises(Exception):
            Author("")  
        with pytest.raises(Exception):
            Author(123)  

    def test_name_is_immutable(self):
        """author name is immutable"""
        author = Author("Carry Bradshaw")
        with pytest.raises(AttributeError):
            author.name = "New Name"

    def test_add_article(self):
        """creates and returns a new article given a magazine and title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = author.add_article(magazine, "How to wear a tutu with style")

        assert article.author == author
        assert article.magazine == magazine

    def test_topic_areas(self):
        """returns unique categories for all magazines by author"""
        author = Author("Carry Bradshaw")
        magazine1 = Magazine("Vogue", "Fashion")
        magazine2 = Magazine("GQ", "Lifestyle")
        author.add_article(magazine1, "Fashion Tips")
        author.add_article(magazine2, "Men's Style")

        assert set(author.topic_areas()) == {"Fashion", "Lifestyle"}
