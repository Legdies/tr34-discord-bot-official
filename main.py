import asyncio
import json
import logging
#import config
#import discord
from discord.ext import commands

from discord.commands import slash_command
from discord.ext.pages import Paginator, Page
import lib.R34newSDK as R34newSDK
from lib.R34newSDK.models import FilePath, Post
import discord
import logging
import datetime
from discord.ui import Button

bot = discord.Bot()
import config
from lib.R34newSDK import ApiClient
api = ApiClient()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command()
async def findpost(ctx, tags):
    posts = await api.ListPosts(tags=[tags], limit=5, page=0)

    try:
        if not posts:
            await ctx.respond("Постов с такими тегами не найдено.", ephemeral=True)
            return
    except Exception as e:
        await ctx.respond("API не доступен", ephemeral=True)
        return






    pages = []

    # Create 5 pages
    for i in range(5):
        page = Page(embeds=[])
        pages.append(page)

    # Add posts to pages
    try:
        for i, post in enumerate(posts['posts']):
            post=json.loads(post)
            embed = discord.Embed(title=f"Page {i + 1}",
                                  description=f"If post cant be loaded\n {post['url']}",
                                  color=discord.Color.random())
            postTags = post['tags']
            limit = postTags[:5]
            embed.add_field(name="tags: ", value=f"{' '.join(tuple(limit))}", inline=True)
            embed.add_field(name="\nRating: ", value=f"{post['rating']}", inline=True)
            embed.set_image(url=f"{post['file']['preview_url']}")
            pages[i].embeds.append(embed)

        paginator = Paginator(pages=pages)
        await paginator.respond(ctx.interaction)
    except Exception as e:
        print(post)
        print(e)



if __name__ == "__main__":
    bot.run(config.TOKEN)



