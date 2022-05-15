class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int:
        ans = -1
        valid_points = []
        min_distance = 10e4
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                valid_points.append(point)
                man_hattan_distance = abs(x - point[0]) + abs(y - point[1])
                if man_hattan_distance < min_distance:
                    min_distance = man_hattan_distance
                    ans = index

        # print(valid_points)
        if valid_points:
            return ans
        else:
            return -1


if __name__ == "__main__":
    x = 3
    y = 4
    points = [[2,3]]

    s = Solution().nearestValidPoint(x, y, points)
    print(s)
