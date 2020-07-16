"""Test Foo Module."""
import json

from django.urls import reverse


def test_hello_world():
    """
    Hello world test.

    Test for hello world
    :return:
    """
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"


def test_ping(client):
    """
    Test ping.

    test function for ping
    :param client:
    :return:
    """
    url = reverse("ping")
    response = client.get(url)
    content = json.loads(response.content)

    assert response.status_code == 200
    assert content["ping"] == "pong"
