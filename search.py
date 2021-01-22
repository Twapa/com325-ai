# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    

    # Keep track of number of states explored
    num_explored = 0
    # stack is data structure used
    stackFrontier = util.Stack()

    startstate = problem.getStartState()
    # start node
    startnode = (startstate, [])

    # Initialize an empty explored set
    explored = set()

    stackFrontier.push(startnode)
    # to looping until solution found
    while not stackFrontier.isEmpty():
        # c is the currentstate and p is the action
        c, p = stackFrontier.pop()
        num_explored =+1
        # check if it is the goal state 
        if problem.isGoalState(c):
                return p
        if  c not in explored:
            # Mark node as explored
            explored.add(c)

            
            # Add neighbors to frontier (state,action and stepcost)
            for state, action, stepcost in problem.getSuccessors(c):
                stackFrontier.push((state, p + [action]))        




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Keep track of number of states explored
    num_explored = 0
    # queue is data structure used
    queueFrontier = util.Queue()

    startstate = problem.getStartState()
    # start node
    startnode = (startstate, [])
    # Initialize an empty explored set
    explored = set()

    queueFrontier.push(startnode)
    # to looping until solution found
    while not queueFrontier.isEmpty():

        c, p = queueFrontier.pop()
        num_explored =+1
        
        
        # check if it is the goal state
        if problem.isGoalState(c):
                return p
        if  c not in explored:

            explored.add(c)
            # Add neighbors to frontier (state,action and stepcost)
            for state, action, stepcost in problem.getSuccessors(c):
                queueFrontier.push((state, p + [action]))        



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # priorityqueue is data structure used
    priorityfrontier = util.PriorityQueue()

    num_expored = 0
    # dictionary used store cost 
    dic ={}
    # Initialize an empty explored set
    explored = set([])

    startstate = problem.getStartState()
    priorityfrontier.push((startstate,[]),0)
    
    dic[startstate]= 0
    # to looping until solution found
    while not priorityfrontier.isEmpty():

        c,p = priorityfrontier.pop()

        # check if it is the goal state
        if problem.isGoalState(c):
            return p
        # Add neighbors to frontier (state,action and stepcost)
        for states in problem.getSuccessors(c):
            # chck the dictionary first
            if states[0] not in (key for key in dic):

                cost =problem.getCostOfActions(p + [states[1]])
                
                priorityfrontier.push((states[0],p +[states[1]]),cost)
                dic[states[0]]= cost
                explored.add(states[0])
                    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    checked = set()
    # priority queue used as data structure
    priorityQueue = util.PriorityQueue()
    priorityQueue.push((problem.getStartState(), []), 0)
    # to keep loopint until solution found
    while not priorityQueue.isEmpty():
        c, actions = priorityQueue.pop()
        if c in checked:
            continue
        checked.add(c)
        if problem.isGoalState(c):
            return actions
        # Add neighbors to frontier (state,action and stepcost)
        for state, action,stepCost in problem.getSuccessors(c):
                priorityQueue.push((state, actions + [action]), stepCost + problem.getCostOfActions(actions) + heuristic(state, problem = problem))
    



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
