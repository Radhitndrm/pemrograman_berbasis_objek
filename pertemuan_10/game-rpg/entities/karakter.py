

class Karakter:
    def __init__(self, nama, hp, serangan):
        self._nama = nama          
        self.__hp = hp            
        self.__serangan = serangan 

    def get_hp(self):
        return self.__hp

    def get_serangan(self):
        return self.__serangan

    def get_nama(self):
        return self._nama

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def set_serangan(self, value):
        if value < 0:
            self.__serangan = 0
        else:
            self.__serangan = value

    def serang(self, target):
        pass
