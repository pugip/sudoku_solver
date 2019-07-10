from lib.puzzle import Puzzle
class TestPuzzle:

  def test_first(self):
    assert 5 != 4 

  def test_valid(self, valid_puzzle):
    print(valid_puzzle.cells)
    assert valid_puzzle.valid()

