# Skrypt budujący choinkę 
import datetime
a = int(input("Jaka wielka ma być choinka: "))

for i in range(1, a+1):
    print((a-i)*" ", i*" *")
print((a-1)*" ", "* ")
print((a-1)*" ", "* ")
present = datetime.datetime.now()
future = datetime.datetime(2020, 12, 24, 23, 0, 0)
difference = future - present
print('Do świąt zostało')
print(difference)
