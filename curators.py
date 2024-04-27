import pandas as pd
import os
import csv

def Import_from_Excel_to_CSV():
    # Укажите путь к папке с Excel файлами
    excel_folder = os.getcwd()
    # Укажите путь к папке, куда будут сохранены CSV файлы
    csv_folder = os.getcwd()
    # Получаем список файлов в папке с Excel файлами
    excel_files = [file for file in os.listdir(excel_folder) if file.endswith('кураторы.xlsx')]
    for excel_file in excel_files:
        # Читаем Excel файл
        df = pd.read_excel(os.path.join(excel_folder, excel_file))
        # Создаем CSV файл из Excel файла
        csv_file = os.path.splitext(excel_file)[0] + '.csv'
        df.to_csv(os.path.join(csv_folder, csv_file), index=False)
       

def get_curator_by_course( course_name):
   file_path = 'кураторы.csv'
   with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Group'] == course_name:
                return list(row.values())

   return None  # Курс не найден