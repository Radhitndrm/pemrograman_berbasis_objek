
class User:
    def __init__(self, username, level):
        self.__username = ""
        self.__level = ""
        self.set_username(username)
        self.set_level(level)

    def info(self):
        print(f"Username: {self.__username}, Level: {self.__level}")

    def get_username(self):
        return self.__username

    def get_level(self):
        return self.__level

    def set_username(self, username_baru):
        if len(username_baru) > 5:
            self.__username = username_baru
            print("Username berhasil diubah.")
        else:
            print("Error: Username terlalu pendek! Minimal 6 karakter.")

    def set_level(self, level_baru):
        allowed_levels = ["User", "Admin", "Super Admin"]
        if level_baru in allowed_levels:
            self.__level = level_baru
            print("Level berhasil diubah.")
        else:
            print(f"Error: Level '{level_baru}' tidak valid!")

user_1 = User("pengguna_baru", "User")
user_1.info()

print("\n--- Mencoba mengubah data via Setter ---")
user_1.set_username("admin") 
user_1.set_level("Moderator")
user_1.info() 

print("\n--- Mencoba lagi dengan data yang valid ---")
user_1.set_username("administrator_sistem")
user_1.set_level("Admin")
user_1.info() 
