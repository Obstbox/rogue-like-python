#!/usr/bin/env python3
import copy
import traceback
import tcod
import rogue.color

from rogue.engine import Engine
import rogue.entity_factories
from rogue.procgen import generate_dungeon

"""
TODO
awkward stuff about rogue.tile_types
must be fixed some how
"""


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        # "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
        # "Cheepicus_14x14.png", 16, 16, tcod.tileset.CHARMAP_CP437
        "Alloy_curses_12x12.png", 16, 16, tcod.tileset.CHARMAP_CP437
        # "Terminus_curses_11x11.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    player = copy.deepcopy(rogue.entity_factories.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )

    engine.update_fov()

    engine.message_log.add_message(
        "Hello and welcome, adventurer, to yet another dungeon!", rogue.color.welcome_text
    )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            try:
                for event in tcod.event.wain():
                    context.convert_event(event)
                    engine.event_handler(event)
            except Exception:
                traceback.print_exc(traceback.format_exc(), rogue.color.error)


# codeguard
if __name__ == "__main__":
    main()
