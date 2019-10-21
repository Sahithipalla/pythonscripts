def my_function(a,b,c=1,d=2):
    return sum((a,b,c,d))
my_function(10,20)

def my_function(*qwer):
    return sum(qwer)
my_function(10,20,20)
def my_function(**kwargs):
    if "flowers" in kwargs:
        print("we have {}".format(kwargs["flowers"]))
    else:
        print("no flowers for you")
my_function(flowers="sun flower")

def my_function(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I will have{} {}".format(args[1],kwargs["flower"]))
my_function(2,1,7,flower="lilly",fruit="cherry")
