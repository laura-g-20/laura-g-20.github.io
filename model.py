import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation
import agentframework
import csv
import tkinter
import requests
import bs4

#Set up variables and empty lists
#agents are the 'sheep' moving around the 'field'. Too many makes model too slow.
#iterations are how many times the agents/sheep are moved
#neighbourhood is a distance variable that decides if 'share_with_neightbours' function is called
num_of_agents = 12
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []

matplotlib.use('TkAgg')

#Make figure variable and set size
fig = plt.figure(figsize=(9, 9))

#Fill in environment list with values from a csv
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)    
    environment.append(rowlist)

#Get initial agent x, y values from online table
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

#Create a list of agents with x and y values from external source    
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

#Agent update function. Called on each animation loop.
def update(iteration):
    fig.clear()
    
    # Move and 'eat' the environment
    random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)
        
        plt.scatter(agent.x,agent.y)
        plt.imshow(environment)
        plt.xlim(0, 99)
        plt.ylim(0, 99)

#Function that is called when the 'Run model' command is chosen
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    canvas.draw()

#Create main window and embedded matplotib canvas
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#Set up menu commands
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()
