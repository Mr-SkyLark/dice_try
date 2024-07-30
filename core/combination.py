from typing import Dict, List

from .roll import Roll, RollType


class Combination:
  def __init__(self, dice_faces: int = None) -> None:
    self.name: str = ''
    """Имя комбинации"""
    self.variants_count: int = 0
    """Количество возможных комбинаций бросков"""
    self.variants: Dict[int, int] = {}
    """Словарь комбинаций ``{значение_броска: количество_выпадений}``"""

    self._roll_order: List[Roll] = []
    """Порядок бросков"""

    if dice_faces is not None:
      self._dice(dice_faces)

  def adv(self):
    """Бросок с преимуществом"""
    self._add_roll(Roll(RollType.ADVANTAGE))
    self.variants_count *= self.variants_count
    new_variants = {}

    for first_value, first_count in self.variants.items():
      for second_value, second_count in self.variants.items():
        if first_count != 0 and second_count != 0:
          value = max(first_value, second_value)
          if new_variants.get(value, 0) == 0:
            new_variants[value] = first_count
          else:
            new_variants[value] += first_count
    self.variants = new_variants

    print(self.__str__())
    return self

  # def adv(self, dice_faces: int):
  #   """Бросок с преимуществом"""
  #   pass

  def x(self, dice_faces: int):
    """Добавление кубика к броску"""
    self._add_roll(Roll(RollType.DICE, dice_faces))
    self.variants_count *= dice_faces
    dice_combination = Combination(dice_faces)
    new_variants = {}

    for first_value, first_count in self.variants.items():
      for second_value, second_count in dice_combination.variants.items():
        if first_count != 0 and second_count != 0:
          value = first_value + second_value
          if new_variants.get(value, 0) == 0:
            new_variants[value] = first_count
          else:
            new_variants[value] += first_count
    self.variants = new_variants

    print(self.__str__())
    return self

  # def chance_first_d10():
  #   first_dice = combination(10)
  #   second_dice = combination(10)
  #   print(first_dice, second_dice)
  #   result = {
  #     'name': 'fd10',
  #     'variants_count': first_dice["variants_count"] * second_dice["variants_count"],
  #     'variants': {},
  #   }
  #   variants = result['variants']
  #   for i in range(1, BORDER + 1):
  #     variants[i] = 0

  #   first_values = first_dice['variants']
  #   second_values = second_dice['variants']

  #   for first_value, first_count in first_values.items():
  #     for second_value, second_count in second_values.items():
  #       # print(f'first: {first_value}, {first_count}',
  #       #       f'second: {second_value}, {second_count}')
  #       if first_count != 0 and second_count != 0:
  #         if first_value != 10:
  #           variants[first_value] += first_count
  #         else:
  #           variants[first_value + second_value] += first_count

  #   print(result)
  #   return result

  def _dice(self, dice_faces: int) -> None:
    """Первая комбинация для куба с количеством граней ``dice_faces``"""
    self._add_roll(Roll(RollType.DICE, dice_faces))
    self.variants_count = dice_faces
    for i in range(1, dice_faces + 1):
      self.variants[i] = 1

  def _build_name(self):
    roll = self._roll_order[-1]
    if roll.type == RollType.DICE:
      _x_symbol = '*' if self.name else ''
      self.name = self.name + f'{_x_symbol}d{roll.value}'
    if roll.type == RollType.ADVANTAGE:
      self.name = f'adv({self.name})'
    if roll.type == RollType.DISADVANTAGE:
      self.name = f'dis({self.name})'

  def _add_roll(self, roll: Roll) -> None:
    self._roll_order.append(roll)
    self._build_name()

  def __str__(self) -> str:
    return str({'name': self.name, 'count': self.variants_count, 'variants': self.variants})
