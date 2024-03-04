# # regex
# # ex1
# import re
# def match_ab_pattern(text):
#     pattern = 'ab*'
#     if re.search(pattern, text):
#         return "Found a match!"
#     else:
#         return "Not matched!"
# print(match_ab_pattern(input()))


# # ex2
# import re
# def a_2to3(txt):
#     pattern = 'ab[2,3]'
#     if re.search(pattern, txt):
#         return "'a' followed by two to three 'b'"
#     else:
#         return 'no'
# print(a_2to3(input()))

# # ex3
# import re
#
# def underscore(text):
#     pattern = r'[a-z]+_[a-z]+'
#     matches = re.findall(pattern, text)
#     return matches
# text =input()
# print(underscore(text))


# # ex4
# import re
#
# def upper_followed_by_lowers(text):
#     pattern = r'[A-Z][a-z]+'
#     matches = re.findall(pattern, text)
#     return matches
# text =input()
# print(upper_followed_by_lowers(text))

# # ex5
# import re
# def a_end_b(txt):
#     x = re.findall('a.*b$', txt)
#     if x:
#         print('yes')
#     else:
#         print('no')
# a_end_b(input())


# # ex6
# import re
#
# def replace_with_colon(text):
#     return re.sub(r'[ ,.]', ':', text)
# text = input()
# print(replace_with_colon(text))


# # ex7
# import re
# def snake_to_camel(snake_str):
#     return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), snake_str)
# snake_case_str = "this_is_snake_case"
# camel_case_str = snake_to_camel(snake_case_str)
# print(camel_case_str)

# # ex8
# import re
#
# def split_at_uppercase(s):
#     return re.findall(r'[A-Z][^A-Z]*', s)
#
# # Example usage
# test_str = "SplitAtUpperCaseLettersInThisString"
# print(split_at_uppercase(test_str))

# # ex9
# import re
#
# def insert_spaces(s):
#     return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
# test_str = "InsertSpacesBetweenCapitalizedWordsLikeThis"
# print(insert_spaces(test_str))

# # ex10
# import re
#
# def camel_to_snake(camel_str):
#     snake_str = re.sub(r'(?<=[a-z])([A-Z])', r'_\1', camel_str)
#     return snake_str.lower()
# camel_case_str = "ThisIsCamelCase"
# snake_case_str = camel_to_snake(camel_case_str)
# print(snake_case_str)
