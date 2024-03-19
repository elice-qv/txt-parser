import os
import chardet


def get_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']


def search_and_collect_data_chardet(search_text, file_name, root_directory, output_file='data.txt'):
    with open(output_file, 'w', encoding='utf-8') as output:
        for root, dirs, files in os.walk(root_directory):
            if file_name in files:
                file_path = os.path.join(root, file_name)
                encoding = get_encoding(file_path)
                with open(file_path, 'r', encoding=encoding, errors='replace') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if search_text.lower() in line.lower():
                            output.write(
                                "--------------------------------------------------------------------------------\n")
                            output.write(f"{file_path}\n")
                            output.write(line)
                            for j in range(1, 4):
                                if i + j < len(lines):
                                    output.write(lines[i + j])
                            output.write(
                                "--------------------------------------------------------------------------------\n\n")


def main_chardet():
    search_text = input("Введите текст для поиска: ")
    file_name = input("Введите имя файла для поиска: ")
    root_directory = input("Введите путь к корневой папке (оставьте пустым для текущей директории): ")
    root_directory = root_directory or '.'

    search_and_collect_data_chardet(search_text, file_name, root_directory)

# Uncomment it before 'run' in IDE
#if __name__ == "__main__":
#    main_chardet()