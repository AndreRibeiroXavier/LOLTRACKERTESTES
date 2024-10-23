import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox, QMessageBox
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

# Lista de times predefinida
lista_times = [
    'Fluxo', 'FURIA', 'INTZ', 'KaBuM', 'Liberty',
    'LOS', 'LOUD', 'Pain Gaming', 'RED Canids', 'Vivo Keyd Stars'
]

# Função simulada para cálculo de probabilidade
def calcular_probabilidade(timex, timey, md):
    return f"Com base nos dados de {timex} e {timey}, a chance do time {timex} vencer é de 55%. O formato é {md}."

# Função chamada quando o botão 'Calcular' é pressionado
def calcular():
    timex = time1_combo.currentText()
    timey = time2_combo.currentText()
    md = tipopartida_combo.currentText()

    if timex == "" or timey == "":
        QMessageBox.warning(janela, "Erro", "Por favor, escolha os dois times.")
        return

    if timex == timey:
        QMessageBox.warning(janela, "Erro", "Os dois times selecionados são iguais. Por favor, escolha times diferentes.")
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

# Combobox para o time 1
time1_label = QLabel("Selecione o primeiro time:")
time1_label.setStyleSheet("color: #00FF00;")
layout.addWidget(time1_label)

time1_combo = QComboBox()
time1_combo.addItems([""] + lista_times)  # Adiciona uma opção vazia
time1_combo.setEditable(False)  # Desabilitar a opção de escrita
time1_combo.setStyleSheet("background-color: #222222; color: #00FF00;")
layout.addWidget(time1_combo)

# Combobox para o time 2
time2_label = QLabel("Selecione o segundo time:")
time2_label.setStyleSheet("color: #00FF00;")
layout.addWidget(time2_label)

time2_combo = QComboBox()
time2_combo.addItems([""] + lista_times)  # Adiciona uma opção vazia
time2_combo.setEditable(False)  # Desabilitar a opção de escrita
time2_combo.setStyleSheet("background-color: #222222; color: #00FF00;")
layout.addWidget(time2_combo)

# Botão de calcular
calcular_btn = QPushButton("Calcular")
calcular_btn.setStyleSheet("background-color: #00FF00; color: #222222; font-weight: bold;")
calcular_btn.clicked.connect(calcular)
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
