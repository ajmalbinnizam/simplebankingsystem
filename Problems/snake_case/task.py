# Python3 program to convert string  
# from camel case to snake case 


# def change_case(str):
#     res = [str[0].lower()]
#     for c in str[1:]:
#         if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#             res.append('_')
#             res.append(c.lower())
#         else:
#             res.append(c)
#
#     return ''.join(res)
#
#
# str = input()
# print(change_case(str))

# -------------------
# import re
# print('_'.join(element.lower() for element in re.findall('[a-zA-Z][^A-Z]*', input())))

string = input()

# new_string = []
# for ch in string:
#     if ch.islower():
#         new_string.append(ch)
#     else:
#         new_string.append('_')
#         new_string.append(ch.lower())
#
# print(''.join(new_string))


a = input()
z = ""
for x in a:
    if x.isupper():
        z = z + "_" + x.lower()
    else:
        z += x
print(z)
