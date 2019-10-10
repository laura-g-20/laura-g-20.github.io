# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:24:35 2019

@author: laura
"""
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation
import agentframework
import csv
import tkinter
import requests
import bs4

num_of_agents = 12
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []

matplotlib.use('TkAgg')

#Downloading table from online
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

#setting figure size
fig = plt.figure(figsize=(9, 9))
#ax = fig.add_axes([0, 0, 1, 1])

#importing in.txt csv and putting the values into lists
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    
    environment.append(rowlist)
      
# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

#...
def update(iteration):
    fig.clear()
    
    # Move the agents-edit
    random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)
        
        plt.scatter(agent.x,agent.y)
        plt.imshow(environment)
        plt.xlim(0, 99)
        plt.ylim(0, 99)

# Create function to 'run' the model
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    canvas.draw()
# Create main window and embedded matplotib canvas
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()


#Make the animated plot.
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)    
#plt.show()

