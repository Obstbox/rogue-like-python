import numpy as np
from tcod.console import Console

# import rogue.tile_types
import rogue


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
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
