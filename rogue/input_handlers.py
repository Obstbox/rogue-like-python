from typing import Optional

import tcod.event

from rogue.actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.KeySym.UP or key == tcod.event.KeySym.k:
            action = MovementAction(dx=0, dy=-1)

        elif key == tcod.event.KeySym.DOWN or key == tcod.event.KeySym.j:
            action = MovementAction(dx=0, dy=1)

        elif key == tcod.event.KeySym.LEFT or key == tcod.event.KeySym.h:
            action = MovementAction(dx=-1, dy=0)

        elif key == tcod.event.KeySym.RIGHT or key == tcod.event.KeySym.l:
            action = MovementAction(dx=1, dy=0)


        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()

        # no valid key
        return action

