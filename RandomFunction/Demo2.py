

info= lambda : print("Hello Lambda function...!!!")
print(info)
# <function <lambda> at 0x016E9DF8>

print(info())
# Hello Lambda function...!!!
# None
print("========================")
result=info()
print(result)

# ===================================================

add=lambda a,b : print(a+b)
print(add(100,200))
x=add(99,101)
print(x)