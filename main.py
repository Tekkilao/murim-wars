import copy
import os
import sys

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

import entity_factories
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

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        FONT_FILE, 32, 8, charmap=tcod.tileset.CHARMAP_TCOD,
    )

    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms = max_rooms,
        room_min_size = room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )
    engine.update_fov()

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

            engine.event_handler.handle_events()



if __name__ == "__main__":
    main()