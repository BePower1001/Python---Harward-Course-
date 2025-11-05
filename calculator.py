x = 1
y = 2
z = x + y
print(z)

#We need to convert string into integer in line 10
x = input("What is x? ")
y = input("What is y? ")

z = int(x) + int(y)
print(z)


#Even now we can do something else with integer

x = int(input("What is x? "))
y = int(input("What is y? "))
print(x + y)

#Working on float numbers

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

#We can round number using Python documentation (round(number or variable,decimal number to round))
print(round((x+y),3))

z = round(x/y,2)
print(z)

z = x/y
print(f"{z:.2f}")


def main():
    x = int(input("What's x: "))
    print("x squared is", square(x))


def square(n):
    return n * n
main()