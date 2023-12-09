from typing import Dict, List, Callable
from collections import namedtuple
from math import lcm


Path = namedtuple("Path", ["left", "right"])

class InstructionManual:

    def __init__(self, input_file: str):
        self.input_file = input_file
        self.extract_mappings()

    def extract_mappings(self):
        with open(self.input_file) as f:
            for line in f:
                # first line
                self.instruction_set = line.strip()
                self.paths: Dict[str, Path] = {}
                break
            for line in f:
                if line.strip() != "":
                    source_stuff, paths_stuff = line.strip().split("=")
                    source = source_stuff.strip()
                    left_stuff, right_stuff = paths_stuff.split(",")
                    left = left_stuff.split("(")[1].strip()
                    right = right_stuff.split(")")[0].strip()
                    self.paths[source] = Path(left, right)
    
    def traverse(self, starting: str, ending_cond: Callable[[str], bool]) -> int:
        traversals = 0
        curr = starting
        leftright = 0
        while not ending_cond(curr):
            traversals += 1
            options = self.paths[curr]
            if self.instruction_set[leftright] == "L":
                curr = options.left
            else:
                curr = options.right
            
            leftright += 1
            if leftright == len(self.instruction_set):
                leftright = 0
        return traversals

    @staticmethod
    def is_zzz(node: str) -> bool:
        return node == "ZZZ"
    
    @staticmethod
    def ends_z(node: str) -> bool:
        return node.endswith("Z")

    def get_starting_nodes(self) -> List[str]:
        return [path for path in self.paths.keys() if path.endswith("A")]   

    def sim_traverse(self) -> int:
        nodes = self.get_starting_nodes()
        traversals = []
        for node in nodes:
            traversals.append(self.traverse(node, self.ends_z))
        return traversals
        

def part1() -> int:
    im = InstructionManual("8_input.txt")
    return(im.traverse("AAA", im.is_zzz))


def part2() -> int:
    im = InstructionManual("8_input.txt")
    return lcm(*im.sim_traverse()) 


if __name__ == "__main__":
    print(part1())
    print(part2())
