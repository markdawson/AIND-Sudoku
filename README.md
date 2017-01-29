# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *Student should provide answer here*

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: *Student should provide answer here*

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.

### Free Response Questions 
**How do we apply constraint propagation to solve the naked twins problem?**

When we see two boxes in the same unit, with the exactly same two possibile digits, we know that that those one of those possibilities _must_ appear in one of those two boxes and the other possibility _must_ appear in the other box. Using that contraint, we can eliminate those possibilities from all other boxes in the unit. Repeating this strategy multiple times ("propogating the contraint") might yield even more progress on the puzzle than doing it just once. 

**How do we apply constraint propagation to solve the diagonal sudoku problem?**

Once we have our contraints defined ("only choice", "elimination", "naked twins", etc.), all we have to do to solve a diagonal sudoku problem is include the diagonals in the "units" or groups of boxes that must contain the digits 1 through 9. If we implemented our containts in a flexbile way, then it should be easy to add the diagonals as units.