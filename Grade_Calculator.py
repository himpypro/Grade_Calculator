print("Grade Calculator")
Sub_1 = int(input("Put your score here: "))
Sub_2 = int(input("Put your score here: "))
Sub_3 = int(input("Put your score here: "))
Sub_4 = int(input("Put your score here: "))
Sub_5 = int(input("Put your score here: "))
Sub_t= (Sub_1+Sub_2+Sub_3+Sub_4+Sub_5)
print("=> Accumulated score: ",Sub_t)
score = Sub_t/5
print("=> Mean score is ",score)
if score in range(100,79,-1):                  #Used If statement with for loop in range.
    print("***You got A+ <Outstanding>***")
elif score in range(70,80):
    print("***You got A <Excellent>***")
elif score in range(60,70):
    print("***You got A- <Very Good>***")
elif score in range(50, 60):
    print("***You got B <Good>***")
elif score in range(40,50):
    print("***You got C <Average>***")
elif score in range(33,40):
    print("***You got D <Pass>***")
else:
    print("Fail <Good Luck>")