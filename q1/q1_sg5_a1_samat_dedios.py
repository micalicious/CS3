class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount


# Create two heroes
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

# Arthur takes 10 damage
arthur.take_damage(10)

# Print their HP
print("Arthur's HP:", arthur.hp)
print("Morgana's HP:", morgana.hp)
