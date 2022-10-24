from PyQt6 import QtCore, QtGui, QtWidgets
from const import TILE_SIZE, Color
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag
from typing import Tuple
from PyQt6.QtCore import QObject
import re

class QLabelCustom(QtWidgets.QLabel):
    def __init__(self, parent: QObject, filename: str, objectName: str, geometry: Tuple[int, int, int, int], *args, **kwargs) -> None:
        super().__init__(parent=parent, objectName=objectName, *args, **kwargs)
        self.set_dragged_status(False)
        self.set_bg_color()
        self.setFixedSize(TILE_SIZE, TILE_SIZE)
        self.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.setPixmap(filename)
        self.setGeometry(*geometry)

    def setPixmap(self, filename: str) -> None:
        self.set_filename(filename)
        super().setPixmap(QtGui.QPixmap(filename))

    def mouseMoveEvent(self, e) -> None:
        if e.buttons() != Qt.MouseButtons.LeftButton or "blank" in self.get_filename():
            return

        self.set_dragged_status(True)

        drag = QDrag(self)
        drag.setMimeData(QMimeData())
        drag.setHotSpot(e.position().toPoint() - self.rect().center())
        drag.exec(Qt.DropActions.MoveAction)

    def set_dragged_status(self, status: bool) -> None:
        self.__dragged = status

    def get_dragged_status(self) -> bool:
        return self.__dragged
    
    def get_filename(self) -> str:
        return self.__filename
    
    def set_filename(self, filename: str) -> None:
        self.__filename = filename

    def set_bg_color(self) -> None:
        objectName = self.objectName().replace("label_", "")
        if (ord(objectName[0]) + int(objectName[1])) % 2 == 0:
            self.__bg_color = Color.WHITE.value
        else:
            self.__bg_color = Color.BLACK.value

        self.update_stylesheet("background-color", self.get_bg_color())
    
    def get_bg_color(self) -> str:
        return self.__bg_color
    
    def update_stylesheet(self, property: str, value: str) -> None:
        match = re.search(f"{property}: [^;]*;", self.styleSheet())
        if match:
            self.setStyleSheet(self.styleSheet().replace(match.group(0), f" {property}: {value};"))
        else:
            self.setStyleSheet(self.styleSheet() + f" {property}: {value};")
        