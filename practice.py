# 1. FizzBuzz Challenge Write a program that iterates from 1 to 50. - Print 'Fizz' for multiples of 3 - Print
# 'Buzz' for multiples of 5 - Print 'FizzBuzz' for multiples of both

for i in range(1,51):
    if (i%3 == 0):
        print("buzz")
    elif(i%5 == 0):
        print("fizz")
    elif(i%5 == 0 and i%3 == 0):
        print("fizzbuzz")


#2. Leap Year Logic Write a function that takes a year as input and returns True if it is a leap year and False otherwise.

def leap_year():
    year = int(input("enetr a year : "))
    if(year %4 == 0 and  year %100 !=0):
        print(True)
    elif(year % 400 == 0):
        print(True)
    else:
        print(False)


leap_year()

# 3. Identity vs Equality Given: L1 = [1,2,3] and L2 = [1,2,3] Explain the difference between L1 == L2 and
# L1 is L2. 
"""
is check wether they refer to same object or same variable 
== check that value is same or not 
"""

#  5. Prime Number Finder Write a while loop that finds and prints the first 10 prime numbers. 
c = 0
num = 2

while c < 10:
    i = 2
    is_prime = True

    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num)
        c += 1

    num += 1


# 6. The Loop Breaker Create a loop from 1 to 20: - If divisible by 4 → pass - If the number is 13 →
# continue - If the number is 18 → break 

for i in range(1,20):
    if(i%4==0):
        pass
    elif(i%13 == 0):
        continue
    elif(i==18):
        break


# 7. Nested Conditionals Write a program that takes a numerical grade (0–100) and returns: A (90+), B
# (80–89), C (70–79), Fail (below 70). 

marks = int(input("enter your marks"))

if (marks >= 90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("Fail")


# 8. Reverse an Integer Using a while loop and arithmetic operators (// and %), reverse the digits of an
# integer


# 9. Runner-Up Score Given a list of scores, find the second-highest score without using sort() or
# sorted(). 

score=[12,13,14,15]
first = max(score)
runner_up = score[0]
for i in score :
    
    if i > runner_up  and i < first:
        runner_up = i

    
print(runner_up)

# 10. Duplicate Removal Write a single line of code to remove duplicates from a list and return unique
# values.
l2=[1,2,3,4,5,6,6,7,8,]
l1 = list(set(l2))

# 11. List Intersection Write a program to find common elements between two lists using the
# membership operator in.

a=[1,2,3,4]
b=[1,4,6,9]
c=[]
for i in a :
    if i in b:
        c.append(i)

print(c)


# 12. Tuple Immutability Test Attempt to change the second element of a tuple and handle the
# resulting error using try-except

t=(1,2,3,4)
try:
    t[1]=0
except Exception as e :
    print(e)


# 13. Character Frequency Counter Take a string input and return a dictionary with character counts. 
sen = input("Enter string: ")

f = {}

for ch in sen:
    if ch in f:
        f[ch] += 1
    else:
        f[ch] = 1

print(f)

# 14. List Comprehension Create a list of squares of all even numbers between 1 and 20 using a single
# line. 

sq = [x*x for x in range(1, 21) if x % 2 == 0]
print(sq)


# 15. Dictionary Comprehension From the dictionary {'a': 1, 'b': 2, 'c': 3, 'd': 4}, create a new dictionary
# containing only items with values greater than 2

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

new_d = {k: v for k, v in d.items() if v > 2}

print(new_d)