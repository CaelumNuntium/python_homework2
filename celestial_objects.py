import math


class CelestialObject(object):
    def __init__(self, ra, dec):
        self.ra = ra
        self.dec = dec

    def show_coordinates(self):
        print(f"right ascension: {self.ra}\ndeclination: {self.dec}")

    def upper_culmination(self, lat):
        return 90 - abs(lat - self.dec)

    def lower_culmination(self, lat):
        return abs(lat + self.dec) - 90


class Star(CelestialObject):
    def __init__(self, ra, dec, temperature, radius):
        self.ra = ra
        self.dec = dec
        self.temperature = temperature
        self.radius = radius
        self.lum = (self.temperature / 5772) ** 4 * self.radius ** 2


class Galaxy(CelestialObject):
    def __init__(self, ra, dec, distance, apparent_mag):
        self.ra = ra
        self.dec = dec
        self.distance = distance
        self.apparent_mag = apparent_mag
        self.abs_mag = self.apparent_mag - 25 - 5 * math.log10(self.distance)


st_petersburg_lat = 59.9375
polaris = Star(ra=37.95454167, dec=89.26411111, temperature=6015, radius=37.5)
print(polaris.lum)
print(polaris.upper_culmination(st_petersburg_lat))
print(polaris.lower_culmination(st_petersburg_lat))
andromeda = Galaxy(ra=10.68458333, dec=41.26916667, distance=0.765, apparent_mag=3.44)
print(andromeda.abs_mag)
print(andromeda.upper_culmination(st_petersburg_lat))
print(andromeda.lower_culmination(st_petersburg_lat))
