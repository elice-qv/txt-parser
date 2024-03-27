import os
import chardet

def get_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def read_file_names(file_list_path='files.txt'):
    try:
        with open(file_list_path, 'r', encoding='utf-8') as file:
            file_names = [line.strip() for line in file.readlines()]
        return file_names
    except FileNotFoundError:
        print(f"Файл {file_list_path} не найден. Будет выполнен поиск во всех файлах.")
        return None

def search_in_files(search_text, file_names, root_directory, output_file='data.txt'):
    processed_files_count = 0
    with open(output_file, 'w', encoding='utf-8') as output:
        for root, dirs, files in os.walk(root_directory):
            for file_name in files:
                if file_names is None or file_name in file_names:
                    file_path = os.path.join(root, file_name)
                    try:
                        encoding = get_encoding(file_path)
                        with open(file_path, 'r', encoding=encoding, errors='replace') as f:
                            lines = f.readlines()
                            for i, line in enumerate(lines):
                                if search_text.lower() in line.lower():
                                    output.write("--------------------------------------------------------------------------------\n")
                                    output.write(f"{file_path}\n")
                                    output.write(line)
                                    for j in range(1, 4):
                                        if i + j < len(lines):
                                            output.write(lines[i + j])
                                    output.write("--------------------------------------------------------------------------------\n\n")
                                    break  # Остановиться после первого найденного совпадения в файле
                        processed_files_count += 1
                        print(f"Обработано файлов: {processed_files_count}. Последний обработанный файл: {file_path}")
                    except Exception as e:
                        print(f"Ошибка при обработке файла {file_path}: {e}")

def search_and_collect_data_interactive():
    search_text = input("Введите ключевое слово для поиска: ")
    root_directory = input("Введите путь к корневой папке для поиска: ")
    file_list_path = 'files.txt'

    file_names = read_file_names(file_list_path)
    if file_names is not None and len(file_names) == 0:
        print("Список файлов для поиска пуст. Будет выполнен поиск во всех файлах.")
        file_names = None

    search_in_files(search_text, file_names, root_directory)

if __name__ == "__main__":
    search_and_collect_data_interactive()
