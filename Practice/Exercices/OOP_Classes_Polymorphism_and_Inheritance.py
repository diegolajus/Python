class User(object): #  Parent Class

    # Parent Method Class
    def sign_in(self):
        print('logged')

    def lazy(self):
        print("Do nothing")

    def run(self):
        print("Run away")

class Wizard(User):# SubClass --> (User) as the parent I want to inherit from
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} attacking with {self.power} fire')
        User.run(self) # POLYMORPHISM : Because we are accepting User as param. in Class Wizard(User)


class Archer(User):    # (User) as the parent I want to inherit from
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'{self.name} attacking with {self.num_arrows} arrows')
        User.lazy(self) # POLYMORPHISM : Because we are accepting User as param. in Class Archer(User)


#Instanciate
wizard1 = Wizard("Medivh",50)
archer1 = Archer("Rexar",99)

#python built function isinstance() for checking

# Is wizard1 an Instance of Wizard Class? --> TRUE
print(isinstance(wizard1, Wizard))  # (instance, Class)  

# Is wizard1 an Instance of Wizard Class? --> FALSE
print(isinstance(wizard1, Archer))  # (instance, Class)  

# Is wizard1 an Instance of Wizard Class? --> TRUE
print(isinstance(wizard1, User))  # (instance, Class) 


# Examples

print(wizard1.sign_in()) # Output: 'logged' 
print(wizard1.attack()) # Output: 'Attacking with 50 fire' 
print(archer1.attack()) # Output: 'Attacking with 50 arrows' 



# Or using a function

def player_attack(char):
    char.attack()

player_attack(wizard1) # Output: 'Attacking with 50 fire' 
player_attack(archer1) # Output: 'Attacking with 50 arrows' 




# Or using a loop

for char in [wizard1,archer1]:
    char.attack()
