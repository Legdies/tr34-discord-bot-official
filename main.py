import asyncio
import logging
import config
import discord
from discord.ext import commands

from discord.commands import slash_command
from discord.ext.pages import Paginator, Page
from tr34_sdk import TR34Api
import discord
import logging
import datetime
from discord.ui import Button
api = TR34Api()
bot = discord.Bot()



@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command()
async def findpost(ctx, tags):
    posts = await api.search_posts(tags=[tags], limit=5, page=0)

    if not posts:
        await ctx.respond("Постов с такими тегами не найдено.", ephemeral=True)
        return

    pages = []

    # Create 5 pages
    for i in range(5):
        page = Page(embeds=[])
        pages.append(page)

    # Add posts to pages
    for i, post in enumerate(posts):
        embed = discord.Embed(title=f"Page {i + 1}", description=f"If post cant be loaded\n {post.main.file}", color=discord.Color.random())
        embed.add_field(name="tags: ",value=f"{' '.join(tuple(post.tags))}")
        embed.set_image(url=f"{post.main.file}")
        pages[i].embeds.append(embed)

    # Handle empty pages
    if len(posts) < 5:
        for i in range(len(posts), 5):
            pages[i].embeds.append(discord.Embed(title=f"Page {i + 1}", description="No posts found."))

    paginator = Paginator(pages=pages)
    await paginator.respond(ctx.interaction)




bot.run(config.TOKEN)

