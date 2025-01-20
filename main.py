import shutil
import os

def archive_folder(folder_path, output_path):
    """
    Архивирует указанную папку в zip-формате.

    Args:
        folder_path (str): Путь к папке, которую нужно архивировать.
        output_path (str): Путь для сохранения архива (без расширения).
    """
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Папка '{folder_path}' не найдена или это не папка.")
    
    # Создаём архив в формате zip
    shutil.make_archive(output_path, 'zip', folder_path)
    print(f"Папка '{folder_path}' успешно архивирована в '{output_path}.zip'")

# Пример использования
folder_to_archive = "/workspaces/Sites/diary"  # Укажите путь к папке
archive_name = "/workspaces/Sites/diary"  # Укажите путь и имя архива (без расширения)

archive_folder(folder_to_archive, archive_name)