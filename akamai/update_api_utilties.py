import ConfigParser
import yaml
import os
import json
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urlparse import urljoin


# Utility functions
def getYMLFromFile(path="../main.yml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def getJSONFromFile(path):
    with open(path, "r") as f:
        return json.load(f)

def getEdgeGridAuthFromConfig(path="~/.edgerc"):
    config = ConfigParser.RawConfigParser()
    config.read(os.path.expanduser(path))
    return EdgeGridAuth(
        client_token=config.get("default", "client_token"),
        client_secret=config.get("default", "client_secret"),
        access_token=config.get("default", "access_token")
    )

def getHostFromConfig(path="~/.edgerc"):
    config = ConfigParser.RawConfigParser()
    config.read(os.path.expanduser(path))
    return config.get("default", "host")


#HTTP Helper Functions 
def akamaiGet(url, baseurl, s):
    return s.get(urljoin(baseurl, url)).content

def akamaiPost(url, baseurl, body, s):
    return s.post(urljoin(baseurl, url), json=body).content

def akamaiPut(url, baseurl, body, s):
    return s.put(urljoin(baseurl, url), json=body).content


