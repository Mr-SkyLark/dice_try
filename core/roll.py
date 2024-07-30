from enum import Enum
from typing import Any, Optional
from dataclasses import dataclass


class RollType(Enum):
  EMPTY = 'none'
  DICE = 'dice'
  ADVANTAGE = 'adv'
  DISADVANTAGE = 'dis'


@dataclass
class Roll:
  """Класс броска"""
  type: RollType = RollType.EMPTY
  """Тип броска"""
  value: Optional[Any] = None
  """Дополнительная информация, если есть(Грани кубика и тп)"""
