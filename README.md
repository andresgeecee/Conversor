# Proyecto de Inteligencia Artificial: Conversor de texto a voz, voz a texto y microfono a texto

- **Nombre**: [Jose Andres Galarza Chavez](https://www.facebook.com/) sigueme en Facebook.

- **Universidad**: Universidad Privada Domingo Savio
- **Carrera**: Ingeniería de Sistemas

## 📌 Introducción

Este proyecto tiene como finalidad desarrollar un sistema que permita al usuario introducir un texto y el programa lo combierta a voz, tambien tenga la opcion de voz a texto y de microfono a texto. Utiliza las librerias de pyttsx3, speech_recognition y PyQt5.

## 🎯 Objetivo

Desarrollar un modelo que utilize IA capaz de leer en voz alta cualquier texto proporcionado, convertir la voz en entradas de texto comprensibles y tener la funcionalidad para transcribir y procesar el habla del usuario a texto.

## 📚 Marco Teórico

Se revisaron conceptos clave servicios basados en inteligencia artificial como Google Speech Recognition para convertir voz en texto.

### Introducción a pyttsx3

es una biblioteca de Python que permite la conversión de texto a voz (Text to Speech, TTS). Con esta biblioteca, los desarrolladores pueden integrar la capacidad de generar voz a partir de texto en sus aplicaciones de Python.

### Introducción a speech_recognition

SpeechRecognition es otra biblioteca de Python que proporciona capacidades de reconocimiento de voz (Speech Recognition). Con esta biblioteca, los desarrolladores pueden agregar funcionalidades de reconocimiento de voz a sus aplicaciones de Python. Permite a los programas escuchar el audio del micrófono o leer archivos de audio y luego transcribir el habla en texto.

SpeechRecognition soporta múltiples motores de reconocimiento de voz, incluyendo Google Speech Recognition, CMU Sphinx, Microsoft Bing Voice Recognition, entre otros. Esto permite a los desarrolladores elegir el motor de reconocimiento que mejor se adapte a sus necesidades y requisitos.

### Código Fuente y Procedimientos de Instalación

#### Pre-requisitos

Asegúrate de tener Python 3.8 o superior instalado en tu sistema. Además, necesitarás pip para instalar las librerías.

#### Instalación de Librerías

Para instalar las librerías necesarias, ejecuta el siguiente comando en tu terminal:

```bash
pip install pyttsx3
```

```bash
pip install SpeechRecognition
```

```bash
pip install PyQt5
```

#### Código para Preprocesamiento de texto a voz, voz a texto y microfono a texto

```python
import pyttsx3
import speech_recognition as SR
import time
from PyQt5 import QtWidgets, QtCore

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicialización del motor de texto a voz (TTS)
        self.motor = pyttsx3.init()
        voces = self.motor.getProperty('voices')
        self.motor.setProperty('voice', voces[0].id)

        # Inicialización del reconocedor de voz
        self.r = SR.Recognizer()

        self.voice_window = None  # Nuevo atributo para la ventana de entrada de voz

        self.initUI()

    def initUI(self):
        # Crear un widget central para la aplicación
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Crear un diseño vertical para organizar los elementos de la interfaz
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Crear etiquetas descriptivas
        label_title = QtWidgets.QLabel("Aplicación de Conversión de Voz", self)
        label_title.setAlignment(QtCore.Qt.AlignCenter)
        label_title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")

        label_sub = QtWidgets.QLabel("Selecciona una opción:", self)
        label_sub.setAlignment(QtCore.Qt.AlignCenter)
        label_sub.setStyleSheet("font-size: 16px; margin-bottom: 10px;")

        # Crear los botones para las diferentes opciones de conversión
        self.btn_texto_a_voz = QtWidgets.QPushButton('Texto a Voz', self)
        self.btn_voz_a_texto = QtWidgets.QPushButton('Voz a Texto', self)
        self.btn_microfono_a_texto = QtWidgets.QPushButton('Micrófono a Texto', self)  # Nuevo botón para la conversión de voz a texto

        # Conectar los botones a las funciones correspondientes
        self.btn_texto_a_voz.clicked.connect(self.mostrar_entrada)
        self.btn_voz_a_texto.clicked.connect(self.voz_a_texto)
        self.btn_microfono_a_texto.clicked.connect(self.mostrar_entrada_microfono)  # Conectar el nuevo botón a una nueva función

        # Agregar los widgets al diseño
        self.layout.addWidget(label_title)
        self.layout.addWidget(label_sub)
        self.layout.addWidget(self.btn_texto_a_voz)
        self.layout.addWidget(self.btn_voz_a_texto)
        self.layout.addWidget(self.btn_microfono_a_texto)  # Agregar el nuevo botón al diseño

        # Estilo de los botones
        self.setStyleSheet("QPushButton {"
                           "background-color: #4CAF50;"
                           "border: none;"
                           "color: white;"
                           "padding: 15px 32px;"
                           "text-align: center;"
                           "text-decoration: none;"
                           "display: inline-block;"
                           "font-size: 16px;"
                           "margin: 4px 2px;"
                           "transition-duration: 0.4s;"
                           "cursor: pointer;"
                           "border-radius: 10px;"
                           "}"
                           "QPushButton:hover {"
                           "background-color: #45a049;"
                           "}")

        self.setWindowTitle('Conversor de Voz')
        self.setGeometry(300, 150, 400, 300)
        self.show()

    # Función para mostrar la ventana de entrada de texto
    def mostrar_entrada(self):
        # Crear una nueva ventana para la entrada de texto
        self.text_window = QtWidgets.QWidget()
        self.text_window.setWindowTitle('Texto a Voz')
        self.text_window.resize(500, 200)

        # Crear un diseño vertical para la nueva ventana
        layout = QtWidgets.QVBoxLayout(self.text_window)

        # Campo de entrada de texto
        self.text_input = QtWidgets.QLineEdit(self.text_window)

        # Establecer el estilo de los botones
        btn_style = "QPushButton { background-color: #4CAF50; border: none; color: white; padding: 15px 32px; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 10px; }"

        # Botón de confirmación
        self.btn_confirmar = QtWidgets.QPushButton('Confirmar', self.text_window)
        self.btn_confirmar.setStyleSheet(btn_style)
        self.btn_confirmar.clicked.connect(self.texto_a_voz)

        # Botón para volver a la ventana original
        self.btn_volver = QtWidgets.QPushButton('Volver', self.text_window)
        self.btn_volver.setStyleSheet(btn_style)
        self.btn_volver.clicked.connect(self.volver_a_original)

        # Agregar los widgets al diseño
        layout.addWidget(self.text_input)
        layout.addWidget(self.btn_confirmar)
        layout.addWidget(self.btn_volver)

        # Ocultar la ventana original y mostrar la nueva ventana
        self.hide()
        self.text_window.show()

    # Función para mostrar la ventana de entrada de voz
    def mostrar_entrada_microfono(self):
        # Crear una nueva ventana para la entrada de voz
        self.voice_window = QtWidgets.QWidget()
        self.voice_window.setWindowTitle('Micrófono a Texto')
        self.voice_window.resize(500, 200)

        # Crear un diseño vertical para la nueva ventana
        layout = QtWidgets.QVBoxLayout(self.voice_window)

        # Estilo de los botones
        btn_style = "QPushButton { background-color: #4CAF50; border: none; color: white; padding: 15px 32px; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 10px; }"

        # Botón de grabación
        self.btn_grabar = QtWidgets.QPushButton('Grabar', self.voice_window)
        self.btn_grabar.setStyleSheet(btn_style)
        self.btn_grabar.clicked.connect(self.microfono_a_texto)

        # Botón para volver a la ventana original
        self.btn_volver = QtWidgets.QPushButton('Volver', self.voice_window)
        self.btn_volver.setStyleSheet(btn_style)
        self.btn_volver.clicked.connect(self.volver_a_original)

        # Agregar los widgets al diseño
        layout.addWidget(self.btn_grabar)
        layout.addWidget(self.btn_volver)

        # Ocultar la ventana original y mostrar la nueva ventana
        self.hide()
        self.voice_window.show()

    # Función para volver a la ventana original desde cualquier ventana secundaria
    def volver_a_original(self):
        # Ocultar la ventana secundaria y mostrar la ventana original
        if self.text_window.isVisible():
            self.text_window.hide()
        if self.voice_window is not None and self.voice_window.isVisible():  # Verificar si voice_window no es None
            self.voice_window.hide()
        self.show()

    # Función para convertir texto a voz
    def texto_a_voz(self):
        texto = self.text_input.text()
        self.motor.say(texto)
        self.motor.save_to_file(texto, 'test.mp3')
        self.motor.runAndWait()

    # Función para convertir voz a texto a partir de un archivo de audio
    def voz_a_texto(self):
        with SR.AudioFile('test.mp3') as source:
            audio = self.r.listen(source)

            try:
                print('Espere un momento, el audio se está leyendo...')
                text = self.r.recognize_google(audio, language='es-ES')
                time.sleep(1.5)
                self.mostrar_texto(text)
            except:
                print('No se logró reconocer el audio')

    # Función para convertir voz del micrófono a texto
    def microfono_a_texto(self):
        with SR.Microphone() as source:
            print("Habla ahora...")
            audio = self.r.listen(source)

            try:
                print('Espere un momento, el audio se está leyendo...')
                text = self.r.recognize_google(audio, language='es-ES')
                time.sleep(1.5)
                self.mostrar_texto(text)
            except:
                print('No se logró reconocer el audio')

    # Función para mostrar el texto reconocido en una ventana
    def mostrar_texto(self, text):
        # Crear una nueva ventana para mostrar el texto reconocido
        self.text_window = QtWidgets.QWidget()
        self.text_window.setWindowTitle('Texto Reconocido')
        self.text_window.resize(500, 200)

        # Crear un diseño vertical para la nueva ventana
        layout = QtWidgets.QVBoxLayout(self.text_window)

        # Widget de texto para mostrar el texto reconocido
        text_widget = QtWidgets.QTextEdit(self.text_window)
        text_widget.setText(text)
        text_widget.setReadOnly(True)

        # Botón para volver a la ventana original
        btn_volver = QtWidgets.QPushButton('Volver', self.text_window)
        btn_volver.setStyleSheet("QPushButton { background-color: #4CAF50; border: none; color: white; padding: 15px 32px; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 10px; }")
        btn_volver.clicked.connect(self.volver_a_original)

        # Agregar los widgets al diseño
        layout.addWidget(text_widget)
        layout.addWidget(btn_volver)

        # Ocultar la ventana original y mostrar la nueva ventana
        self.hide()
        self.text_window.show()

# Función principal para ejecutar la aplicación
def main():
    app = QtWidgets.QApplication([])
    ex = App()
    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()

```

Este código muestra cómo se puede decir en voz lo que el usuario escriba, tambien convierte la voz en entradas de texto y tambien de microfono a texto.

## 📋 Metodología de trabajo utilizando Kanban

- **Definición de Tareas**: Se realizó una reunión inicial para identificar las tareas necesarias para el desarrollo del proyecto, como la implementación de la interfaz gráfica, la integración de las bibliotecas de texto a voz y reconocimiento de voz, y la configuración del entorno de desarrollo.
- **Asignación de Tareas y Priorización**: Cada tarea se asignó a un miembro del equipo, considerando las habilidades y disponibilidad de cada uno. Se priorizaron las tareas críticas para el funcionamiento básico del sistema.
- **Seguimiento y Revisión**: Se establecieron reuniones regulares para revisar el progreso de las tareas, identificar posibles obstáculos y ajustar el plan según sea necesario. Se utilizó un tablero Kanban para visualizar el estado de cada tarea.
- **Iteración y Mejora Continua**: Se fomentó la retroalimentación y la iteración en el desarrollo del proyecto. Se realizaron pruebas periódicas para identificar errores y áreas de mejora, y se realizaron ajustes en el código y la funcionalidad.

## 🖥️ Modelado o Sistematización

El desarrollo del sistema se basó en la integración de diferentes componentes para lograr la funcionalidad deseada:

- **Interfaz Gráfica**: Se utilizó PyQt5 para desarrollar una interfaz de usuario intuitiva y fácil de usar.
- **Texto a Voz y Voz a Texto**: Se implementaron las bibliotecas pyttsx3 y SpeechRecognition para permitir la conversión de texto a voz y de voz a texto, respectivamente.
- **Procesamiento de Audio**: Se utilizó el módulo de SpeechRecognition para capturar y procesar audio desde el micrófono del usuario.
- **Funcionalidades Adicionales**: Se añadieron funcionalidades como la capacidad de guardar la salida de texto a voz como archivo de audio y la visualización del texto reconocido en una ventana separada.

## 📊 Conclusiones

El proyecto logró cumplir con los objetivos establecidos al desarrollar un sistema funcional que permite la conversión de texto a voz, voz a texto y de micrófono a texto. La integración de diversas bibliotecas y la implementación de una interfaz gráfica amigable proporcionan una experiencia de usuario satisfactoria. Sin embargo, se identificaron áreas de mejora, como la optimización del reconocimiento de voz en entornos ruidosos y la expansión de las funcionalidades para soportar múltiples idiomas y acentos.

## 📚 Bibliografía

- https://pypi.org/project/pyttsx3/
- https://pypi.org/project/SpeechRecognition/
- https://pypi.org/project/PyQt5/

## 📁 Anexos

- Código Fuente: [GitHub](https://github.com/josegalarza31/conversor)

![Texto alternativo](https://github.com/andresgeecee/Conversor/blob/master/img/Conversor%20-%20Visual%20Studio%20Code.png?raw=true)
