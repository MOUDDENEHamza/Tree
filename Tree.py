"""Created by : MOUDDENE Hamza"""

"""--import random library--"""

from random import *

"#############This functions will help us to manage trees#################"


def tree_void(tree):
    """this function checks if the tree contains only the root"""

    if tree[1] == [] and tree[2] == []:
        return 1

    return 0


def root(a):
    """this funtion returns the root of the tree"""

    return a[0]


def create_tree(a, g, d):
    """this function creates a tree"""

    return [a, [g], [d]]


def left_children(a):
    """this function will return the left son of tree"""

    if a[1] == []:
        return []

    else:
        return a[1]


def right_children(a):
    """this function will return the right son of tree"""

    if a[2] == []:
        return []

    else:
        return a[2]


def number_leaf(tree):
    """this function counts the leaves in the tree"""

    if tree == []:
        return 0

    if tree_void(tree) == 1:
        return 1

    else:
        return number_leaf(left_children(tree)) + number_leaf(right_children(tree))


"############################### Tree, ABR & AVL for test ########################################"

tree1 = ["d", [], []]

tree2 = ["r", ["z", ["b", [], []], ["c", [], []]], ["d", [], []]]

tree3 = [8, [10, [13, [0, [], []], [7, [], []]], [14, [], []]], [85, [20, [], []], [21, [], []]]]

tree4 = [56, [83, [118, [0, [2, [], []], []], [-1, [], []]], []], [-400, [], []]]

abr1 = [12, [7, [5, [], [6, [], []]], [10, [], []]], [17, [], [82, [41, [], []],
                                                               []]]]  # Arbre du slide 23 du cours, ATTENTION, les valeurs ont été modifiés pour avoir un ABR

abr2 = [34, [22, [7, [], [17, [9, [8, [], []], [16, [], []]], [21, [], []]]],
             [29, [25, [23, [], []], [28, [27, [26, [], []], []], []]], [32, [30, [], []], []]]],
        [66, [50, [37, [36, [35, [], []], []], [44, [], []]], [56, [55, [52, [51, [], []], []], []], []]],
         [71, [70, [68, [67, [], []], [69, [], []]], []],
          [81, [80, [], []], [97, [94, [88, [], []], []], []]]]]]  # Arbre du slide 26 du cours

not_avl = [12, [8, [5, [4, [2, [], []], []], [7, [], []]], [11, [], []]], [18, [17, [], []], []]]  # Arbre du slide 41

avl = [12, [8, [5, [4, [], []], []], [11, [], []]], [18, [17, [], []], []]]  # Arbre du slide 41

"###################################################################################################"

"""##################################--First part : Tree--#########################################################"""


def max_value(tree):
    """this function finds the maximum value in tree"""

    if tree_void(tree) == 1:
        return root(tree)

    else:
        return max(root(tree), max_value(left_children(tree)), max_value(right_children(tree)))


# print(max_value(tree3))


def big_tree(a, b):
    """this function returns the tree that contains more leaves"""

    maxi = max(number_leaf(a), number_leaf(b))

    if maxi == number_leaf(a):
        return a

    if maxi == number_leaf(b):
        return b


# print(big_tree(tree3, tree4))


def extract_value(tree):
    """this function extracts the list of values from BST"""

    list = []

    if tree:
        list.append(root(tree))
        list += extract_value(left_children(tree))
        list += extract_value(right_children(tree))

    return list


# print(extract_value(tree3))


def extract_value_level(tree, level):
    """this functions will return the data of nodes in the same level"""

    list = []

    if tree == []:
        return

    if level == 0 and tree != []:
        list.append(root(tree))

    else:
        list += extract_value_level(left_children(tree), level - 1)
        list += extract_value_level(right_children(tree), level - 1)

    return list


# print(extract_value_level(tree3, 2))


"""###############################--Second part : BST--########################################"""""


def check_bst(tree, mini, maxi):
    """this function checks if the tree is a BST"""

    if tree_void(tree) == 1:
        return True

    if left_children(tree) != [] and right_children(tree) != []:
        return root(tree) <= maxi and root(tree) >= mini and check_bst(left_children(tree), mini,
                                                                       root(tree)) and check_bst(right_children(tree),
                                                                                                 root(tree), maxi)

    if left_children(tree) != [] and right_children(tree) == []:
        return root(tree) <= maxi and root(tree) >= mini and check_bst(left_children(tree), mini, root(tree))

    if left_children(tree) == [] and right_children(tree) != []:
        return root(tree) <= maxi and root(tree) >= mini and check_bst(right_children(tree), root(tree), maxi)


# garden = [tree3, tree4, abr1, abr2, avl, not_avl]
# for tree in garden:
#     mini = min(extract_value(tree))
#     maxi = max(extract_value(tree))
#     print(check_bst(tree, mini, maxi))


def inorder_parcing(tree):
    """this function browse the tree with an inorder parcing"""

    if tree:
        inorder_parcing(left_children(tree))
        print(root(tree))
        inorder_parcing(right_children(tree))


# inorder_parcing(abr1)


def postorder_parcing(tree):
    """this function browses the tree with an post-order parcing"""

    if tree:
        postorder_parcing(left_children(tree))
        postorder_parcing(right_children(tree))
        print(root(tree))


# postorder_parcing(abr1)

"""
REMARQUE:
    le type de parcours infixe traite le sous-arbre gauche puis la racine , et dernierement le sous-arbre droite
    le type de parcours suffixe traite les sous-arbre du noeud avant qu'il traite le noeud
    on déduit que le deuxième parcours est plus couteux au niveau du temps
"""


def maxi_bst(tree):
    """returns the data of the max node in binary search tree"""

    return max(extract_value(tree))


# print(maxi_bst(abr1))


def mini_bst(tree):
    """returns the data of the min node in the binary search tree"""

    return min(extract_value(tree))


# print(mini_bst(abr1))


def find_value(tree, value):
    """returns a True or False,depending on the existence of value in this binary search tree"""

    if tree == []:
        return False

    if root(tree) == value:
        return True

    return find_value(left_children(tree), value) or find_value(right_children(tree), value)


# print(find_value(abr1, 7))

def height(tree):
    """returns the height of binary search tree"""

    if tree == []:
        return 0

    else:
        return 1 + max(height(left_children(tree)), height(right_children(tree)))


# print(height(abr1))


def find_succesor(tree, node):
    """returns the successor or the successors of a given node"""

    list = []

    if tree:

        if node == root(tree) and left_children(tree) != [] and right_children(tree) != []:
            list += [left_children(tree)[0], right_children(tree)[0]]


        elif node == root(tree) and tree_void(tree):
            return []

        elif node == root(tree) and left_children(tree) != [] and right_children(tree) == []:
            list.append(left_children(tree)[0])

        elif node == root(tree) and left_children(tree) == [] and right_children(tree) != []:
            list.append(right_children(tree)[0])

        list += find_succesor(left_children(tree), node)
        list += find_succesor(right_children(tree), node)

    return list


# print(find_succesor(abr1, 17))
# print(find_succesor(abr2, 50))


def sorted_bst(tree):
    """displays a list containing the values sorted of BST"""

    list = extract_value(tree)

    while list != sorted(list):

        for i in range(len(list) - 1):

            if list[i + 1] < list[i]:
                list[i], list[i + 1] = list[i + 1], list[i]

    return list


# print(sorted_bst(abr1))


def is_avl(tree):
    """checks if the BST is an AVL"""

    if tree is avl:
        return True

    return False

# print(is_avl(abr1))
# print(is_avl(abr2))
# print(is_avl(not_avl))
# print(is_avl(avl))
