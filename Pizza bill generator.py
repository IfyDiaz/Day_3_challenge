print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")

if size == "s":
  s = 15
  p = input("do you want pepperoni? Y or N ?")
  if p == "y":
    s +=2
  c = input("do you want extra-cheese? Y or N ?")  
  if c == "y":
    s +=1
    print(f"please pay ${s}")
  else:
    print(f"please pay ${s}")
elif size == "m":
  m = 20
  p = input("do you want pepperoni? Y or N ?")
  if p == "y":
    m +=2
  c = input("do you want extra-cheese? Y or N ?")  
  if c == "y":
    m +=1
    print(f"please pay ${m}")
  else:
    print(f"please pay ${m}")
elif size == "l":
  l = 25
  p = input("do you want pepperoni? Y or N ?")
  if p == "y":
    l +=2
  c = input("do you want extra-cheese? Y or N ?")  
  if c == "y":
    l +=1
    print(f"please pay ${l}")
  else:
    print(f"please pay ${l}")

else :
  print("please choose the correct size using the letter l, m, s")
