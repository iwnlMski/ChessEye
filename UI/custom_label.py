from PyQt6 import QtCore, QtGui, QtWidgets
from const import TILE_SIZE, Color
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag
from typing import Tuple
from PyQt6.QtCore import QObject
import re


class QLabelCustom(QtWidgets.QLabel):
    def __init__(self, parent: QObject, filename: str, objectName: str, geometry: Tuple[int, int, int, int], is_board_tile: bool = True, *args, **kwargs) -> None:
        super().__init__(parent=parent, objectName=objectName, *args, **kwargs)
        self.is_board_tile = is_board_tile
        self.dragged_status = False
        self.bg_color = objectName
        self.setFixedSize(TILE_SIZE, TILE_SIZE)
        self.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.setPixmap(filename)
        self.setGeometry(*geometry)

    def setPixmap(self, filename: str) -> None:
        self.filename = filename
        super().setPixmap(QtGui.QPixmap(filename))

    def mouseMoveEvent(self, e) -> None:
        if e.buttons() != Qt.MouseButtons.LeftButton or "blank" in self.filename:
            return

        self.dragged_status = True

        drag = QDrag(self)
        drag.setMimeData(QMimeData())
        drag.setHotSpot(e.position().toPoint() - self.rect().center())
        drag.exec(Qt.DropActions.MoveAction)

    @property
    def dragged_status(self) -> bool:
        return self._dragged

    @dragged_status.setter
    def dragged_status(self, status: bool) -> None:
        self._dragged = status

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, filename: str) -> None:
        self._filename = filename

    @property
    def bg_color(self) -> str:
        return self._bg_color

    @bg_color.setter
    def bg_color(self, objectName: str) -> None:
        if self.is_board_tile:
            objectName = objectName.replace("board_tile_", "")
            if (ord(objectName[0]) + int(objectName[1])) % 2 == 0:
                self._bg_color = Color.WHITE.value
            else:
                self._bg_color = Color.BLACK.value

            self.update_stylesheet("background-color", self.bg_color)
        else:
            self._bg_color = Color.NOT_SET.value

    def update_stylesheet(self, property: str, value: str) -> None:
        match = re.search(f"{property}: [^;]*;", self.styleSheet())
        if match:
            self.setStyleSheet(self.styleSheet().replace(
                match.group(0), f" {property}: {value};"))
        else:
            self.setStyleSheet(self.styleSheet() + f" {property}: {value};")
