import unittest
from eye_engine import Engine, Board, Field, Position


class EngineTest(unittest.TestCase):
    def test_move_call(self):
        self.assertEqual(Engine().move(Board(), Field(Position(1, 2)), Field(Position(1, 2))), None)


if __name__ == '__main__':
    unittest.main()
