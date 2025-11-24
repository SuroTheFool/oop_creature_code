class Creature:
    def __init__(self, name, hp, attack_power):
        self.__name = name
        self.__hp = hp
        self.__attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.__name} cannot attack because it is defeated.")
            return
        print(f"{self.__name} attacks {target.get_name()} for {self.__attack_power} damage!")
        target.take_damage(self.__attack_power)
    def get_name(self):
        return self.__name
    def get_attack_power(self):
        return self.__attack_power
    def get_hp(self):
        return self.__hp
    def take_damage(self,amount):
        if amount < 0:
            print("Error : Amount cannot be zero or less")
            amount = 0
        self.__hp -= amount
    def is_alive(self):
        return self.__hp > 0
    def __str__(self):
        return f"{self.__name} (HP: {self.__hp})"
class FlyingCreature(Creature):
    def __init__(self,name,hp,attack_power):
        super().__init__(name,hp,attack_power)
        self.__altitude = 0
    def fly_to(self,new_altitude):
        self.__altitude = new_altitude
    def attack(self, target):
        super().attack(target)
        if self.__altitude > 50:
            additional_dmg = self.__altitude / 10
            target.take_damage(additional_dmg)
            print(f"{self.get_name()} raise in altitude and attack again : {additional_dmg:.0f}")

class FireCreature(Creature):
    def __init__(self,name,hp,attack_power):
        super().__init__(self,name,hp,attack_power)
        self.fire_level  = 0
    def emit_fire(self,new_fire):
        self.altitude = new_fire
    def attack(self, target):
        super().attack(target)

class Trainer:
    def __init__(self,name):
        self.__name = name
        self.__team = []
    def add_creature(self,creature):
        self.__team.append(creature)
    def remove_creature(self,creature):
        self.__team.remove(creature)
    def get_team_size(self):
        return len(self.__team)
    def get_creature(self,index):
        return self.__team[index]

    def show_team(self):
        print(f"{self.__name} team:")
        for c in self.__team:
            print(c)


if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")

    # Test 2: Basic attack
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Wolf attacks Sheep")
    wolf.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.get_hp()}")
    print()

    # Test 3: HP does not go below zero
    dragon = FlyingCreature("Dragonling", 200, 13)
    dragon.fly_to(70)
    mouse = Creature("Mouse", 20, 1)
    print("Test 3: Dragonling overkills Mouse")
    dragon.attack(mouse)
    print(f"Mouse HP should now be 0 → Actual: {mouse.get_hp()}")
    print()

    Suro = Trainer("Suro")
    Suro.add_creature(dragon)
    Suro.add_creature(mouse)
    Suro.show_team()
    
    # # Test 4: is_alive()
    # slime = Creature("Slime", 10, 2)
    # print("Test 4: Slime alive?")
    # print("Slime should be alive →", slime.is_alive())
    # slime.hp = 0
    # print("Slime should NOT be alive →", slime.is_alive())
    # print()

    # # Test 5: Dead creature cannot attack
    # ghost = Creature("Ghost", 0, 10)
    # knight = Creature("Knight", 50, 7)
    # print("Test 5: Ghost tries to attack Knight")
    # ghost.attack(knight)
    # print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    # print()

    # # Test 6: Multiple attacks
    # print("Test 6: Goblin attacks Slime twice")
    # slime.hp = 10
    # goblin.attack(slime)
    # goblin.attack(slime)
    # print(f"Slime should be at HP 0 → Actual: {slime.hp}")
    # print()

    # print("=== Tests Completed ===")