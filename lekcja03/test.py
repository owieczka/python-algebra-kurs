import unittest
from liczbynaturalne import LiczbaNaturalna

class TestLiczbyNaturalne(unittest.TestCase):
  def test_01_representation(self):
    """
    Test sprawdza czy poprawie tworzona jest reprezentacja liczby w pamieci komputera
    """
    l1 = LiczbaNaturalna("1")
    self.assertEqual(str(l1),"1","Liczba 1 jest nie poprawie tworzona w pamięci")

    l1 = LiczbaNaturalna("12345678901234567890")
    self.assertEqual(str(l1),"12345678901234567890","Duże liczby powyżej 20 znaków nie są poprawnie reprezentowane w pamięci")
    

    with self.assertRaises(TypeError,msg="Brak sprawdzania błedów typów podczas tworzenia reprezentacji liczby naturalnej"):
      l1 = LiczbaNaturalna(2)
      
  def test_02_add(self):
    """
    Sprawdza poprawność implementacji operacji dodawania
    """
    l1 = LiczbaNaturalna("2")
    l2 = LiczbaNaturalna("4")
    self.assertEqual(str(l1+l2),"6","Bład dodawania liczb")

    l1 = LiczbaNaturalna("2345")
    l2 = LiczbaNaturalna("12")
    self.assertEqual(str(l1+l2),"2357","Bład dodawania liczb o różnej długości")

    l1 = LiczbaNaturalna("99999")
    l2 = LiczbaNaturalna("1")
    self.assertEqual(str(l1+l2),"100000","Bład dodawania liczb z przeniesieniem")

    l1 = LiczbaNaturalna("9999999999999999999999999")
    l2 = LiczbaNaturalna("9999999999999999999999999")
    self.assertEqual(str(l1+l2),"19999999999999999999999998", "Bład dodawania dużych liczby z przeniesieniem")

if __name__=="__main__":
  unittest.main()
