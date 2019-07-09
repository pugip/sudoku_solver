from lib.puzzle import Puzzle
class TestPuzzle:

  def test_first(self):
    assert 5 != 4 

  def test_valid(self):
    p=('... ..3 19.'
       '2.. .1. .6.'
       '..1 92. 5..'
  
       '5.2 6.7 ..1'
       '673 .9. ..5'
       '.98 ..4 67.'
  
       '32. 14. ..6'
       '.56 ... 21.'
       '... 5.. ...')
    p = p.replace(' ', '')
    print(p)
    puzzle = Puzzle(p)
    print(puzzle.cells)
    assert puzzle.valid() 

