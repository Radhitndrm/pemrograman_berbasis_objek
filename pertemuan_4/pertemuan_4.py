class Character:
    def __init__(self, name, health, attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power
        print(f"{self.__name} bergabung ke dalam pertarungan!")

    def show_info(self):
        print("\n--- Character Info ---")
        print(f"Name: {self.__name}")
        print(f"Health: {self.__health}")
        print(f"Attack Power: {self.__attack_power}")

    def attack(self, target):
        print(f"{self.__name} menyerang {target.get_name()} !")
        target.take_damage(self.__attack_power)

    def take_damage(self, damage):
        self.__health -= damage       
        if self.__health <= 0:
            print(f"{self.__name} telah dikalahkan!")
            self.__health = 0
        else:
            print(f"Health {self.__name} tersisa {self.__health}")

    def get_name(self):
        return self.__name


class Warrior(Character):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.__armor = armor
        print(f"Armor set to: {self.__armor}")

    def show_info(self):
         super().show_info()
         print(f"Armor: {self.__armor}")
            

print("--- Membuat Objek dari Parent Class ---")
aragorn = Character("Aragorn", 100, 15)
aragorn.show_info()

print("\n--- Membuat Objek dari Child Class ---")
gimli = Warrior("Gimli", 120, 20, 5)
gimli.show_info()

print("\n--- Pertarungan Dimulai ---")
aragorn.attack(gimli)
gimli.attack(aragorn)
