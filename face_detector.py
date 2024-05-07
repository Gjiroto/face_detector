import cv2
import numpy as np

def detectar_rostros(imagen):
  """
  Función para detectar rostros en una imagen.

  Args:
    imagen: Una imagen en formato OpenCV (numpy array).

  Returns:
    Una lista de tuplas que contienen las coordenadas de los rectángulos alrededor de los rostros detectados.
  """

  # Convertir la imagen a escala de grises
  imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

  # Detectar rostros
  rostros = clasificador.detectMultiScale(imagen_gris, 1.1, 4)

  # Almacenar las coordenadas de los rostros
  coordenadas_rostros = []

  # Recorrer cada rostro detectado
  for (x, y, w, h) in rostros:
    # Crear un rectángulo alrededor del rostro
    rectangulo = (x, y, w, h)

    # Agregar el rectángulo a la lista
    coordenadas_rostros.append(rectangulo)

  return coordenadas_rostros

# Cargar el clasificador de rostros
clasificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Iniciar la captura de video
captura = cv2.VideoCapture(0)  # 0 para la cámara web principal

# Crear una ventana para mostrar la imagen
ventana = 'Detección de rostros'
cv2.namedWindow(ventana)

while True:
  # Capturar un frame de video
  ret, frame = captura.read()

  # Detectar rostros en el frame
  coordenadas_rostros = detectar_rostros(frame)

  # Dibujar rectángulos alrededor de los rostros
  for (x, y, w, h) in coordenadas_rostros:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

  # Mostrar el frame resultante en la ventana
  cv2.imshow(ventana, frame)

  # Salir del bucle si se presiona la tecla 'q'
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Liberar la captura de video
captura.release()

# Cerrar la ventana
cv2.destroyWindow(ventana)
