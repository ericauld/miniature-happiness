#!/usr/bin/env python3

import requests
import sys
import os

download_num = sys.argv[1]
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3' }
url = f'https://www.gutenberg.org/cache/epub/{download_num}/pg{download_num}.txt'
response = requests.get(url, headers)
try:
    print(response.text)
except BrokenPipeError:
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(1)

