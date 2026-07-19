# # String Handling
#
#
# s="Hello World"
#
# print(s)
#
# print(type(s))
#
# print(len(s))
#
# print(s.lower())
# print(s.upper())
# print(s.replace("o","x"))
# print(s.index("o"))
# print(s.count("o"))
# print(s.find("o"))
# print(s.find("x"))
# print(s.index("o"))
# # print(s.index("x"))
# x=s.split()
# print(s.split())
# print(s.split("o"))
# sep=" "
# sep.join(x)
# print(sep.join(x))
# print(s[3:8:4])
# print(s[-1:-12:-1])
# print(s[::-1])
# print(reversed(s[::-1]))




# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# Lambda function
# Anonymous function
# Single line function
# Faster than def function
# No use of print or return statement

l1=[1,2,3,4,5]
l2=[10,20,30,40,50]

a=lambda x,y: x if x>y else y

print(a(l1,l2))


# Lambda with Map:
