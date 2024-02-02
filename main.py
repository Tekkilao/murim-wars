import os
import sys

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

from handlers.input_handlers import EventHandler
from entity import Entity
from handlers.engine import Engine
from maps.procgen import generate_dungeon

os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]

DATA_FOLDER = "data"
FONT_FILE = os.path.join(DATA_FOLDER, "dejavu10x10.png")
def main() -> None:
    screen_width = 80
    screen_height = 60

    map_width = 80
    map_height = 55

    tileset = tcod.tileset.load_tilesheet(
        FONT_FILE, 32, 8, charmap=tcod.tileset.CHARMAP_TCOD,
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2 ), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 ), int(screen_height / 2 ), "@", (255, 255, 0))
    entities = {npc, player}

    game_map =generate_dungeon(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Murim Wars",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()