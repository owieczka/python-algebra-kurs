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

    l1 = LiczbaNaturalna("0")
    self.assertEqual(str(l1),"0","Zła reprezentacja liczby zero")

    l1 = LiczbaNaturalna("000")
    self.assertEqual(str(l1),"0","Złe trymowanie liczby 000")

    l1 = LiczbaNaturalna("000032")
    self.assertEqual(str(l1),"32","Złe trymowanie liczby o zbędne zera z lewej strony")
    
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

  def test_03_sub(self):
    """
    Test sprawdza poprawność implementacji odejmowania liczb naturalnych
    """
    l1 = LiczbaNaturalna("9")
    l2 = LiczbaNaturalna("5")
    self.assertEqual(str(l1-l2),"4","Błąd odejmowania prostych liczby jedno cyfrowych")

    l1 = LiczbaNaturalna("5")
    l2 = LiczbaNaturalna("9")
    with self.assertRaises(OverflowError,msg="Brak sprawdzania błedów czy wynik nie jest liczbą ujemną"):
      l3 = l1 - l2

    l1 = LiczbaNaturalna("12")
    l2 = LiczbaNaturalna("9")
    self.assertEqual(str(l1-l2),"3","Błąd odejmowania liczb z pożyczaniem")

    l1 = LiczbaNaturalna("987")
    l2 = LiczbaNaturalna("599")
    self.assertEqual(str(l1-l2),"388","Błąd odejmowania liczby z wielokrotnym pożyczaniem")

    l1 = LiczbaNaturalna("1343987")
    l2 = LiczbaNaturalna("599")
    self.assertEqual(str(l1-l2),"1343388","Błąd odejmowania liczby z wielokrotnym pożyczaniem")

    l1 = LiczbaNaturalna("5")
    l2 = LiczbaNaturalna("912323")
    with self.assertRaises(OverflowError,msg="Brak sprawdzania błedów czy wynik nie jest liczbą ujemną, gdy odjemna ma więcej cyfr"):
      l3 = l1 - l2

    l1 = LiczbaNaturalna("0")
    l2 = LiczbaNaturalna("0")
    self.assertEqual(str(l1-l2),"0","Bład odejmowania 0-0")

  def test_04_lshift(self):
    """
    Test sprawdza poprawność implementacji przesunięcia w lewo
    """
    l1 = LiczbaNaturalna("12")
    self.assertEqual(str(l1<<1),"120","Błąd przesunięcia w lewo")

    l1 = LiczbaNaturalna("12")
    self.assertEqual(str(l1<<4),"120000","Błąd przesunięcia w lewo")

  def test_05_ilshift(self):
    """
    Test sprawdza poprawność implementacji przesunięcia w lewo w miejscu
    """
    l1 = LiczbaNaturalna("12")
    l1 <<= 1
    self.assertEqual(str(l1),"120","Błąd przesunięcia w lewo")

    l1 = LiczbaNaturalna("12")
    l1 <<= 4
    self.assertEqual(str(l1),"120000","Błąd przesunięcia w lewo")

  def test_06_mul(self):
    """
    Test sprawdza poprawność implementacji mnożenia liczb naturalnych
    """
    l1 = LiczbaNaturalna("2")
    l2 = LiczbaNaturalna("4")
    self.assertEqual(str(l1*l2),"8","Błąd mnożenia prostych liczby jedno cyfrowych")

    l1 = LiczbaNaturalna("121212")
    l2 = LiczbaNaturalna("4")
    self.assertEqual(str(l1*l2),"484848","Błąd mnożenia liczb przez liczby jedno cyfrowe bez przeniesienia")

    l1 = LiczbaNaturalna("123456")
    l2 = LiczbaNaturalna("4")
    self.assertEqual(str(l1*l2),"493824","Błąd mnożenia liczby przez liczby jedno cyfrowe z przeniesieniem")

    l1 = LiczbaNaturalna("24")
    l2 = LiczbaNaturalna("36")
    self.assertEqual(str(l1*l2),"864","Błąd mnożenia liczby przez liczby jedno cyfrowe z przeniesieniem")    
    
if __name__=="__main__":
  unittest.main()
