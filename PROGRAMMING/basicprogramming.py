class BasicProgram:
    # 1. Write a Python function that accepts two integer numbers. If the product
    # of the two numbers is less than or equal to 1000,
    # return their product; otherwise, return their sum
    def product_Or_sum(self, a, b):
        if a * b <= 1000:
            return a * b
        else:
            return a + b

    # 2.Iterate through the first 10 numbers(0–9).In each iteration, print the current
    # number, the previous number, and their sum.
    def cumulative_sum(self):
        previous_num = 0
        for current_num in range(10):
            print("Current number: ", current_num)
            print("Previous Number: ", previous_num)
            sum = current_num + previous_num
            print("Sum: ", sum)
            previous_num = current_num

    #3.Display only those characters which are
    # present at an even index number in given string.
    def stringindex_stringslicing(self, a):
        size = len(a)
        for i in range(0, size):
            if i % 2 == 0:
                print("Index[", i, "]", a[i])

    #4.Write a function to remove characters from a string starting from i
    # ndex 0 up to n and return a new string.
    def substring_removal(self, word, n):
        print("Original String: ", word)
        new_str = word[n:]
        print(new_str)

    #5.Write a program to swap the values of two variables,
    # a and b, without using a third temporary variable.
    #tuple unpacking-->a,b=(b,a)

    def swap_without_temp_var(self, a, b):
        a, b = (b, a)
        print("Num1 after swap:", a)
        print("Num2 after swaps:", b)
        return

    #6.Write a program that calculates the factorial of
    # a given number (e.g., 5!) using a for loop.
    def factorial(self,n):
        f=1
        if n<=1:
            return 1
        else:
            while n!=0:
                f=f*n
                n=n-1
        return f
    # 7.Create a list of 5 fruits. Add a new fruit to the end of the list,
    # then remove the second fruit (at index 1).

    def list_manipulation(self,arr,index):
        arr.pop(index)
        return arr
    def list_add(self,arr,ele,index):
        if len(arr)<=0:
            arr.append(ele)
        else:
            arr.insert(index,ele)
        return arr
    #8.Write a program that takes a string and
    # reverses it (e.g., “Python” becomes “nohtyP”).

    def reverse_string(self,word):
        n=len(word)
        rev=""
        for i in range(n-1,-1,-1):
            rev=rev+word[i]
        return rev
    # 9.Write a program to count the total number of
    #  vowels (a, e, i, o, u) present in a given sentence.
    def vowel_counter(self,word):
        vowel="aeiou"
        count=0
        for i in word:
            if i in vowel:
                count=count+1
        return count
    #10.Given a list of integers, find and
    # print both the largest and the smallest numbers.
    def min_max(self,arr):
        max_num=arr[0]
        min_num=arr[0]
        for i in arr:
            if i>max_num:
                max_num=i
            if i<min_num:
                min_num=i
        return (max_num,min_num)
    # 11.Write a program to find how many times
    # the substring “Emma” appears in a given string.
    def string_counter(self,str_x,word):
        str_new=[]
        count=0
        str_new=str_x.split(" ")
        print("str_new: ",str_new)
        for i in str_new:
            if word==i:
                count=count+1
        return count
    #Write a program to check if a given
    # number is a palindrome (reads the same forwards and backwards).
    def palindrome_checker(self,num):
        rev=0
        temp=num
        while(num!=0):
            digit=num%10
            rev=rev*10+digit
            num=num//10
        if(rev==temp):
            return True
        else:
            return False

    # Write a function called exponent(base, exp)
    # that returns an integer value of the base raised to the power of the exponent.
    def exponent(self,base, exp):
        power=abs(exp)
        res = 1
        if base==0 or base==0 and power==0:
            return "Undefined"
        elif exp < 0:
            for i in range(power):
                res = res * base
                res = 1/res
        elif exp>0:
            for i in range(power):
                res=res*base


        return res

    #fibonnaci

    def fibonnaci(self,n):
        num1=0
        num2=1
        for i in range(n):
            num3=num1+num2
            print(num1)
            num1=num2
            num2=num3





# base, exp = int(input("Enter base: ")), int(input("Enter exponent: "))
# print("Exponental Value: ", obj.exponent(base,exp))


# n=int(input("Enter a num: "))
# print("Is Palindrome? :", obj.palindrome_checker(n))

# sentence=input("Enter your string: ")
# word=input("Enter the word to be counted: ")
# print(obj.string_counter(sentence,word))

# arr=[]
# n=int(input("Enter the array size: "))
# for num in range(n):
#     num=int(input("Enter Element: "))
#     arr.append(num)
# max_value, min_value=obj.min_max(arr)
# print("Max: ",max_value,"Min: ",min_value)

# word=input("Enter a word: ")
# print(obj.vowel_counter(word))
#print(obj.reverse_string(word))


# arr=[]
# n= int(input("Enter the number of items"))
# for i in range (n):
#     num = (input("Enter the item"))
#     arr.append(num)
# print(obj.list_add(arr,"elderberry",n))
# print(obj.list_manipulation(arr,2))


# n = int(input("Enter a num"))
# print(obj.factorial(n))
# a = int(input("Enter num1:: "))
# b = int(input("Enter num2: "))
# obj.swap_without_temp_var(a, b)
#obj.substring_removal(word,num)
#obj.stringindex_stringslicing(a)
#obj.cumulative_sum()
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# print(obj.product_Or_sum(a,b))

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine is now running!")
car_obj=Car("Camry","Toyota","2022")
car_obj.start_engine()