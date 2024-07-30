from core.container import Container
from core.combination import Combination


def run():
  container = Container()

  container.list.append(Combination(6))
  container.list.append(Combination(4).x(4))
  container.list.append(Combination(6).x(6))
  container.list.append(Combination(8).x(8))
  container.list.append(Combination(10).x(10))
  container.list.append(Combination(12).x(12))

  container.view()
