from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rogue.engine import Engine
    from rogue.entity import Entity


class BaseComponent:
    entity: Entity    # Owning entity instace

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine
