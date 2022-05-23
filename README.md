# 3-heuristic-algorithms-in-Python-for-Travelling-Salesman-Problem
As alternative heuristic techniques; genetic algorithm, simulated annealing algorithm and city swap algorithm are implemented in Python for Travelling Salesman Problem. Details on implementation and test results can be found in this repository. 

All 3 algorithms have been tested as a solution to the Traveling Salesman Problem. In our problem, it is assumed that the 2-dimensional Euclidean space is valid. That is, distances will be calculated as 2-dimensional euclidean distances. In our problem, coordinates of 51 cities are used as dataset from a csv file. If you want, you can enter new city coordinates in the csv file or edit the already entered ones and run the algorithms again. The programs have been written to allow you to edit the dataset as you wish. 
And the best known solution's cost for this symmetric TSP is 426.

# On how to use the codes for those who want to use them
You can edit the csv file to use any of the 3 codes with your own dataset (i.e. to change city coordinates or to add or remove new cities).

To use the City Swap Algorithm code, you need to run the "testCode.py" file in the folder. The only argument you can manipulate in this code is the "dataset", and we've already mentioned how you can change it.

To use the Simulated Annealing Algorithm code with your desired argument values; you can write the start temperature you want to the second argument in the main function, the desired cooling rate value (between 0-1) to the third argument in the main function, the lower bound of the temperature to the fourth, and the tolerance value of the local search to the fifth.

To use the Genetic Algorithm code with the argument values you want; the first of the arguments in the main function is how many generations you want to create, the second is the number of individuals in one generation, the third is the number of parent "pairs" to be selected in parent selection, the fourth is the crossover probability for a parent pair value, the fifth is mutation probability of a child solution. 

![image](https://user-images.githubusercontent.com/82934361/169900647-fb10fa0b-7619-471e-beaa-a8dbc55808cd.png)
