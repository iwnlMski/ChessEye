from PyQt6 import QtGui, QtWidgets
from const import DEFAULT_BOARD_IMAGES, TILE_SIZE, PieceImage, LabelType
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

        self.centralwidget = QtWidgets.QWidget(
            self, objectName="centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.pushButton = QPushButtonCustom(self.centralwidget)
        self.pushButton.setGeometry(QRect(500, 170, 75, 24))
        self.pushButton.setObjectName("pushButton")

        self.set_up_board_tiles()
        self.set_up_side_stacks()

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        event.accept()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        widget_list = self.centralWidget().children()
        dragged_piece = LabelHelperFunctions.get_label_by_dragged_status(
            widget_list)
        new_board_tile = LabelHelperFunctions.get_board_tile_from_position(
            event.position().x(), event.position().y(), widget_list)

        if not dragged_piece:
            return

        if new_board_tile:
            if LabelType.TILE.value in dragged_piece.objectName():
                if dragged_piece.piece_color != new_board_tile.piece_color:
                    LabelHelperFunctions.update_piece_stack(
                        new_board_tile, widget_list)
                    LabelHelperFunctions.delete_piece_from_board(
                        new_board_tile)
                LabelHelperFunctions.swap_two_labels(
                    dragged_piece, new_board_tile)

            elif LabelType.STACK_PIECE.value in dragged_piece.objectName():
                if new_board_tile.filename:
                    LabelHelperFunctions.update_piece_stack(
                        new_board_tile, widget_list)
                    LabelHelperFunctions.delete_piece_from_board(
                        new_board_tile)
                LabelHelperFunctions.add_piece_from_stack(
                    dragged_piece, new_board_tile, widget_list)

        elif not new_board_tile:
            if LabelType.TILE.value in dragged_piece.objectName():
                LabelHelperFunctions.update_piece_stack(
                    dragged_piece, widget_list)
                LabelHelperFunctions.delete_piece_from_board(dragged_piece)

        event.setDropAction(Qt.DropActions.MoveAction)
        event.accept()

    def set_up_board_tiles(self):
        for i in range(8, 0, -1):
            for char in range(ord("A"), ord("I")):
                QLabelCustom(
                    parent=self.centralwidget,
                    filename=DEFAULT_BOARD_IMAGES.get(
                        f"{chr(char)}{i}", ""),
                    objectName=f"{LabelType.TILE.value}{chr(char)}{i}",
                    geometry=((char-ord("A"))*TILE_SIZE, (i-1)
                              * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )

    def set_up_side_stacks(self):
        for i, piece in enumerate(PieceImage):
            x_coord = 500 if "WHITE" in piece.name else 560
            QLabelCustom(
                parent=self.centralwidget,
                filename=piece.value,
                objectName=f"{LabelType.STACK_PIECE.value}{piece.name.lower()}",
                geometry=(x_coord, (i % 6) * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                is_board_tile=False
            )
            QtWidgets.QLabel(
                parent=self.centralwidget,
                text="0",
                objectName=f"{LabelType.PIECE_COUNTER.value}{piece.name.lower()}",
            ).setGeometry(x_coord, (i % 6) * TILE_SIZE, 9, 9)

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
