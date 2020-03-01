from anytree import Node, RenderTree
from anytree.exporter import DotExporter

pos = []
root = Node(["NYC",0.0])
node1= Node(["Albany", 39], parent=root)
node2 = Node(["Miami", 40], parent=root)
node3 = Node(["Miami", 18], parent=node1)
node4 = Node(["Albany", 12], parent=node2)
node5 = Node(["NYC", 11], parent=node3)
node6 = Node(["NYC", 19], parent=node4)
pos.append(node5)
pos.append(node6)
for x in pos:
    total = 0
    path = str(x)
    res = [i for i in range(len(path)) if path.startswith(', ', i)]
    for i in res:
        total+= float(path[i+2:i+4])
    print(total)



# DotExporter(root).to_picture("udo.png")
str = str(node6)
print(str)
res = [i for i in range(len(str)) if str.startswith(', ', i)]

total = 0
for i in res:
    # print(float(str[i+2:i+4]))
    total+= float(str[i+2:i+4])




# for pre, fill, node in RenderTree(root):
#     print("%s%s" % (pre, node.name))