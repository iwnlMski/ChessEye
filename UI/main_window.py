from PyQt6 import QtGui, QtWidgets
from const import DEFAULT_BOARD_IMAGES, TILE_SIZE, Piece
from PyQt6.QtCore import Qt
from custom_label import QLabelCustom, StackPieceLabel, UnclickableLabel
from helper_functions import LabelHelperFunctions


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setObjectName("MainWindow")
        self.resize(700, 700)
        self.setAcceptDrops(True)

        self.centralwidget = QtWidgets.QWidget(
            self, objectName="centralwidget")
        self.setCentralWidget(self.centralwidget)

        for i in range(8, 0, -1):
            for char in range(ord("A"), ord("I")):
                QLabelCustom(
                    parent=self.centralwidget,
                    filename=DEFAULT_BOARD_IMAGES.get(
                        f"{chr(char)}{i}", "../img/blank.png"),
                    objectName=f"board_tile_{chr(char)}{i}",
                    geometry=((char-ord("A"))*TILE_SIZE, (i-1)
                              * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )

        for i, piece in enumerate(Piece):
            x_coord = 500 if "WHITE" in piece.name else 560
            temp_stack_piece_label = StackPieceLabel(
                parent=self.centralwidget,
                filename=piece.value,
                objectName=f"stack_piece_{piece.name.lower()}",
                geometry=(x_coord, (i % 6) * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            )
            var = UnclickableLabel(
                parent=self.centralwidget,
                text="0",
                objectName=f"stack_piece_counter_{piece.name.lower()}",
            )
            var.setGeometry(x_coord, (i % 6) * TILE_SIZE, 9, 9)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        event.accept()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        drop_position_label = LabelHelperFunctions.get_label_by_position(
            event.position().x(), event.position().y(), self.centralwidget.children())
        dragged_label = LabelHelperFunctions.get_label_by_dragged_status(
            self.centralwidget.children())

        if drop_position_label and dragged_label:
            if isinstance(dragged_label, QLabelCustom):
                if drop_position_label.filename and dragged_label.filename.split("_")[0] != drop_position_label.filename.split("_")[0]:
                    LabelHelperFunctions.update_piece_stack(
                        drop_position_label, self.centralWidget().children())
                    LabelHelperFunctions.delete_piece_from_board(
                        drop_position_label)
                LabelHelperFunctions.swap_two_labels(
                    dragged_label, drop_position_label)

                event.setDropAction(Qt.DropActions.MoveAction)
                event.accept()
            elif isinstance(dragged_label, StackPieceLabel):
                if drop_position_label.filename:
                    LabelHelperFunctions.update_piece_stack(
                        drop_position_label, self.centralWidget().children())
                    LabelHelperFunctions.delete_piece_from_board(
                        drop_position_label)
                LabelHelperFunctions.add_piece_from_stack(
                    dragged_label, drop_position_label, self.centralWidget().children())

                event.setDropAction(Qt.DropActions.MoveAction)
                event.accept()
        elif dragged_label and not drop_position_label:
            LabelHelperFunctions.update_piece_stack(
                dragged_label, self.centralWidget().children())
            LabelHelperFunctions.delete_piece_from_board(dragged_label)

            event.setDropAction(Qt.DropActions.MoveAction)
            event.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
