import csv
from random import sample
import xml.etree.ElementTree as ET

def count_books_with_long_titles(file_path="books.csv", title_length_threshold=30):
    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter=";")
        count = sum(1 for row in reader if len(row[1]) > title_length_threshold)
    return count

def search_books_by_author(search_author, file_path="books.csv"):
    search_author = search_author.lower()
    result = set()

    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if search_author in (row[4].lower(), row[3].lower()):
                date = int(row[6][6:10])  # Extracting the year from the date
                if 2016 <= date <= 2018:
                    result.add(row[1])

    if not result:
        print('Ничего не найдено')
    else:
        for book in result:
            print(book)

def random_books_to_txt(file_path="books.csv", output_file="result.txt", num_random_books=20):
    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter=";")
        rows = list(reader)

        random_books = sample(rows, num_random_books)

        with open(output_file, 'w') as output:
            for i, book in enumerate(random_books, start=1):
                output.write(f"{i} {book[3]}. {book[1]} - {book[6]}\n")

def extract_currency_codes(xml_file_path='currency.xml', nominal_values=(10, 100)):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    C_Code = [node.find('CharCode').text
              for node in root.findall('.//Valute')
              if int(node.find('Nominal').text) in nominal_values]
    return C_Code

# Task 1
count_long_titles = count_books_with_long_titles()
print(count_long_titles)

# Task 2
print('Введите автора')
search_input = input().lower()
search_books_by_author(search_input)

# Task 3
random_books_to_txt()

# Task 4
currency_codes = extract_currency_codes()
print(*currency_codes)

