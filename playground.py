#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning Python

import aiohttp
import asyncio


async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Response: {response.status}')
            return response.status


pool = asyncio.get_event_loop()
pool.run_until_complete(fetch_page('http://www.goyoom.com'))
