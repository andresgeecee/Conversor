import pyttsx3
import speech_recognition as SR
import time
from PyQt5 import QtWidgets, QtCore

class App(QtWidgets.QMainWindow):
    def __init__(self):
        # inicializa la instancia de la clase base(QtWidgets.QMainWindow)
        super().__init__()

        # Inicialización del motor de texto a voz (TTS)
        self.motor = pyttsx3.init()
        # Obtencion de las voces disponibles
        voces = self.motor.getProperty('voices')
        # Establece la voz predeterminada
        self.motor.setProperty('voice', voces[0].id) 

        # Inicialización del reconocedor de voz
        self.r = SR.Recognizer()
        # Nuevo atributo para la ventana de entrada de voz
        self.voice_window = None  
        # Llama al método para inicializar la interfaz de usuario
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
        self.setProperty('rate',1000)
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
    # Crea una instancia de QApplication para manejar la aplicación PyQt
    app = QtWidgets.QApplication([])
    # Crea una instancia de la aplicación principal (clase App)
    ex = App()
    # Muestra la ventana principal de la aplicación
    ex.show()
    # Ejecuta la aplicación y entra en el bucle de eventos
    app.exec_()
# Verifica si este script se está ejecutando directamente
if __name__ == '__main__':
    # Llama a la función principal para iniciar la aplicación
    main()