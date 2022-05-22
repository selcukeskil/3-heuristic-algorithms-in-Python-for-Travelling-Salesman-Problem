# -*- coding: utf-8 -*-


import numpy as np 
import math as math

def objective_calculator(solution,dataset): #Calculates the objective function value (cost) of any solution (tour)
    cost = 0
    for i in range(len(solution)-2):                     
        cost += euclid_calculator(solution[i], solution[i+1],dataset)  #To the euclid_calculator function, send the cities in the solution whose objective function value will be calculated, two at a time
    
    return cost
        

def euclid_calculator(city_1, city_2, dataset): #Calculates the euclidean distance between any two cities in the dataset
    
    return math.sqrt((dataset.loc[city_1-1,"x"]-dataset.loc[city_2-1,"x"])**2 + (dataset.loc[city_1-1,"y"]-dataset.loc[city_2-1,"y"])**2) #Calculates the euclidean distance with formula using the city coordinates in the "dataset" dataframe
    
    
def city_swap(city_1,city_2,current_solution,dataset): 
    
    tour_choice=current_solution.copy()                #In these lines, an array called tour_choice is created to try the swap on that array first.
    keeper=tour_choice[city_1].copy()
    tour_choice[city_1]=tour_choice[city_2].copy()
    tour_choice[city_2]=keeper 
    
    if objective_calculator(tour_choice,dataset) < objective_calculator(current_solution,dataset): #The objective function values ​​of the new tour we tried and the previous tour are compared, checking if the new solution is better
        print("Current cost: ",objective_calculator(tour_choice,dataset))        #The objective function value of the tour, which is the better solution, is printed
        current_solution=tour_choice                                             #The better tour found is assigned to current_solution i.e. kept in that variable 
        print("Current tour:", current_solution)                                 #The new solution is printed
        print("-------------------------------------------------------------")
    return current_solution
        
    
def main(dataset): #Argument of the main function is the dataset of the coordinates of the cities in "euclidean space"
    np.random.seed(28) #You can choose random seed
    partly_initial_solution= np.random.permutation(range(1,len(dataset)+1))  #Randomly sorts the city numbers and creates the starting tour (starting solution)
    initial_solution = np.append(partly_initial_solution, [partly_initial_solution[0]]) #Adds the city at the beginning of the tour to the end of the tour to make the salesman return to where he started
    
    current_solution = initial_solution #Assigns the initial solution to the current solution 
    for k in range(10): #Trying to swap all cities with each other using nested for loops (You can change that "10" as you wish)
        for i in range(1,len(dataset)-1):
            for j in range(i+1,len(dataset)):
                current_solution = city_swap(i,j,current_solution,dataset) #The cities to be swapped in the loop are sent to the city_swap function, with the current solution and dataset
        
    print("Results:")
    print("-> Cost of best solution: ", objective_calculator(current_solution,dataset))
    print("-> Best Tour Founded: ", current_solution)    
    return(current_solution)