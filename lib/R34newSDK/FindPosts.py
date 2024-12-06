"""
API.ListPosts
~~~~~~~~~~~~~~

Find post by tags, accept page number and number of posts on one request.

"""


import asyncio
import json

import aiohttp
from . import APIurl
from .models import FilePath, Post

class ApiClient:
    def __init__(self):
        pass

    async def FindPosts(self,
                        page: int = 1,
                        limit: int =1,
                        tags: list[str] = None, ):
        '''
        Base function to Find Posts.
        :param page: to split number of posts to a multiple pages
        :param limit: limit the number of posts on a single page.
        :param tags: Used to find posts using tags.
        :return: json.object
        '''

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