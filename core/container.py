from typing import List

from core.combination import Combination


class Container:
  """Контейнер накиданных комбинаций. Хранит и отображает"""
  def __init__(self) -> None:
    self.list: List[Combination] = []

  def view(self):
    count = max([max(combination.variants.keys()) for combination in self.list])

    title = '\t'
    for combination in self.list:
      text = combination.name
      if len(text) >= 8:
        title = title + f'{text}\t'
      else:
        title = title + f'{text}\t\t'
    print(title)

    for i in range(1, count + 1):
      string = f'{i}\t'
      for combination in self.list:
        percent = round(combination.variants.get(i, 0) / combination.variants_count * 100, 2)
        if percent <= 5:
          text = f'* {percent}%'
        else:
          text = f'  {percent}%'

        if len(text) >= 8:
          text = f'{text}\t'
        else:
          text = f'{text}\t\t'
        string = string + text
      print(string)
