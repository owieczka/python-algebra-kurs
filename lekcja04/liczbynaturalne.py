from typing import Sequence
#from multipledispatch import dispatch
from itertools import zip_longest

class LiczbaNaturalna():
  def __init__(self, nowe_cyfry: str | Sequence[int]) -> None:
    self.cyfry : list[int]
    if isinstance(nowe_cyfry,list): 
      self.cyfry = nowe_cyfry
    elif isinstance(nowe_cyfry,str):
      self.cyfry = []
      nowa_cyfra: str
      for nowa_cyfra in reversed(nowe_cyfry):
        match nowa_cyfra:
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
            raise Exception(f"Błąd znak {nowa_cyfra} nie jest cyfrą")
    else:
      raise TypeError(f"Typ {type(nowe_cyfry)} nie jest wspierany")
    # Trymowanie zer z lewej strony liczby
    index_end : int = 0
    cyfra : int
    for cyfra in reversed(self.cyfry):
      if cyfra > 0:
        break
      index_end += 1
    if index_end > 0 and len(self.cyfry) > 1: # Wyłączenie przypadku że tylko 1 zero
      if index_end == len(self.cyfry): # Trzeba zostawić jedno 0 gdy liczba składa się z samych zer
        self.cyfry = [0]
      else:
        self.cyfry = self.cyfry[:-index_end]
    
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
    """
    Operator dodawania
    """
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

  def __sub__(self, druga_liczba : "LiczbaNaturalna") -> "LiczbaNaturalna":
    """
    Operator odejmowania
    """
    cyfry_wyniku: list[int] = []
    pozyczka = 0;
    cyfra_wyniku: int = 0
    for cyfra_pierwszej_liczby, cyfra_drugiej_liczby in zip_longest(self.cyfry, druga_liczba.cyfry, fillvalue = 0):
      if cyfra_pierwszej_liczby - pozyczka < cyfra_drugiej_liczby: # Trzeba pożyczyć
        cyfra_wyniku = 10 + cyfra_pierwszej_liczby - pozyczka - cyfra_drugiej_liczby
        pozyczka = 1;
      else: 
        cyfra_wyniku = cyfra_pierwszej_liczby - pozyczka - cyfra_drugiej_liczby
        pozyczka = 0
      cyfry_wyniku.append(cyfra_wyniku)
    if pozyczka: # Jeśli po odejęciu ostatniej cyfry nadal jest pożyczka mamy błąd
      raise OverflowError("Wynik odejmowania jest ujemny")
    if cyfra_wyniku == 0 and len(cyfry_wyniku) > 1:
      return LiczbaNaturalna(cyfry_wyniku[:-1])
    else:
      return LiczbaNaturalna(cyfry_wyniku)  
