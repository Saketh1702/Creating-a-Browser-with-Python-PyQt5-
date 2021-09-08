# import the necessary libraries
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


# creating main window class
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # creating a QWebEngineview
        self.browser = QWebEngineView()

        # setting default browser url as Google
        self.browser.setUrl(QUrl("http://google.com"))

        # adding action of url getting changed when changed
        self.browser.urlChanged.connect(self.update_urlbar)

        # adding action when loading is finished
        self.browser.loadFinished.connect(self.update_title)

        # setting this browser as central widget or main window
        self.setCentralWidget(self.browser)

        # creating a status bar object
        self.status = QStatusBar()

        # adding statusbar to the main window
        self.setStatusBar(self.status)

        # creating QToolBar for Navigation
        navtb = QToolBar("Navigation")

        # adding this toolbar to the main window
        self.addToolBar(navtb)

        # adding actions to the toolbar
        # creating action for the back button
        back_btn = QAction("Back", self)

        # setting status tip
        back_btn.setStatusTip("Back to the previous page")

        # adding action to the back button
        # making browser go back
        back_btn.triggered.connect(self.browser.back)

        # adding this to the toolbar
        navtb.addAction(back_btn)

        # do similarly for the forward button
        forward_btn = QAction("Forward", self)
        forward_btn.setStatusTip("Forward to next page")

        # adding action to the button
        # making browser go forward
        forward_btn.triggered.connect(self.browser.forward)
        navtb.addAction(forward_btn)

        # similarly for refresh button
        refresh_btn = QAction("Refresh", self)
        refresh_btn.setStatusTip("Refresh page")

        # adding action to the refresh button
        # making browser to refresh
        refresh_btn.triggered.connect(self.browser.reload)
        navtb.addAction(refresh_btn)

        # similarly for home button
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go Home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # adding a seperator in the toolbar
        navtb.addSeparator()

        # creating a line edit for the url
        self.urlbar = QLineEdit()

        # adding action when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding this to the toolbar
        navtb.addWidget(self.urlbar)

        # adding stop action to the toolbar
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")

        # adding action to the stop button
        # making the browser stop
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # showing all the components
        self.show()

    # method for updating the title of the window
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - My Browser" % title)

    # method called by home action
    def navigate_home(self):

        # open the google
        self.browser.setUrl(QUrl("http://www.google.com"))

    # method called by the line edit when return key is passed
    def navigate_to_url(self):

        q = QUrl(self.urlbar.text())

        # if url scheme is blank
        if q.scheme() == "":
            # set url scheme to html
            q.setScheme("http")

        # set the url to the browser
        self.browser.setUrl(q)

    #method for updating url
    #this method is called by the QWebEngineView object
    def update_urlbar(self, q):

        # setting text to the url bar
        self.urlbar.setText(q.toString())

        # setting cursor position of the url bar
        self.urlbar.setCursorPosition(0)

# creating a PyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("My Browser")

# creating a main window object
window = MainWindow()

#loop
app.exec()

