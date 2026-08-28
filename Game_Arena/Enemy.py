class Enemy:
    type_of_enemy: str
    health_points: int = 100
    attack_damage: int = 1

def talk(self=None):
    print(f'I am a {self.type_of_enemy}. So be prepared')


def walk_forward(self=None):
    print(f'{self.type_of_enemy}. Move Closer')


def attack(self=None):
    print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage')

