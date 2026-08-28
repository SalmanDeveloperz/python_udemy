from Enemy import *
enemy= Enemy()
enemy.type_of_enemy="Zombie"  #this was a quick fix, coz we didn't assign or add any field for the type_of_enemy

print(enemy.walk_forward())
# print(f'{enemy.type_of_enemy} has {enemy.health_points} health and the attack damage{enemy.attack_damage}')