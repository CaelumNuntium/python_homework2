import math


class Star(object):
    def __init__(self, m):
        self.m = m

    def __lt__(self, other):
        return self.m.__lt__(other.m)

    def __le__(self, other):
        return self.m.__le__(other.m)

    def __gt__(self, other):
        return self.m.__gt__(other.m)

    def __ge__(self, other):
        return self.m.__ge__(other.m)

    def __repr__(self):
        return f"Star (abs. magnitude = {self.m})"

    def __str__(self):
        return self.__repr__()


def find_cluster_magnitude(star_list, dist):
    g = 10 ** 0.4
    res = 0
    for star in star_list:
        res += math.pow(g, -star.m)
    return -2.5 * math.log10(res) - 5 + 5 * math.log10(dist)


stars = [Star(4), Star(1), Star(4), Star(3), Star(3), Star(4), Star(3), Star(2), Star(2), Star(4)]
print(sorted(stars))
print(find_cluster_magnitude(stars, 1000))
