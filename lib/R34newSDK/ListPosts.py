"""
API.ListPosts
~~~~~~~~~~~~~~

List posts from first page

Accept page number and number of posts to display

"""


import asyncio
import json

import aiohttp
from . import APIurl
from .models import FilePath, Post

class ApiClient:
    def __init__(self):
        pass

    async def ListPosts(self,
                        page: int,
                        limit: int,
                        tags: list[str], ):

        endpoint = APIurl + f"post/search?page={page}&limit={limit}&tags={','.join(tags)}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(endpoint) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        raise Exception(f"Error {response.status}: {await response.text()}")
            except aiohttp.client_exceptions.ClientConnectorError:
                return "Failed to connect to API. Please check the URL or your network connection."
            except aiohttp.ClientError as e:
                return f"HTTP error occurred: {e}"

#Currently in work!