import fitz  # PyMuPDF

def compress_pdf(input_path, output_path, quality=50):
    doc = fitz.open(input_path)
    for page in doc:
        pix = page.get_pixmap()
        pix.set_dpi(72)  # Установите DPI, соответствующий вашим требованиям
        img = pix.tobytes("png")  # Сохраняем страницу как изображение
        page.clean_contents()  # Удаляем содержимое страницы
        page.insert_image(page.rect, stream=img)  # Вставляем изображение обратно в PDF
    doc.save(output_path, garbage=4, deflate=True, clean=True)  # Сохраняем изменения

input_path = "./files/presentation/SOLWELL.pdf"
output_path = "./files/presentation/SOLWELL_final.pdf"
compress_pdf(input_path, output_path)
