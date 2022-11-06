from .board import Board
from .field import Field


class Engine:
    @staticmethod
    def move(board: Board, piece_field: Field, target_field: Field):
        pass


'''

 from_moves = self.valid_moves(
            from_field, self.board)
        if to_field not in from_moves:
            raise RuntimeError(
                f"{from_field} cannot move to {to_field}, available moves: {', '.join([str(f) for f in from_moves])}")
        captured_figure = to_field.figure
        self.board.move(from_field, to_field)
        if captured_figure:
            self.captured_pieces[self.current_player_color].append(
                captured_figure)
def move(self, field_from: Field, field_to: Field):
      moved_figure = field_from.figure
       if not moved_figure:
            raise RuntimeError(f"No figure in {field_from}")

        captured_figure = field_to.figure
        if captured_figure and captured_figure.color == moved_figure.color:
            raise RuntimeError(
                f"Unable to move figure {moved_figure} on top of another same color figure {captured_figure}")

        field_from.capture(field_to)

    def capture(self, field_to):
        field_to.piece = None
        field_to.piece, self.piece = self.piece, field_to.piece
        field_to.piece.history.append(field_to)

def move_relative(self, rc, perspective=Color.WHITE):
    sign = 1 if perspective is Color.WHITE else -1
    coord = Position(self.row + (rc.row*sign), self.col + (rc.col*sign))
    return coord if (0 <= coord.row < 8) or (0 <= coord.col < 8) else None


class Move(Enum):
    FORWARD = [[Coord(1, 0), move_filter]]
    DOUBLE_FORWARD = [[Coord(2, 0), pawn_double_filter]]
    PAWN_CAPTURE = [[Coord(1, 1), capture_filter], [
        Coord(1, -1), capture_filter]]
    KNIGHT = [[Coord(2, 1), move_or_capture_filter], [Coord(-2, -1), move_or_capture_filter], [Coord(-2, 1), move_or_capture_filter], [Coord(2, -1), move_or_capture_filter],
              [Coord(1, 2), move_or_capture_filter], [Coord(-1, -2), move_or_capture_filter], [Coord(-1, 2), move_or_capture_filter], [Coord(1, -2), move_or_capture_filter]]
    KING = [[Coord(1, 0), move_or_capture_filter], [
        Coord(0, 1), move_or_capture_filter], [Coord(1, 1), move_or_capture_filter], [Coord(-1, -1), move_or_capture_filter], [Coord(1, -1), move_or_capture_filter], [Coord(-1, 1), move_or_capture_filter], [Coord(-1, 0), move_or_capture_filter], [Coord(0, -1), move_or_capture_filter]]


def valid_moves(self, field: Field, board: Board) -> List[Field]:
        figure = field.figure
        if not figure:
            raise RuntimeError(
                f"Field {field} does not contain a figure to move")

        moves: List[Move] = []
        if figure.type is Piece.PAWN:
            moves.extend(
                [Move.FORWARD, Move.DOUBLE_FORWARD, Move.PAWN_CAPTURE])
        if figure.type is Piece.KNIGHT:
            moves.append(Move.KNIGHT)
        if figure.type is Piece.KING:
            moves.append(Move.KING)

        fields = []
        for move in moves:
            for rel_coord, filter_fn in move.value:
                target_coord = field.position.move_relative(
                    rel_coord, perspective=figure.color)
                if not target_coord:
                    continue

                target_field = board.get_field_coord(
                    target_coord)
                if not target_field:
                    continue

                if filter_fn(field, target_field):
                    fields.append(target_field)
        return fields


def capture_filter(field_from: Field, field_to: Field):
    figure_to = field_to.figure
    figure_from = field_from.figure
    return figure_to and figure_from and (figure_to.color is not figure_from.color)


def move_filter(field_from: Field, field_to: Field):
    return field_from.figure and not field_to.figure


def move_or_capture_filter(field_from: Field, field_to: Field):
    return capture_filter(field_from, field_to) or move_filter(field_from, field_to)


def pawn_double_filter(field_from: Field, field_to: Field):
    figure = field_from.figure
    if not figure:
        raise ValueError("No piece for pawn double forward move")
    row = 1 if figure.color is Color.WHITE else 6
    return move_filter(field_from, field_to) if field_from.position.row is row else False
'''
