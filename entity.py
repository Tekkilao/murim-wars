from __future__ import annotations
import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from maps.game_map import GameMap

T = TypeVar("T", bound="Entity")


class Entity:
    def __init__(
            self,
            char: str,
            color: Tuple[int, int, int],
            name: str = "<Unnamed>",
            blocks_movement: bool = False,
    ):

        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement

    def spawn(self: T, gamemap: GameMap, x: int, y: int ) -> T:
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

