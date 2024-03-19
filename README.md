# Friendly use
# About

Simple python parser with decode any symbols. If you want to check logs in many folders it yor choice
Enjoy and if you have a new idea just create issue or fork

# How to use
Install requirements
```bash
pip install chardet
```
And run script.py
```bash
cd path/txt-parser
python3 script.py
```

The script will request input data in the format: 
    - search_text (str): Текст для поиска. (The text to search for.)
    - file_name (str): Имя файла, в которых нужно искать слова. (The name of the file to search for words in.) 
    - root_directory (str): Путь к корневой директории для поиска. (The path to the root directory to search.)
    - output_file (str): Путь к файлу для записи результатов. (The path to the file to record the results.)

The script will parse the file with the specified name and create a file in the root folder with the script data.txt with decrypted data (if it was encrypted)



