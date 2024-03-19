# Friendly use
## About

Simple python parser with decode any symbols. If you want to check logs in many folders it yor choice
Enjoy and if you have a new idea just create issue or fork

## Запуск скрипта (scroll down for english ver)
Зависимости
``bash
pip install chardet
```
запустите script.py в cmd/powershell/terminal находясь в папке со скриптом
``bash
cd path/txt-синтаксический
анализатор python3 parser.py
```

Скрипт запросит входные данные в формате:

- Enter the key words: Текст для поиска.
- Enter file name (empty for choose all files): Имя файла, в котором нужно искать слова (вы можете оставить поле пустым, просто нажав Enter, тогда поиск будет выполнен по всем файлам)
- Enter root directory: путь к корневому каталогу для поиска.

Скрипт проанализирует файл с указанным именем и создаст файл в корневой папке со скриптом data.txt с расшифрованными данными (если они были зашифрованы)


### How to use 
Install requirements
```bash
pip install chardet
```
And run script.py
```bash
cd path/txt-parser
python3 parser.py
```

The script will request input data in the format: 

- Enter the key words: The text to search for.
- Enter file name: The name of the file in which to search for words (you can leave the field empty by simply pressing Enter, then the search will be performed on all files)
- Enter root directory: The path to the root directory to search.

The script will parse the file with the specified name and create a file in the root folder with the script data.txt with decrypted data (if it was encrypted)



