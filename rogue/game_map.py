from __future__ import annotations
from typing import Iterable, TYPE_CHECKING


import numpy as np
from tcod.console import Console

import rogue.tile_types
if TYPE_CHECKING:
    from entity import Entity


class GameMap:
    def __init__(self, width: int, height: int, entities: Iterable[Entity] = ()):
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=rogue.tile_types.wall, order="F")

        # visible now
        self.visible = np.full((width, height), fill_value=False, order="F")
        # seen before
        self.explored = np.full((width, height), fill_value=False, order="F")

    def in_bounds(self, x: int, y: int) -> bool:
        """ return true if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.
        light for visible tiles
        dark for explored but not visible
        SHROUD for rest
        """
        console.rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=rogue.tile_types.SHROUD
        )

        for entity in self.entities:
            # only print entities that are in the FOV
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)
