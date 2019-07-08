from lib.cell import Cell
class TestCell:

  
# methods
# get_row
# get_col
# get_block
  def test_get_row(self):
    b = Cell(4, 1, 1)
    assert b.row == 1

  def test_get_col(self):
    b = Cell(4, 1, 1)
    assert b.col == 1

  def test_get_block(self):
    b = Cell(4, 1, 1)
    assert b.block == 1
