from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys
import string
from lxml import html
from datetime import datetime

import openpyxl

from lib import l

CUTS = ('пгт', 'поселок городского типа',  'посёлок городского типа', 'пос', 'поселение', 'поселок', 'посёлок',
         'п', 'рп', 'рабочий посёлок', 'рабочий поселок', 'кп', 'курортный посёлок', 'курортный поселок', 'пс',
         'сс', 'смн', 'дп', 'дачный поселок', 'дачный посёлок', 'садовое товарищество',
         'садоводческое некоммерческое товарищество', 'садоводческое товарищество', 'снт', 'нп', 'пст', 'ж/д_ст',
         'ж/д ст', 'железнодорожная станция', 'с', 'село', 'м', 'д', 'дер', 'деревня', 'сл', 'ст', 'ст-ца',
         'станица', 'х', 'хут', 'хутор', 'рзд', 'у', 'урочище', 'клх', 'колхоз', 'свх', 'совхоз', 'зим', 'зимовье',
         'микрорайон', 'мкр', 'аллея', 'а', 'бульвар', 'б-р', 'бул', 'в/ч', 'военная часть', 'военный городок',
          'гск', 'гаражно-строительный кооператив', 'гк', 'гаражный кооператив', 'кв-л', 'квартал', 'линия',
         'лин', 'наб', 'набережная', 'переулок', 'пер', 'переезд', 'пл', 'площадь', 'пр-кт', 'пр-т', 'проспект', 'пр',
         'проезд', 'тер', 'терр', 'территория', 'туп', 'тупик', 'ул', 'улица', 'ш', 'шоссе')
STOPWORDS = ('мкр', 'микрорайон', 'область', 'обл', 'район', 'р-н' , 'поселок', 'посёлок', 'город', 'городок',
             'москва', 'московская', 'люберцы', 'реутов', 'апрелевка', 'балашиха', 'бронницы', 'верея', 'видное',
             'Волоколамск', 'Воскресенск', 'Высоковск', 'Голицыно', 'Дедовск', 'Дзержинский', 'Дмитров',
             'долгопрудный', 'домодедово', 'дрезна', 'дубна', 'егорьевск', 'жуковский', 'зарайск', 'звенигород',
             'ивантеевка', 'истра', 'кашира', 'клин', 'коломна', 'королёв', 'котельники', 'красноармейск',
             'красногорск', 'краснозаводск', 'краснознаменск', 'кубинка', 'куровское', 'ликино-дулёво', 'лобня',
             'лосино-петровский', 'луховицы', 'лыткарино', 'люберцы', 'можайск', 'мытищи', 'наро-фоминск', 'ногинск',
             'одинцово', 'озёры', 'орехово-Зуево', 'павловский посад', 'пересвет', 'подольск', 'протвино',
             'пушкино', 'пущино', 'раменское', 'реутов', 'рошаль', 'руза', 'сергиев посад', 'серпухов',
             'солнечногорск', 'старая купавна', 'ступино', 'талдом', 'фрязино', 'химки', 'хотьково',
             'черноголовка', 'чехов', 'шатура', 'щёлково', 'электрогорск', 'электросталь', 'электроугли', 'яхрома',
             'подъезд')


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("MooseAche")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('images', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 1.00"))
        layout.addWidget(QLabel("Copyright 2020 Denis Alekseev"))
        layout.addWidget(QLabel("Copyright 2015 MooseAche Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok"))

        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(QIcon(os.path.join('images', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join('images', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join('images', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(os.path.join('images', 'home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.my_html = ''
        self.browser.loadFinished.connect(self.preview_loaded)
        self.browser.loadProgress.connect(self.preview_loading)

        self.countAvitos = 0
        self.clbPreviewLoading = QAction(QIcon(os.path.join('images', 'avito1.png')), "Check", self)
        self.clbPreviewLoading.setStatusTip(str(self.countAvitos))
        self.clbPreviewLoading.triggered.connect(self.preview_loaded)
        navtb.addAction(self.clbPreviewLoading)

        self.chbSummON = False
        self.clbSumm = QAction(QIcon(os.path.join('images', 'square.png')), "Check", self)
        self.clbSumm.setStatusTip("ON / OFF")
        self.clbSumm.triggered.connect(self.clbSumm_clicked)
        navtb.addAction(self.clbSumm)

        navtb.addSeparator()

        self.httpsicon = QLabel()  # Yes, really!
        self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(QIcon(os.path.join('images', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction(QIcon(os.path.join('images', 'disk--arrow.png')), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        help_menu = self.menuBar().addMenu("&Help")

        about_action = QAction(QIcon(os.path.join('images', 'question.png')), "About MooseAche", self)
        about_action.setStatusTip("Find out more about MooseAche")  # Hungry!
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "MooseAche Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to MooseAche Homepage")
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)
        # ----------
        self.idINfinderS = tuple()
        self.wb = openpyxl.Workbook(write_only=True)
        self.ws = self.wb.create_sheet('Авито')
        self.ws.append(['idINfinder','linkINfinder','address','metro','floor','maxFloor','roomCount','agentComission',
                        'buyerComission','square', 'cost'])
        # ----------
        self.show()

        self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))

    def closeEvent(self, event):
        self.wb.save('avito_' + datetime.now().strftime("%H-%M-%S_%d-%m-%Y") + '.xlsx')
        event.accept()

    def clbSumm_clicked(self):
        self.chbSummON = not self.chbSummON
        if self.chbSummON:
            self.clbSumm.setIcon(QIcon(os.path.join('images', 'chSquare.png')))
        else:
            self.clbSumm.setIcon(QIcon(os.path.join('images', 'square.png')))

    def processHtml(self, html_x):
        self.my_html = str(html_x)
        return

    def preview_loading(self):
        self.clbPreviewLoading.setIcon(QIcon(os.path.join('images','refresh.png')))

    def preview_loaded(self):
        self.clbPreviewLoading.setIcon(QIcon(os.path.join('images','avito1.png')))
        self.browser.page().toHtml(self.processHtml)
        if len(self.my_html) < 1000:
            return
        if self.browser.page().url().toString().find('avito') > -1 and self.chbSummON:
            tree = html.fromstring(self.my_html)
            cards = tree.xpath('//div[@class="item_table-wrapper"]')
            for card in cards:
                linkINfinder, address, metro = '', '', ''
                floor, maxFloor, roomCount, agentComission, buyerComission, idINfinder, cost = 0, 0, 0, 0, 0, 0, 0
                square = 0.0
                for element in card.getiterator():
                    if element.attrib.get('class', None):
                        if 'snippet-link' in str(element.attrib['class']).split():
                            linkINfinder = element.attrib['href']
                            if linkINfinder[:4] != 'http':
                                linkINfinder = 'https://www.avito.ru' + linkINfinder
                            if not str(linkINfinder).strip():
                                continue
                            for i in range(len(linkINfinder) - 1, -1, -1):
                                if linkINfinder[i] not in string.digits:
                                    ch_num = i + 1
                                    break
                            idINfinder = int(linkINfinder[ch_num:])
                            parts = str(element.attrib['title']).split(',')
                            for part in parts:
                                if part.find('/') > -1:
                                    floor = l(part.split('/')[0])
                                    maxFloor = l(part.split('/')[1])
                                elif part.find('²') > -1:
                                    square = l(part)
                                else:
                                    roomCount = l(part)
                        elif 'item-address__string' in str(element.attrib['class']).split():
                            addressStopped = ''
                            for adr in str(element.text).lower().split(','):
                                stopped = False
                                for stopword in STOPWORDS:
                                    if adr.find(stopword) > -1:
                                        stopped = True
                                if not stopped:
                                    addressStopped += ' ' + adr
                            addressList = addressStopped.strip().replace(',', '').replace('.', '') \
                                .replace('  ', ' ').replace('  ', ' ').split(' ')
                            firsts = str(addressList).lower().strip().strip('\n').split(',')
                            if firsts[len(firsts)-1].strip()[0] in string.digits or (firsts[len(firsts)-1].strip()[0]
                                                         == 'к' and firsts[len(firsts)-1].strip()[1] in string.digits):
                                filteredAddres = firsts[len(firsts)-2].strip() + ' ' + firsts[len(firsts)-1].strip()
                            else:
                                filteredAddres = firsts[len(firsts) - 1]
                            addressFine = filteredAddres.replace(',', '').replace('.', '') \
                                .replace('  ', ' ').replace('  ', ' ').strip().strip().split(' ')
                            address = ''
                            addrs = []
                            for adr in addressFine:
                                if adr not in CUTS:
                                    addrs.append(adr)
                            missed = -1
                            for i, addr in enumerate(addrs):
                                if i == 0 and addr[0] in string.digits:
                                    missed = i
                                elif missed > -1 and addr[0] in string.digits:
                                    address += addrs[missed] + ' ' + addr + ' '
                                    missed = -1
                                else:
                                    address += addr + ' '
                            address = address.strip().strip('\n')
                        elif 'snippet-price-commission' in str(element.attrib['class']).split():
                            agentComission = l(element.text)
                            buyerComission = l(element.text)
                        elif 'snippet-price' in str(element.attrib['class']).split():
                            cost = l(element.text)
                        elif 'item-address-georeferences-item__content' in str(element.attrib['class']).split():
                            metro = str(element.text)
                        elif 'item-address-georeferences-item__after' in str(element.attrib['class']).split():
                            metro += ' ' + str(element.text)
                if idINfinder not in self.idINfinderS:
                    self.ws.append([idINfinder, linkINfinder, address, metro, floor, maxFloor, roomCount,
                                agentComission, buyerComission, square, cost])
                    self.idINfinderS += (idINfinder,)
            if self.chbSummON:
                self.clbPreviewLoading.setStatusTip(str(len(self.idINfinderS)))
                self.len_avitos = len(self.idINfinderS)
                self.countAvitos = len(self.idINfinderS)
            return

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - MooseAche" % title)

    def navigate_mozarella(self):
        self.browser.setUrl(QUrl("https://www.udemy.com/522076"))

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            self.browser.setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = self.browser.page().toHtml()
            with open(filename, 'w') as f:
                f.write(html)

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.browser.print_)
        dlg.exec_()

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok"))

    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_urlbar(self, q):

        if q.scheme() == 'https':
            # Secure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-ssl.png')))

        else:
            # Insecure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
app.setApplicationName("MooseAche")
app.setOrganizationName("MooseAche")
app.setOrganizationDomain("MooseAche.org")

window = MainWindow()

app.exec_()
