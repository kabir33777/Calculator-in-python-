print(" _________      ______   ")
print("|  _______|    /  /\  \   ")
print("| |           /  /  \  \   ")
print("| |          /  /____\  \   ")
print("| |_______  /  /      \  \   ")
print("|_________|/__/        \  \    By Kabir3377 ")











i = str(input("type start or quit to end  "))
if  i != "quit" and i != "start":
  while i != "quit" or i != "start":
    print("invalid input")
    i = str(input("type start or quit to end   "))
while i == "start":
  Num = float(input("Num  "))
  Operation = str(input("Operation  "))
  Num2 = float(input("Num  "))
  if Operation == '+':
    print(Num + Num2)
  if Operation == '-':
    print(Num - Num2)
  if Operation == '*':
    print(Num * Num2)
  if Operation == '/':
    print( Num / Num2)
  if Operation == '%':
    print(  Num / Num2 * 100 )
  Work = str(input("type quit to end to 0 to begin once more   "))
  if Work == "quit":
    i = "quit"
print("Thanks")