import csv
from math import inf
from anytree import Node, RenderTree, find_by_attr


def csv_tolist():
    results = []
    with open("some.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')  # change contents to floats
        for row in reader:  # each row is a list
            results.append(row)
    return results

def to_tree(results,origin, pos):
    root = Node([origin, 0])
    parentnode = root
    for x in range(pos):
        if x == 0:
            for y in results:
                if y[0] == root.name[0]:
                    node = Node([y[1], y[pos]], parent=parentnode)
        else:
            parentnode = node
            for y in results:
                if y[0] == parentnode.name[0]:
                    node = Node([y[1], y[pos]], parent=parentnode)
                node = Node([y[1], y[pos]], parent=parentnode)
                print(node)

    print(node)
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
    return root






def find_next(results,next,origin, pos):
    # next = ''
    add = ''
    min = inf
    for x in results:
        if x[0]==origin:
            if min>float(x[pos]) and x[1] not in next:
                min = float(x[pos])
                add = x[1]
                print(add)
    next.append(add)
    return next


def main():

    next = []
    results = csv_tolist()
    to_tree(results,"NYC",3)
    next.append("NYC")
    # print(find_next(results,next,next[0],2))
    # print(find_next(results,next, next[1], 3))
    # print(find_next(results,next, next[2], 4))
    # print(find_next(results,next, next[3], 5))
    next.append("NYC")


main()