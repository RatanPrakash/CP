# # # class Node:
# # #     def __init__(self, value):
# # #         self.value = value
# # #         self.children = []

# # # def construct_tree(n, values, parents):
# # #     nodes = [Node(value) for value in values]
# # #     root = nodes[0]
# # #     for i in range(1, n):
# # #         parent = nodes[parents[i-1]-1]
# # #         parent.children.append(nodes[i])
# # #     return root

# # # def print_tree(root, level=0, label='.'):
# # #     """Print the tree structure on the console."""
# # #     prefix = ' ' * (level * 4) + label + ': '
# # #     print(prefix + str(root.value))
# # #     for i, child in enumerate(root.children):
# # #         print_tree(child, level + 1, f'C{i}')

# # # def max_value(node):
# # #     if not(node.children):
# # #         return node.value
    
# # #     mini = 1e10
# # #     for i, child in enumerate(node.children):
# # #         child_value = max_value(child)
# # #         if child_value >= node.value:
# # #             mini = min((child_value+node.value)//2, mini)
# # #         else:
# # #             mini = min(child_value, mini)
# # #     return mini

# # # # Read the number of test cases
# # # t = int(input())

# # # for _ in range(t):
# # #     # Read the number of vertices
# # #     n = int(input())

# # #     # Read the initial values written at vertices
# # #     values = list(map(int, input().split()))

# # #     # Read the parent information
# # #     parents = list(map(int, input().split()))

# # #     # Construct the tree
# # #     root = construct_tree(n, values, parents)
# # #     # print_tree(root)

# # #     # Calculate the maximum possible value written at the root
# # #     mini = 1e10
# # #     for i, child in enumerate(root.children):
# # #         mini = min(mini, max_value(child))
# # #     mini += root.value 

# # #     # Print the result
# # #     print(mini)









# # class Node:
# #     def __init__(self, value):
# #         self.value = value
# #         self.children = []

# # def construct_tree(n, values, parents):
# #     nodes = [Node(value) for value in values]
# #     root = nodes[0]
# #     for i in range(1, n):
# #         parent = nodes[parents[i-1] - 1]  # Adjust for 1-based index
# #         parent.children.append(nodes[i])
# #     return root

# # def print_tree(root, level=0, label='.'):
# #     """Print the tree structure on the console."""
# #     prefix = ' ' * (level * 4) + label + ': '
# #     print(prefix + str(root.value))
# #     for i, child in enumerate(root.children):
# #         print_tree(child, level + 1, f'C{i}')

# # def max_value(node):
# #     if not node.children:
# #         return node.value
    
# #     mini = float('inf')
# #     for i, child in enumerate(node.children):
# #         child_value = max_value(child)
# #         if child_value >= node.value:
# #             mini = min((child_value + node.value) // 2, mini)
# #         else:
# #             mini = min(child_value, mini)
# #     return mini

# # # Read the number of test cases
# # t = int(input())

# # for _ in range(t):
# #     # Read the number of vertices
# #     n = int(input())
# #     if n == 1:
# #         values = int(input())
# #         print(values)
# #         continue

# #     # Read the initial values written at vertices
# #     values = list(map(int, input().split()))

# #     # Read the parent information
# #     parents = list(map(int, input().split()))

# #     # Construct the tree
# #     root = construct_tree(n, values, parents)
# #     # print_tree(root)

# #     # Calculate the maximum possible value written at the root
# #     mini = float('inf')
# #     for i, child in enumerate(root.children):
# #         mini = min(mini, max_value(child))
# #     mini += root.value 

# #     # Print the result
# #     print(mini)


# import sys
# sys.setrecursionlimit(1000000000+1)  # Increase the recursion limit

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

# def construct_tree(n, values, parents):
#     nodes = [Node(value) for value in values]
#     root = nodes[0]
#     for i in range(1, n):
#         parent = nodes[parents[i-1] - 1]  # Adjust for 1-based index
#         parent.children.append(nodes[i])
#     return root

# def print_tree(root, level=0, label='.'):
#     """Print the tree structure on the console."""
#     prefix = ' ' * (level * 4) + label + ': '
#     print(prefix + str(root.value))
#     for i, child in enumerate(root.children):
#         print_tree(child, level + 1, f'C{i}')

# def max_value(node):
#     if not node.children:
#         return node.value
    
#     mini = float('inf')
#     for i, child in enumerate(node.children):
#         child_value = max_value(child)
#         if child_value >= node.value:
#             mini = min((child_value + node.value) // 2, mini)
#         else:
#             mini = min(child_value, mini)
#     return mini

# # Read the number of test cases
# t = int(input())

# for _ in range(t):
#     # Read the number of vertices
#     n = int(input())
#     if n == 1:
#         values = int(input())
#         print(values)
#         continue

#     # Read the initial values written at vertices
#     values = list(map(int, input().split()))

#     # Read the parent information
#     parents = list(map(int, input().split()))

#     # Construct the tree
#     root = construct_tree(n, values, parents)
#     # print_tree(root)

#     # Calculate the maximum possible value written at the root
#     mini = float('inf')
#     for i, child in enumerate(root.children):
#         mini = min(mini, max_value(child))
#     mini += root.value 

#     # Print the result
#     print(mini)


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def construct_tree(n, values, parents):
    nodes = [Node(value) for value in values]
    root = nodes[0]
    for i in range(1, n):
        parent = nodes[parents[i-1] - 1]  # Adjust for 1-based index
        parent.children.append(nodes[i])
    return root

def print_tree(root, level=0, label='.'):
    """Print the tree structure on the console."""
    prefix = ' ' * (level * 4) + label + ': '
    print(prefix + str(root.value))
    for i, child in enumerate(root.children):
        print_tree(child, level + 1, f'C{i}')

def max_value(node):
    stack = [(node, False)]
    values = {}
    while stack:
        current, visited = stack.pop()
        if visited:
            if not current.children:
                values[current] = current.value
            else:
                mini = float('inf')
                for child in current.children:
                    child_value = values[child]
                    if child_value >= current.value:
                        mini = min((child_value + current.value) // 2, mini)
                    else:
                        mini = min(child_value, mini)
                values[current] = mini
        else:
            stack.append((current, True))
            for child in current.children:
                stack.append((child, False))
    return values[node]

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of vertices
    n = int(input())
    if n == 1:
        values = int(input())
        print(values)
        continue

    # Read the initial values written at vertices
    values = list(map(int, input().split()))

    # Read the parent information
    parents = list(map(int, input().split()))

    # Construct the tree
    root = construct_tree(n, values, parents)
    # print_tree(root)

    # Calculate the maximum possible value written at the root
    mini = float('inf')
    for i, child in enumerate(root.children):
        mini = min(mini, max_value(child))
    mini += root.value 

    # Print the result
    print(mini)
