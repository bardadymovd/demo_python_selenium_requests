import requests


base_url = "https://reqres.in"


def test_01_get():
    """test get method - read purpose as part of CRUD testing"""

    r = requests.get(base_url + "/api/users/2")
    assert r.status_code == 200

    content = r.json()["data"]
    assert content["id"] == 2
    assert content["email"] == "janet.weaver@reqres.in"
    assert content["first_name"] == "Janet"
    assert content["last_name"] == "Weaver"


def test_02_post():
    """test post method - create purpose as part of CRUD testing"""

    body = {"name": "morpheus", "job": "leader"}
    r = requests.post(base_url + "/api/users", body)
    assert r.status_code == 201

    content = r.json()
    assert content["name"] == "morpheus"
    assert content["job"] == "leader"


def test_03_put():
    """test put method - update purpose as part of CRUD testing"""

    body = {"name": "morpheus", "job": "zion resident"}
    r = requests.put(base_url + "/api/users/2", body)
    assert r.status_code == 200

    content = r.json()
    assert content["name"] == "morpheus"
    assert content["job"] == "zion resident"


def test_04_delete():
    """test delete method - delete purpose as part of CRUD testing"""

    r = requests.delete(base_url + "/api/users/2")
    assert r.status_code == 204


def test_05_registration_and_login():
    """test registration and successful login flow"""

    body = {"email": "eve.holt@reqres.in", "password": "pistol"}
    r = requests.post(base_url + "/api/register", body)
    assert r.status_code == 200
    assert "token" in r.json().keys()

    body = {"email": "eve.holt@reqres.in", "password": "pistol"}
    r = requests.post(base_url + "/api/login", body)
    assert r.status_code == 200
    assert "token" in r.json().keys()


def test_06_registration_and_failed_login():
    """test registration and unsuccessful login flow"""

    body = {"email": "eve.holt@reqres.in", "password": "pistol"}
    r = requests.post(base_url + "/api/register", body)
    assert r.status_code == 200
    assert "token" in r.json().keys()

    body = {"email": "eve.holt@reqres.in"}
    r = requests.post(base_url + "/api/login", body)
    assert r.status_code == 400
