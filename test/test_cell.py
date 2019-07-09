from lib.cell import Cell
class TestCell:

  def test_use_none_value(self):
    b = Cell(None, 1, 1)
    assert b.value == None 

  def test_get_value(self):
    b = Cell(4, 1, 1)
    assert b.value == 4
  
  def test_get_row(self):
    b = Cell(4, 1, 1)
    assert b.x_coord == 1

  def test_get_col(self):
    b = Cell(4, 1, 1)
    assert b.y_coord == 1

  def test_get_block(self):
    b = Cell(4, 4, 8)
    assert b.block() == 5
