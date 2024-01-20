from typing import Sequence
#from multipledispatch import dispatch
from itertools import zip_longest

class LiczbaNaturalna():
  def __init__(self, nowe_cyfry: str | Sequence[int]) -> None:
    if isinstance(nowe_cyfry,list): 
      self.cyfry = nowe_cyfry
    elif isinstance(nowe_cyfry,str):
      self.cyfry = []
      for cyfra in reversed(nowe_cyfry):
        match cyfra:
          case '0':
            self.cyfry.append(0)
          case '1':
            self.cyfry.append(1)
          case '2':
            self.cyfry.append(2)
          case '3':
            self.cyfry.append(3)
          case '4':
            self.cyfry.append(4)
          case '5':
            self.cyfry.append(5)
          case '6':
            self.cyfry.append(6)
          case '7':
            self.cyfry.append(7)
          case '8':
            self.cyfry.append(8)
          case '9':
            self.cyfry.append(9)
          case _:
            raise Exception(f"Błąd znak {cyfra} nie jest cyfrą")
    else:
      raise TypeError(f"Typ {type(nowe_cyfry)} nie jest wspierany")                              
  """
  @dispatch(str)
  def __init__(self, nowe_cyfry: str) -> None: 
    self.cyfry = []
    for cyfra in reversed(nowe_cyfry):
      match cyfra:
        case '0':
          self.cyfry.append(0)
        case '1':
          self.cyfry.append(1)
        case '2':
          self.cyfry.append(2)
        case '3':
          self.cyfry.append(3)
        case '4':
          self.cyfry.append(4)
        case '5':
          self.cyfry.append(5)
        case '6':
          self.cyfry.append(6)
        case '7':
          self.cyfry.append(7)
        case '8':
          self.cyfry.append(8)
        case '9':
          self.cyfry.append(9)
        case _:
          raise Exception(f"Błąd znak {cyfra} nie jest cyfrą")


  @dispatch(list)
  def __init__(self, nowe_cyfry: Sequence[int]) -> None: 
    self.cyfry = nowe_cyfry
  """

  def __repr__(self) -> str:
    
    s = "LiczbaNaturalna([" + ",".join(map(lambda cyfra: f"{cyfra}",self.cyfry)) + "])"
    return s

  def __str__(self) -> str:
    return "".join(map(lambda cyfra: f"{cyfra}",reversed(self.cyfry)))

  def __add__(self, druga_liczba : "LiczbaNaturalna") -> "LiczbaNaturalna":
    cyfry_wyniku: list[int] = []
    przeniesienie = 0
    for cyfra_pierwszej_liczby, cyfra_drugiej_liczby in zip_longest(self.cyfry, druga_liczba.cyfry, fillvalue = 0):
      suma = cyfra_pierwszej_liczby + cyfra_drugiej_liczby + przeniesienie
      cyfra_wyniku = suma % 10
      przeniesienie = suma // 10
      cyfry_wyniku.append(cyfra_wyniku)
    if przeniesienie: # Jeśli po dodawaniu nadal jest przeniesienie dodaj cyfrę do wyniku
      cyfry_wyniku.append(przeniesienie)
    return LiczbaNaturalna(cyfry_wyniku)
  
def main():
  print("Main")
  l1 = LiczbaNaturalna("10")
  #l2 = LiczbaNaturalna({})
  l3 = LiczbaNaturalna("6758")
  l4 = LiczbaNaturalna([2,3,4])
  #l5 = LiczbaNaturalna([1,"2",3,4]) # type error
  l6 = l1 + l3
  print(f"{l1} + {l3} = {l6}")

if __name__=="__main__":
  main()
#repr
#typeerror
#typing overload
#czy string jest sequence in duck typing?
#typing dispatch
#sprawdzac stan kazdej cyfry 
