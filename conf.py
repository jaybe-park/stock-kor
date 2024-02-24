import json


def get_key(name: str):
    keys = json.loads(open('./conf.json').read())['key']
    if name in keys.keys():
        return keys[name]
    else:
        return None


def get_url(name: str):
    urls = json.loads(open('./conf.json').read())['url']
    if name in urls.keys():
        return urls[name]
    else:
        return None
