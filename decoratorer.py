def sub (a,b):
    print(a-b)
def sub_d(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
sub=sub_d(sub)
sub(2,4)