import requests


def send_request(count):
    resp = requests.get("https://jservice.io/api/random", params={"count": count})

    return resp.json()
