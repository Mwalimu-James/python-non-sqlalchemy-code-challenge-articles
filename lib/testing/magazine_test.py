import pytest
from classes.many_to_many import Article, Magazine, Author


class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_name_is_valid(self):
        """magazine name is a string between 2 and 16 characters"""
        with pytest.raises(Exception):
            Magazine("A", "Fashion")  
        with pytest.raises(Exception):
            Magazine("This is Way Too Long", "Fashion")  
        with pytest.raises(Exception):
            Magazine(123, "Fashion")  

    def test_name_is_mutable(self):
        """magazine name is mutable and validated"""
        magazine = Magazine("Vogue", "Fashion")
        magazine.name = "New Yorker"
        assert magazine.name == "New Yorker"

        with pytest.raises(Exception):
            magazine.name = 2  
        with pytest.raises(Exception):
            magazine.name = "This Name is Way Too Long to Be Valid"

    def test_category_is_valid(self):
        """magazine category is a non-empty string"""
        with pytest.raises(Exception):
            Magazine("Vogue", "")  
        with pytest.raises(Exception):
            Magazine("Vogue", 123)  
    def test_category_is_mutable(self):
        """magazine category is mutable and validated"""
        magazine = Magazine("Vogue", "Fashion")
        magazine.category = "Lifestyle"
        assert magazine.category == "Lifestyle"

        with pytest.raises(Exception):
            magazine.category = ""  
        with pytest.raises(Exception):
            magazine.category = 123  
    def test_article_titles(self):
        """returns list of titles for all articles in magazine"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "Fashion Tips")
        Article(author, magazine, "Style Guide")

        assert magazine.article_titles() == ["Fashion Tips", "Style Guide"]

    def test_contributing_authors(self):
        """returns authors who have written more than 2 articles for magazine"""
        author1 = Author("Carry Bradshaw")
        author2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author1, magazine, "Fashion Tips")
        Article(author1, magazine, "Style Guide")
        Article(author1, magazine, "Men's Fashion")
        Article(author2, magazine, "Architecture Trends")

        assert author1 in magazine.contributing_authors()
        assert author2 not in magazine.contributing_authors()
