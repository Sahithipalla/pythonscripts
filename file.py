%%writefile test.txt
Hello sahithi
how are you
where are you

my_file=open("test.txt")
my_file.read()

my_file.seek(0)
my_file.read()
my_file.seek(0)
my_text=my_file.read()
my_text
my_file.seek(0)
my_file.readlines()

my_file.close()pwd
pwd

my_file=open('C:/Users/NcodeIT/test.txt')
my_file.read()
%%writefile test2.txt
sahithi
sahi
sai
supriya
with open("test2.txt",mode="r") as f:
    print(f.read())
with open("test2.txt",mode="a") as f:
    f.write("\nsahuu")
with open("test2.txt",mode="w") as f:
    f.write("It is based on marvel comics")
with open("test2.txt",mode="w+") as f:
    f.write(" i am sahithi")
    with open("test2.txt",mode="r") as f:
    print(f.read())
    
        
    
    
    
