
while True:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("Interest cannot be less than zero.")
    else:
        break

while True:
    rate = float(input("Enter the principle amount: "))
    if rate < 0:
        print("Rate cannot be less than zero.")
    else:
        break
while True:
    Time = int(input("Enter the principle amount: "))
    if Time < 0:
        print("Time cannot be less than zero.")
    else:
        break

print(f"{principle}")
print(f"{rate}")
print(f"{time}")

total = principle * pow((1 + rate/100),time)
print(f"Balance after {time} year/s: ${total:.2f}")