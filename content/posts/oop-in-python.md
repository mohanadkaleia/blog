Title: OOP in Python
Date: 2018-01-27 06:18
Author: mohanad
Category: Article, Code
Tags: concepts, OOP
Slug: oop-in-python
Status: published
Cover: https://mohanad.kaleia.io/wp-content/uploads/2018/01/OOP-2.png
![](https://mohanadkaleia.com/wp-content/uploads/2018/01/OOP-2.png){.aligncenter .size-full .wp-image-784 width="601" height="281"}

During my Master as a Computer Engineer, I worked with Python for data analysis, machine learning and deep learning projects. Python becomes more and more popular especially for writing AI and machine learning algorithms. But that is not the only thing that makes it great programming language, Python is just as C++ and Java supports Object Oriented Programming OOP. Which makes it suitable not just for research purposes but also for large scale applications.

[In this article I will discuss OOP concepts in Python. As well as, we will highlight the differences in OOP between C++ and Python as a comparison between the two.]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

<div>

[Python is designed from the beginning to support Object Oriented Programming concepts, providing the ability to build  large scale applications. If you don’t know or you kind of don’t remember the concepts of OOP we will review them here briefly in this article. OOP concepts are divided into 5 aspects as follow:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

-   [**Class**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[: represents a prototype for an object. This prototype describe object’s attributes and behavior]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}
-   [**Object**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[: an instance of its defined class]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}[prototype). An object can hold values for attributes and execute functions defined by its prototype. ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}
-   [**Abstraction**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[: with abstraction a class can hide some of its details and expose only specific information to the outside ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}
-   [**Inheritance**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[: one of most important aspects in OOP is inheritance for code reusability. ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}
-   [**Polymorphisim**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[: means the ability to have same function with different behavior.]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

<div>

</div>

<div>

[We will go through these concepts one by one with an example for each of them. ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

</div>

<div>

<div>

[**Class**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} {#class usually-unique-id="795834399202508773348651"}
=================================================================================================================================================

</div>

<div>

[In python a class can be created using the keyword class, as follow: ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

``` {.prettyprint}
class ClassName:
   'Optional class documentation string'
   class_suite
```

</div>

<div>

</div>

<div>

[The three lines above describe how we can create new class in Python, where we start with the keyword]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [“]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-ldquo}[class” then the class name we want with a semicolon. Just right after the definition the class we can write a description about it as in line number 2.The documentation can be accessed using the pre-defined class attribute \_\_doc\_\_. The rest will be the class body that defines the class attributes and functions. We will create now an example where we will create a class that represents a prototype of vehicle.]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

</div>

<div>

``` {.prettyprint}
class Vehicle:
        'Vehicle class'

        # Class variable
        count = 0

        # Constructor
        def __init__(self, make, color, tag):
                self.make = make
                self.color = color
                self.tag = tag
                Vehicle.count += 1

        # Class function
        def printTag(self):
                print self.tag

        def printCount(self):
                print "Total number of created Vehicles %d" % Vehicle.count
```

</div>

<div>

<div>

[The variable]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [“]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-ldquo}[count” in line 5 represents a class variable that is shared between all instances. Function \_\_init\_\_ represents the constructor function. This is a special method that is called first thing when create an object. It takes the parameter ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[**self**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[ as first parameter,]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}[all functions should contains ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[**self**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[ as a first argument). Where, ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[**self**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[ points to the object calling the method. ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

</div>

<div>

[Both methods have ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[**self**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[ as their first argument. C++ and Java both have a hidden first argument in their class methods, which points to the object that the method was called for and can be accessed using the keyword ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[**this**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[. Python methods also use a reference to the current object, but when you are ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[*defining*]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}[ a method you must explicitly specify the reference as the first argument. No need to include it when calling a method from an object.]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

</div>

<div>

[Instance variables or attributes are defined inside of a method. ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

</div>

<div>

[Here is how we create an instance of the class we just created: ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

</div>

<div>

``` {.prettyprint}
v1 = Vehicle('Mazda', 'Golden', 123456)
v2 = Vehicle('Toyoya', 'White', 987654321)

v1.printTag()
v2.printCount()
# Read object's attribute
print v1.make

# Write object attribute
v1.color = 'Red'

# Print the documentation of Vehicle's Class
print Vehicle.__doc__
```

</div>

<div>

 [The output of the previous code: ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} 

``` {.prettyprint}
123456
Total number of created Vehicles 2
Mazda
An example for creating Class in Python
```

</div>

<div>

<div>

[**Inheritance **]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} {#inheritance usually-unique-id="460032109328526802090971"}
========================================================================================================================================================

</div>

<div>

[In Python inheritance is done by write the base class(s) between parentheses as follow: ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

</div>

<div>

``` {.prettyprint}
class SubClass(ParentClass1 [,ParentClass2,...]):
  'Optional class documentation string'
   class_suite
```

</div>

<div>

[Where inheritance is very useful for code reusability. As an example, we will create another class that inherits the base class Vehicle we created previously. We will name this class Truck. ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

![User-uploaded image: image.png](https://paper.dropbox.com/ep/redirect/image?url=https%3A%2F%2Fd2mxuefqeaa7sj.cloudfront.net%2Fs_B3063C0BA4037C8144261290720D92A4BC683786E0FE12D462268244990A7B76_1517009033386_image.png&hmac=JgOVrb620DHE98U5YJ48St9G7leSxmVjpRaizhXo7SM%3D&width=1490)

</div>

<div>

``` {.prettyprint}
class Truck(Vehicle):
        def __init__(self, make, color, tag, numWheels):
                self.numWheels = numWheels
                Vehicle.__init__(self, make, color, tag)

        def printNumberOfWheels(self):
                print self.numWheels
                
        def printTag(self):
                print "Truck Vehicle with tag %d" % self.tag
```

</div>

<div>

  

``` {.prettyprint}
truck1 = Truck('Toyoya', 'Yellow', 123, 8)
truck1.printCount()
truck1.printNumberOfWheels()
```

</div>

<div>

[Output:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

 

``` {.prettyprint}
Total number of created Vehicles 3
8
```

</div>

<div>

<div>

[In the constructor of the new subclass Truck, we called the init method of the parent class to initialize it with thee needed parameters. Inheritance allows subclasses to call method from their parents as we can see that the truck1 object can call function from Vehicle class]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [“]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-ldquo}[print Count()”.]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

</div>

<div>

[**Overloading**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} {#overloading usually-unique-id="436644805142917165108053"}
=======================================================================================================================================================

</div>

<div>

[Overloading allows us to redefine a function with different types of parameters. We will create another class for passenger vehicles and we will overload the method printTag() as folllow:]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

</div>

<div>

</div>

<div>

``` {.prettyprint}
class Car(Vehicle):
        def __init__(self, make, color, tag, numPassenger):
                self.numPassenger = numPassenger
                Vehicle.__init__(self, make, color, tag)

        def numPassenger(self):
                print self.numPassenger

        def printTag(self):
                print "Passenger vehicle with tag %d" % self.tag
```

</div>

<div>

</div>

<div>

[We see in the]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [“]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-ldquo}[Car” class we have the function printTag same function in Truck class, but with different implementation where they print different text. Here we test the code we just wrote: ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

``` {.prettyprint}
truck1 = Truck('Toyoya', 'Yellow', 123, 8)
truck1.printTag()

car = Car('Mazda', 'White', 1, 4)
car.printTag()
```

</div>

<div>

 [Output: ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

``` {.prettyprint}
Truck Vehicle with tag 123
Passenger vehicle with tag 1
```

</div>

<div>

<div>

[In addition, we can overload predefined functions]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}[e.g., \_\_init\_\_, \_\_del\_\_). ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

<div>

[**Data Hiding:**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} {#data-hiding usually-unique-id="251265233555039317213752"}
========================================================================================================================================================

</div>

<div>

[Data hiding is used to hide or make some of class attributes or functions to be private. This is extremely useful when making a library to be used from other users and you don’t want to expose the  details of this library. Python support data hiding]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [(]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-lparen}[Abstraction) by adding double underscore prefix before the attribute or the functions desired to be secret.  A secret attribute cannot be accessed directly out of the class, you need to write a getter function in order to get a secret variable.]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

``` {.prettyprint}
class SecretClass:
        __secret = 0
        
        def __init__(self):
                SecretClass.__secret += 1
        
        def getSecret(self):
                print SecretClass.__secret
                
s = SecretClass()
s.getSecret()
print s.__secret
```

</div>

<div>

[The last line will cause an error of unknown attribute. This is becuase we defined]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} [“]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .h-ldquo}[secret” to be private.]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

<div>

[**Overriding:**]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z} {#overriding usually-unique-id="419801474254299118523153"}
=======================================================================================================================================================

</div>

<div>

[Overriding means to rewrite the behavior of a function inherited from a base class in the subclass. The following is an example of overriding: ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}

</div>

<div>

``` {.prettyprint}
class parentClass:
  def doSomething(self):
    print "I'm parent class doing something"
    
class subclass(parentClass):
  def doSomething(self):
    print "I'm subclass class doing different thing"
    
c = subclass()
c.doSometing()
```

</div>

</div>

<div>

The output:

</div>

<div>

``` {.prettyprint}
I'm subclass class doing different thing
```

</div>

<div>

**[Resources: ]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z}**

</div>

1.  [<https://www.tutorialspoint.com/python/python_classes_objects.htm>]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .url}
2.  [<https://www.tutorialspoint.com/cplusplus/cpp_object_oriented.htm>]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .url}
3.  [<http://www.ddegjust.ac.in/studymaterial/mca-3/ms-17.pdf>]{.author-d-iz88z86z86za0dz67zz78zz78zz74zz68zjz80zz71z9iz90z9z84ztz82zbz73z7e6z82zz77zz87zz69zz80zz66zz74zlqbz70zmz73zwmz68z4umxyz79z .url}
4.  https://www.flaticon.com (I got some of the icon from here)

</div>

 

By Mohanad Shab Kaleia
