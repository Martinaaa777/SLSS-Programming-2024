# big ideas:
# - classes allow us to couple data and functions together
# - Objects are the actual representation of the classes in our Python scripts.


#create a pokeman class: this represents a pokemon
class pokemon: # use a capital letter for class name
    def __init__ (self):
        """a special metod (function) called the
         Costructor. cointains all the properties
        that describe a pokemon."""
        self.name = ""
        self.weight= 0
        self.id = 0
        self.height = 0
        self.type= "normal"

        print ("a new pokemon is born")
        

# create 2 pokemon using our class
# make one pokemon that is pikachu
pokemon_one= pokemon()
#change some proprities (its name)
print (pokemon_one.name)
pokemon_one.name = "pikachu"
print (pokemon_one.name)
# change its id
pokemon_one.id = 25
print (pokemon_one.id)
#change type
pokemon_one.type = "eletric"
print (pokemon_one.type)


# make one pokemon of your choise
# store it in a variable called pokemon_two, name= squirtle, id =4, type= water
 

pokemon_two= pokemon ()
pokemon_two.name = "squirtle"
pokemon_two.id = 4
pokemon_two.type = "water"
print (pokemon_two.name )
print (pokemon_two.id )
print (pokemon_two.type)