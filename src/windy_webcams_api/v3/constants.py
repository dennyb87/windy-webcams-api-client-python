from enum import Enum, unique


@unique
class WebcamFeature(str, Enum):
    categories = "categories"
    images = "images"
    location = "location"
    player = "player"
    urls = "urls"


@unique
class Category(str, Enum):
    landscape = "landscape"
    traffic = "traffic"
    meteo = "meteo"
    uncategorized = "uncategorized"
    building = "building"
    indoor = "indoor"
    city = "city"
    water = "water"
    area = "area"
    forest = "forest"
    mountain = "mountain"
    island = "island"
    beach = "beach"
    airport = "airport"
    park = "park"
    harbor = "harbor"
    pool = "pool"
    golf = "golf"
    lake = "lake"
    bay = "bay"
    square = "square"
    coast = "coast"
    sportarea = "sportarea"
    resort = "resort"
    camping = "camping"
    xmasmarket = "xmasmarket"
    underwater = "underwater"
    other = "other"


@unique
class Continent(str, Enum):
    AF = "AF"
    AN = "AN"
    AS = "AS"
    EU = "EU"
    NA = "NA"
    OC = "OC"
    SA = "SA"
