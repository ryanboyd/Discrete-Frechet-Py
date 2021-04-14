#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

def EuclideanDistance(x1, y1, x2, y2):
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def ComputeDistance(distances, i, j, P, Q):

    if (distances[i][j] > -1):
        return distances[i][j]

    if (i == 0 and j == 0):
                distances[i][j] = EuclideanDistance(P[0][0], P[0][1], Q[0][0], Q[0][1]);
    
    elif  (i > 0 and j == 0):
        distances[i][j] = max(ComputeDistance(distances, i - 1, 0, P, Q),
                              EuclideanDistance(P[i][0], P[i][1], Q[0][0], Q[0][1]))
        
    elif (i == 0 and j > 0):
        distances[i][j] = max(ComputeDistance(distances, 0, j - 1, P, Q),
                              EuclideanDistance(P[0][0], P[0][1], Q[j][0], Q[j][1]))
        
    elif (i > 0 and j > 0):
        distances[i][j] = max(min(ComputeDistance(distances, i - 1, j, P, Q),
                              min(ComputeDistance(distances, i - 1, j - 1, P, Q),
                                  ComputeDistance(distances, i, j - 1, P, Q))),
                                  EuclideanDistance(P[i][0], P[i][1], Q[j][0], Q[j][1]))

    else:
        distances[i][j] = float('inf');

    return distances[i][j];


def FrechetDistance(P, Q):
    distances = [ [ None for y in range(len(P)) ]
                         for x in range(len(Q)) ]

    for y in range(0, len(P)):
        for x in range(0, len(Q)):
            distances[y][x] = -1

    return ComputeDistance(distances, len(P) - 1, len(Q) - 1, P, Q)



if __name__ == '__main__':
    P = [[1,1], [2,2], [3,3], [4,4]]
    Q = [[1,2], [2,1], [3,1], [4,7]]

    print('Frechet Distance: ' + str(FrechetDistance(P, Q)))
 
