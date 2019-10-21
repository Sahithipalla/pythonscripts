#conversion odf numbers
num=int(input("enter a number:"))
print("Binary value is:{}".format(bin(num)))
print("Octal value is:{}".format(oct(num)))
print("Hexadecimal value is:{}".format(hex(num)))

#removing vowels
vowels=('a','e','i','o','u')
message=input("Enter message:")
new_message=""
for letters in message:
    if letters  in vowels:
        new_message=new_message+letters
print("message with vowels {}".format(new_message))
#encryption using dict
my_dict={'A':'E','B':'F','C':'G','V':'J','S':'W',
         'N':'M','I':'U','O':'R','X':'F','Z':'B',
         'L':'D','1':'3','4':'5','0':'2','6':'7',
         '8':'0','9':'1',' ':' '}
msg=input("Enter msg:").upper()
encrypted=""
for l in msg:
    if l in my_dict:
        encrypted=my_dict[l]
    else:
        encrypted+=l
        print(encrypted.lower())