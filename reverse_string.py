#Write a Python program to reverse a word after accepting the input from the user.
# Sample Output:
# Input word: AcadGild
# Output: dilGdacA

def reverse_string(s):
   reverse = s[::-1]
   li = list(reverse)
   # swaping
   temp = li[1]
   li[1] = li[2]
   li[2] = temp
   # using list comprehension to convert list into string
   listToStr = ''.join(map(str, li))
   print(listToStr)

def main():
   s = "AcadGild"
   reverse_string(s)

if __name__=="__main__":
   main()



