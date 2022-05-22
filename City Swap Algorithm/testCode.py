# -*- coding: utf-8 -*-


import time                    #Required library to calculate Computational Time
import pandas as pd            #Required library to use DataFrames


import citySwapAlgorithm         #Import the code of the algorithm to the test code

dataset = pd.read_csv('dataset.csv')     #Import the csv file containing the data


start_time = time.time()                 #Keeps the start time
solution = citySwapAlgorithm.main(dataset)              #Runs our algorithm with dataset as argument 
comp_time = time.time() - start_time     #Keeps the difference between the end time and the start time
print(f"-> Computational Time: {comp_time} seconds")     #Prints Computational Time
