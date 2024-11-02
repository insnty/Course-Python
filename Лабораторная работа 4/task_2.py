# Конвертер из CSV в JSON формат

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Открытие файла для получения чтения словарей из сsv строк
    with open(INPUT_FILENAME, 'r') as file_input:
        reader = csv.DictReader(file_input)
        data = [row for row in reader]
        # Запись данных в файл в формате JSON
        with open(OUTPUT_FILENAME, 'w') as file_output:
            json.dump(data, file_output, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
