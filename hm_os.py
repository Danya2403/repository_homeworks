import os
import shutil


class FileManager:
    def init(self, current_directory='.'):
        self.current_directory = current_directory

    def list_contents(self):
        print(f"Содержимое директории {self.current_directory}:")
        for item in os.listdir(self.current_directory):
            print(item)

    def create_directory(self, directory_name):
        path = os.path.join(self.current_directory, directory_name)
        os.mkdir(path)
        print(f"Создана новая директория: {path}")

    def delete(self, name):
        path = os.path.join(self.current_directory, name)
        if os.path.isfile(path):
            os.remove(path)
            print(f"Файл удален: {path}")
        elif os.path.isdir(path):
            os.rmdir(path)
            print(f"Директория удалена: {path}")
        else:
            print(f"Файл или директория не найдены: {path}")

    def copy(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
            print(f"Файл скопирован: {source_path} -> {destination_path}")
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, destination_path)
            print(f"Директория скопирована: {source_path} -> {destination_path}")
        else:
            print(f"Файл или директория не найдены: {source_path}")

    def move(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        os.rename(source_path, destination_path)
        print(f"Файл или директория перемещены: {source_path} -> {destination_path}")

    def search_file(self, filename):
        for root, dirs, files in os.walk(self.current_directory):
            if filename in files:
                print(f"Файл найден: {os.path.join(root, filename)}")
                return os.path.join(root, filename)
        print(f"Файл не найден: {filename}")

    def change_permissions(self, name, mode):
        path = os.path.join(self.current_directory, name)
        os.chmod(path, mode)
        print(f"Изменены права доступа для {path} на {oct(mode)}")


# Пример использования:
while True:
    print("""Написать свой файловый менеджер, используя модуль os Python. Файловый менеджер должен иметь следующие функции:
            1. Просмотр содержимого текущей директории.
            2. Создание новой директории.
            3. Удаление директории или файла.
            4. Копирование файла или директории.
            5. Перемещение файла или директории.
            6. Поиск файла по имени в текущей директории и всех поддиректориях.
            7. Изменение прав доступа к файлу или директории.
            Файловый менеджер должен быть реализован в виде класса и иметь
            необходимые по вашему мнению атрибуты и методы\n""")
    choose = int(input("Ваш выбор: "))
    file_manager = FileManager()
    if choose == 1:

        file_manager.list_contents()
    elif choose == 2:

        directory_name = input("Имя новой директории: ")
        file_manager.create_directory('Новая_директория')
    elif choose == 3:

        dir_or_file_name = input("Введите имя файла или директории для удаления: ")
        file_manager.list_contents()
    elif choose == 4:

        to_copy = input("Введите имя файла или директории для копирования: ")
        destination = input("Введите конечную директорию для копирования: ")
        file_manager.copy(to_copy, destination)
    elif choose == 5:

        source = input("Введите исходную директорию: ")
        destination = input("Введите желаемую директорию: ")
        file_manager.move('Исходная_директория', 'Желаемая_директория')

elif choose == 6:
        file_name = input("Введите имя файла для поиска: ")
        file_manager.search_file(file_name)
        file_manager.list_contents()
    elif choose == 7:
        file_name = input("Введите имя файла: ")
        mode = int(input("Введите mode в десятичной системе счисления\n(ВНИМАНИЕ! Вводить нужно 8-ное число, то есть, к примеру, для задачи доступа User: RWE, GROP: RW, WORLD: RW нужно ввести 0o755: "), base=8)
        file_manager.change_permissions(file_name, mode)