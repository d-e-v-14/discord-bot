from discord import Embed

class Pagination:
    def __init__(self, embeds: list[Embed]) -> None:
        self.embeds = embeds
        self.curr = 0

    def __getitem__(self, i: int) -> Embed:
        return self.embeds[i]

    def __len__(self) -> int:
        return len(self.embeds)

    def next_page(self) -> Embed:
        if len(self) > self.curr:
            self.curr += 1

    def prev_page(self) -> Embed:
        if self.curr >= 0:
            self.curr -= 1

    def first_page(self) -> Embed:
        self.curr = 0

    def last_page(self) -> Embed:
        self.curr = len(self) - 1
