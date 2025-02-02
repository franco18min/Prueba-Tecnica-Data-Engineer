import csv

#Funcion para convertir un archivo CSV a PSV
def convert_csv_to_psv(input_file, output_file):
    try:
        # Abrimos el archivo infectado en modo lectura
        with open(input_file, mode='r', encoding='utf-8') as infile:
            # Leemos las lineas del archivo
            lines = infile.readlines()

            # Por conveniencia eliminamos la primera fila, la cual es una linea corrupta ya que puede causar problemas de lectura
            if lines and lines[0].startswith("ARCHIVO INFECTADO"):
                lines.pop(0)  # Eliminamos la primera fila

            # Vamos a procesar la fila siguiente que por logica y estructura corresponde a los nombres de las columnas
            header = lines[0].strip().split('~')  # Separamos por el caracter "~"
            header = [f'"{col}"' for col in header]  # Encerramos cada nombre de columna entre comillas

            # Procesamos las filas de datos restantes que estan separadas por comas
            data_rows = [line.strip().split(',') for line in lines[1:]]

            # Determinamos el numero maximo de columnas en el archivo
            max_columns = max(len(header), max(len(row) for row in data_rows))

            # Abrimos el archivo de salida en modo escritura
            with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
                # Escribimos la fila de nombres de columnas
                outfile.write('|'.join(header) + '\n')

                # Codificamos un writer para escribir las filas de datos en formato PSV
                writer = csv.writer(outfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)

                # Escribimos las filas de datos asegurando que tengan el mismo número de columnas
                for row in data_rows:
                    # Si esta vacio el valor, rellenamos con cadenas vacías si la fila tiene menos columnas que el máximo
                    padded_row = row + [''] * (max_columns - len(row))
                    writer.writerow(padded_row)

        print(f"Archivo PSV generado exitosamente: {output_file}")

    except Exception as e:
        print(f"Error durante la conversión: {e}")


# Archivos de entrada y salida para la conversión
input_file = 'starts_data.csv'  # Archivo infectado
output_file = 'starts_data.psv'  # Archivo PSV resultante

# Ejecutamos la función de conversión
convert_csv_to_psv(input_file, output_file)