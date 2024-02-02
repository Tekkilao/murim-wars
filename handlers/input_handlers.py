from typing import Optional
import tcod.event
from handlers.actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.KeySym.w:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.KeySym.s:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.KeySym.a:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.KeySym.d:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()

        return action