from .entity import Entity

player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

orc = Entity(char="o", color=(190, 63, 63), name="Orc", blocks_movement=True)
troll = Entity(char="T", color=(63, 120, 63), name="Troll", blocks_movement=True)
