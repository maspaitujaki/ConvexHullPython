import copy

from myConvexHull import utils


def ConvexHull(arr):
    ch = CHull(arr)
    return ch


class CHull:
    def __init__(self, points):
        self.simplices = []
        self.points = [[0, 0, 0] for _ in range(len(points))]
        for i in range(len(points)):
            self.points[i] = [points[i][0], points[i][1], i]
        self.__search_simplices()

    def __search_simplices(self):
        # Himpunan titik-titik diurutkan berdasarkan absis lalu ordinat
        sorted_points = utils.sort_coordinates(self.points)

        # Dua titik terekstrem merupakan bagian dari ConvexHull
        p_start = sorted_points.pop(0)
        p_end = sorted_points.pop()
        # self.simplices.append([p_start[2], p_end[2]])

        # Membagi ke 2 himpunan, ini merupakan 2 himpunan kanan dan kiri pertama
        s1 = utils.left_set(copy.deepcopy(sorted_points), p_start, p_end)
        s2 = utils.right_set(copy.deepcopy(sorted_points), p_start, p_end)

        # Masuk ke dalam fungsi yang rekurens untuk mencari simplex-simplex ConvexHull
        # Menggunakan algoritma divide and conquer
        self.__dnc_chull_left(s1, p_start, p_end)
        self.__dnc_chull_right(s2, p_start, p_end)

    def __dnc_chull_left(self, points, p_start, p_end):
        if len(points) == 0:
            self.simplices.append([p_start[2], p_end[2]])
        else:
            p_farthest = utils.farthest_point(points, p_start, p_end)
            s_left = utils.left_set(points, p_start, p_farthest)
            s_right = utils.left_set(points, p_farthest, p_end)
            self.__dnc_chull_left(s_left, p_start, p_farthest)
            self.__dnc_chull_left(s_right, p_farthest, p_end)

    def __dnc_chull_right(self, points, p_start, p_end):
        if len(points) == 0:
            self.simplices.append([p_start[2], p_end[2]])
        else:
            p_farthest = utils.farthest_point(points, p_start, p_end)
            s_left = utils.right_set(points, p_start, p_farthest)
            s_right = utils.right_set(points, p_farthest, p_end)
            self.__dnc_chull_right(s_left, p_start, p_farthest)
            self.__dnc_chull_right(s_right, p_farthest, p_end)
