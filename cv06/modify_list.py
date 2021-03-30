from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl, QAbstractListModel, QByteArray
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2 import QtCore
from PySide2.QtNetwork import QSslSocket

import typing
from PySide2.QtPositioning import QGeoCoordinate
import sys
import json
from enum import Enum

VIEW_URL = "view.qml"  


class NumberListModel(QAbstractListModel):
    def __init__(self,filename=None):
        """Initialize and load list from given file"""
        QAbstractListModel.__init__(self)
        self.number_list = [1,2,3,4]

    def rowCount(self, parent:QtCore.QModelIndex=...) -> int:
        """ Return number of cities in the list"""
        return len(self.number_list)

    def data(self, index:QtCore.QModelIndex, role:int=...) -> typing.Any:
        """ For given index and DisplayRole return name of the selected city"""
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole:
            return self.number_list[index.row()]
    
    @Slot()
    # Add element to the list and inform QML about it
    # This way of the implementation is big performance issue, but it is easiest to implement
    # and universal for any change in the list
    def add_num(self):
        print("Add num")
        # Inform QML that all elements will be removed
        self.beginRemoveRows(self.index(0).parent(),0, len(self.number_list)-1)
        # Save list to temporary variable and clear the model list
        tmplist = self.number_list
        self.number_list = []
        # Inform QML that all elements were removed
        self.endRemoveRows()

        # Here will QML refresh GUI

        # Inform QML that we will add new elements
        self.beginInsertRows(self.index(0).parent(),0,len(tmplist))
        # Restore list and modify it
        self.number_list = tmplist
        self.number_list.append(6)
        # Inform QML that the elements were added
        self.endInsertRows()

        # Here will QML refresh GUI

    @Slot()
    # Add element to the list and inform QML about it
    # This way of the implementation is big performance issue, but it is easiest to implement
    # and universal for any change in the list
    def del_num(self):
        self.beginRemoveRows(self.index(0).parent(),0, len(self.number_list)-1)
        tmplist = self.number_list
        self.number_list = []
        self.endRemoveRows()

        self.beginInsertRows(self.index(0).parent(),0,len(tmplist)-2)
        self.number_list = tmplist
        self.number_list.pop()
        self.endInsertRows()
        print("Del num")

app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
numberlist_model = NumberListModel()
ctxt = view.rootContext()
ctxt.setContextProperty('numberListModel',numberlist_model)
view.setSource(url)
view.show()
app.exec_()
