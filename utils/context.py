from typing import Any, Optional, Coroutine
from discord.ext.commands import Context as OldContext
from discord import Embed


class Context(OldContext):
    async def reply(
        self,
        content: Optional[str] = None,
        *args: Any,
        embed: Optional[Embed] = None,
        create_embed: Optional[bool] = False,
        **kwargs: Any,
    ) -> Coroutine:
        if content.count(":") > 1:
            return await super().reply(content.replace(":", ""))
        return await super().reply("Haha Nice Try")
