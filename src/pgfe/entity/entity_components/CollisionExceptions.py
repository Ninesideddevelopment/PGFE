


import dataclasses, typing

from pgfe.entity.entity_components.AbstractComponent import AbstractComponent

if typing.TYPE_CHECKING:
    from rampant.world.tiles.Tile import Tile


@dataclasses.dataclass
class CollisionExceptions(AbstractComponent):
    def __init__(self):
        super().__init__()
        self.unconditional: CollisionRules.Unconditional = self.Unconditional()
        self.conditional: CollisionRules.Conditional = self.Conditional()

    class Unconditional(list):
        def add(self, tile: "type[Tile]"):
            self.append(tile)

        def remove(self, tile: "type[Tile]"):
            super().remove(tile)

        def get_rules(self):
            return [i for i in self]

    class Conditional(dict):
        def add(self, tile: "type[Tile]", condition: "typing.Callable[[Tile], Tile|None]"):
            self[tile] = condition

        def remove(self, tile: "type[Tile]"):
            super().pop(self, tile)

        def get_rules(self):
            return {(t, c) for t, c in self.items()}