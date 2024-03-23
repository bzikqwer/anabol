import fitz  # Импорт библиотеки PyMuPDF
import os
import shutil  # Для переименования (перемещения) файлов

def compress_pdf(input_path, output_path):
    doc = fitz.open(input_path)
    # Используем временное имя для оптимизированного файла
    temp_output_path = output_path + ".temp"
    doc.save(temp_output_path, garbage=4, deflate=True, clean=True)
    doc.close()
    # Заменяем исходный файл оптимизированным
    shutil.move(temp_output_path, output_path)

def compress_pdf_in_directory(input_directory, output_directory=None):
    if output_directory is None:
        output_directory = input_directory

    for filename in os.listdir(input_directory):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            compress_pdf(input_path, output_path)

input_directory = './files/products/ru/final/'
output_directory = None  # Модифицированные файлы заменят исходные

compress_pdf_in_directory(input_directory, output_directory)
