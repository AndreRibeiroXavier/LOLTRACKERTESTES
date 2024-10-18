import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox, QComboBox
from PyQt6.QtGui import QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

# Função simulada para cálculo de probabilidade
def calcular_probabilidade(timex, timey, md):
    return f"Com base nos dados de {timex} e {timey}, a chance do time {timex} vencer é de 55%. O formato é {md}."

# Função chamada quando o botão 'Calcular' é pressionado
def calcular():
    timex = time1_input.text()
    timey = time2_input.text()
    md = tipopartida_combo.currentText()

    if not timex or not timey:
        QMessageBox.warning(janela, "Erro", "Por favor, insira os nomes dos dois times.")
        return

    resultado = calcular_probabilidade(timex, timey, md)
    QMessageBox.information(janela, "Resultado", resultado)

# Inicializando o app e a janela principal
app = QApplication(sys.argv)
janela = QWidget()
janela.resize(500, 600)
janela.setWindowTitle("LOLTRACKER")

# Layout vertical
layout = QVBoxLayout()

# Adicionando o logotipo
logo_label = QLabel()
pixmap = QPixmap("/mnt/data/LOLTRACKER (1).png")  # Caminho para o logotipo
logo_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
layout.addWidget(logo_label)

# Adicionando o título
titulo = QLabel("Bem-vindo ao LolTracker!\nOnde ninguém aposta no escuro...")
titulo.setStyleSheet("color: #00FF00; font-size: 18px; font-weight: bold;")
titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
layout.addWidget(titulo)

# Combobox para selecionar o tipo de partida
tipopartida_combo = QComboBox()
tipopartida_combo.addItems(["Melhor de 3", "Melhor de 5", "Partida única"])
tipopartida_combo.setStyleSheet("background-color: #222222; color: #00FF00;")
layout.addWidget(tipopartida_combo)

# Input do time 1
time1_label = QLabel("Digite o nome do primeiro time:")
time1_label.setStyleSheet("color: #00FF00;")
layout.addWidget(time1_label)

time1_input = QLineEdit()
time1_input.setStyleSheet("background-color: #222222; color: #00FF00;")
layout.addWidget(time1_input)

# Input do time 2
time2_label = QLabel("Digite o nome do segundo time:")
time2_label.setStyleSheet("color: #00FF00;")
layout.addWidget(time2_label)

time2_input = QLineEdit()
time2_input.setStyleSheet("background-color: #222222; color: #00FF00;")
layout.addWidget(time2_input)

# Botão de calcular
calcular_btn = QPushButton("Calcular")
calcular_btn.setStyleSheet("background-color: #00FF00; color: #222222; font-weight: bold;")
calcular_btn.clicked.connect(calcular)  # Conecta o clique do botão à função calcular
layout.addWidget(calcular_btn)

# Configurando o layout e exibindo a janela
janela.setLayout(layout)

# Mudando a cor de fundo da janela
palette = janela.palette()
palette.setColor(QPalette.ColorRole.Window, QColor("#111111"))
janela.setPalette(palette)

janela.show()

# Executando o app
sys.exit(app.exec())
