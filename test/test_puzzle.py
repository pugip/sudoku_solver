from lib.puzzle import Puzzle
class TestPuzzle:

    def test_first(self):
        assert 5 != 4

    def test_valid(self, valid_puzzle):
        print(valid_puzzle.cells)
        assert valid_puzzle.valid()

    def test_valid_with_invalid_columns(self, invalid_column_puzzle):
        print(invalid_column_puzzle.cells)
        assert not invalid_column_puzzle.valid()

    def test_valid_with_invalid_rows(self, invalid_row_puzzle):
        print(invalid_row_puzzle.cells)
        assert not invalid_row_puzzle.valid()

    def test_valid_with_invalid_blocks(self, invalid_block_puzzle):
        print(invalid_block_puzzle.cells)
        assert not invalid_block_puzzle.valid()
