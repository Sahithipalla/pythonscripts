
 def greeting(name="sahi"):
     return("hello" +name)
greeting()
greeting("sahithi")

result=greeting("sahithi")
print(result)
type(result) 

def even_numbers(my_list):
    """
    It is function to return even numbers
    input:dict
    output=A dict in even numbers
    """
    enum=[]
    for numbers in my_list:
        if numbers%2==0:
            enum.append(numbers)
    return(enum)
even_numbers([1,2,3,4,5,6])
help(even_numbers)
def bmi_cal(name,height_m,weight_kg):
   """
   bmi cal to read
   input=name,height,weight
   output=bmi
   """
   bmi=weight_kg/(height_m**2)
   print("BMI:")
   print(bmi)
   if bmi<30:
        return name+"is not overweight"
   else:
        return name+"is overweight"
   bmi_cal("yasasvitha",1.75,70)







