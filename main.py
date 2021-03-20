from classes.sort_order import SortOrder
from manager.tools_manager import ToolsManager
from classes.material import Material
from classes.country import Country
from classes.wood_tools import WoodTools
from classes.ground_tools import GroundTools
from classes.size import Size

if __name__ == '__main__':
    tools = [WoodTools("Saw", 500, 29.99, Material.IRON,
                       Country.UKRAINE, "Woodcutters", Size.LIGHT),
             WoodTools("Ax", 880, 35.00, Material.COPPER,
                       Country.GERMANY, "Woodcutters", Size.MIDDLE),
             GroundTools("Supper Shovel", 780, 20.99, Material.PINE,
                         Country.USA, "Army units", "ВСЛ-110"),
             GroundTools("Infantry Shovel", 980, 45.00, Material.OAK,
                         Country.CHINA, "Army units", "Linneman's shovel")]

    manager = ToolsManager(tools)
    print("Search by material of tools")
    list_of_tools_searched_by_material = manager.search_by_material(Material.IRON)
    for tools in list_of_tools_searched_by_material:
        print(tools)

    print("Search by weight of tools")

    list_of_tools_searched_by_weight = manager.search_by_weight(weight=780)
    for tools in list_of_tools_searched_by_weight:
        print(tools)

    print("Sort by price")

    list_of_tools_sorted_by_price = manager.sort_by_price(SortOrder.ASC)
    for tools in list_of_tools_sorted_by_price:
        print(tools)
