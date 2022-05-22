# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import time                    #Required library to calculate Computational Time
import random


dataset = pd.read_csv('dataset.csv')     #Import the excel file containing the data

cities=np.array(dataset)


def calculate_distance(cities , solution):
    solution_for_distance_calculation = np.append(solution, [solution[0]], axis=0) #Appends the city index at the beginning of the solution array to the end of the array
    distance = 0
    next_city_index_founder=0 
    
    for i in solution_for_distance_calculation: #i will hold first city indexes
        next_city_index_founder += 1
        if next_city_index_founder < len(solution_for_distance_calculation):
            next_city_index=solution_for_distance_calculation[next_city_index_founder] #Find the second city indexes here
            distance += np.sqrt(((cities[next_city_index,0]-cities[i,0])**2)+((cities[next_city_index,1]-cities[i,1])**2)) #First city and second city indexes are used when calculating euclidean distance
            
    return distance

def parent_selection(population, number_of_pairs_M):
    current_parents = []
    
    #Parent selection from a population
    parent_counter = 1
    
    while parent_counter <= 2*number_of_pairs_M: #We will select twice as many parents as the desired number of parent "pairs" i.e. M, so a parent will be selected every time this loop is iterated   
        
        random_float = random.uniform(0,population["fitness"].sum()) #A float number is randomly selected in the range of 0 and the sum of fitness values
        cumulative_counter = 0 #Variable to assign the larger number in the cumulative test
    
        for solution, fitness in population.itertuples(index=False): 
            
            cumulative_counter_copy = cumulative_counter   #cumulative_counter_copy is the variable to assign the smaller number in the cumulative test   
            cumulative_counter += fitness 
            
            if cumulative_counter_copy <= random_float <= cumulative_counter:   #If the randomly generated float number is in the cumulative range, the parent in question is selected
                
                append_checker = True #But first, check if the solution in question is already in the current parent list
                for parent in current_parents:
                    if parent is solution:
                        append_checker = False
                        
                        
                if append_checker == True: #If the solution in question is not found in the current parent list, it is appended
                    current_parents.append(solution)        
                    parent_counter += 1
    
    return current_parents


def crossover(current_parents, crossover_probability):
    children = [] #Children created with crossover will be kept in this list        
    for parent_index_holder in range(1, len(current_parents)): #Loop created to iterate from the second parent
        if random.uniform(0,1) < crossover_probability: #Crossover to parent pairs with the probability specified in the crossover_probability argument
            
            parent_1 = current_parents[parent_index_holder-1]
            parent_2 = current_parents[parent_index_holder]
            
            left_bound = random.randint(1, len(current_parents[0])) #left border of crossover is randomly determined
            right_bound = random.randint(left_bound, len(current_parents[0])) #right border of crossover is randomly determined
            
            #Child creation as a result of crossover is done here
            child =np.array([]) #An empty array is created to create its child
            for j in range(left_bound): #The part of the child from the beginning to the left bound comes from parent 1
                child = np.append(child, parent_1[j])
            
            for k in range(left_bound,right_bound): #The part of child between left bound and right bound comes from parent 2
                child = np.append(child, parent_2[k])
                
            for l in range(right_bound, len(parent_1)): #The part of the child from the right bound to the end comes from parent 1
                child = np.append(child, parent_1[l])
            
            #Mappings for currently created children are created here
            maps_list = []
            for m in range(left_bound, right_bound):
                maps_list.append([parent_1[m],parent_2[m]])
            
            #Fix the infeasible child here
            child = infeasible_child_fixer(child, maps_list)
            
            #Created child are appended to the children array
            children.append(child) 
    
    return children
                
def infeasible_child_fixer(child, maps_list):
    #print("Mappings: ",maps_list)              #You can print mappings for current child if you want
    #print("Ve child ilk hali bu: " , child)    #You can print current child before fixing          

    i=1
    while i==1:        
        
        controlled_city_index_holder = -1
        for controlled_city in child: #The number of each city in child will be checked
            controlled_city_index_holder += 1    
            
            city_counter = 0 #This variable will keep the number of currently checked city in that child solution
            for city in child: #The number of currently checked city is found in this for loop
                if city == controlled_city:
                    city_counter += 1
            
            if city_counter < 2:
                
                will_break = False
            
            if city_counter > 1: #If controlled city is more than 1 in the current child solution; we need to replace controlled_city with the city it is mapped to
                for a_map in maps_list:
                    if a_map[0] == controlled_city: #Mapping where controlled_city is located
                        
                        child[controlled_city_index_holder] = a_map[1] #Replace the controlled city in the child solution with the other city in that mapping
                        
                        will_break = True
                        
                        maps_list.remove(a_map)          #Used mapping is removed from the mapping list
 
                        break
                            
                    elif a_map[1] == controlled_city: #Mapping where controlled_city is located

                        child[controlled_city_index_holder] = a_map[0] #Replace the controlled city in the child solution with the other city in that mapping

                        will_break = True
                        
                        maps_list.remove(a_map)         #Used mapping is removed from the mapping list
  
                        break
                    
                
            if will_break:
                break
        #print("This is the new version of the child solution after the change: ",child)        #You can print the new version of the child solution after the change
        
        #There was a change in the child solution, so we have to start the checking process from the beginning
        
        #But first we check if the child solution is fixed
        child_fixed = True
        city_counts = []
        for city in child:
            count = 0
            
            for check in child:
                if city == check:
                    count += 1
                    
            city_counts.append([city, count])
        #print("Here is the list of cities in the new version of the child solution and how many they are:", city_counts)   #You can print the list of cities in the new version of the child solution and how many they are   
        
        #Check if any city is more than 1 in the new child solution
        for count in city_counts:
            if count[1] > 1:
                child_fixed = False

        #If the child solution is fixed, we finish checking it.            
        if child_fixed:
            i=2
            break
    
    #print("Fixed version of that child solution: ", child) #You can print the fixed version of that child solution
    return child
        
    
#Apply mutation to child solutions, with a probability, by inverting a random part of it                    
def mutate_children(children, mutation_probability):
    children_after_mutation = []
    
    for child in children:
        if random.uniform(0, 1) <= mutation_probability:
            left_bound = random.randint(0,len(child))
            right_bound = random.randint(left_bound,len(child))
            child[left_bound:right_bound] = child[left_bound:right_bound][::-1]
            children_after_mutation.append(child)
        else:
            children_after_mutation.append(child)
            
    return children_after_mutation
            
def generation_creator(population, mutated_children, cities):
    #A dataframe named "children" containing children and fitness values is created
    integer_mutated_children = []
    mutated_children_fitnesses = []
    for child in mutated_children:
        child = child.astype(int) 
        integer_mutated_children.append(child)
        distance = calculate_distance(cities,child)
        fitness = 1/distance
        mutated_children_fitnesses.append(fitness)
    children = pd.DataFrame(list(zip(integer_mutated_children,mutated_children_fitnesses)),columns=['solution','fitness'])
    children.sort_values(by='fitness',axis=0,inplace=True,ascending=False)
    
    #The best half of the children are selected to be included in the population
    choosen_children_number = round(len(children)/2)
    choosen_children = children.head(choosen_children_number)

    #From the worst members of the current population, as many solutions as children to be added are discarded
    population = population.head(len(population)-choosen_children_number)
   
    #Selected children are added to the remaining solutions in the population; new population is also sorted by fitness
    new_population = pd.concat([population, choosen_children])
    new_population.sort_values(by='fitness',axis=0,inplace=True,ascending=False)

    return new_population
            




def main(generation_number, number_of_individuals, number_of_pairs_M, crossover_probability, mutation_probability):
    
    k = 0 #keeps the current generation number
    
    #A dataframe named "population" containing initial population and fitness values is created
    solutions = []
    fitnesses = []
    for i in range(0,number_of_individuals): #for loop's range is number_of_individuals, since there will be as many individuals in the population as are entered as argument
        solution=np.random.permutation(len(cities))
        solutions.append(solution)
        distance = calculate_distance(cities,solution)
        fitness = 1/distance                 #The fitness value of a solution (i.e. an individual) is calculated with 1/distance
        fitnesses.append(fitness)
    population = pd.DataFrame(list(zip(solutions,fitnesses)),columns=['solution','fitness'])
    population.sort_values(by='fitness',axis=0,inplace=True,ascending=False)  #Individuals in the population are ranked in descending order of fitness values  
    
    print("Initial population: ")  #Initial population is printed
    print(population)
    
    #Genetic search starts (new generations will be produced as many as the desired generation number)
    for i in range(generation_number):
        k+=1
        
        #parents are created to produce the next generation
        current_parents = parent_selection(population, number_of_pairs_M)  
                    
        
        #Child solutions are created by crossover
        children = crossover(current_parents, crossover_probability)
        
        
        #Child solutions are mutated with a probability
        mutated_children = mutate_children(children, mutation_probability) #inversion mutation uyguladık
        
        
        #Replacement is done and new generation is created
        population = generation_creator(population, mutated_children, cities)
        print("--------------------------")
        print("Generation number: ",k )

        print(population)
        for solution, fitness in population.itertuples(index=False):
            print("Best solution founded: ", np.append(solution, [solution[0]], axis=0))
            print("Cost of that solution: ", calculate_distance(cities , solution) )
        
            break
            
    
start_time = time.time()                 #Keeps the start time

main(1700, 100, 25, 0.7, 0.5) #(generation number, number of individuals in a generation, Number of parent "pairs" to be selected in parent selection, crossover probability for a parent pair, mutation probability for a child solution)

comp_time = time.time() - start_time     #Subtracts the start time from the end time and keeps the result
print(f"-> Computational Time: {comp_time} seconds")     #Prints computational time
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    