from core.container import Container
from core.combination import Combination


def run():
  container = Container()

  base_dice = 6
  container.list.append(Combination(base_dice))
  container.list.append(Combination(base_dice).x(4))
  container.list.append(Combination(base_dice).x(6))
  container.list.append(Combination(base_dice).x(4).x(4))
  container.list.append(Combination(base_dice).x(8))
  container.list.append(Combination(base_dice).x(10))
  container.list.append(Combination(base_dice).x(6).x(4))
  container.list.append(Combination(base_dice).x(8).x(4))
  container.list.append(Combination(base_dice).x(6).x(6))
  container.list.append(Combination(20).adv())
  container.list.append(Combination(base_dice).x(12))

  container.view()
