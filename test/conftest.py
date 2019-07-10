import pytest

from lib.puzzle import Puzzle

@pytest.fixture
def valid_puzzle():
    ps = ('... ..3 19.'
          '2.. .1. .6.'
          '..1 92. 5..'

          '5.2 6.7 ..1'
          '673 .9. ..5'
          '.98 ..4 67.'

          '32. 14. ..6'
          '.56 ... 21.'
          '... 5.. ...')
    ps = ps.replace(' ', '')
    yield Puzzle(ps)
