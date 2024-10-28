class A(object):
    def __init__(self,x,y):
        self.a =x
        self.b=y

    def test(self):
        return self.a+self.b

class B(A):
    def __init__(self,x,y):
        super().__init__(x,y)

    def test(self):
        return (super().test()*2)


[v1,v2] =list(map(int,input().split()))
obj =B(v1,v2)
print(obj.test())
