# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node #if list is empty, return it since copy should be empty as well
        dic = {node: Node(node.val)} #main node value equal to first node value
        self.dfs(node, dic)
        return dic[node]
    #O(V) space complexity from dic dictionary with copied vertices
    #O(V+E) runtime from traveling all vertices and all edges
    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                dic[neighbor] = Node(neighbor.val)
                self.dfs(neighbor, dic)
            dic[node].neighbors.append(dic[neighbor])