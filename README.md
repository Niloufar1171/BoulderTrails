# BoulderTrails

Take home assigment

The Problem
We the North American team who are split across Boulder and Montreal often enjoy spending time in the outdoors. Some of us would like to bike while some of us are happy just walking, some of us like to challenge ourselves with difficult hikes while some of us would like to ease in slowly.

The good part is that the Boulder county releases data about the trails as open data. Your assignment is to help us find a trail that suits our requirement.

This is a freeform assignment. You can write a web API that returns a set of trails. You can write a web frontend that visualizes the trails. We also spend a lot of time in the shell, so a CLI that gives us a couple of options would be great.

The only requirement for the assignment is that it allow us to filter the trails by at least 2 criteria. You can choose to pivot the choices based on any of the options in there - bike trail vs walking trail, with the option of fishing vs not etc.

Feel free to tackle this problem in a way that demonstrates your expertise of an area or takes you out of your comfort zone.

Boulder's trail head data is located here you can download a CSV of the data from that site.

Solution
Set up configuration environement
Convert csv data into json
Create an end point to test everything is working on local
Installing pip 24.2
pip install Flask
pip install Flask-restful
Create a key,value pair map to manipulate the data.
To do
a List of key valiue pair map in the model folder
a file for mapping each Entitiy for filtering
