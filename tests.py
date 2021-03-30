import unittest
import main
from classes.country import Country
from classes.ground_tools import GroundTools
from classes.material import Material
from classes.size import Size
from classes.sort_order import SortOrder
from classes.wood_tools import WoodTools
from manager.tools_manager import ToolsManager


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.a = WoodTools("Saw", 500, 29.99, Material.IRON,
                           Country.UKRAINE, "Woodcutters", Size.LIGHT)
        self.b = WoodTools("Ax", 880, 35.00, Material.COPPER,
                           Country.GERMANY, "Woodcutters", Size.MIDDLE)
        self.c = GroundTools("Supper Shovel", 780, 36.99, Material.PINE,
                             Country.USA, "Army units", "ВСЛ-110")
        self.d = GroundTools("Infantry Shovel", 980, 45.00, Material.OAK,
                             Country.CHINA, "Army units", "Linneman's shovel")
        result = [self.a, self.b, self.c, self.d]
        self.ToolsManager = ToolsManager(result)
        self.maxDiff = None

    def test_search_by_material(self):
        self.assertEqual(self.ToolsManager.search_by_material(Material.IRON), [self.a])

    def test_sort_by_price(self):
        self.assertEqual(self.ToolsManager.sort_by_price(SortOrder.ASC), [self.a, self.b, self.c, self.d])

    def test_search_by_weight(self):
        self.assertEqual(self.ToolsManager.search_by_weight(980), [self.d])


if __name__ == '__main__':
    unittest.main()
