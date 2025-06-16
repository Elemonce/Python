import pytest
from book import Book

# test_valid_creation that create books with valid title and isbn.
# test_creation_with_invalid_title that create books with an invalid title.
# test_creation_with_invalid_isbn that create books with an invalid isbn.

@pytest.mark.parametrize("title", [
    "1984",
    "The Hunger Games",
    "To Kill a Mockingbird"])

@pytest.mark.parametrize("isbn", [
    "9780439023481",
    "9789510459959",
    "9780060888695"
])
def test_valid_creation(title, isbn):
    Book(title, isbn)


def test_creating_with_invalid_title():
    with pytest.raises(RuntimeError):
        Book("", "9780060888695")

@pytest.mark.parametrize("isbn", [
    "97804390423481",
    "9789510454992359",
    "97800608884695"
])
def test_creation_with_invalid_isbn(isbn):
    with pytest.raises(RuntimeError):
        Book("1984", isbn)

