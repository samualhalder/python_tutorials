a=11
def fun1():
    a=14
    def f2():
        print(a)
    f2()
fun1()
print(a)
