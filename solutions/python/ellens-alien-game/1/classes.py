"""Solution to Ellen's Alien Game exercise."""

class Alien:
    health = 3
    total_aliens_created = 0

    def __init__(self,x,y):
        self.x_coordinate =x
        self.y_coordinate =y
        self.health = Alien.health
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x,new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other_object):
        pass


def new_aliens_collection(alien_start_positions):
    aliens = []

    for position in alien_start_positions:
        aliens.append(Alien(*position))

    return aliens


#TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates

