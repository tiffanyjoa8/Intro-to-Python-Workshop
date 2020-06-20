
# A variable with an Integer (whole number) value
my_age = 21

# A variable with a String (text) value
my_name = "Tiffany"

# We can print out the content of variables in a couple of ways:
print(my_age)
print("Hello " + my_name + "!")
print("Hello {}, you are {} years old".format(my_name, my_age))
      
a = 5
b = 10
c = a * b
print (my_age)

print ("a * b = {}".format(c))
      
#task 3
def my_function(num1,num2):
    num3 = num1 * num2
    print ("The output: {}".format(num3))
    print (num1 * num2)
    
my_function(4, 5)
last = "joa"

def create_full_name(my_name, last):
  full_name = my_name.upper() + " " + last
  print("hello")  
  return full_name

result = create_full_name("Neil", "Armstrong")
print(result)

names = []

planets = ["Mercury", "Venus", "Earth", "Mars"]

print(planets)

planets.append("Jupiter")
planets.append("Saturn")

print(planets)
print(planets[1])
     
planets.insert(0, "das me")
print(planets)

for planet in planets:
  print(planet)
