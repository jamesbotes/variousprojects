import random

#create the human Class
class Human:
    # in order to have methods the class will need a constructor
    def __init__(self, premature = False, disabled = False, dead = False):
        self.premature = premature
        self.disabled = disabled
        self.dead = dead
        
        if self.premature == True: #is premature then the weight of the baby will be catagorised into weight calsses
            self.weight = random.uniform(0.45, 2.00)
            self.disabled = random.choice([True, False])
        else:
            self.weight = random.uniform(2.01, 4.00)
        #Assign a Sex to the child randomly
        sexes = ['M','F','T']
        self.gender = sexes[random.randint(-1, len(sexes)-1)]
       
        #sex = ([random.choice(sexes) for n in sexes]) #Failed attempt       
        #for sex in sexes: #Sexes are the iterable MFT #Failed Attempt
         #   self.gender = sex
           #self.gender 
        #self.gender = "M"

    def kill(self):
        if self.dead == True:
            print("Already dead buddy")
        else:
            self.dead = True

    def disable(self,damage):
        if (self.disabled == True and damage < 5):
            print("You are already disabled")
        elif (self.disabled == True and damage > 5):
            self.kill() #This is how you call anothe method inside this class
        elif (self.disabled == False and damage > 8):
            self.kill()           
        else:            
            self.disabled = True


        
    
    #destroy the entity
    def __del__(self):
        print("Now Dead")
    
    #def __int__(self,gender,weight): #States
    #    self.gender = gender
    #    self.weight = weight

        
#behaviours / methods
    # def walk(self):
    # Sit
    # Masturbate
    # Disable
    # Choose a religion
    # Choose a Political party
    # Make Friends / enemies
    # Destruct
