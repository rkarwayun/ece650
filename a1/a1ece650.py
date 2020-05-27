from __future__ import print_function

import re
import sys

in_street = dict()
street_list = dict()
# vertex_list = dict()
ver_list = dict()
intersection_list = list()
edge_list = dict()


class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return '({0:.2f},{1:.2f})'.format(self.x, self.y)

    def __str__(self):
        return repr(self)

    """def __eq__(self, p):
        return self.x == p.x and self.y == p.y"""

    def prnt(self):
        opt = "(" + '{0:.2f}'.format(self.x) + "," + '{0:.2f}'.format(self.y) + ")"
        return opt


def point(p1, p2):
    if p1.x == p2.x and p1.y == p2.y:
        return True
    else:
        return False


class Edge(object):
    def __init__(self, s, d):
        self.v1 = int(s)
        self.v2 = int(d)

    def __repr__(self):
        return "<" + str(self.v1) + "," + str(self.v2) + ">"

    def prnt(self):
        opt = "<" + str(self.v1) + "," + str(self.v2) + ">"
        return opt


def edge(e1, e2):
    if e1.v1 == e2.v1 and e1.v2 == e2.v2:
        return True
    else:
        return False


def printVertices():
    sys.stdout.write("V = {" + '\n')
    i = 0
    for p in ver_list:
        strin = "  " + str(p) + ": " + ver_list.get(p).prnt()
        # if i < len(vertex_list) - 1:
            # strin = strin
        sys.stdout.write(strin + '\n')
        i = i + 1
    sys.stdout.write("}" + '\n')


def printEdges():
    sys.stdout.write("E = {" + '\n')
    i = 0
    for e in edge_list:
        strin = "  " + e.prnt()
        if i < len(edge_list) - 1:
            strin = strin + ","
        sys.stdout.write(strin + '\n')
        i = i + 1
    sys.stdout.write("}" + '\n')


def addStreet(name, plist):
    # check if street is already present in the db.
    if name in street_list:
        pass
    else:
        # iterate to find the current number
        key_list = in_street.keys()
        maxi = 0
        for ii in key_list:
            maxi = max(maxi, ii)
        maxi = maxi + 1
        in_street[maxi] = name
        street_list[name] = plist
    # print(street_list)


def updateStreet(name, plist):
    if name in street_list:
        street_list[name] = plist


def remove(name):
    if name in street_list:
        street_list.pop(name)
        for ii in in_street:
            if in_street[ii] == name:
                in_street.pop(ii)
                break


def addOrUpdateStreet(name, pList):
    name1 = str(name).lower()
    street_list[name1] = pList


def addVertexToList(v):
    # ver_list is <index, vertex>
    ind = 0
    for i in ver_list:
        ind = max(ind, i)
        if point(ver_list.get(i), v):
            return
    ind = ind + 1
    ver_list[ind] = v



def isEdge(e):
    for e1 in edge_list:
        if edge(e1, e):
            return True
    return False


def inVertex(p1):
    for i in ver_list:
        if point(ver_list.get(i), p1):
            return True
    return False


def getV(p):
    for i in ver_list:
        if point(ver_list.get(i), p):
            return i


def addEdgeToList(p1, p2):
    if point(p1, p2):
        return
    if inVertex(p1) and inVertex(p2):
        v1 = getV(p1)
        v2 = getV(p2)
        if v1 is not None and v2 is not None:
            e = Edge(v1, v2)
            e2 = Edge(v2, v1)
            if isEdge(e) or isEdge(e2):
                pass
            else:
                edge_list[e] = "Yes"


def addIntersection(p1):
    for i in intersection_list:
        if point(p1, i):
            return
    intersection_list.append(p1)


def distance(p1, p2):
    dist_2 = (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
    dist = float(dist_2 ** 0.5)
    return dist


def isBetween(p1, p2, p):
    if point(p1, p) or point(p2, p):
        return False
    f1 = float(distance(p1, p) + distance(p2, p))
    s1 = '{0:.5f}'.format(f1)  # '{0:.2f}'.format(self.x)
    f2 = float(distance(p1, p2))
    s2 = '{0:.5f}'.format(f2)
    d1 = str(distance(p1, p) + distance(p2, p))
    d2 = str(distance(p1, p2))
    # if distance(p1, p) + distance(p2, p) is distance(p1, p2):
        # return True
    if s1 == s2:
        return True
    else:
        return False


def findPoint(i1):
    pass


def reduceE(p):
    edge_copy = edge_list.copy()
    for e in edge_copy:
        i1, i2 = e.v1, e.v2
        p1 = ver_list.get(i1)
        p2 = ver_list.get(i2)
        if isBetween(p1, p2, p) is True:
            edge_list.pop(e)
            # print(e, p1, p2, p)
            addEdgeToList(p1, p)
            addEdgeToList(p2, p)




def reduceEdges():
    for i in intersection_list:
        reduceE(i)


def intersection(p1, p2, p3, p4):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    x3, y3 = p3.x, p3.y
    x4, y4 = p4.x, p4.y

    a1 = float(y2 - y1)
    b1 = float(x1 - x2)
    c1 = float((a1 * x1) + (b1 * y1))
    a2 = float(y4 - y3)
    b2 = float(x3 - x4)
    c2 = float((a2 * x3) + (b2 * y3))

    min_l1_x = min(x1, x2);
    min_l1_y = min(y1, y2)
    max_l1_x = max(x1, x2);
    max_l1_y = max(y1, y2)
    min_l2_x = min(x3, x4);
    min_l2_y = min(y3, y4)
    max_l2_x = max(x3, x4);
    max_l2_y = max(y3, y4)

    det = float((a1 * b2) - (a2 * b1))

    if det != 0:
        # print("154", p1, p2, p3, p4)
        # print(a1, b1, c1, a2, b2, c2, det)
        x = float(((b2 * c1) - (b1 * c2)) / det)
        y = float(((a1 * c2) - (a2 * c1)) / det)
        # print("x:", x, "y,", y)
        l1 = False
        l2 = False

        if min_l1_x <= x <= max_l1_x:
            if min_l1_y <= y <= max_l1_y:
                l1 = True
        if min_l2_x <= x <= max_l2_x:
            if min_l2_y <= y <= max_l2_y:
                l2 = True
        if l1 == True and l2 == True:
            addVertexToList(p1)
            addVertexToList(p2)
            pint = Point(x, y)
            # print(p1, p2, p3, p4, pint)
            addVertexToList(pint)
            addIntersection(pint)
            addVertexToList(p3)
            addVertexToList(p4)
            addEdgeToList(p1, pint)
            addEdgeToList(p2, pint)
            addEdgeToList(p3, pint)
            addEdgeToList(p4, pint)
        else:
            pass
    elif point(p2, p3):
        addVertexToList(p1)
        addVertexToList(p2)
        addVertexToList(p3)
        addVertexToList(p4)
        addEdgeToList(p1, p2)
        addIntersection(p3)
        addEdgeToList(p3, p4)
    elif point(p1, p4):
        addVertexToList(p1)
        addVertexToList(p2)
        addVertexToList(p3)
        addVertexToList(p4)
        addEdgeToList(p1, p2)
        addEdgeToList(p3, p4)
        addIntersection(p4)
    elif x1 == x2 == x3 == x4:
        """logic for intersection point and adding it to appropriate databases"""
        range1 = abs(y2 - y1)
        range2 = abs(y4 - y3)
        if range1 > range2:
            parent = 1
        else:
            parent = 2
        if parent == 1:
            if min_l1_y < y3 < max_l1_y:
                addVertexToList(p1)
                addVertexToList(p2)
                addVertexToList(p3)

                # testing code begins
                addIntersection(p3)
                addEdgeToList(p1, p2)
                addEdgeToList(p3, p4)
                # testing code ends

            if min_l1_y < y4 < max_l1_y:
                addVertexToList(p1)
                addVertexToList(p2)
                addVertexToList(p4)

                # testing code begins
                addIntersection(p4)
                addEdgeToList(p1, p2)
                addEdgeToList(p3, p4)
                # testing code ends

        elif parent == 2:
            if min_l2_y < y1 < max_l2_y:
                addVertexToList(p3)
                addVertexToList(p4)
                addVertexToList(p1)

                # testing code begins
                addIntersection(p1)
                addEdgeToList(p1, p2)
                addEdgeToList(p3, p4)
                # testing code ends

            if min_l2_y < y2 < max_l2_y:
                addVertexToList(p3)
                addVertexToList(p4)
                addVertexToList(p2)

                # testing code begins
                addIntersection(p2)
                addEdgeToList(p1, p2)
                addEdgeToList(p3, p4)
                # testing code ends

    elif y1 == y2 == y3 == y4:
        """logic for intersection point and adding it to appropriate databases"""
        range1 = abs(x2 - x1)
        range2 = abs(x4 - x3)
        if range1 > range2:
            parent = 1
        else:
            parent = 2
        if parent == 1:
            if min_l1_x < x3 < max_l1_x:
                addVertexToList(p1)
                addVertexToList(p2)
                addVertexToList(p3)

                # testing code begins
                addIntersection(p3)

                addIntersection(p1)
                addIntersection(p2)

                addEdgeToList(p1, p2)
                addEdgeToList(p4, p3)
                # testing code ends

            if min_l1_x < x4 < max_l1_x:
                addVertexToList(p1)
                addVertexToList(p2)
                addVertexToList(p4)

                # testing code begins
                addIntersection(p4)

                addIntersection(p1)
                addIntersection(p2)


                addEdgeToList(p1, p2)
                addEdgeToList(p3, p4)
                # testing code ends

        if parent == 2:
            if min_l2_x < x1 < max_l2_x:
                addVertexToList(p3)
                addVertexToList(p4)
                addVertexToList(p1)

                # testing code begins
                addIntersection(p1)

                addIntersection(p4)
                addIntersection(p3)

                addEdgeToList(p1, p2)
                addEdgeToList(p3, p4)
                # testing code ends

            if min_l2_x < x2 < max_l2_x:
                addVertexToList(p3)
                addVertexToList(p4)
                addVertexToList(p2)

                # testing code begins
                addIntersection(p2)

                addIntersection(p3)
                addIntersection(p4)

                addEdgeToList(p1, p2)
                addEdgeToList(p3, p4)
                # testing code ends




def generateGraph():
    # finding the max index in the in_street dict
    numm = 0
    for i in in_street:
        numm = max(numm, i)

    # clearing existing lists
    # vertex_list.clear()
    ver_list.clear()
    edge_list.clear()
    for i in intersection_list:
        intersection_list.remove(i)

    # computing the vertices and edges for the current input
    # print(in_street)
    # print(street_list)
    for i in range(1, numm + 1):
        if in_street.get(i) is None:
            continue
        for j in range(i + 1, numm + 1):
            if j == i:
                continue
            if in_street.get(j) is None:
                continue

            street1 = in_street.get(i)
            street2 = in_street.get(j)

            if street_list.get(street1) is None or street_list.get(street2) is None:
                continue

            list1 = street_list.get(street1)
            list2 = street_list.get(street2)

            l1 = len(list1)
            l2 = len(list2)

            # print(street1, list1)
            # print(street2, list2)

            for ii in range(1, l1):
                for jj in range(1, l2):
                    p1 = list1[ii - 1];
                    p2 = list1[ii]
                    p3 = list2[jj - 1]
                    p4 = list2[jj]
                    # print(p1, p2, p3, p4)
                    intersection(p1, p2, p3, p4)
    # print(ver_list)
    reduceEdges()
    # print(intersection_list)

    """for i in ver_list:
        print(i, ver_list[i])"""


    printVertices()
    printEdges()


def isInDB(name):
    # counter-intuitive, it is returning false when it is in DB
    if name in street_list:
        return False
    else:
        return True


def isValidName(name):
    # checking if name is purely alphabetical
    for ch in name:
        if ch.isalpha() or ch.isspace():
            pass
        else:
            return False
    return True


def brackets(coord):
    flag = True
    chh = []
    i = 0
    while i < len(coord) and flag:
        h = coord[i]
        if h == "(":
            chh.append("(")
        elif h == ")":
            if len(chh) == 0:
                flag = False
            else:
                chh.pop()
        i = i + 1
    return (len(chh) == 0) and flag


def isvalid(coor):
    reg = r'\(-?\d+,-?\d+\)'
    comp = re.compile(reg)
    if comp.match(coor):
        return True
    else:
        # print(coor)
        return False


def readCoordinates(coor):
    coor = re.sub(' +', '', coor)
    coor = re.sub('\)\(', ') (', coor)
    coor = re.sub('\(', '(', coor)
    coor1 = coor.split(' ')
    # print("here", coor1)
    if all(isvalid(chh) for chh in coor1):
        pass
    else:
        return []
    coor.strip()
    # print(coor)
    reg = r'[ ]?\(-?\d+,-?\d+\)'
    compreg = re.compile(reg)
    """if compreg.match(coor):
        pass
    else:
        return []"""
    cc = compreg.findall(coor)
    coor.replace(" ", "")
    # print(coor)
    pp = list()
    pList = list()
    for ch in cc:
        reg2 = '\(+|,+|\)+'
        c = re.split(reg2, ch)
        # print(c)
        for i in c:
            i = i.strip()
            if i != "":
                pp.append(float(i))
    if len(pp) % 2 != 0:
        # print(pp)
        return []
    else:
        index = 0
        while index + 1 < len(pp):
            p = Point(pp[index], pp[index + 1])
            pList.append(p)
            index = index + 2
        return pList


def parseInput(line):
    # try:
    if line[0] == 'r':
        c = re.split(' +"|"', line)
        # print(c, len(c))
    else:
        c = re.split('" + | +"|"', line)
        # print(c, len(c))

    if len(c) < 1 or len(c) > 3:
        sys.stderr.write("Error: Unidentified or incorrect command. Please check the command." + '\n')
        return

    if c[0] == 'r':
        try:
            try:
                if len(c) == 3 and c[2] == '' and line[1] == " ":
                    name = c[1]
                    # print(street_list)
                    name = name.lower()
                    del street_list[name]

                    for ii in in_street:
                        if in_street[ii] == name:
                            del [ii]
                            break
                    # print(street_list)
                else:
                    sys.stderr.write("Error: r command syntax is not proper." + '\n')
            except KeyError:
                sys.stderr.write("Error: Given street was either never added or was already deleted." + '\n')
        except UnboundLocalError and IndexError:
            sys.stderr.write("Error: r command syntax is not proper." + '\n')
    elif c[0] == 'g':
        if len(c) == 1 and c[0] == 'g':
            # print("generating graph")
            generateGraph()
            pass
        else:
            sys.stderr.write("Error: g command syntax is not proper." + '\n')
    elif c[0] == 'a':
        try:
            indd = line.find(c[2])
            c[1] = c[1].lower()
            if line[1] == " " and c[2] != "" and line[indd] == " ":
                if isValidName(c[1]) and isInDB(c[1]):
                    if brackets(c[2]):
                        pList = readCoordinates(c[2])
                        if len(pList) != 0:
                            # print(c[1], pList)
                            name = c[1].lower()
                            addStreet(name, pList)
                            pass
                        else:
                            sys.stderr.write(
                                "Error: Please check the coordinates in the command as they are not in order." + '\n')
                    else:
                        sys.stderr.write(
                            "Error: Please check the parenthesis in the command as they are not in order." + '\n')
                else:
                    sys.stderr.write("Error: Please check the street name as either it is not proper or is already added." + '\n')
            else:
                sys.stderr.write("Error: Please check the command syntax and input it accordingly." + '\n')
        except UnboundLocalError and IndexError:
            sys.stderr.write("Error: Please check the command syntax and input it accordingly." + '\n')
    elif c[0] == 'c':
        try:
            indd = line.find(c[2])
            c[1] = c[1].lower()
            if line[1] == " " and c[2] != "" and line[indd] == " ":
                if isValidName(c[1]) and (isInDB(c[1]) == False):
                    if brackets(c[2]):
                        pList = readCoordinates(c[2])
                        if len(pList) != 0:
                            # print(c[1], pList)
                            name = c[1].lower()
                            updateStreet(name, pList)
                        else:
                            sys.stderr.write(
                                "Error: Please check the coordinates in the command as they are not in order." + '\n')
                    else:
                        sys.stderr.write(
                            "Error: Please check the parenthesis in the command as they are not in order." + '\n')
                else:
                    sys.stderr.write("Error: Please check the street name as either it is not proper or was not added." + '\n')
            else:
                sys.stderr.write("Error: Please check the command syntax and input it accordingly." + '\n')
        except UnboundLocalError and IndexError:
            sys.stderr.write("Error: Please check the command syntax and input it accordingly." + '\n')
    else:
        sys.stderr.write("Error: Above command is not recognized." + '\n')


# except:
# sys.stderr.write("Error: Unidentified or Incorrect command\n")


def main():
    while True:
        # print("Awaiting Input")
        line = sys.stdin.readline()
        line = line.strip()
        if line == '':
            # print("Exiting....")
            break
        else:
            parseInput(line)


if __name__ == '__main__':
    main()
