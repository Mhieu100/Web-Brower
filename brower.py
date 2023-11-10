import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.setGeometry(100, 100, 800, 600)

        self.browser_tabs = QTabWidget()
        self.browser_tabs.setTabsClosable(True)
        self.browser_tabs.tabCloseRequested.connect(self.close_tab)

        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.search_bar = QToolBar()  # Thanh tìm kiếm

        

        

        self.new_tab_button = QAction(QIcon("add.png"), "New Tab", self)
        self.new_tab_button.triggered.connect(self.add_new_tab)
        self.new_tab_button.triggered.connect(lambda: self.load_url("https://google.com"))
        self.search_bar.addAction(self.new_tab_button)

        self.search_bar.addWidget(self.url_bar)

        self.google_search = QAction(QIcon("search.png"), "Google Search", self)
        self.google_search.triggered.connect(self.search_google)
        self.search_bar.addAction(self.google_search)

        
        self.nav_bar = QToolBar()  # Thanh toolbar thứ hai
        self.gmail_button = QAction(QIcon("gmail.png"), "Gmail", self)
        self.gmail_button.triggered.connect(lambda: self.load_url("https://mail.google.com"))
        

        self.youtube_button = QAction(QIcon("youtube.png"), "YouTube", self)
        self.youtube_button.triggered.connect(lambda: self.load_url("https://www.youtube.com"))
       

        self.facebook_button = QAction(QIcon("facebook.png"), "Facebook", self)
        self.facebook_button.triggered.connect(lambda: self.load_url("https://www.facebook.com"))
      

        self.nav_bar.addAction(self.gmail_button)
        self.nav_bar.addSeparator()
        self.nav_bar.addAction(self.youtube_button)
        self.nav_bar.addSeparator()
        self.nav_bar.addAction(self.facebook_button)
        

        self.central_layout.addWidget(self.search_bar)
        self.central_layout.addWidget(self.nav_bar)
        self.central_layout.addWidget(self.browser_tabs)

        self.setCentralWidget(self.central_widget)

        self.add_new_tab(QUrl("https://www.google.com"), "Homepage")

    def add_new_tab(self, url=None, label="Blank"):
        browser = QWebEngineView()
        index = self.browser_tabs.addTab(browser, label)
        self.browser_tabs.setCurrentIndex(index)
        if url:
            browser.setUrl(url)

    def close_tab(self, index):
        if self.browser_tabs.count() > 1:
            widget = self.browser_tabs.widget(index)
            widget.deleteLater()
            self.browser_tabs.removeTab(index)

    def navigate_to_url(self):
        text = self.url_bar.text()
        if not text.startswith("http://") and not text.startswith("https://"):
            text = "http://" + text
        qurl = QUrl(text)
        if qurl.isValid():
            self.browser_tabs.currentWidget().setUrl(qurl)

    def search_google(self):
        search_text = self.url_bar.text()
        self.load_url(f"https://www.google.com/search?q={search_text}")

    def load_url(self, url):
        self.url_bar.setText(url)
        self.navigate_to_url()

   
def main():
    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
