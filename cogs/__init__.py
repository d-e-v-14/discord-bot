from logging import getLogger

from discord.ext.commands import Cog

from core import Bot

__all__ = ("Plugin",)

log = getLogger(__name__)


class Plugin(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        super().__init__()

    async def cog_load(self) -> None:
        log.info(f"Loaded {self.qualified_name} cog")

    async def cog_unload(self) -> None:
        log.info(f"Unloaded {self.qualified_name} cog")
