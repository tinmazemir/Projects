import sys
import sqlite3
import os
import functions as fun
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from InstagramAPI import InstagramAPI

api = InstagramAPI

Followers = []
Following = []
FollowersClean = []
FollowingClean = []
Unfollowers = []
Unfollowing = []

class LoginScreen(QWidget):
   def __init__(self):
      super().__init__()
      Text = QFont("Times",13)
      self.loginButton = QPushButton("Login")
      self.username = QLineEdit()
      self.username.setPlaceholderText("USERNAME")
      self.Pass = QLineEdit()
      self.Pass.setEchoMode(QLineEdit.Password)
      self.Pass.setPlaceholderText("PASSWORD")
      self.instructions = QLabel("Login with Instagram Username and Password")
      self.instructions.setFont(Text)

      vertical = QVBoxLayout()
      vertical.addWidget(self.instructions)
      vertical.addStretch()
      vertical.addWidget(self.username)
      vertical.addWidget(self.Pass)
      vertical.addWidget(self.loginButton)
      vertical.addStretch()
      horizontal = QHBoxLayout()
      horizontal.addStretch()
      horizontal.addLayout(vertical)
      horizontal.addStretch()

      self.loginButton.clicked.connect(self.LoginFunction)
      self.Pass.returnPressed.connect(self.LoginFunction)

      self.setLayout(horizontal)
      self.setWindowTitle("InstagramAPP-Login")
      self.setGeometry(300,300,650,500)
      self.show()

   def LoginFunction(self):
      global api
      api = InstagramAPI(self.username.text(),self.Pass.text())  
      #api = InstagramAPI("tinmazemir","***")
      if(api.login()):
         #print("Login succes!")
         user_id = api.username_id
         global Followers,Following
         Followers = api.getTotalFollowers(user_id)
         Following = api.getTotalFollowings(user_id)
         fun.cleaner(Followers,FollowersClean)
         fun.cleaner(Following,FollowingClean)
         fun.process(Mode="unfollowers",  UNF_For_finder=Unfollowers, Followers_For_finder=FollowersClean, Following_For_finder=FollowingClean,)
         fun.process(Mode="unfollowing",  UNF_For_finder=Unfollowing, Followers_For_finder=FollowersClean, Following_For_finder=FollowingClean)
         self.close()
         self.newPage = ProcessScreen()
      else:
         #print("Can't login!")
         self.again = LoginScreen()
         self.close()

class ProcessScreen(QWidget):
   def __init__(self):
      super().__init__()
      self.Text = QFont("Times",13)
      self.UnfollowersList = QListWidget()
      self.UnfollowingList = QListWidget()
      self.username = QLineEdit()
      self.username.setPlaceholderText("USERNAME")
      self.multiSelectingButton = QPushButton("Multi Selecting")
      self.followButton = QPushButton("Follow")
      self.unfollowButton = QPushButton("Unfollow")
      self.unfollowersText = QLabel("Unfollowers")
      self.unfollowersText.setFont(self.Text)
      self.unfollowingText = QLabel("Fans")
      self.unfollowingText.setFont(self.Text)
      
      for i in Unfollowers:
         self.item = QListWidgetItem(str(i))
         self.UnfollowersList.addItem(self.item)
      for i in Unfollowing:
         self.item = QListWidgetItem(str(i))
         self.UnfollowingList.addItem(self.item)
      
      self.UnfollowersList.itemSelectionChanged.connect(self.ItemSelecting_U)
      self.UnfollowingList.itemSelectionChanged.connect(self.ItemSelecting_F)
      self.unfollowButton.clicked.connect(self.U_ProcessFunction)
      self.followButton.clicked.connect(self.F_ProcessFunction)
      self.multiSelectingButton.clicked.connect(self.OpenMultiSelecting)

      textH = QHBoxLayout()
      textH.addStretch()
      textH.addWidget(self.unfollowersText)
      textH.addStretch()
      textH.addStretch()
      textH.addWidget(self.unfollowingText)
      textH.addStretch()
      textH.addStretch()
      textH.addStretch()
      
      mainH = QHBoxLayout()
      mainH.addWidget(self.UnfollowersList)
      mainH.addWidget(self.UnfollowingList)
   
      addV = QVBoxLayout()
      addV.addWidget(self.multiSelectingButton)
      addV.addStretch()
      addV.addStretch()
      addV.addWidget(self.username)
      addV.addWidget(self.unfollowButton)
      addV.addWidget(self.followButton)
      mainH.addLayout(addV)

      mainV = QVBoxLayout()
      mainV.addLayout(textH)
      mainV.addLayout(mainH) 
      
      self.setLayout(mainV)
      self.setWindowTitle("InstagramAPP")
      self.setGeometry(300,300,650,500)
      self.show()

   def U_ProcessFunction(self):
      if(self.username.text() not in Unfollowers):
         error = QMessageBox()
         error.setText("No such user was found")
         error.setWindowTitle("Error")
         error.setIcon(QMessageBox.Warning)
         error.show()
         QTest.qWait(2500)
      else:
         for i in Following:  
            if(self.username.text() == i["username"]):
               self.userid = i["pk"]
               api.unfollow(self.userid)
               Unfollowers.remove(self.username.text())
               self.refresh = ProcessScreen()
               self.close()
   def F_ProcessFunction(self):
      if(self.username.text() not in Unfollowing):
         error = QMessageBox()
         error.setText("No such user was found")
         error.setWindowTitle("Error")
         error.setIcon(QMessageBox.Warning)
         error.show()
         QTest.qWait(2500)
      else:
         for i in Followers:
            if(self.username.text() == i["username"]):
               self.userid = i["pk"]
               api.follow(self.userid)
               Unfollowing.remove(self.username.text())
               self.refresh = ProcessScreen()
               self.close() 
   def ItemSelecting_U(self):
      for item in self.UnfollowersList.selectedItems():
         self.username.setText(item.text())
         break
   def ItemSelecting_F(self):
      for item in self.UnfollowingList.selectedItems():
         self.username.setText(item.text())
         break
   def OpenMultiSelecting(self):
      self.refresh = MultiSelecting()
      self.close()

class MultiSelecting(QWidget):
   def __init__(self):
      super().__init__()
      self.Text = QFont("Times",13)
      self.UnfollowersList = QListWidget()
      self.UnfollowingList = QListWidget()
      self.UnfollowersList.setSelectionMode(QListWidget.MultiSelection)
      self.UnfollowingList.setSelectionMode(QListWidget.MultiSelection)
      self.SingleSelectingButton = QPushButton("Single Selecting")
      self.UnfollowButton = QPushButton("Unfollow Selection All")
      self.FollowButton = QPushButton("Follow Selection All")
      self.unfollowersText = QLabel("Unfollowers")
      self.unfollowersText.setFont(self.Text)
      self.unfollowingText = QLabel("Fans")
      self.unfollowingText.setFont(self.Text)

      for i in Unfollowers:
         self.item = QListWidgetItem(str(i))
         self.UnfollowersList.addItem(self.item)
      for i in Unfollowing:
         self.item = QListWidgetItem(str(i))
         self.UnfollowingList.addItem(self.item)
      
      self.SingleSelectingButton.clicked.connect(self.OpenSingleSelecting)
      self.UnfollowButton.clicked.connect(self.U_ProcessFunction)
      self.FollowButton.clicked.connect(self.F_ProcessFunction)

      textH = QHBoxLayout()
      textH.addStretch()
      textH.addWidget(self.unfollowersText)
      textH.addStretch()
      textH.addStretch()
      textH.addWidget(self.unfollowingText)
      textH.addStretch()
      textH.addStretch()
      textH.addStretch()
      
      mainH = QHBoxLayout()
      mainH.addWidget(self.UnfollowersList)
      mainH.addWidget(self.UnfollowingList)
      addV = QVBoxLayout()
      addV.addWidget(self.SingleSelectingButton)
      addV.addStretch()
      addV.addWidget(self.UnfollowButton)
      addV.addWidget(self.FollowButton)
   
      mainH.addLayout(addV)
      mainV = QVBoxLayout()
      mainV.addLayout(textH)
      mainV.addLayout(mainH) 
      self.setLayout(mainV)
      self.setWindowTitle("InstagramAPP")
      self.setGeometry(300,300,650,500)
      self.show()

   def U_ProcessFunction(self):
      if(len(self.UnfollowersList.selectedItems()) <= 0):
         error = QMessageBox()
         error.setText("No such selected user was found from 'Unfollowers'")
         error.setWindowTitle("Error")
         error.setIcon(QMessageBox.Warning)
         error.show()
         QTest.qWait(2500)
      else:
         for item in self.UnfollowersList.selectedItems():
            for i in Following:
               if(item.text() == i["username"]):
                  self.userid = i["pk"]
                  api.unfollow(self.userid)
                  Unfollowers.remove(item.text())
         self.refresh = MultiSelecting()
         self.close()          
   def F_ProcessFunction(self):
      if(len(self.UnfollowingList.selectedItems()) <= 0):
         error = QMessageBox()
         error.setText("No such selected user was found from 'Fans'")
         error.setWindowTitle("Error")
         error.setIcon(QMessageBox.Warning)
         error.show()
         QTest.qWait(2500)
      else:
         for item in self.UnfollowingList.selectedItems():
           for i in Followers:
               if(item.text() == i["username"]):
                  self.userid = i["pk"]
                  api.follow(self.userid)
                  Unfollowing.remove(item.text())
         self.refresh = MultiSelecting()
         self.close()    
   def OpenSingleSelecting(self):
      self.refresh = ProcessScreen()
      self.close()

def ScreenMain():
   app = QApplication(sys.argv)
   app.setStyle('Fusion')
   
   dark_palette = QPalette()
   dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
   dark_palette.setColor(QPalette.WindowText, Qt.white)
   dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
   dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
   dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
   dark_palette.setColor(QPalette.ToolTipText, Qt.white)
   dark_palette.setColor(QPalette.Text, Qt.white)
   dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
   dark_palette.setColor(QPalette.ButtonText, Qt.white)
   dark_palette.setColor(QPalette.BrightText, Qt.red)
   dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
   dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
   dark_palette.setColor(QPalette.HighlightedText, Qt.black)
   app.setPalette(dark_palette)
   
   screen = LoginScreen()
   sys.exit(app.exec_())

ScreenMain()
