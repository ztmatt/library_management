# li = [11, 22, 33, 1, 4, 32, 33, 22]
# l0 = list(set(li))
# l1 = sorted(l0, key=li.index)
# print(l0)
# print(l1)
# print(lambda x:x)
def func(i):
    def inner(a):
        return a*i
    return inner
foo = func(8)
print(foo(8))


