# 3-heuristic-algorithms-in-Python-for-Travelling-Salesman-Problem
As alternative heuristic techniques; genetic algorithm, simulated annealing algorithm and city swap algorithm are implemented in Python for Travelling Salesman Problem. Details on implementation and test results can be found in this repository. 

All 3 algorithms have been tested as a solution to the Traveling Salesman Problem. In our problem, it is assumed that the 2-dimensional Euclidean space is valid. That is, distances will be calculated as 2-dimensional euclidean distances. In our problem, coordinates of 51 cities are used as dataset from a csv file. If you want, you can enter new city coordinates in the csv file or edit the already entered ones and run the algorithms again. The programs have been written to allow you to edit the dataset as you wish. 
And the best known solution's cost for this symmetric TSP is 426.

# On how to use the codes for those who want to use them
You can edit the csv file to use any of the 3 codes with your own dataset (i.e. to change city coordinates or to add or remove new cities).

To use the City Swap Algorithm code, you need to run the "testCode.py" file in the folder. The only argument you can manipulate in this code is the "dataset", and we've already mentioned how you can change it.

To use the Simulated Annealing Algorithm code with your desired argument values; you can write the start temperature you want to the second argument in the main function, the desired cooling rate value (between 0-1) to the third argument in the main function, the lower bound of the temperature to the fourth, and the tolerance value of the local search to the fifth.

To use the Genetic Algorithm code with the argument values you want; the first of the arguments in the main function is how many generations you want to create, the second is the number of individuals in one generation, the third is the number of parent "pairs" to be selected in parent selection, the fourth is the crossover probability for a parent pair value, the fifth is mutation probability of a child solution. 

# Comparison of algorithm performances in terms of "closeness of the best solution to the optimum" and "computational time"

1) The output of the City Swap Algorithm code is as shown below.

![image](https://user-images.githubusercontent.com/82934361/169900647-fb10fa0b-7619-471e-beaa-a8dbc55808cd.png)

2) When the following arguments are written to the main function, the output of the Simulated Annealing Algorithm code is as shown below.
![image](https://user-images.githubusercontent.com/82934361/169907189-3f5c0958-81c2-4234-83af-659759b58fba.png)

![image](https://user-images.githubusercontent.com/82934361/169902750-0e2cca4e-47df-413d-9473-574648d906ba.png)

3) When the following arguments are written to the main function, the output of the Genetic Algorithm code is as shown below.
![image](https://user-images.githubusercontent.com/82934361/169906970-3ba84ad1-7a45-4680-8194-c6ff123c3829.png)

![image](https://user-images.githubusercontent.com/82934361/169904072-0fdfb5aa-def6-477f-bee4-d0d7df74c07d.png)

4) When the following arguments are written to the main function, the output of the Genetic Algorithm code is as shown below.
![image](https://user-images.githubusercontent.com/82934361/169905468-c6044ea8-5ced-4332-9b26-611bdbd3dfe1.png)

![image](https://user-images.githubusercontent.com/82934361/169905598-890672d5-e243-46fb-9c24-503942d37c66.png)


Note that the best known solution for this symmetrical TSP costs 426. 
As you can see in output 4, the Genetic Algorithm found the closest solution to optimum, but it took about 3 times longer than Simulated Annealing Algorithm and 12 times longer than City Swap Algorithm to reach this solution. 
As you can see in the 3rd output, when we changed the arguments we used in the Genetic Algorithm code, the computational time of the Genetic Algorithm became about 10 seconds shorter than the computational time of the Simulated Annealing Algorithm. However, as you can see in output 2, the Simulated Annealing Algorithm was able to produce a better solution by running 10 seconds longer.
As you can see in the 1st output, the City Swap Algorithm took much less time than the remaining two algorithms, but the best solution it found is also much worse than the remaining two algorithms. 
Note: It should be noted that City Swap Algorithm is a greedy improvement heuristic algorithm. The situation we observed as a result of the codes we wrote confirms our theoretical knowledge about improvement algorithms. A greedy algorithm is any algorithm that follows the method of making the locally optimal choice at each stage. In many problems, a greedy strategy does not produce an optimal solution, but a greedy heuristic can find locally optimal solutions that approach a globally optimal solution in as short a time as possible. So basically in short, greedy improvement algorithms like City Swap Algorithm can be used to find a good solution to a problem as fast as possible.


