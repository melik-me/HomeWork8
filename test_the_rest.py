import requests

def test_create_book(base_url, book_dict):
    response = requests.post(base_url + "books/", data=book_dict)
    assert response.status_code == 201
    resp_dict = response.json()
    for key in book_dict:
        assert book_dict[key] == resp_dict[key]
    book_dict["id"] = resp_dict["id"]

def test_create_book_again(base_url, book_dict):
    response = requests.post(base_url + "books/", data=book_dict)
    response = requests.post(base_url + "books/", data=book_dict)
    assert response.status_code == 201
    resp_dict = response.json()
    for key in book_dict:
        assert book_dict[key] == resp_dict[key]
    book_dict["id"] = resp_dict["id"]
    id = str(int(book_dict["id"]) - 1)
    requests.delete(base_url + "books/" + "{}".format(id))

def test_create_book_no_author(base_url):
    dict = {
        "title": "Ender’s Game",
        "author": ""
    }
    response = requests.post(base_url + "books/", data=dict)
    assert response.status_code == 400

def test_create_book_no_title(base_url):
    dict = {
        "title": "",
        "author": "Orson Scott Card"
    }
    response = requests.post(base_url + "books/", data=dict)
    assert response.status_code == 400

def test_create_book_no_data(base_url):
    dict = {
        "title": "",
        "author": ""
    }
    response = requests.post(base_url + "books/", data=dict)
    assert response.status_code == 400

def test_create_book_empty_dict(base_url):
    dict = {}
    response = requests.post(base_url + "books/", data=dict)
    assert response.status_code == 400

def test_create_book_wrong_url(book_dict):
    url = "http://pulse-rest-testing.herokuapp.com/boooks/"
    response = requests.post(url, data=book_dict)
    assert response.status_code == 404


def test_read_book(base_url, book_dict):
    response = requests.post(base_url + "books/", data=book_dict)
    resp_dict = response.json()
    response = requests.get(base_url + "books/" + str(resp_dict["id"]))
    assert response.status_code == 200
    resp_dict = response.json()
    for key in book_dict:
        assert book_dict[key] == resp_dict[key]
    book_dict["id"] = resp_dict["id"]

def test_read_book_wrong_id(base_url):
    response = requests.get(base_url + "books/" + "99999")
    assert response.status_code == 404

def test_read_book_wrong_url(base_url, book_dict):
    url = "http://pulse-rest-testing.herokuapp.com/boooks/"
    response = requests.post(base_url + "books/", data=book_dict)
    resp_dict = response.json()
    book_dict["id"] = resp_dict["id"]
    response = requests.get(url + str(book_dict["id"]))
    assert response.status_code == 404

def test_update_book(base_url, book_dict):
    response = requests.post(base_url + "books/", data=book_dict)
    resp_dict = response.json()
    book_dict["id"] = resp_dict["id"]
    response = requests.put(base_url + "books/" + str(book_dict["id"]), data={"title": "Speaker for the Dead"})
    book_dict["title"] = "Speaker for the Dead"
    assert response.status_code == 200
    resp_dict = response.json()
    assert book_dict["title"] == resp_dict["title"]

def test_update_book_wrong_url(base_url, book_dict):
    url = "http://pulse-rest-testing.herokuapp.com/boooks/"
    response = requests.post(base_url + "books/", data=book_dict)
    resp_dict = response.json()
    book_dict["id"] = resp_dict["id"]
    response = requests.put(url + str(book_dict["id"]), data={"title": "Speaker for the Dead"})
    assert response.status_code == 404

def test_update_book_wrong_id(base_url, book_dict):
    response = requests.post(base_url + "books/", data=book_dict)
    resp_dict = response.json()
    book_dict["id"] = resp_dict["id"]
    response = requests.put(base_url + "books/" + "99999", data={"title": "Speaker for the Dead"})
    assert response.status_code == 404

def test_update_book_wrong_data(base_url, book_dict):
    response = requests.post(base_url + "books/", data=book_dict)
    resp_dict = response.json()
    book_dict["id"] = resp_dict["id"]
    response = requests.put(base_url + "books/" + str(book_dict["id"]), data={"year": "1986"})
    assert response.status_code == 200

def test_update_book_empty_dict(base_url, book_dict):
    dict = {}
    response = requests.post(base_url + "books/", data=book_dict)
    resp_dict = response.json()
    book_dict["id"] = resp_dict["id"]
    response = requests.put(base_url + "books/" + str(book_dict["id"]), data=dict)
    assert response.status_code == 200

def test_delete_book(base_url, book_dict):
    response = requests.post(base_url, data=book_dict)
    resp_dict = response.json()
    book_dict["id"] = resp_dict["id"]
    response = requests.delete(base_url + "books/" + str(book_dict["id"]))
    assert response.status_code == 204
    response = requests.get(base_url + "books/")
    book_list = response.json()
    for book in book_list:
        assert book != book_dict

def test_create_role(base_url, role_dict):
    response = requests.post(base_url + "roles/", data=role_dict)
    assert response.status_code == 201
    resp_dict = response.json()
    role_dict["id"] = resp_dict["id"]
    assert role_dict == resp_dict

def test_create_role_again(base_url, role_dict):
    response = requests.post(base_url + "roles/", data=role_dict)
    response = requests.post(base_url + "roles/", data=role_dict)
    assert response.status_code == 201
    resp_dict = response.json()
    for key in role_dict:
        assert role_dict[key] == resp_dict[key]
    role_dict["id"] = resp_dict["id"]
    id = str(int(role_dict["id"]) - 1)
    requests.delete(base_url + "roles/" + "{}".format(id))


def test_create_role_no_name(base_url):
    dict = {
        "name": "",
        "type": "The Gunslinger",
        "level": 80,
        "book": 422
    }
    response = requests.post(base_url + "roles/", data=dict)
    assert response.status_code == 400

def test_create_role_no_type(base_url):
    dict = {
        "name": "Roland Deschain",
        "type": "",
        "level": 80,
        "book": 422
    }
    response = requests.post(base_url + "roles/", data=dict)
    assert response.status_code == 400

def test_create_role_no_data(base_url):
    dict = {
        "name": "",
        "type": "",
        "level": "",
        "book": ""
    }
    response = requests.post(base_url + "roles/", data=dict)
    assert response.status_code == 400

def test_create_role_empty_dict(base_url):
    dict = {}
    response = requests.post(base_url + "roles/", data=dict)
    assert response.status_code == 400

def test_create_role_wrong_url(role_dict):
    url = "http://pulse-rest-testing.herokuapp.com/roooles/"
    response = requests.post(url, data=role_dict)
    assert response.status_code == 404

def test_read_role(base_url, role_dict):
    response = requests.post(base_url + "roles/", data=role_dict)
    resp_dict = response.json()
    role_dict["id"] = resp_dict["id"]
    response = requests.get(base_url + "roles/" + str(resp_dict["id"]))
    assert response.status_code == 200
    resp_dict = response.json()
    assert role_dict == resp_dict

def test_read_role_wrong_id(base_url):

    response = requests.get(base_url + "roles/" + "99999")
    assert response.status_code == 404

def test_read_role_wrong_url(base_url, role_dict):
    url = "http://pulse-rest-testing.herokuapp.com/roooles/"
    response = requests.post(base_url + "roles/", data=role_dict)
    resp_dict = response.json()
    role_dict["id"] = resp_dict["id"]
    response = requests.get(url + str(role_dict["id"]))
    assert response.status_code == 404

def test_update_role(base_url, role_dict):
    response = requests.post(base_url + "roles/", data=role_dict)
    resp_dict = response.json()
    role_dict["id"] = resp_dict["id"]
    response = requests.put(base_url + "roles/" + str(role_dict["id"]), data={"level": 88})
    role_dict["level"] = 88
    assert response.status_code == 200
    resp_dict = response.json()
    assert role_dict["level"] == resp_dict["level"]

def test_update_role_wrong_url(base_url, role_dict):
    url = "http://pulse-rest-testing.herokuapp.com/roooles/"
    response = requests.post(base_url + "roles/", data=role_dict)
    resp_dict = response.json()
    role_dict["id"] = resp_dict["id"]
    response = requests.put(url + str(role_dict["id"]), data={"level": 88})
    assert response.status_code == 404

def test_update_role_wrong_id(base_url, role_dict):
    response = requests.post(base_url + "roles/", data=role_dict)
    resp_dict = response.json()
    role_dict["id"] = resp_dict["id"]
    response = requests.put(base_url + "roles/" + "99999", data={"level": 88})
    assert response.status_code == 404

def test_update_role_wrong_data(base_url, role_dict):
    response = requests.post(base_url + "roles/", data=role_dict)
    resp_dict = response.json()
    role_dict["id"] = resp_dict["id"]
    response = requests.put(base_url + "roles/" + str(role_dict["id"]), data={"year": "1986"})
    assert response.status_code == 200

def test_update_role_empty_dict(base_url, role_dict):
    dict = {}
    response = requests.post(base_url + "roles/", data=role_dict)
    resp_dict = response.json()
    role_dict["id"] = resp_dict["id"]
    response = requests.put(base_url + "roles/" + str(role_dict["id"]), data=dict)
    assert response.status_code == 200

def test_delete_role(base_url, role_dict):
    response = requests.post(base_url + "roles/", data=role_dict)
    resp_dict = response.json()
    role_dict["id"] = resp_dict["id"]
    response = requests.delete(base_url + "roles/" + str(role_dict["id"]))
    assert response.status_code == 204
    response = requests.get(base_url + "roles/")
    role_list = response.json()
    for role in role_list:
        assert role != role_dict