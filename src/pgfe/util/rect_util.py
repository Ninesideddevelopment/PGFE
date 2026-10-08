
from pgfe.game_object import GameObject


def x_bound(self: GameObject, obj: GameObject):
    if (self.rect.left < obj.rect.right) and (self.rect.right > obj.rect.left):
        return True
    else:
        return False

def y_bound(self: GameObject, obj: GameObject):
    if (self.rect.top < obj.rect.bottom) and (self.rect.bottom > obj.rect.top):
        return True
    else:
        return False