
import abc

from pgfe import Enum
from pgfe.entity.entity_components.colliders.AbstractCollider import AbstractCollider


class AABBCollider(AbstractCollider, abc.ABC):
    def __init__(self):
        super().__init__()

    def collide(self, sprite, axis) -> tuple[bool, bool]:
        if axis == Enum.Axis.X:
            to_return = [False, False]
            if self.velocity.x > 0:
                self.rect.right = sprite.rect.left
                self.velocity.x = 0
                to_return[0] = True
            if self.velocity.x < 0:
                self.rect.left = sprite.rect.right
                self.velocity.x = 0
                to_return[1] = True
            return tuple(to_return)

        if axis == Enum.Axis.Y:
            to_return = [False, False]
            if self.velocity.y > 0:
                self.rect.bottom = sprite.rect.top
                self.velocity.y = 0
                to_return[1] = True
            if self.velocity.y < 0:
                self.rect.top = sprite.rect.bottom
                self.velocity.y = 0
                to_return[0] = True
            return tuple(to_return)

        return False, False
