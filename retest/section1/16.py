#16.

def mk(x):
    def mk1():
        print("decorated")
        x()
    return mk1
def mk2():
    print("ordinary")
p=mk(mk2)
p()    

Ans: mk(x) function is decorator 