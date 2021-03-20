from audioop import reverse

from classes.sort_order import SortOrder
from classes.material import Material


class ToolsManager:
    def __init__(self, tools=[]):
        self.tools = tools

    def __del__(self):
        pass

    def search_by_material(self, material: Material):
        search_material = []
        for tools in self.tools:
            if tools.material == material:
                search_material.append(tools)
        return search_material

    def search_by_weight(self, weight: int):
        search_weight = []
        for tools in self.tools:
            if tools.weight == weight:
                search_weight.append(tools)
        return search_weight

    def sort_by_price(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            return sorted(self.tools, key=lambda tools: tools.price, reverse=False)
        return sorted(self.tools, key=lambda tools: tools.price, reverse=True)
