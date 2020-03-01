import copy
from collections import deque
from queue import Queue
import heapq

day1=[["NYC","Tbilisi","594"],["NYC","Budapest","607"]]
day2=[["Budapest","Tbilisi","94"],["Tbilisi","Budapest","67"]]
day3= [["Tbilisi","NYC","394"],["Budapest","NYC","697"]]
day_list = [day1,day2,day3]


def price():
    pass


def search(start_point):
    path = []

def choose_path_a_star(a_map, start_point):
    priority_queue = []
    path = []
    cost_so_far = {}
    came_from = {}
    came_from[start_point] = True
    cost_so_far[start_point] = 0
    heapq.heappush(priority_queue, (start_point, 0))
    while priority_queue:
        current, position = heapq.heappop(priority_queue)
        if a_map.is_goal(current):
            path1 = []
            while current != start_point:
                path1.append(current)
                current = came_from[current]
            path.append(path1)
        for pos in a_map.valid_moves_from(current):
            new_cost= cost_so_far[current]+price(current,pos)
            if pos not in cost_so_far or new_cost<cost_so_far[pos]:
                cost_so_far[pos]=new_cost
                priority = new_cost+price(a_map.goals, pos)
                heapq.heappush(priority_queue, (pos,priority))
                came_from[pos] = current
    if len(path) == 0:
        return path,came_from
    return min(path), came_from

