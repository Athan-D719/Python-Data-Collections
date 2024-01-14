def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

print("****names****")
for f in L:
    print(f)

print("****call each of them****")
for f in L:
    print(f(-2))

print("****just the first one in the list****")
print(L[0])
print(L[0](3))

'''****names****
<function square at 0x000001EF45AAC7B8>
<built-in function abs>
<function <lambda> at 0x000001EF45AAC840>
****call each of them****
4
2
-1
****just the first one in the list****
<function square at 0x000001EF45AAC7B8>
9'''
