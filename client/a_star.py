import client
import ast
import random

# AUXILIAR
class Queue:
    def __init__(self):
         self.queue_data = []

    def isEmpty(self):
        if len(self.queue_data) == 0:
            return True
        else:
            return False

    def pop(self):
        return self.queue_data.pop(0)

    def insert(self,element):
        return self.queue_data.append(element)

    def getQueue(self):
        return self.queue_data

#
class Node:
    def __init__(self,state,parent,action,path_cost):
        self.state = state
        self.parent = parent
        self.action =action
        self.path_cost = path_cost

    def getState(self):
        return self.state

    def getParent(self):
        return self.parent

    def getAction(self):
        return self.action

    def getPathCost(self):
        return self.path_cost

    def getParent(self):
        return self.parent

