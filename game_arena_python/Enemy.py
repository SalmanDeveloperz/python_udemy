class Enemy:
    type_of_enemy: str
    health_points: int = 100
    attack_damage: int = 1


    def __init__(self, type_of_enemy, health_points,attack_damage):
        print("Create new Enemy")

    def talk(self):
        print(f'I am a {self.type_of_enemy}. So be prepared')

    def walk_forward(self):
        print(f'{self.type_of_enemy}. Move Closer')


    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage')

