'''
Created on 6 de nov de 2016

@author: ze
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import sqlite3
from threading import Thread
import time




try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Riese(QWidget):
   
    
    def __init__(self, parent = None):
        super(Riese, self).__init__(parent)
        layoutPrincipal = QVBoxLayout()
        self.resize(1280,900)
        #########################################################
        
        
        ###################TITULO PRINCIPAL NA JANELA###################
        ################################################################
        newfont = QFont("Times", 70)
        self.titulo= QLabel(self)
        self.titulo.setText("Pedidos")
        self.titulo.setFont(newfont)
        self.titulo.setStyleSheet("QLabel {color:white}")
        fLayout = QFormLayout()
        fLayout.addRow(self.titulo)
        ##################################################################
        
        #################LISTA PRINCIPAL ONDE ARMAZENA TODOS OS LANCHES##############
        #############################################################################
        self.lista= QListWidget()
        a = QFont("Times", 20) 
        self.lista.setFont(a)
        ##############################################################################
        
        ###############################################################################################
        self.btnDEL= QPushButton('Deletar',self)
        self.btnDEL.setObjectName("connect")
        self.connect(self.btnDEL, SIGNAL("clicked()"),self.dele)
        ################################################################################################
        
       
        ################################################################################################
        self.btnCancel= QPushButton('Fechar',self)
        self.btnCancel.setObjectName("connect")
        self.connect(self.btnCancel, SIGNAL("clicked()"),self.close)
        ################################################################################################
        
        
        #################################################################################################
        self.hboxBotoes = QHBoxLayout()
        self.hboxBotoes.addWidget(self.lista)
        self.hboxBotoes.addWidget(self.btnDEL)
        self.hboxBotoes.addWidget(self.btnCancel)
        ##################################################################################################
        
        ########################################ADICIONA OS WIDGET CRIADOS NA JANELA####################################
        layoutPrincipal.addLayout(fLayout)
        layoutPrincipal.addLayout(self.hboxBotoes)
        self.setLayout(layoutPrincipal)
        ############################################################################################################
        
        
        ####################################################PAPEL DE PAREDE###############################
        self.palette    = QPalette()
        self.palette.setBrush(QPalette.Background,QBrush(QPixmap("wpp.jpg")))
        self.setPalette(self.palette)
        ##################################################################################################
        
        ###############################TITULO DA JANELA####################
        self.setWindowTitle("Pedidos")
        #################################################################
        
        #####OBTER INFORMCOES DO BANCO DE DADOS##############
        self.newL = []
        def dados():
            while True:
                time.sleep(3)
                self.conn = sqlite3.connect("pedidos.db")
                self.c = self.conn.cursor()
                self.banc= self.c.execute("SELECT * FROM pedidos")
                self.listas= self.banc.fetchall()
                self.novo=[]
                self.matriz=[]
                for self.lista_feia in self.listas:
                    self.novo=[]
                    for self.agrupamento in self.lista_feia:
                        self.novo.append(self.agrupamento)
                    self.matriz.append(self.novo)
                
                for i in range(len(self.matriz)):
                    if self.matriz[i][0] not in self.newL:#server para nao repetir elementos na lista
                        conta=(-len(self.matriz[i][1])+100)
                        st=" "*conta
                        self.item = QListWidgetItem(self.matriz[i][1]+st+"MESA:"+self.matriz[i][2])
                        self.lista.addItem(self.item)
                        
                for i in range(len(self.matriz)):
                    if self.matriz[i][0] not in self.newL:
                        self.newL.append(self.matriz[i][0])
                        
        ######THREAD######
        
        Thread(target=dados).start()
   
       ######################################################################################################## 
        
    """ deletar elemento da lista"""
    def dele(self):
        for item in self.lista.selectedItems():
            self.lista.takeItem(self.lista.row(item))
            
    

    
if __name__ == '__main__':
    import sys
    root=QApplication(sys.argv)
    app=Riese(None)
    app.show()
    root.exec_()
    
    
