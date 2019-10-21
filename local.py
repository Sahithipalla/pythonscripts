name="I am global"

def greeting():
#    name="I am enclosing local"
    def hello():
#        name="I am local"
        print("hello, "+name)
    hello()
greeting()   



b=100
def greeting():
    global b
    b=200
    print("value B is {}".format(b))
print(b)
greeting()
print(b)