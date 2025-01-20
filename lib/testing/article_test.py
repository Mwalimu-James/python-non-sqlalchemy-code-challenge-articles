import pytest
from classes.many_to_many import Article, Magazine, Author


class TestArticle:
    """Article in many_to_many.py"""

    def test_has_title(self):
        """Article is initialized with a title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert article_1.title == "How to wear a tutu with style"
        assert article_2.title == "Dating life in NYC"

    def test_title_is_valid(self):
        """title is between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")

        with pytest.raises(Exception):
            Article(author, magazine, "Test")  

        with pytest.raises(Exception):
            Article(author, magazine, "How to wear a tutu with style and walk confidently down the street") 

    def test_title_is_immutable(self):
        """title is immutable"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")

        with pytest.raises(AttributeError):
            article.title = "New Title"

    def test_has_author(self):
        """article has an author"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")

        assert article.author == author

    def test_has_magazine(self):
        """article has a magazine"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")

        assert article.magazine == magazine
