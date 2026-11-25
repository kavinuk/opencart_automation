import json
import csv
import openpyxl

def read_json_date(file_path: str) :
    data =[]
    try:
        file = open(file_path, 'r')
        json_data = json.load(file)
        for record in json_data:
            data.append(tuple(record.values()))
    except Exception as e:
        print(f"Error reading json file: {e}")
    return data


def read_csv_date(file_path: str) :
    data =[]
    try:
        file = open(file_path, newline='',encoding='utf-8')
        reader = csv.DictReader(file)
        for row in reader:
            data.append(tuple(row.values()))
    except Exception as e:
        print(f"Error reading csv file: {e}")
    return data

def read_excel_date(file_path: str, sheet_name: str = None)  :
    data =[]
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name] if sheet_name else workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(row)
    except Exception as e:
        print(f"Error reading excel file: {e}")
    return data

