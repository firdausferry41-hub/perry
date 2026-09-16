#PYTHON FUNCTION#
# function call#
def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')


#function arguments#
def greet(name):
    print("Hello", name)

# pass argument
greet("John")


#function to add two numbers#
# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)


#return statement#
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)


#pass atatement#
def future_function():
    pass

# this will execute without any action or error
future_function()  


#library function#
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)

#PYTHON FUNCTION ARGUMENTS#
#function arguments#
def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(2, 3)

#with default values#
def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a = 2)

# function call with no arguments
add_numbers()


#keyword argument#
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')


#with arbitrary arguments#
# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)



#PYTHON VARIABLE SCOPE#
def add_numbers():
    sum = 5 + 4

#local variable#
def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function


#global variable#
# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)


#nonlokal variable#
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()


#PYTHON GLOBAL KEYWORD#
#acces and modify#
c = 1 # global variable

def add():
    print(c)

add()

# Output: 1

# global variable
# c = 1 

# def add():

#      # increment c by 2
#     c = c + 2

#     print(c)

# add()

# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()

# Output: 3 


#PYTHON RECURSION#
#example
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


#PYTHON MODULES#
# Python Module addition

def add(a, b):

   result = a + b
   return result

# import module by renaming it
import math as m

print(m.pi)

# Output: 3.141592653589793

# import only pi from math module
from math import pi

print(pi)

# Output: 3.141592653589793

# import all names from the standard module math
from math import *

print("The value of pi is", pi)

#PYTHON PACKAGE#


#PYTHON MAIN FUNCTION#
def main():
    print("Hello World")

if __name__=="__main__":
    main()




#PYTHON FILES#
#PYTHON DIRECTORY AND FILES MANAGEMENT#
import os

folder = "data_saya"

# Membuat folder jika belum ada
if not os.path.exists(folder):
    os.mkdir(folder)

while True:
    print("\n=== DIRECTORY AND FILE MANAGEMENT ===")
    print("1. Lihat isi folder")
    print("2. Buat file")
    print("3. Baca file")
    print("4. Hapus file")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\nIsi folder:")
        for item in os.listdir(folder):
            print("-", item)

    elif pilihan == "2":
        nama = input("Masukkan nama file: ")
        isi = input("Masukkan isi file: ")

        path = os.path.join(folder, nama)

        with open(path, "w") as file:
            file.write(isi)

        print("File berhasil dibuat.")

    elif pilihan == "3":
        nama = input("Masukkan nama file: ")
        path = os.path.join(folder, nama)

        if os.path.exists(path):
            with open(path, "r") as file:
                print("\nIsi file:")
                print(file.read())
        else:
            print("File tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Masukkan nama file: ")
        path = os.path.join(folder, nama)

        if os.path.exists(path):
            os.remove(path)
            print("File berhasil dihapus.")
        else:
            print("File tidak ditemukan.")

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")


#CSV FILES#
import csv

# Menulis CSV
with open("mahasiswa.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["NIM", "Nama", "Jurusan"])
    writer.writerow(["001", "Andi", "Informatika"])
    writer.writerow(["002", "Budi", "Sistem Informasi"])
    writer.writerow(["003", "Citra", "Informatika"])

print("Data berhasil dibuat.\n")


# Membaca CSV
print("=== DATA MAHASISWA ===")

with open("mahasiswa.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("NIM     :", row["NIM"])
        print("Nama    :", row["Nama"])
        print("Jurusan :", row["Jurusan"])
        print()

#READING CSV FILES IN PYTHON#
import csv

with open("mahasiswa.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

#WRITING CSV FILES IN PYTHON#
import csv

with open("mahasiswa.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["NIM", "Nama", "Jurusan"])
    writer.writerow(["001", "Andi", "Informatika"])
    writer.writerow(["002", "Budi", "Sistem Informasi"])

print("File CSV berhasil dibuat!")