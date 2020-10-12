import math


def distance(p1, p2):
    # Calculate the distance
    return math.sqrt(pow(p1[0] - p2[0], 2)
                     + pow(p1[1] - p2[1], 2))


def brutePerimeter(points_x):
    minPer = math.inf

    for i in range(0, len(points_x)-2):
        for j in range(i+1, len(points_x)-1):
            for k in range(j+1, len(points_x)):

                d1 = distance(points_x[i], points_x[j])
                d2 = distance(points_x[i], points_x[k])
                d3 = distance(points_x[j], points_x[k])
                if sum([d1, d2, d3]) < minPer:
                    minPer = sum([d1, d2, d3])
                # p1_x, p1_y, p2_x, p2_y = points_x[i][0], points_x[i][1], points_x[i + 1][0], points_x[i + 1][1]

    return minPer, 0, 0, 0, 0


if __name__ == '__main__':
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(brutePerimeter(points))