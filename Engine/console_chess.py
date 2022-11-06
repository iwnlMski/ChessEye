from logging import error, basicConfig

import eye_engine

FONT_RED = "\x1b[31;1m"
FONT_CLEAR = '\033[0m'
basicConfig(format=f"\t{FONT_RED}%(message)s{FONT_CLEAR}")


def main():
    game = eye_engine.Game()
    print(game)

    while not game.won():
        move = input("Input move (eg. a2a4): ")
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
