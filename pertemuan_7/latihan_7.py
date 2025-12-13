
import os
from datetime import datetime


class FileAnalyzer:
    def __init__(self, file_path):
        self.__file_path = file_path

        if os.path.exists(file_path):
            self.__file_ada = True
            self.__file_size = os.path.getsize(file_path)
        else:
            self.__file_ada = False
            print(f"Error: File '{file_path}' tidak ditemukan.")

    def get_file_size(self, unit="bytes"):
        if not self.__file_ada:
            return None

        if unit.lower() == "kb":
            return self.__file_size / 1024
        return self.__file_size

    def get_modification_time(self):
        if not self.__file_ada:
            return None

        waktu_modifikasi = os.path.getmtime(self.__file_path)
        return datetime.fromtimestamp(waktu_modifikasi)

    def analyze(self):
        print("=" * 50)
        print(f"Analisis File: {self.__file_path}")
        print("=" * 50)

        if not self.__file_ada:
            print("File tidak dapat dianalisis karena tidak ditemukan.")
            print("=" * 50)
            return

        ukuran_kb = self.get_file_size("KB")
        waktu_modif = self.get_modification_time()

        print(f"Status File       : Ada")
        print(f"Ukuran File       : {ukuran_kb:.2f} KB")
        print(f"Waktu Modifikasi  : {waktu_modif.strftime('%d %B %Y, %H:%M:%S')}")
        print("=" * 50)


file1 = FileAnalyzer("dokumen.txt")
file1.analyze()

file2 = FileAnalyzer("file_khayalan.txt")
file2.analyze()
