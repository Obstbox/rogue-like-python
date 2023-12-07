from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rogue.engine import Engine
    from rogue.entity import Entity
    from rogue.game_map import GameMap


class BaseComponent:
    parent: Entity    # Owning entity instace

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    @property
    def engine(self) -> Engine:
        return self.gamemap.engine
