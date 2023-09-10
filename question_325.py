# The United States uses the imperial system of weights and measures,
# which means that there are many different, seemingly arbitrary units to measure distance.
# There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.

# Create a data structure that can efficiently convert a certain quantity of one unit
# to the correct amount of any other unit.
# You should also allow for additional units to be added to the system.


from collections import defaultdict


class ConversionGraph:
    def __init__(self):
        # Graph as an adjacency list
        self.graph = defaultdict(dict)

    def add_conversion(self, unit_from, unit_to, factor):
        """Add conversion factor between unit_from and unit_to."""
        self.graph[unit_from][unit_to] = factor
        self.graph[unit_to][unit_from] = 1 / factor

    def _find_conversion_factor(self, current, target, visited, current_factor):
        """Recursive helper function to find conversion factor."""
        if current == target:
            return current_factor

        visited.add(current)

        for neighbor, factor in self.graph[current].items():
            if neighbor not in visited:
                conversion_factor = self._find_conversion_factor(
                    neighbor, target, visited, current_factor * factor
                )
                if conversion_factor is not None:
                    return conversion_factor

        return None

    def convert(self, quantity, unit_from, unit_to):
        """Convert quantity from unit_from to unit_to."""
        if unit_from not in self.graph or unit_to not in self.graph:
            raise ValueError("Units not recognized.")

        factor = self._find_conversion_factor(unit_from, unit_to, set(), 1)

        if factor is None:
            raise ValueError(f"No conversion path found from {unit_from} to {unit_to}.")

        return quantity * factor


# Create conversion graph
conv_graph = ConversionGraph()

# Add basic imperial distance conversions
conv_graph.add_conversion("inch", "foot", 1 / 12)
conv_graph.add_conversion("foot", "yard", 1 / 3)
conv_graph.add_conversion("yard", "chain", 1 / 22)
conv_graph.add_conversion("chain", "mile", 1 / 80)

# Add some conversions to metric system
conv_graph.add_conversion("inch", "cm", 2.54)
conv_graph.add_conversion("cm", "meter", 1 / 100)

# Test conversions
print(conv_graph.convert(12, "inch", "foot"))  # Output should be 1
print(conv_graph.convert(1, "mile", "inch"))  # Output should be 63,360
print(conv_graph.convert(1, "meter", "yard"))  # Output should be approximately 1.094

# Add a new unit
conv_graph.add_conversion("furlong", "mile", 1 / 8)

# Test conversion with new unit
print(conv_graph.convert(1, "furlong", "chain"))  # Output should be 10
