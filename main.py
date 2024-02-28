from PIL import Image
import pytesseract

# Ruta de la imagen
ruta_imagen = 'img2.png'
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'  # Ruta a tu ejecutable de Tesseract

# # Cargar la imagen
# imagen = Image.open(ruta_imagen)
#
# # Utilizar pytesseract para extraer el texto de la imagen
# texto_extraido = pytesseract.image_to_string(imagen)
#
# # Obtener las coordenadas del cuadro del texto en la imagen
# cuadro_texto = pytesseract.image_to_boxes(imagen)
#
# # Imprimir el texto extraído y las coordenadas del cuadro
# print("Texto extraído:", texto_extraido)
#
# for cuadro in cuadro_texto.splitlines():
#     cuadro_info = cuadro.split()
#     letra, x1, y1, x2, y2 = cuadro_info[0], int(cuadro_info[1]), int(cuadro_info[2]), int(cuadro_info[3]), int(cuadro_info[4])
#     print(f"Letra: {letra}, Coordenadas X: {x1}-{x2}, Coordenadas Y: {y1}-{y2}")
#

# Cargar la imagen
imagen = Image.open(ruta_imagen)

# Utilizar pytesseract para extraer la información detallada del texto en la imagen
datos_texto = pytesseract.image_to_data(imagen, output_type=pytesseract.Output.DICT)

arrPalabrasPos = []
# Iterar sobre las palabras y sus coordenadas
for i, palabra in enumerate(datos_texto['text']):
    x = datos_texto['left'][i]
    y = datos_texto['top'][i]
    w = datos_texto['width'][i]
    h = datos_texto['height'][i]

    if len(palabra.strip()) > 0:
        arrPalabrasPos.append(palabra)

        # Imprimir información de la palabra y sus coordenadas
        print(f"Palabra: {palabra}, Coordenadas X: {x}-{x+w}, Coordenadas Y: {y}-{y+h}")


arrPalabrasSinPos = pytesseract.image_to_data(imagen, output_type=pytesseract.Output.DICT)
arrPalabrasSinPos = [entrada for entrada in arrPalabrasSinPos['text'] if len(entrada.strip()) > 0]

print(f"Número de palabras encontradas: { len(arrPalabrasSinPos)}")
print(f"Número de palabras encontradas2: {len(arrPalabrasPos)}")
