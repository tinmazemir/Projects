import sys
import sqlite3
import os
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


baglanti = sqlite3.connect("DATA.db")
arac = baglanti.cursor()
app = QApplication(sys.argv)

class Giris_screen(QWidget):
   def __init__(self):
      super().__init__()
      signal = pyqtSignal()
      self.button_kayit = QPushButton("Kayit Ol")
      self.button_giris = QPushButton("Giris")
      self.button_cikis = QPushButton("X")
      self.kullanici_adi = QLineEdit()
      self.kullanici_adi.setPlaceholderText("KULLANICI ADI")
      self.sifre = QLineEdit()
      self.sifre.setEchoMode(QLineEdit.Password)
      self.sifre.setPlaceholderText("SIFRE")


      cikis_kismi = QHBoxLayout()
      cikis_kismi.addStretch()
      cikis_kismi.addWidget(self.button_cikis)
      cikis_kismi.addStretch()

      dik = QVBoxLayout()
      dik.addLayout(cikis_kismi)
      dik.addStretch()
      dik.addStretch()

      dikey = QVBoxLayout()
      dikey.addStretch()
      dikey.addWidget(self.kullanici_adi)
      dikey.addWidget(self.sifre)
      dikey.addWidget(self.button_giris)
      dikey.addWidget(self.button_kayit)
      dikey.addStretch()


      yatay = QHBoxLayout()
      yatay.addStretch()
      yatay.addLayout(dikey)
      yatay.addStretch()
      yatay.addLayout(dik)

      self.button_giris.clicked.connect(self.kontrol)
      #self.button_giris.pressed(()).connect(self.kontrol)
      self.button_kayit.clicked.connect(self.kayit_user)
      self.button_cikis.clicked.connect(self.cikis_founction)

      self.setLayout(yatay)
      self.setWindowTitle("GIRIS")
      self.setGeometry(300,300,650,500)
      self.show()



   def cikis_founction(self):
      self.close()
   def kontrol(self):
      durum = 1
      user =  self.kullanici_adi.text()
      passw = self.sifre.text()
      kullanici_list = []
      pass_list = []
      kullanicilar = arac.execute("SELECT * from  users")
      for i in kullanicilar:
         for x in i:
            if(durum == 1):
               kullanici_list.append(x)
               durum = 0
            else:
               pass_list.append(x)
               durum = 1
      if(user not in kullanici_list):
         error = QMessageBox()
         error.setIcon(QMessageBox.Warning)
         error.setWindowTitle("HATA")
         error.setText("Boyle bir kullanici bulunamadi")
         error.show()
         QTest.qWait(2500)
         self.close()
         self.yenileme = Giris_screen()

      for i in range(len(kullanici_list)):
         if(user == kullanici_list[i]):
            if(passw == pass_list[i]):
               onay = QMessageBox()
               onay.setText("GIRIS BASARILI")
               onay.setWindowTitle("ONAY")
               onay.show()
               QTest.qWait(1000)
               onay.close()
               self.ekran = Ana_screen()
               self.close()
            else:
               error = QMessageBox()
               error.setText("Boyle bir kullanici bulunamadi")
               error.setWindowTitle("HATA")
               error.setIcon(QMessageBox.Warning)
               error.show()
               QTest.qWait(2500)
               self.close()
               self.yenileme = Giris_screen()
   def kayit_user(self):
      self.kayit = kayit_ekrani()
   def keyPressEvent(self,event):
        if event.key() == Qt.Key_Escape:
            self.close()
class kayit_ekrani(QWidget):
   def __init__(self):
      super().__init__()
      self.button_kayit = QPushButton("Kayit")
      self.kullanici_adi = QLineEdit()
      self.kullanici_adi.setPlaceholderText("KULLANICI ADI")
      self.sifre = QLineEdit()
      self.sifre.setEchoMode(QLineEdit.Password)
      self.sifre.setPlaceholderText("SIFRE")


      dikey = QVBoxLayout()
      dikey.addStretch()
      dikey.addWidget(self.kullanici_adi)
      dikey.addWidget(self.sifre)
      dikey.addWidget(self.button_kayit)
      dikey.addStretch()

      yatay = QHBoxLayout()
      yatay.addStretch()
      yatay.addLayout(dikey)
      yatay.addStretch()

      self.button_kayit.clicked.connect(self.kayit_kesin)

      self.setLayout(yatay)
      self.setWindowTitle("KAYIT")
      self.setGeometry(400,400,350,200)
      self.show()

   def kayit_kesin(self):
      ad = self.kullanici_adi.text()
      pas = self.sifre.text()
      arac.execute("INSERT INTO users (user_name,password) VALUES (?,?)",(ad,pas))
      baglanti.commit()
      self.close()
      def keyPressEvent(self,event):
           if event.key() == Qt.Key_Escape:
               self.close()
class Ana_screen(QWidget):
   def __init__(self):
      super().__init__()
      font_1 = QFont("Algerian",21)
      self.karsilama = QLabel()
      self.karsilama.setText("Hosgeldiniz Bu Bir Sifreleme Uygulamasidir")
      self.url  = QLabel()
      self.karsilama.setFont(font_1)

      self.data_text = QLineEdit()
      self.data_text.setPlaceholderText("METNI GIRINIZ")


      self.button_1 = QPushButton("SIFRELE/SIFRE COZ")
      self.button_gozat = QPushButton("DOSYA BUL")

      ana_yatay = QVBoxLayout()
      textler = QVBoxLayout()
      butonlar = QVBoxLayout()
      butonlar_kucultme = QHBoxLayout()
      logo_bosluk = QVBoxLayout()
      logo_bosluk.addStretch()

      butonlar_kucultme_bosluk  = QHBoxLayout()
      butonlar_kucultme_bosluk.addStretch()
      butonlar_kucultme_bosluk_2  = QHBoxLayout()
      butonlar_kucultme_bosluk_2.addStretch()

      butonlar.addStretch()
      butonlar.addWidget(self.button_1)
      butonlar.addStretch()
      butonlar.addWidget(self.url)
      butonlar.addWidget(self.button_gozat)
      butonlar.addStretch()

      textler.addStretch()
      textler.addWidget(self.karsilama)
      textler.addStretch()
      textler.addWidget(self.data_text)

      butonlar_kucultme.addLayout(butonlar_kucultme_bosluk)
      butonlar_kucultme.addLayout(butonlar)
      butonlar_kucultme.addLayout(butonlar_kucultme_bosluk_2)

      ana_yatay.addLayout(textler)
      ana_yatay.addLayout(butonlar_kucultme)

      self.button_1.clicked.connect(self.c_gecis)
      self.button_gozat.clicked.connect(self.dosya_bul_click)


      self.setLayout(ana_yatay)
      self.setWindowTitle("SIFRELEME")
      self.setGeometry(300,300,650,500)
      self.show()

   def c_gecis(self):
      sifrelenecek = open("sifrelenecek.txt","w")
      data = self.data_text.text()
      sifrelenecek.write(data)
      sifrelenecek.close()
      os.startfile("c_source.exe")
      QTest.qWait(1780)
      self.sifreleme = Sifreleme_screen()
      self.close()

   def dosya_bul_click(self):
      dosyaUrl = QFileDialog.getOpenFileName(self,"Lütfen bir dosya seçiniz")
      self.url.setText(str(dosyaUrl[0])) #urleyi ekrana yazdirmak icin
      text_point = open(dosyaUrl[0],"r")
      data = text_point.read()
      self.data_text.setText(data)
   def keyPressEvent(self,event):
        if event.key() == Qt.Key_Escape:
            self.close()
class Sifreleme_screen(QWidget):
      def __init__(self):
         super().__init__()
         font_1 = QFont("Algerian",21)
         font_2 = QFont("Times",16)
         self.karsilama = QLabel()
         self.kapat = QPushButton("KAPAT")
         self.geri = QPushButton("<")
         self.farkli_kaydet = QPushButton("Farkli kaydet")

         self.karsilama.setFont(font_1)
         self.Metin = QTextEdit()
         self.Metin.setFont(font_2)

         sifrelenmis = open("sifrelenmis.txt","r")
         global data_text
         data_text = sifrelenmis.read()
         self.Metin.setText(data_text)
         sifrelenmis.close()
         #os.remove("sifrelenmis.txt")

         self.kapat.clicked.connect(self.cikis_founction)
         self.geri.clicked.connect(self.geri_founction)
         self.farkli_kaydet.clicked.connect(self.kayit_founction)

         ana_dikey = QHBoxLayout()
         button_yatay = QVBoxLayout()
         metin_yatay = QVBoxLayout()

         metin_yatay.addWidget(self.karsilama)
         metin_yatay.addStretch()
         metin_yatay.addWidget(self.Metin)
         metin_yatay.addStretch()
         metin_yatay.addWidget(self.farkli_kaydet)

         button_yatay.addWidget(self.kapat)
         button_yatay.addWidget(self.geri)
         button_yatay.addStretch()
         button_yatay.addStretch()

         ana_dikey.addLayout(metin_yatay)
         ana_dikey.addLayout(button_yatay)

         self.setLayout(ana_dikey)
         self.setWindowTitle("SIFRELEME")
         self.setGeometry(300,300,650,500)
         self.show()

      def cikis_founction(self):
         self.close()
      def geri_founction(self):
         self.geri  = Ana_screen()
         self.close()
      def kayit_founction(self):
         kayit_adresi =  QFileDialog.getSaveFileName(self,"Lutfen bir adres secin")
         #print(kayit_adresi)
         #print(data_text)
         text_farkli_kaydet = open(kayit_adresi[0],"w")
         text_farkli_kaydet.write(data_text)
         text_farkli_kaydet.close()
         self.close()
      def keyPressEvent(self,event):
           if event.key() == Qt.Key_Escape:
               self.close()

deneme = Giris_screen()
sys.exit(app.exec_())
