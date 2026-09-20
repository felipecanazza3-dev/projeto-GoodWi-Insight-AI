def OUT():
    return "== OUT =="

class GW:
    hello: str
    def __init__(self,hello=''):
        self.hello=hello
    def ad(self):
        hello='hello world!'
        self.hello=hello
    def out(self):
        return self.hello
    def __str__(self):
        return f"{self.hello}"

if __name__=='__main__':
    print(OUT())
    o=GW()
    o.ad()
    print(o.out())

