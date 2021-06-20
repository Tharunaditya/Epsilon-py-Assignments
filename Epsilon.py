#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#--------Square Rectangle
def square_prover(l,b): #Defined a function with parameters l and b 
    if l==b:       # checking whether the length is equal to breadth 
       return "Yes"   # if equal then returns Yes
    else:
       return "No"    #If not returns No
    
x=int(input())        # takinng the length input in int data tyoe 
y=int(input())          # taking the breadth input in int data type 
print(square_prover(x,y)) #calling our fuction by considering our x and y as arguments
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#---------VBIT Employee
def bonusmachine(s,y): #defined a funtion bonusmachine  with parameters s and y
    if y>5:             # y stands for years of service if the years of sevice greater than clg offers bonus 
        bonus=int((5/100)*s) # bonus calculation expression 
        return f"Bonus is {bonus}"    # if the years of experience is greater than 5 it will with this statement 
    else:   # if years of service is less than 5 then it returns to No bonus
        return "No Bonus"
x=int(input())  # salaary input
z=int(input()) #years of service input 
print(bonusmachine(x,z)) # calling the function by considering the x and z as arguments
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#------multiplication table
def tenmultiples(x): # defineing the function of ten multiples 
    i=0   # declaruing some variable for increment and multiplication  
    while i<10: # while that i value less then 10 the loop iterates with the i increment of 1 
        i+=1 # that is how i becomes i + 1 for each and ever ith time
        print(x*i)  # for every new i value it executes and prints the multiple of i and the x 
    return ' '  # and returns to a space otherwise it will return to the none
z=int(input())  # taking the input as z 
print(tenmultiples(z)) # calling our function by considering the z as argument 
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#-------Reverse String 39
def reverse(s): # i defined a function with name reverse with parameter s
  str= "" #then a variable assigned with empty string 
  for i in s: #using for loop i tried to take each letter one by one from the parameter string s
    str = i + str # then i added the each letter in the beginning of the empty string which returns me a reversed string 
  return str     # returned the string                                                         #after all the iterations 
  
k=str(input()) # by using k variable i tried to take the user input in string data type
print (reverse(k)) #then i called our function by considering the k as a parameter hence the work done
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#
#--------Name Age Function
def nameage(name,age): # Defining the function as nameage with parameter name and age 
    print(f'{name} {age}') # pinting the name and age together with the apace separator 
    return ' ' # returning with empty space other wise it will return to none 
x=str(input())   # taking the input of the name string through the x variable
y=int(input()) # taking the input of the age in integer data type 
print(nameage(x,y)) # calling our function by considering the x and y as arguments in the place of name and age 
#------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------#