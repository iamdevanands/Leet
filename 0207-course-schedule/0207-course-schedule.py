class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        # Build the graph
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1

        queue = []

        # Add all courses with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        front = 0
        count = 0

        while front < len(queue):
            node = queue[front]
            front += 1
            count += 1

            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses