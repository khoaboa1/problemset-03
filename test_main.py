from main import *

### PART 1: SEARCHING UNSORTED LISTS

# 2 pts
def test_isearch():
    assert isearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])

# 2 pts
def test_isearch2():
    assert isearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert isearch([], 2) == (2 in [])

# 2 pts
def test_rsearch():
    assert rsearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])

# 2 pts
def test_rsearch2():
    assert rsearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert rsearch([], 2) == (2 in [])

### PART 3: PARENTHESES MATCHING

# 2 pts
def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(', 'a', ')', '(', ')']) == True

# 2 pts
def test_parens_match_iterative2():
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_iterative(['(', '(', ')']) == False
    assert parens_match_iterative(['(', 'a', ')', ')', '(']) == False

# 2 pts
def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(', 'a', ')', '(', ')']) == True

# 2 pts
def test_parens_match_scan2():
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False
    assert parens_match_scan(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_scan(['(', '(', ')']) == False
    assert parens_match_scan(['(', 'a', ')', ')', '(']) == False

# 2 pts
def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(', 'a', ')', '(', ')']) == True

# 2 pts
def test_parens_match_dc2():
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
    assert parens_match_dc(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_dc(['(', '(', ')']) == False
    assert parens_match_dc(['(', 'a', ')', ')', '(']) == False
    assert parens_match_dc([]) == True 
