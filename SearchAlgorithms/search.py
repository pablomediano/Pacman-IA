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
from game import Directions
from typing import List

def update_exploration_metrics(agent, state):
    """
    Updates exploration metrics:
    - visited positions
    - visit frequency per position
    """
    current_position = state.getPacmanPosition()

    if current_position not in agent.visited_positions:
        agent.unique_positions += 1
        agent.visited_positions.add(current_position)

    agent.visit_frequency[current_position] = (
        agent.visit_frequency.get(current_position, 0) + 1
    )



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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Performs a Depth-First Search (DFS).

    The algorithm explores the deepest nodes in the search tree first.
    It returns a list of actions that leads from the initial state
    to a goal state, implementing a graph search to avoid cycles.

    For debugging purposes, the following calls may be useful:
    print("Start:", problem.getStartState())
    print("Is start a goal?:", problem.isGoalState(problem.getStartState()))
    print("Start successors:", problem.getSuccessors(problem.getStartState()))
    """

    solution = []                 # List of actions that form the final solution
    path = {}                     # Dictionary to reconstruct the path (child -> parent)
    visited = {}                  # Dictionary of visited states
    stack = util.Stack()          # Stack used for Depth-First Search

    start_state = problem.getStartState()
    stack.push((start_state, '', 0))   # (state, action, cost)
    visited[start_state] = ''

    # If the initial state is already the goal
    if problem.isGoalState(start_state):
        return solution

    # Main DFS loop
    while not stack.isEmpty():
        current_state, action, cost = stack.pop()
        visited[current_state] = action

        # Check if goal has been reached
        if problem.isGoalState(current_state):
            goal_state = current_state
            break

        # Expand successors
        for successor in problem.getSuccessors(current_state):
            next_state, next_action, next_cost = successor

            if next_state not in visited:
                path[next_state] = current_state
                stack.push(successor)

    # Path reconstruction from goal to start
    while goal_state in path:
        parent_state = path[goal_state]
        solution.insert(0, visited[goal_state])
        goal_state = parent_state

    return solution

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def exploration(problem):
     # Stack for DFS traversal
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
exp = exploration
