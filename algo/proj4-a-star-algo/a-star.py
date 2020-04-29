import heapq
import math
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Map:
    roads: List[List[int]]
    intersections: Dict[int, List[float]]


map_10 = Map(
    roads=[[7, 6, 5], [4, 3, 2], [4, 3, 1], [5, 4, 1, 2], [1, 2, 3], [7, 0, 3], [0], [0, 5], [9], [8]],
    intersections={
        0: [0.7798606835438107, 0.6922727646627362], 1: [0.7647837074641568, 0.3252670836724646],
        2: [0.7155217893995438, 0.20026498027300055], 3: [0.7076566826610747, 0.3278339270610988],
        4: [0.8325506249953353, 0.02310946309985762], 5: [0.49016747075266875, 0.5464878695400415],
        6: [0.8820353070895344, 0.6791919587749445], 7: [0.46247219371675075, 0.6258061621642713],
        8: [0.11622158839385677, 0.11236327488812581], 9: [0.1285377678230034, 0.3285840695698353]})


def euclidean_distance(x1, y1, x2, y2):
    """Calculates "ordinary" straight-line distance between two points in Euclidean space."""
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def distances_to_goal(intersections, goal):
    """Calculates Euclidean distance from every intersections to the goal."""
    distances = {}
    goal_x, goal_y = intersections[goal]
    for intersection in intersections:
        inter_x, inter_y = intersections[intersection]
        distances[intersection] = euclidean_distance(inter_x, inter_y, goal_x, goal_y)
    return distances


def road_lengths(map_):
    """Calculates Euclidean distance for each road."""
    lengths = {}
    for road, neighbors in enumerate(map_.roads):
        start_x, start_y = map_.intersections[road]
        for neighbor in neighbors:
            end_x, end_y = map_.intersections[neighbor]
            road_length = euclidean_distance(start_x, start_y, end_x, end_y)
            lengths[(road, neighbor)] = road_length
            lengths[(neighbor, road)] = road_length
    return lengths


class Node:
    def __init__(self, id_, x, y, len_to_start=float("inf"), prev=None):
        self.id = id_
        self.x = x
        self.y = y
        self.prev = prev
        self.len_to_start = len_to_start

    def __repr__(self):
        return "Node_{id_}[({x_coord}, {y_coord}), previous={prev}]".format(
            id_=self.id, x_coord=self.x, y_coord=self.y, prev=self.prev)

    def __lt__(self, other):
        return self.len_to_start < other.len_to_start


class Graph:
    def __init__(self, map_):
        self._roads = map_.roads
        self._roads_len = road_lengths(map_)
        self._intersections = map_.intersections
        self.nodes = {}
        for intersection_id in map_.intersections:
            x, y = map_.intersections[intersection_id]
            self.nodes[intersection_id] = Node(intersection_id, x, y)

    def find_path(self, start, goal):
        dists_to_goal = distances_to_goal(self._intersections, goal)
        self.nodes[start].len_to_start = dists_to_goal[start]
        visited = set()
        h = [self.nodes[start]]  # min-heap stores the sequence of nodes traverse.
        while h:
            node = heapq.heappop(h)
            # The destination node is reached.
            if node.id == goal:
                break
            # Skip if already visited.
            if node.id in visited:
                continue
            # Add neighbours to the heap.
            for neighbours_node_id in self._roads[node.id]:
                dist_to_start = node.len_to_start + self._roads_len[(node.id, neighbours_node_id)] + dists_to_goal[
                    neighbours_node_id]
                if dist_to_start < self.nodes[neighbours_node_id].len_to_start:
                    self.nodes[neighbours_node_id].len_to_start = dist_to_start
                    self.nodes[neighbours_node_id].prev = node.id
                heapq.heappush(h, self.nodes[neighbours_node_id])
            visited.add(node.id)

        # Backtracking.
        node = self.nodes[goal]
        path = []
        while node:
            path.append(node.id)
            node = self.nodes[node.prev] if node.prev else None
        return path


def shortest_path(map_, start, goal):
    g = Graph(map_)
    return g.find_path(start, goal)


if __name__ == "__main__":
    print(shortest_path(map_10, 0, 4))
