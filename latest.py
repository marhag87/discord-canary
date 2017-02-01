#!/bin/env python
"""Script that downloads the latest source for discord"""

import argparse
import sys
import json
import requests as req

def latest_version(canary=False):
    """Find out which the latest version is"""

    if canary is True:
        url = 'https://discordapp.com/api/updates/canary?platform=linux'
    else:
        url = 'https://discordapp.com/api/updates?platform=linux'
    resp = req.get(url)
    return json.loads(resp.text).get('name')

def download_latest(canary=False):
    """Download the latest version"""

    version = latest_version(canary=canary)

    if canary is True:
        url = 'https://discordapp.com/api/download/canary?platform=linux&format=tar.gz'
        name = 'discord-canary-{}.tar.gz'.format(version)
    else:
        url = 'https://discordapp.com/api/download?platform=linux&format=tar.gz'
        name = 'discord-{}.tar.gz'.format(version)

    with open(name, 'wb') as handle:
        resp = req.get(
            url,
            stream=True,
        )

        if resp.ok:
            for block in resp.iter_content(1024):
                handle.write(block)
            print('Downloaded {}'.format(name))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            'Download or check latest version of discord'
        )
    )
    parser.add_argument(
        '-d',
        action='store_true',
        help='download',
    )
    parser.add_argument(
        '-c',
        action='store_true',
        help='canary',
    )

    args = parser.parse_args()
    if args.d is True:
        download_latest(canary=args.c)
    else:
        print(latest_version(canary=args.c))
