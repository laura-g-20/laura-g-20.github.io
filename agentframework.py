import random

#This represents the 'agent' part of an Agend Based Model. 
#It contains methods to set an initial position within an environment
#and to move within/modify that environment.
class Agent():
    def __init__ (self, environment, agents, y = None, x = None):   
        if x is None:
            self.x = random.randint(0,100)
        else:
            self.x = x
        if y is None:
            self.y = random.randint(0,100)
        else:
            self.y = y       
        self.environment = environment
        self.agents = agents
        self.store = 0
    
    #Move the agents     
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
    
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
    #This function changes the environment by transferring values
    #from the environment to the agent. It won't do this if the
    #environment is almost depleted.
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10         
    
    #This function shares resources gathered from the environment (in
    #the 'eat()' method) to nearby agents, where 'Nearby' is defined by
    #the 'neighbours' variable (expressed as a distance threshold).
    #Resources are shared evenly between agents(e.g. if agent A has
    #50 and agent B has 10, both would end up with 30 each).
    def share_with_neighbours(self, neighbourhood):   
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #Uncomment this to check that sharing is working
                #print("sharing " + str(dist) + " " + str(ave))

    #Calculate distance between two agents
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5    
