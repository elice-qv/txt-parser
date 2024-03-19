import os
import chardet


def get_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']


def search_and_collect_data_any_file(search_text, root_directory, output_file='data.txt'):
     with open(output_file, 'w', encoding='utf-8') as output:
        for root, dirs, files in os.walk(root_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
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
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")


def main():
    search_text = input("Enter the key words: ")
    file_name = input("Enter file name (empty for choose all files): ")
    root_directory = input("Enter root directory: ")
    root_directory = root_directory or '.'

    if file_name:
        search_and_collect_data_any_file(search_text, root_directory, file_name)
    else:
        search_and_collect_data_any_file(search_text, root_directory)

# Uncomment it before 'run' in IDE
if __name__ == "__main__":
    main()