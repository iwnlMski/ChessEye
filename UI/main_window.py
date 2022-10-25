from PyQt6 import QtGui, QtWidgets
from const import DEFAULT_BOARD_IMAGES, TILE_SIZE
from PyQt6.QtCore import Qt, QRect
from custom_label import QLabelCustom
from helper_functions import LabelHelperFunctions
from board_state import BoardState


class QPushButtonCustom(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        
        return super().mousePressEvent(event)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setObjectName("MainWindow")
        self.resize(700, 700)
        self.setAcceptDrops(True)

        self.centralwidget = QtWidgets.QWidget(self, objectName="centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.pushButton = QPushButtonCustom(self.centralwidget)
        self.pushButton.setGeometry(QRect(500, 170, 75, 24))
        self.pushButton.setObjectName("pushButton")

        for i in range(8, 0, -1):
            for char in range(ord("A"), ord("I")):
                _ = QLabelCustom(
                    parent=self.centralwidget,
                    filename=DEFAULT_BOARD_IMAGES.get(f"{chr(char)}{i}", ""),
                    objectName=f"label_{chr(char)}{i}",
                    geometry=((char-ord("A"))*TILE_SIZE, (i-1)*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    )

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        event.accept()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        drop_position_label = LabelHelperFunctions.get_label_by_position(event.position().x(), event.position().y(), self.centralwidget.children())
        dragged_label = LabelHelperFunctions.get_label_by_dragged_status(self.centralwidget.children())

        if drop_position_label and dragged_label:
            LabelHelperFunctions.swap_two_labels(drop_position_label, dragged_label)
            
            event.setDropAction(Qt.DropActions.MoveAction)
            event.accept()

    def get_board_state(self):
        bs = BoardState(self.centralWidget().children())

        print(bs.to_json())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    MainWindow.get_board_state()
    sys.exit(app.exec())
