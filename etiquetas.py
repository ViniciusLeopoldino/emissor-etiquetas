# Instalar as bibliotecas necessárias: pip install pandas python-barcode reportlab 
# Executar: python etiquetas.py


import os
import time
import pandas as pd
import barcode
from barcode.writer import ImageWriter

def gerar_codigo_barras(lote):
    """Gera um código de barras para o lote."""
    codigo = barcode.get('code128', lote, writer=ImageWriter())
    filename = f"codigo_barras_{lote}"
    codigo.save(filename)
    time.sleep(0.1)  # Pequeno delay para garantir que o arquivo seja salvo
    return filename + ".png"

def main():
    # Importar o CSV
    df = pd.read_csv('lotes.csv')
    lotes = df['LOTES'].tolist()

    # Gerar PNGs para cada lote
    for lote in lotes:
        codigo_barras_path = gerar_codigo_barras(lote)
        if not os.path.exists(codigo_barras_path):
            print(f"Erro: O arquivo {codigo_barras_path} não foi encontrado.")
        else:
            print(f"Código de barras gerado: {codigo_barras_path}")

if __name__ == "__main__":
    main()
