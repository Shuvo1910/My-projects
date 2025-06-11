# chack the input (num) whether it is positive or nor.
num = -13
if num < 0:
    print("Negative")
elif num > 0:
    print("Positive")
else: 
    print("Zero") 


# Chack the stage of age.
name = "Shuvo"
age = 19
if age <= 13:
    print("Child")
elif age <= 19:
    print("Teenager") 
elif age >= 20:
    print("Adult") 
 
          
# Chack the letter is vowel or not:
letter = "A"
if letter in ("A", "a", "E", "e", "I", "i", "O","o", "U", "u" ):
    print("The letter is vowel.")
else:
    print("The letter is not a vowel")


# Chack the letter is vowel or not:

sentence = "The boy got the highest mark"
vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
found = {
        'a': False, 
         'e': False, 
         'i': False, 
         'o': False, 
         'u': False
}

for letter in sentence.lower(): 
    if letter in vowel:
        vowel[letter] += 1
      

    if letter in found:
            found[letter] = True
            break

print("Total Vowel:", vowel)
print("Vowels found:", found)



# Chack student's marks and print grade:
mark = 93
if mark >= 90:
    print("Grade: A")
elif mark >= 80:
    print("Grade: B")
elif mark >= 70:
    print("Grade: C")
elif mark >= 60:
    print("Grade: D")
else:
    print("Grade: F")
print("exit...")


# nested "if" condition.
year = 18 
print("Ok") if year >= 18 else print("You are not allowed"); print("Nineteen") if year == 19 else None


# Simple calculator:
print("1 +")
print("2 -")
print("3 *")
print("4 /")
operator = input("Enter your choice:") 
num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
if operator == "1":
    print(num1+num2)
elif operator == "2":
    print(num1-num2)
elif operator == "3":
    print(num1*num2)
elif operator == "4":
    if num1 == 0:
        print("Error")
    else:
        print(num1/num2)
else:
    print("Invalid choice")
    
    
# Write a for loop to print the multiplication table of a given number. 
num = 5
for i in range(1,11):
    print(num, "*", i, "=", num * i)

def count_character_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


# Example usage
string = "banana"
result = count_character_frequency(string)
print(result)

out = {}
words = ['b','n','a']
value = [1,2,3]
for i in range(len(words)):
    out[words[i]] = [value[i]]
print(out)

ran = {}
kye = ['Shuvo','Nahid','Ratul','Rajib']
value = [60,55,40,75]
for i in range(len(kye)):
    ran[kye[i]] = value[i]
print(ran)

 