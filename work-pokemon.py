# martina panosetti

# Create a new child-class of pokemon for the type of your choice
#   - create a new child class
#   - create a constructor and set the default values for its properties
#       - i.e. its name, id, type, etc.
#   - create a new method for its attack

# create a class and the characteristics of a pokemon
class GloomPokemon:  
    def __init__( self, name = "Gloom", weight=8.6, id=44, height=0.8, type ="grass poison"):
        self.name = name 
        self.weight= weight
        self.id = id
        self.height = height
        self.type= type

        print (self.name)
        print (self.weight)
        print (self.id)
        print (self.height)
        print (self.type)

# create a new attack
    def new_attack (self): 
        print (f"{self.name} used acid!")