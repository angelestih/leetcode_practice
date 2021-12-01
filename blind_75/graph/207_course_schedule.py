from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = self.build_adjacency_list(numCourses, prerequisites)
        state_array = [0] * (numCourses)
        #states for every vertex: -1 for being processed
        #                          0 for not processed yet
        #                          1 for processed already
        for vertex in range(numCourses):
            if self.vertex_cyclic(vertex, state_array, adjacency_list) == True:
                return False
        return True

    def build_adjacency_list(self, num_vertices, edge_list):
        adjacency_list = []
        #used for building a graph representation
        #by creating instance of list for each vertex
        #and adding the prerequisite to the second element of the course

        for i in range(num_vertices):
            adjacency_list.append([])

        for course_a,course_b in edge_list:
            adjacency_list[course_b].append(course_a)
        return adjacency_list

    def vertex_cyclic(self, vertex, state_array, adjacency_list):
        if state_array[vertex] == 1:
            #vertex was processed already, can be passed along
            return False
        if state_array[vertex] == -1:
            #vertex still being processed in a previous recursive call
            # thus, it has a cycle
            return True
        #begin recursive call to process vertex
        state_array[vertex] = -1
        for v in adjacency_list[vertex]:
            if self.vertex_cyclic(v, state_array, adjacency_list) == True:
                return True
        #finish process after end of recursive calls
        state_array[vertex] = 1
        return False
        #done

