'''
We are going to make an application called "Plants in Season." 

This app is going to show the best plants to grow in different times of the year. 

               PLANTS IN SEASON 

               by rav3ndust (https://rav3ndust.xyz) 

               licensed under the MIT license. 

This is the Welcome Screen.
'''
######################################################################################
import os 
import sys
import PySimpleGUI as gui
# we're going to go with a dark theme for the window. 
gui.theme('Dark')
# define the functions we are going to use 
def springPlants():     # called when the user clicks on the "Spring" button.
    os.system('python3 seasons/spring.py')
def summerPlants():     # called when the user clicks on the "Summer" button. 
    os.system('python3 seasons/summer.py')
def autumnPlants():     # called when the user clicks on the "Autumn" button.
    os.system('python3 seasons/autumn.py')
def winterPlants():     # called when the user clicks on the "Winter" button.
    os.system('seasons/winter.py')
def exitButton():            # called when the user clicks on the "Exit" button.
    sys.exit()
######################################################################################
'''
Now, we're going to build out the GUI. 

We want it to be simple and thoughtfully laid out. 

This is the Welcome Screen, so we should welcome the user, tell them a brief summary of what the app is all about, and let them choose which season they want to see. 

The app should then present them with the best plants to grow in that season, and a little information on the plant.
'''
# now, we can define the layout of the window. 
welcomeLayout = [[gui.Text("Hi there - welcome to Plants in Season.")],
                [gui.Text("This is a project by Raven's Ridge at https://ravensridge.xyz.")],
                [gui.Text("This app aims to show you the best plants to grow your garden all throughout the year. Select the season you'd like to learn about to see some of the very best plants to grow in that season.")],
                [gui.Text("Click a season to begin - and happy gardening!")],
                [gui.Button("Spring", springPlants), gui.Button("Summer", summerPlants), gui.Button("Autumn", autumnPlants), gui.Button("Winter", winterPlants)],
                [gui.Button("Exit", exitButton)]]
# now, we can build the window.
welcomeWindow = gui.Window("Plants in Season", welcomeLayout)
# and now, we can show the window.
welcomeWindow.Finalize()
welcomeWindow.Read()
######################################################################################