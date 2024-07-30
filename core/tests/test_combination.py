from ..combination import Combination


def test_empty_init():
  combination = Combination()
  assert combination.name == ''
  assert combination.variants_count == 0
  assert combination.variants == {}


def test_dice_init():
  combination = Combination(6)
  expected_variants = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
  }
  assert combination.name == 'd6'
  assert combination.variants_count == 6
  assert combination.variants == expected_variants


def test_dice_x_dice():
  combination = Combination(6).x(6).x(6)
  expected_variants = {
    3: 1,
    4: 3,
    5: 6,
    6: 10,
    7: 15,
    8: 21,
    9: 25,
    10: 27,
    11: 27,
    12: 25,
    13: 21,
    14: 15,
    15: 10,
    16: 6,
    17: 3,
    18: 1,
  }
  assert combination.name == 'd6*d6*d6'
  assert combination.variants_count == 216
  assert combination.variants == expected_variants


def test_advantage_dice():
  combination = Combination(6).adv()
  expected_variants = {
    1: 1,
    2: 3,
    3: 5,
    4: 7,
    5: 9,
    6: 11,
  }
  assert combination.name == 'adv(d6)'
  assert combination.variants_count == 36
  assert combination.variants == expected_variants
