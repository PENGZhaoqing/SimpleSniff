from PyQt4 import QtGui
import pyqt_ui
from PyQt4.QtCore import *
import netifaces
from StringIO import StringIO
from scapy.all import *


class SniffThread(QThread):
    def __init__(self, main_window, pkt_buffer):
        QThread.__init__(self)
        self.mainWindow = main_window
        self.interface = ''
        self.filter_text = ''
        self.buffer = pkt_buffer
        self.stop = False

    def render(self, interface, filter_text):
        self.interface = interface
        self.filter_text = filter_text
        self.start()

    def run(self):
        try:
            self.mainWindow.running_info.setText("Sniffing... by thread No. " + str(self.currentThreadId()))
            sniff(filter=self.filter_text, iface=self.interface, prn=self.print_summary,
                  stop_filter=lambda x: self.stop)
            self.mainWindow.running_info.setText("Ready to sniff")
        except Exception, e:
            self.mainWindow.running_info.setText("Terminated due to Error: " + str(e))

    def halt(self):
        self.stop = True

    def print_summary(self, pkt):
        pkt_list = list(expand(pkt))
        time = datetime.fromtimestamp(pkt.time)
        info = pkt.summary()
        protocol = None
        src = None
        dst = None
        try:
            length = pkt.len
        except:
            length = None
        for i in range(len(pkt_list)):
            # TODO: parse HTTP protocol
            if pkt_list[i].name not in ['Raw', 'Padding']:
                protocol = pkt_list[i].name
            try:
                src = pkt_list[i].src
                dst = pkt_list[i].dst
            except:
                pass
        self.buffer.append(pkt)
        l = [str(time), str(src), str(dst), str(protocol), str(length), str(info)]
        self.emit(SIGNAL("output(PyQt_PyObject)"), l)


class SniffTool(QtGui.QMainWindow, pyqt_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.set_options()
        self.pkt_buffer = []
        self.filter_table.cellClicked.connect(self.show_detail)
        self.filter_table.cellClicked.connect(self.show_hexdump)
        self.filterButton.clicked.connect(self.start_thread)
        self.haltButton.clicked.connect(self.halt_thread)
        self.running_info.setText("Ready to sniff")
        self.thread = None

    def start_thread(self):
        if self.thread is not None and self.thread.isRunning():
            self.running_info.setText('Please wait for the ending of the last thread and Try it again')
        else:
            text = str(self.filterText.text())
            interface = str(self.interface_2.currentText())
            self.pkt_buffer = []
            self.filter_table.setRowCount(0)
            self.detail_widget.clear()
            self.hexdump_list.clear()
            self.thread = SniffThread(self, self.pkt_buffer)
            self.connect(self.thread, SIGNAL("output(PyQt_PyObject)"), self.push_entry)
            self.thread.render(interface=interface, filter_text=text)

    def halt_thread(self):
        self.thread.halt()

    def push_entry(self, l):
        row = self.filter_table.rowCount()
        self.filter_table.insertRow(row)
        if len(self.filter_table.selectedItems()) == 0:
            self.filter_table.scrollToBottom()
        self.filter_table.setItem(row, 0, QtGui.QTableWidgetItem(l[0]))
        self.filter_table.setItem(row, 1, QtGui.QTableWidgetItem(l[1]))
        self.filter_table.setItem(row, 2, QtGui.QTableWidgetItem(l[2]))
        self.filter_table.setItem(row, 3, QtGui.QTableWidgetItem(l[3]))
        self.filter_table.setItem(row, 4, QtGui.QTableWidgetItem(l[4]))
        self.filter_table.setItem(row, 5, QtGui.QTableWidgetItem(l[5]))

    def set_options(self):
        l = netifaces.interfaces()
        self.interface_2.addItems(l)
        header = self.filter_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(5, QtGui.QHeaderView.Stretch)

    def show_detail(self, row, col):
        self.detail_widget.clear()
        self.filter_table.selectRow(row)
        # TODO: custom method to parse pkt
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture
        pkt = self.pkt_buffer[row]
        pkt.show()
        sys.stdout = save_stdout
        text = capture.getvalue().split('\n')
        for line in text:
            self.detail_widget.addItem(line)

    def show_hexdump(self, row, col):
        self.filter_table.selectRow(row)
        self.hexdump_list.clear()
        pkt = self.pkt_buffer[row]
        text = hex_encode(pkt).split('\n')
        for line in text:
            self.hexdump_list.addItem(line)
            # line = str(line).encode("HEX")


def expand(x):
    yield x
    while x.payload:
        x = x.payload
        yield x


def hex_encode(x):
    x = str(x)
    l = len(x)
    i = 0
    result = ""
    while i < l:
        result += str("%04x     " % i)
        for j in xrange(16):
            if i + j < l:
                result += str("%02X  " % ord(x[i + j]))
            else:
                result += "      "
            if j % 16 == 7:
                result += "  "
        result += "    "
        result += sane_color(x[i:i + 16])
        i += 16
        result += '\n'
    return result


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    tool = SniffTool()
    tool.show()
    app.exec_()
