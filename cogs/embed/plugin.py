from discord import Embed
from discord.ext import commands
from cogs import Plugin
from core import Bot
from discord.ext.commands import Context


class Embed(Plugin):
    @commands.command(name="embed", description="Create Embed")
    async def embed(self, ctx: Context, title: str, description: str) -> None:
        e: Embed = Embed()
        e.add_field(name=title, value=description)
        e.set_footer(f"Requested by {ctx.author}")
        await ctx.send(embed=e)


async def setup(bot: Bot) -> None:
    await bot.add_cog(Embed(bot))
