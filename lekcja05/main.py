from liczbynaturalne import LiczbaNaturalna
  
def main():
  print("Main")
  l1 = LiczbaNaturalna("10")
  #l2 = LiczbaNaturalna({})
  l3 = LiczbaNaturalna("6758")
  l4 = LiczbaNaturalna([2,3,4])
  #l5 = LiczbaNaturalna([1,"2",3,4]) # type error
  l6 = l1 + l3
  print(f"{l1} + {l3} = {l6}")

  l1 = LiczbaNaturalna("15")
  l2 = LiczbaNaturalna("9")
  l3 = l1 - l2
  print(f"{l1} - {l2} = {l3}")

  #l1 = LiczbaNaturalna("9")
  #l2 = LiczbaNaturalna("15")
  #l3 = l1 - l2
  #print(f"{l1} - {l2} = {l3}")

  l1 = LiczbaNaturalna("0")
  l2 = LiczbaNaturalna("0")
  l3 = l1 - l2
  print(f"{l1} - {l2} = {l3}")

  l1 = LiczbaNaturalna("12")
  l1 = l1 << 1
  print(f"{l1}")

  l1 = LiczbaNaturalna("2")
  l2 = LiczbaNaturalna("4")
  l3 = l1 * l2
  print(f"{l1} * {l2} = {l3}")

  l1 = LiczbaNaturalna("2004")
  l2 = LiczbaNaturalna("123456")
  l3 = l1 * l2
  print(f"{l1} * {l2} = {l3}")

  
if __name__=="__main__":
  main()
#repr
#typeerror
#typing overload
#czy string jest sequence in duck typing?
#typing dispatch
#sprawdzac stan kazdej cyfry 
