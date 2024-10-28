# Instalar as bibliotecas necessárias: pip install pandas python-barcode reportlab 
# Executar: python etiquetas.py

import os
import time
import pandas as pd
import barcode
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import mm

def gerar_codigo_barras(lote):
    """Gera um código de barras para o lote."""
    codigo = barcode.get('code128', lote, writer=ImageWriter())
    filename = f"codigo_barras_{lote}"
    codigo.save(filename)
    time.sleep(0.1)  # Pequeno delay para garantir que o arquivo seja salvo
    return filename + ".png"

def gerar_pdf_etiquetas(lotes):
    """Gera um arquivo PDF com etiquetas de código de barras."""
    pdf_filename = "etiquetas.pdf"
    page_width, page_height = 100 * mm, 70 * mm
    c = canvas.Canvas(pdf_filename, pagesize=(page_width, page_height))

    for lote in lotes:
        codigo_barras_path = gerar_codigo_barras(lote)
        if not os.path.exists(codigo_barras_path):
            print(f"Erro: O arquivo {codigo_barras_path} não foi encontrado.")
        else:
            c.drawImage(codigo_barras_path, 0, page_height - 40 * mm, width=100 * mm, height=30 * mm)
            c.drawString(30 * mm, page_height - 50 * mm, f"Lote: {lote}") 
            c.showPage()  # Adiciona uma nova página para a próxima etiqueta

    c.save()
    print(f"Arquivo PDF gerado: {pdf_filename}")

def main():
    # Importar o CSV
    df = pd.read_csv('lotes.csv')
    lotes = df['LOTES'].tolist()

    # Gerar PDF com etiquetas
    gerar_pdf_etiquetas(lotes)

if __name__ == "__main__":
    main()
