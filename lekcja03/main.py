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

if __name__=="__main__":
  main()
#repr
#typeerror
#typing overload
#czy string jest sequence in duck typing?
#typing dispatch
#sprawdzac stan kazdej cyfry 
