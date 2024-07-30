import random
import statistics


def k(faces: int) -> int:
  """Получить рандомное число при броске кубика с количеством граней ``faces``"""
  return random.randint(1, faces)


def average(*args):
  """Грубое вычисление минимума | среднего | максимума путём массового накидывания кубов"""
  results_list = []
  for i in range(10000):
    result = 0
    for dice in args:
      result += k(dice)
    results_list.append(result)
  print('average k', args, ':', min(results_list), '|', statistics.median(results_list), '|', max(results_list))
