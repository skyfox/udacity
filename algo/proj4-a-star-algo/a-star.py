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
    """Node represents a 'rich' intersection.

    It is intersection in core, but with additional properties. It makes an intersection closer to graph theory.
    """

    def __init__(self, id_, x, y, distance_to_goal=float("inf"), way_to_start=float("inf")):
        self.id = id_
        self.x = x
        self.y = y
        self.distance_to_goal = distance_to_goal
        self.way_from_start = way_to_start

    def __repr__(self):
        """Represents the node as a string.

        Very useful and convenient for debugging.
        """
        return "Node_{id_}[({x_coord}, {y_coord}), from_start={way_to_start}, to_goal={dist_to_goal}]".format(
            id_=self.id, x_coord=self.x, y_coord=self.y, way_to_start=self.way_from_start,
            dist_to_goal=self.distance_to_goal)

    def __lt__(self, other):
        """Estimates which node is 'heavier'.

        This is very useful for priority queue, because it implements comparison interface. Hence heapq can properly
        store nodes.
        """
        return (self.way_from_start + self.distance_to_goal) < (other.way_from_start + other.distance_to_goal)


class Graph:
    """Graph representation of a given map abstraction.

    Similar to Node class this one adds a few useful auxiliary elements to represent Map as a graph from graph theory.
    """
    def __init__(self, map_):
        self._roads = map_.roads
        self._roads_len = road_lengths(map_)
        self._intersections = map_.intersections

        # Create nodes
        self.nodes = {}
        for intersection_id in map_.intersections:
            x, y = map_.intersections[intersection_id]
            self.nodes[intersection_id] = Node(intersection_id, x, y)

    def find_path(self, start, goal):
        # Add distances to goal for each Node
        distances = distances_to_goal(self._intersections, goal)
        for node_id in distances:
            self.nodes[node_id].distance_to_goal = distances[node_id]

        self.nodes[start].way_from_start = 0  # Start node has 0-th way to itself.
        pq = []  # Create a min-heap to store the traverse priority.
        heapq.heappush(pq, self.nodes[start])
        visited = {start}
        path_tracker = {start: None}  # Stores the order of traverse.

        while pq:
            node = heapq.heappop(pq)
            for neighb_node_id in self._roads[node.id]:
                neighb_way_from_start = node.way_from_start + self._roads_len[(node.id, neighb_node_id)]
                if neighb_node_id not in visited or neighb_way_from_start < self.nodes[neighb_node_id].way_from_start:
                    heapq.heappush(pq, self.nodes[neighb_node_id])
                    self.nodes[neighb_node_id].way_from_start = neighb_way_from_start
                    visited.add(neighb_node_id)
                    path_tracker[neighb_node_id] = node.id

        # Restore the path from start to goal.
        path = []
        key = goal
        while key:
            path.append(key)
            key = path_tracker[key]
        return path[::-1]


def shortest_path(map_, start, goal):
    g = Graph(map_)
    return g.find_path(start, goal)


if __name__ == "__main__":
    print(shortest_path(map_10, 0, 4))
