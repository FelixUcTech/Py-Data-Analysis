from PyPDF2 import PdfReader

# Ruta del archivo PDF
pdf_path = 'zodiaco1613.pdf'
# Ruta del archivo de salida
output_text_path = 'zodiaco1613.txt'

# Función para extraer texto del PDF y guardarlo en un archivo de texto plano
def convert_pdf_to_text(pdf_path, output_text_path):
    reader = PdfReader(pdf_path)
    with open(output_text_path, 'w', encoding='utf-8') as text_file:
        for page in reader.pages:
            text = page.extract_text()
            if text:
                text_file.write(text + '\n')  # Agregar salto de línea entre páginas
    print(f"El contenido del PDF ha sido guardado en {output_text_path}")

# Llamada a la función
convert_pdf_to_text(pdf_path, output_text_path)