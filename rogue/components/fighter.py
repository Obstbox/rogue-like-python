from __future__ import annotations

from typing import TYPE_CHECKING

import rogue.color

from rogue.components.base_component import BaseComponent
from rogue.input_handlers import GameOverEventHandler
from rogue.render_order import RenderOrder

if TYPE_CHECKING:
    from rogue.entity import Actor


class Fighter(BaseComponent):
    parent: Actor

    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self._hp = hp
        self.defense = defense
        self.power = power

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        # ensures hp always between 0 and max_hp
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.parent.ai:
            self.die()

    def die(self) -> None:
        if self.engine.player is self.parent:
            death_message = "You died!"
            death_message_color = rogue.color.player_die
            self.engine.event_handler = GameOverEventHandler(self.engine)
        else:
            death_message = f"{self.parent.name} is dead!"
            death_message_color = rogue.color.enemy_die

        self.parent.char = "%"
        # self.entity.color = (191, 0, 0)
        self.parent.color = (120, 120, 120)
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"remains of {self.parent.name}"
        self.parent.render_order = RenderOrder.CORPSE

        self.engine.message_log.add_message(death_message, death_message_color)
