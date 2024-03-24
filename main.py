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
async def findpost(ctx, arg):
    post = await api.get_post(arg)
    embed = discord.Embed(title=f"Post {arg}")
    pages = [

        Page(embeds=[embed.set_image(url=f"{post.main.file}"),
                     embed.add_field(name="tags: ", value=f"```{' '.join(tuple(post.tags))}```")])

    ]
    pagginator = Paginator(pages=pages)
    await pagginator.respond(ctx.interaction)



bot.run(config.TOKEN)

