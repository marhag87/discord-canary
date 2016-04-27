#!/bin/env python
"""Script that downloads the latest source for discord-canary"""

import json
import requests as req

def latest_version():
    """Find out which the latest version is"""

    resp = req.get('https://discordapp.com/api/updates/canary?platform=linux')
    return json.loads(resp.text).get('name')

def download_latest():
    """Download the latest version"""

    version = latest_version()
    with open("discord-canary-%s.tar.gz" % version, 'wb') as handle:
        resp = req.get('https://discordapp.com/api/download/canary?platform=linux&format=tar.gz',
                       stream=True)

        if resp.ok:
            for block in resp.iter_content(1024):
                handle.write(block)
            print("Downloaded discord-canary-%s.tar.gz" % version)

if __name__ == '__main__':
    download_latest()
