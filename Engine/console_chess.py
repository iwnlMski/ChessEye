from logging import error, basicConfig

from eye_engine import Game, Font

basicConfig(format=f"\t{Font.RED}%(message)s{Font.CLEAR}")


def main():
    game = Game()
    print(game)

    while not game.won():
        move = input(
            f"{game.current_player} to move (eg. a2a4): {Font.BLUE if game.current_player.owns_black() else Font.WHITE}")
        if len(move) != 4:
            error(f"Input {move} length invald")
            continue
        piece_position_name = move[0:2]
        target_position_name = move[2:]

        try:
            game.move(piece_position_name, target_position_name)
        except RuntimeError as runtime_error:
            error(f"Error: {runtime_error}")
            continue

        print(game)


if __name__ == "__main__":
    main()
