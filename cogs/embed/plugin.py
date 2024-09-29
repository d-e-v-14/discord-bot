from discord import Embed as DiscordEmbed  
from discord.ext import commands
from cogs import Plugin
from core import Bot
from discord.ext.commands import Context


class EmbedCommand(Plugin): 
    @commands.command(name="embed", description="Create Embed")
    async def embed(self, ctx: Context, title: str, description: str) -> None:
        e: DiscordEmbed = DiscordEmbed(title=title, description=description) 
        e.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=e)


async def setup(bot: Bot) -> None:
    await bot.add_cog(EmbedCommand(bot))
