import sys
sys.path.append('..')

import pytest
import sys
import main

@pytest.fixture
def app():
    app = main.create_instance()
    app.debug = True
    return app.test_client()

# unit test 1
def test_hello_world(app):
    res = app.get("/")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"Greetings Sauce Labs! Greetings from Raj!" in res.data