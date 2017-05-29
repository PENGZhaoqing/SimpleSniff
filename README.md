# SimpleSniff

A very simple sniff tool implementation with the same basic function of wireshark by pyqt4 and scapy. 

## Prerequisite

Install the following libs first:

* pyqt4
* scapy
* qt designer(optimal)

## Usage:

```
git clone https://github.com/PENGZhaoqing/SimpleSniff
cd SimpleSniff
sudo python simple_sniff.py
```

**Note** : because scapy requires sudo prevelige to sniff the package from the network interface, so we use `sudo` to execute

### For developement tips

You can use [qt designer](http://doc.qt.io/qt-4.8/designer-manual.html) to design the UI and use the followings command to convert ui file directly to python file, which can be imported in `simple_sniff.py`  as module

```
pyuic4 pyqt.ui -o pyqt_ui.py
```

Here we give the `pyqt.ui` file

### Todo list

1. Parse more protocol like HTTP
2. Improve thread management
3. Add database support
4. Custom the extract method of package

## Demo

![demo](demo.gif)

If you like, please star it!!!
Welcome comtributors

## ScreenShot

<img src="screenshoot.png">
