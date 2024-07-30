from core.container import Container
from core.combination import Combination


def run():
  container = Container()

  container.list.append(Combination(6))
  container.list.append(Combination(6).x(6))
  container.list.append(Combination(6).x(6).x(6))

  container.view()
