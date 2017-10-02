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
    return [s, s, w, s, w, w, s, w]


def generic_search_1(problem, fringe, push_into_fringe):

    visited = set()
    # state model is (node, path, cost)
    start_state = (problem.getStartState(), ['Stop'], 0)
    push_into_fringe(fringe, start_state)

    if problem.isGoalState(problem.getStartState()):
        return 'Stop'

    while not fringe.isEmpty():
        current_state = fringe.pop()
        current_node = current_state[0]
        current_path = current_state[1]
        current_cost = current_state[2]

        if problem.isGoalState(current_node):
            current_path.remove(current_path[0])
            return current_path

        if current_node not in visited:
            visited.add(current_node)
            for successor in problem.getSuccessors(current_node):
                child_node = successor[0]
                child_action = successor[1]
                child_cost = successor[2]

                new_path = current_path + [child_action]
                new_cost = current_cost + child_cost

                new_state = (child_node, new_path, new_cost)
                push_into_fringe(fringe, new_state)


def generic_search_2(problem, fringe, push_into_fringe):

    visited = set()
    # state model is (node, path, cost)
    start_state = (problem.getStartState(), ['Stop'], 0)
    push_into_fringe(fringe, start_state, 0)

    if problem.isGoalState(problem.getStartState()):
        return 'Stop'

    while not fringe.isEmpty():
        current_state = fringe.pop()
        current_node = current_state[0]
        current_path = current_state[1]
        current_cost = current_state[2]

        if problem.isGoalState(current_node):
            current_path.remove(current_path[0])
            return current_path

        if current_node not in visited:
            visited.add(current_node)
            for successor in problem.getSuccessors(current_node):
                child_node = successor[0]
                child_action = successor[1]
                child_cost = successor[2]

                new_path = current_path + [child_action]
                new_cost = current_cost + child_cost

                new_state = (child_node, new_path, new_cost)
                push_into_fringe(fringe, new_state, new_cost)

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    def push_into_fringe(fringe, state):
        fringe.push(state)

    return generic_search_1(problem, fringe, push_into_fringe)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    def push_into_fringe(fringe, state):
        fringe.push(state)

    return generic_search_1(problem, fringe, push_into_fringe)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    def push_into_fringe(fringe, state, cost):
        fringe.push(state, cost)

    return generic_search_2(problem, fringe, push_into_fringe)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    def push_into_fringe(fringe, state, cost):
        new_cost = cost + heuristic(state[0], problem)
        fringe.push(state, new_cost)

    return generic_search_2(problem, fringe, push_into_fringe)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
