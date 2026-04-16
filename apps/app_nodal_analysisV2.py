import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QDoubleSpinBox, QGroupBox, 
                             QFormLayout, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap

# --- FUNÇÃO PARA COMPATIBILIDADE COM PYINSTALLER ---
def resource_path(relative_path):
    """ Obtém o caminho absoluto para os recursos, necessário para o .exe """
    try:
        # O PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class CalculadoraCircuito(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("⚡ Análise de Supernó - Problema 3.3 (Sadiku)")
        self.setMinimumSize(1000, 600)
        self.setStyleSheet("QMainWindow { background-color: #f5f5f5; }")

        # Widget Principal
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout_principal = QHBoxLayout(self.main_widget)

        self.init_sidebar()
        self.init_conteudo_principal()
        
        # Cálculo inicial
        self.calcular()

    def init_sidebar(self):
        """Painel Lateral de Entradas"""
        sidebar_layout = QVBoxLayout()
        group_box = QGroupBox("🔧 Parâmetros do Circuito")
        group_box.setStyleSheet("QGroupBox { font-weight: bold; border: 1px solid gray; margin-top: 10px; }")
        
        form_layout = QFormLayout()

        # Inputs de Tensão
        self.v_fonte_1 = self.criar_input(14.0)
        self.v_superno = self.criar_input(6.0)
        
        # Inputs de Resistência
        self.r1 = self.criar_input(4.0)
        self.r2 = self.criar_input(3.0)
        self.r3 = self.criar_input(2.0)
        self.r4 = self.criar_input(6.0)

        form_layout.addRow("Fonte Esquerda (V):", self.v_fonte_1)
        form_layout.addRow("Fonte Supernó (V):", self.v_superno)
        
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        form_layout.addRow(line)

        form_layout.addRow("Resistor R1 (Ω):", self.r1)
        form_layout.addRow("Resistor R2 (Ω):", self.r2)
        form_layout.addRow("Resistor R3 (Ω):", self.r3)
        form_layout.addRow("Resistor R4 (Ω):", self.r4)

        group_box.setLayout(form_layout)
        sidebar_layout.addWidget(group_box)
        sidebar_layout.addStretch()
        
        self.layout_principal.addLayout(sidebar_layout, 1)

    def init_conteudo_principal(self):
        """Área de Imagem e Display de Resultados"""
        conteudo = QVBoxLayout()

        # Carregamento da Imagem usando resource_path
        self.label_imagem = QLabel()
        caminho_imagem = resource_path("images/nodal.png")
        pixmap = QPixmap(caminho_imagem)
        
        if not pixmap.isNull():
            self.label_imagem.setPixmap(pixmap.scaled(600, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            self.label_imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            self.label_imagem.setText(f"⚠️ Erro: Imagem não encontrada em:\n{caminho_imagem}")
            self.label_imagem.setStyleSheet("color: red; font-weight: bold;")
            self.label_imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        conteudo.addWidget(self.label_imagem)

        # Painel de Resultados
        self.group_resultados = QGroupBox("📊 Resultados da Análise")
        res_layout = QVBoxLayout()
        
        self.label_v = QLabel("Tensão v: ---")
        self.label_i = QLabel("Corrente i: ---")
        self.label_v2 = QLabel("Nó v2: ---")
        
        fonte_grande = QFont("Segoe UI", 16, QFont.Weight.Bold)
        for lbl in [self.label_v, self.label_i]:
            lbl.setFont(fonte_grande)
            lbl.setStyleSheet("color: #1A5276;")
            res_layout.addWidget(lbl)
            
        self.label_v2.setStyleSheet("color: #566573; font-size: 14px;")
        res_layout.addWidget(self.label_v2)
        
        self.group_resultados.setLayout(res_layout)
        conteudo.addWidget(self.group_resultados)
        
        self.layout_principal.addLayout(conteudo, 2)

    def criar_input(self, valor_inicial):
        sb = QDoubleSpinBox()
        sb.setRange(0.01, 9999.0)
        sb.setValue(valor_inicial)
        sb.setSuffix(" Ω" if valor_inicial < 10 else " V")
        sb.valueChanged.connect(self.calcular)
        return sb

    def calcular(self):
        try:
            # g = 1/R (Condutância)
            g1, g2, g3, g4 = 1/self.r1.value(), 1/self.r2.value(), 1/self.r3.value(), 1/self.r4.value()
            v_f1, v_sn = self.v_fonte_1.value(), self.v_superno.value()

            # Equação do Supernó: v * (g1+g2+g3+g4) = v_f1*g1 - v_sn*(g3+g4)
            v_resultado = (v_f1 * g1 - v_sn * (g3 + g4)) / (g1 + g2 + g3 + g4)
            v2 = v_resultado + v_sn
            i_resultado = v2 / self.r3.value()

            self.label_v.setText(f"Tensão v: {v_resultado:.3f} V")
            self.label_i.setText(f"Corrente i: {i_resultado:.3f} A")
            self.label_v2.setText(f"Potencial no segundo nó (v2): {v2:.3f} V")
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Estilo moderno para a interface
    app.setStyle("Fusion") 
    window = CalculadoraCircuito()
    window.show()
    sys.exit(app.exec())