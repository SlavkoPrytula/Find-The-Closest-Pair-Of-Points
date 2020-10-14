import math
import time


def distance(p1, p2):
    # Calculate the distance
    return math.sqrt(pow(p1[0] - p2[0], 2)
                     + pow(p1[1] - p2[1], 2))


def closest_pair_range(P, Q, d):
    midPoint = P[len(P) // 2][0]
    p1_x = p1_y = p2_x = p2_y = 0

    # Get the points in range (-d, d) according tho the mid point
    rangeDist = [Q[i] for i in range(len(Q)) if midPoint - d <= Q[i][0] <= midPoint + d]
    minDist = math.inf

    # i + 1, min(i + 15, len(rangeDist))
    # or
    # i + 1, min(i + int(d) // 2, len(rangeDist))
    # or
    # i + 1, min(i + int(d ** (1.0/5.0)), len(rangeDist))
    for i in range(len(rangeDist)):
        # Check at most 15 next values
        for j in range(i + 1, min(i + 15, len(rangeDist))):
            dNew = distance(rangeDist[i], rangeDist[j])

            if dNew < minDist:
                p1_x, p1_y, p2_x, p2_y = rangeDist[i][0], rangeDist[i][1], rangeDist[j][0], rangeDist[j][1]
                minDist = dNew  # Update the min distance
    return minDist, ([p1_x, p1_y], [p2_x, p2_y])


def bruteForce(points_x):
    p1_x = p1_y = p2_x = p2_y = 0
    minDist = math.inf

    # Take the min distance of possible pairs
    for i in range(len(points_x) - 1):
        if distance(points_x[i], points_x[i + 1]) < minDist:
            minDist = distance(points_x[i], points_x[i + 1])  # Update the min distance
            p1_x, p1_y, p2_x, p2_y = points_x[i][0], points_x[i][1], points_x[i + 1][0], points_x[i + 1][1]
    return minDist, ([p1_x, p1_y], [p2_x, p2_y])


def closest_pair(P):
    # Brut if tree points are left:
    lenP = len(P)
    if lenP <= 3:
        return bruteForce(P)

    # Sort arrays by x and y coordinates
    Pn = sorted(P, key=lambda x: x[0])
    Qn = sorted(P, key=lambda x: x[1])

    midPoint = lenP // 2
    Qx = Pn[:midPoint]  # Get left part of array with x sorted
    Rx = Pn[midPoint:]  # Get right part of array with x sorted

    # Recursively call
    dLeft, ([p1Left_x, p1Left_y], [p2Left_x, p2Left_y]) = closest_pair(Qx)  # Left side min
    dRight, ([p1Right_x, p1Right_y], [p2Right_x, p2Right_y]) = closest_pair(Rx)  # Right side min

    # Take the min value and assign the points
    if dLeft > dRight:
        minDistAll = dRight
        p1Min_x, p1Min_y, p2Min_x, p2Min_y = \
            p1Right_x, p1Right_y, p2Right_x, p2Right_y
    else:
        minDistAll = dLeft
        p1Min_x, p1Min_y, p2Min_x, p2Min_y = \
            p1Left_x, p1Left_y, p2Left_x, p2Left_y

    # Check the middle for closest pair of points
    d, ([p1_x, p1_y], [p2_x, p2_y]) = closest_pair_range(Pn, Qn, minDistAll)
    minDistPlane = min(d, minDistAll)

    # Return the min distance on a plane
    if minDistPlane == d:
        return minDistPlane, ([p1_x, p1_y], [p2_x, p2_y])
    else:
        return minDistPlane, ([p1Min_x, p1Min_y], [p2Min_x, p2Min_y])


if __name__ == '__main__':
    # points = [(82, 66), (33, 62), (98, 12), (41, 25), (92, 94),
    #           (17, 29), (78, 30), (25, 92), (19, 82), (42, 31)]
    # points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    points = [(447, 323), (781, 905), (40, 510), (952, 246), (409, 123), (913, 668), (203, 705), (504, 546), (752, 56), (557, 410), (181, 171), (849, 280), (97, 56), (10, 725), (608, 990), (107, 86), (642, 738), (448, 389), (241, 287), (808, 821), (979, 589), (729, 693), (695, 820), (341, 483), (69, 801), (500, 203), (545, 748), (592, 628), (56, 4), (743, 309), (959, 268), (3, 830), (300, 691), (626, 472), (827, 429), (786, 372), (170, 543), (98, 782), (383, 518), (510, 110), (543, 140), (801, 422), (16, 176), (958, 501), (280, 20), (685, 392), (469, 256), (26, 641), (62, 738), (265, 217), (349, 311), (181, 986), (409, 726), (151, 798), (888, 386), (631, 971), (176, 939), (226, 926), (480, 817), (415, 249), (971, 338), (250, 799), (917, 73), (243, 514), (892, 511), (994, 55), (962, 682), (802, 197), (916, 282), (333, 965), (513, 127), (82, 744), (678, 412), (595, 877), (828, 476), (855, 315), (294, 388), (32, 604), (264, 267), (995, 532), (71, 144), (75, 787), (529, 376), (48, 454), (466, 500), (439, 271), (937, 86), (46, 360), (435, 41), (708, 710), (638, 171), (508, 85), (359, 679), (709, 890), (736, 706), (491, 333), (414, 972), (492, 699), (810, 636), (325, 719)]
    start = time.time()
    print(closest_pair(points))
    print(time.time() - start)
