import logging
import config
import discord
from discord.ext import commands
from searcher import Searcher
bot = discord.Bot()
logger = logging.getLogger("bot")
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
##TODO Сделать навигацию и эмбеды


@bot.slash_command()
async def findpost(ctx, post_id:int):

    try:
        searcher = Searcher({"post_id": post_id})
        data, main_file_url, tags = searcher.getPost()
        embed = discord.Embed(title="yay", color=discord.Color.random())
        tagstupled = " ".join(tags)
        embed.add_field(name="Tags: ", value=f"```{tagstupled}```", inline=True)
        embed.set_image(url=f"{main_file_url}")
        await ctx.respond(embed=embed)
        logging.info(f"{ctx.author} searched post {post_id}")
        #await ctx.send("xx", view=MyView())
    except Exception as e:
        await ctx.send("Error happened")
        logging.info(e)






##TODO Перепривязать SDK
bot.run(config.TOKEN)