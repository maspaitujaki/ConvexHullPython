import copy

import numpy as np


def sort_coordinates(points):
    return sorted(points, key=lambda k: [k[0], k[1]])


def determinant(p_start, p_end, p):
    p_s = copy.deepcopy(p_start)
    p_e = copy.deepcopy(p_end)
    pp = copy.deepcopy(p)

    p_s[2] = 1
    p_e[2] = 1
    pp[2] = 1

    p_s = np.array(p_s)
    p_e = np.array(p_e)
    pp = np.array(pp)

    mat = [p_s, p_e, pp]
    return np.linalg.det(mat)


def point_distance_to_line(p_start, p_end, p):
    p_start, p_end, p = to_np_arr(p_start, p_end, p)
    return np.abs(np.cross(p_end - p_start, p_start - p)) / np.linalg.norm(p_end - p_start)


def farthest_point(points, p_start, p_end):
    p = None
    for point in points:
        if p is None:
            p = point
        d_p = point_distance_to_line(p_start, p_end, p)
        d_point = point_distance_to_line(p_start, p_end, point)
        if d_point > d_p:
            p = point
        elif d_point == d_p and angle(p_start, point, p_end) > angle(p_start, p, p_end):
            p = point
    return p


def angle(p1, p2, p3):
    a, b, c = to_np_arr(p1, p2, p3)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.arccos(cosine_angle)


def to_np_arr(p1, p2=None, p3=None):
    p1 = np.array([p1[0], p1[1]])
    if p2 is None:
        return p1
    p2 = np.array([p2[0], p2[1]])
    if p3 is None:
        return p1, p2
    p3 = np.array([p3[0], p3[1]])
    return p1, p2, p3


def left_set(points, p_start, p_end):
    s = []
    for p in points:
        if determinant(p_start, p_end, p) > 0 and p[2] != p_start[2] and p[2] != p_end[2]:
            s.append(p)
    return s


def right_set(points, p_start, p_end):
    s = []
    for p in points:
        if determinant(p_start, p_end, p) < 0 and p[2] != p_start[2] and p[2] != p_end[2]:
            s.append(p)
    return s
