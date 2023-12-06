from typing import List
from collections import namedtuple


CategoryMap = namedtuple("CategoryMap", ["source", "destination", "range"])

class SeedMappings:

    def __init__(self, input_file: str, is_seed_range: bool = False):
        self.input_file = input_file
        self.extractMappings(is_seed_range)

    def extractMappings(self, is_seed_range: bool = False) -> None:
        with open(self.input_file) as f:
            for line in f:
                # seeds
                if line.startswith("seeds"):
                    self.seeds = line.split(":")[1].strip().split(" ")
                    self.seeds = [int(seed) for seed in self.seeds]

                if line.startswith("seed-to-soil"):
                    self.seed_to_soil: List[CategoryMap] = []
                    for line in f:
                        if line.strip() == "":
                            break
                        [dest, src , rge] = line.split()
                        self.seed_to_soil.append(CategoryMap(int(src), int(dest), int(rge)))
                if line.startswith("soil-to-fertilizer"):
                    self.soil_to_fertilizer: List[CategoryMap] = []
                    for line in f:
                        if line.strip() == "":
                            break
                        [dest, src , rge] = line.split()
                        self.soil_to_fertilizer.append(CategoryMap(int(src), int(dest), int(rge)))
                if line.startswith("fertilizer-to-water"):
                    self.fertilizer_to_water: List[CategoryMap] = []
                    for line in f:
                        if line.strip() == "":
                            break
                        [dest, src , rge] = line.split()
                        self.fertilizer_to_water.append(CategoryMap(int(src), int(dest), int(rge)))
                if line.startswith("water-to-light"):
                    self.water_to_light: List[CategoryMap] = []
                    for line in f:
                        if line.strip() == "":
                            break
                        [dest, src , rge] = line.split()
                        self.water_to_light.append(CategoryMap(int(src), int(dest), int(rge)))
                if line.startswith("light-to-temperature"):
                    self.light_to_temperature: List[CategoryMap] = []
                    for line in f:
                        if line.strip() == "":
                            break
                        [dest, src , rge] = line.split()
                        self.light_to_temperature.append(CategoryMap(int(src), int(dest), int(rge)))
                if line.startswith("temperature-to-humidity"):
                    self.temperature_to_humidity: List[CategoryMap] = []
                    for line in f:
                        if line.strip() == "":
                            break
                        [dest, src , rge] = line.split()
                        self.temperature_to_humidity.append(CategoryMap(int(src), int(dest), int(rge)))
                if line.startswith("humidity-to-location"):
                    self.humidity_to_location: List[CategoryMap] = []
                    for line in f:
                        if line.strip() == "":
                            break
                        [dest, src , rge] = line.split()
                        self.humidity_to_location.append(CategoryMap(int(src), int(dest), int(rge)))

    @staticmethod
    def calculate_mapping(input: List[int], mappings: List[CategoryMap]) -> List[int]:
        results = []
        for value in input: 
            found = False
            for mapping in mappings:
                if mapping.source <= value <= (mapping.source + mapping.range):
                    offset = mapping.destination - mapping.source
                    results.append(value + offset)
                    found = True
            if not found:
                results.append(value)
            
        return results


def part1() -> int:
    mf = SeedMappings("5_input.txt")

    # seed to soil    
    soils = mf.calculate_mapping(mf.seeds, mf.seed_to_soil)
    fertilizers = mf.calculate_mapping(soils, mf.soil_to_fertilizer)
    waters = mf.calculate_mapping(fertilizers, mf.fertilizer_to_water)
    lights = mf.calculate_mapping(waters, mf.water_to_light)
    temps = mf.calculate_mapping(lights, mf.light_to_temperature)
    humidities = mf.calculate_mapping(temps, mf.temperature_to_humidity)
    locations = mf.calculate_mapping(humidities, mf.humidity_to_location)

    return min(locations)


if __name__ == "__main__":
    print(part1())


