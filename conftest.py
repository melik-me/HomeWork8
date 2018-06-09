import pytest
import requests

@pytest.fixture
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/"

@pytest.fixture
def book_dict(base_url):
     book_dict = {"title": "Ender’s Game", "author": "Orson Scott Card"}
     yield book_dict
     if "id" in book_dict:
         requests.delete(base_url + "books/" + str(book_dict["id"]))

@pytest.fixture
def role_dict(base_url):
    role_dict = {"name": "Roland Deschain", "type": "The Gunslinger", "level": 80, "book": 422}
    yield role_dict
    if "id" in role_dict:
        requests.delete(base_url + "roles/" + str(role_dict["id"]))
