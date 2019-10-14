[Back](index.md)

I was tasked with building an Agent Based Model as a way to learn the basics of python, following the instructions on this [website](https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl/) from Leeds University.

The code is commented and should make sense by itself, but here is a quick description in people-friendly language of what the model does. A fairly easy way to think of it is that we are creating a list of 'sheep' (agents), who move around a 'field' (environment) dependant on a random number, eating 'grass' (the value of the environment) as they go around. The amount of grass that the sheep eat changes depending on how close they are to each other and how much grass is available. 

The final stage of the model is an animated GUI that shows the sheep moving around their field, changing the amount of grass beneath them as they go! Dive into the commented .py files to see this all in action.

The code is comprised of two files: a runtime file, [`model.py`](https://github.com/laura-g-20/laura-g-20.github.io/blob/master/model.py), and a class to describe the Agent, [`agentframework.py`](https://github.com/laura-g-20/laura-g-20.github.io/blob/master/agentframework.py).

The files have been run and tested using Spyder (Python 3.7) on a Windows machine. The graphics backend has to be set to TKinter for the GUI to display correctly. The only other file you should need to run it is [in.txt](https://github.com/laura-g-20/laura-g-20.github.io/files/3722436/in.txt).

