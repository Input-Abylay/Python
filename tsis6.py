# # ex1
# from functools import reduce
#
# def multiply_numbers_in_list(numbers_list):
#     result = reduce(lambda x, y: x * y, numbers_list)
#     return result
# numbers_list = [1, 2, 3, 4, 5]
# result = multiply_numbers_in_list(numbers_list)
# print(result)


# # # ex2
# a = input()
# up = list(filter(lambda x: x.isupper(), a))
# low = list(filter(lambda x: x.islower(), a))
# print(len(up), len(low))



# # ex3
# a = input().replace(" ", "").lower()
# if a == a[::-1]:
#     print('Pali')
# else:
#     print('not pali')

# # ex4
# import time
# from math import sqrt
#
# def delayed_square_root(number, delay_ms):
#     delay_s = delay_ms / 1000
#     time.sleep(delay_s)
#     result = sqrt(number)
#     return result
#
# number = int(input())
# delay_ms = int(input())
#
# result = delayed_square_root(number, delay_ms)
# print(f"Square root of {number} after {delay_ms} milliseconds is {result}")


# # ex5
# b = (1,2,' ',True)
# c = (1,2,'',True)
# print(all(b), all(c))


# Python Directories and Files exercises

# #ex1
# import os
#
# def list_directories(path):
#     try:
#         directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
#         print("Directories in '{}':".format(path))
#         for directory in directories:
#             print(directory)
#     except FileNotFoundError:
#         print("The specified path does not exist.")
#
# def list_files(path):
#     try:
#         files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
#         print("Files in '{}':".format(path))
#         for file in files:
#             print(file)
#     except FileNotFoundError:
#         print("The specified path does not exist.")
#
# def list_all(path):
#     try:
#         entries = os.listdir(path)
#         print("Directories and files in '{}':".format(path))
#         for entry in entries:
#             print(entry)
#     except FileNotFoundError:
#         print("The specified path does not exist.")
#
# # Example usage:
# path = input("Enter the path to list contents: ")
#
# print("\nListing only directories:")
# list_directories(path)
#
# print("\nListing only files:")
# list_files(path)
#
# print("\nListing all directories and files:")
# list_all(path)


# # ex2
# import os
#
#
# def check_access(path):
#     if os.path.exists(path):
#         print(f"'{path}' exists.")
#     else:
#         print(f"'{path}' does not exist.")
#         return
#
#     if os.access(path, os.R_OK):
#         print(f"'{path}' is readable.")
#     else:
#         print(f"'{path}' is not readable.")
#
#     if os.access(path, os.W_OK):
#         print(f"'{path}' is writable.")
#     else:
#         print(f"'{path}' is not writable.")
#
#     if os.access(path, os.X_OK):
#         print(f"'{path}' is executable.")
#     else:
#         print(f"'{path}' is not executable.")
#
#
# path = input("Enter the path to check access: ")
# check_access(path)


# # ex3
# import os
#
#
# def test_path(path):
#     if os.path.exists(path):
#         print(f"The path '{path}' exists.")
#
#         directory, filename = os.path.split(path)
#
#         if directory:
#             print(f"Directory portion: {directory}")
#         else:
#             print("No directory portion.")
#
#         if filename:
#             print(f"Filename portion: {filename}")
#         else:
#             print("No filename portion.")
#     else:
#         print(f"The path '{path}' does not exist.")
#
#
# path = input("Enter the path to test: ")
# test_path(path)



# # ex4
# def count_lines(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
#             number_of_lines = len(lines)
#             print(f"The number of lines in the file is: {number_of_lines}")
#     except FileNotFoundError:
#         print("The file was not found. Please check the file path.")
#
# file_path = input("Enter the path to the text file: ")
# count_lines(file_path)


# # ex5
# def write_list_to_file(file_path, my_list):
#     try:
#         with open(file_path, 'w') as file:
#             for item in my_list:
#                 file.write("%s\n" % item)
#         print(f"List has been successfully written to {file_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# my_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
# file_path = 'my_list_file.txt'
#
# write_list_to_file(file_path, my_list)


# # ex6
# import string
#
# def generate_text_files():
#     for letter in string.ascii_uppercase:
#         file_name = f"{letter}.txt"
#         try:
#             with open(file_name, 'w') as file:
#                 pass
#             print(f"Created {file_name}")
#         except Exception as e:
#             print(f"An error occurred while creating {file_name}: {e}")
#
# generate_text_files()


# # ex7
# def copy_file(source_path, destination_path):
#     try:
#         with open(source_path, 'r') as source_file:
#             with open(destination_path, 'w') as destination_file:
#                 content = source_file.read()
#                 destination_file.write(content)
#         print(f"Contents copied from {source_path} to {destination_path}")
#     except FileNotFoundError:
#         print("The source file does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# source_path = 'Lab2.txt'
# destination_path = 'Lab3.txt'
#
# copy_file(source_path, destination_path)

# # ex8
# import os
#
#
# def delete_file(file_path):
#     if not os.path.exists(file_path):
#         print(f"The file '{file_path}' does not exist.")
#         return
#
#     if not os.access(file_path, os.W_OK):
#         print(f"The file '{file_path}' is not accessible or cannot be deleted due to permissions.")
#         return
#
#     # Attempt to delete the file
#     try:
#         os.remove(file_path)
#         print(f"The file '{file_path}' has been successfully deleted.")
#     except Exception as e:
#         print(f"An error occurred while trying to delete the file: {e}")
#
#
# file_path = input("Enter the path of the file to delete: ")
# delete_file(file_path)