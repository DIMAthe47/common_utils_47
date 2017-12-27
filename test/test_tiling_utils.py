import unittest
import numpy as np
from itertools_utils import chunkify
import itertools

from tiling_utils import generate_tiles_rects


class TilingUtilsTest(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.rect_shape = (100, 100)
        self.true_tiles_rects = [(0, 0, 60, 60), (60, 0, 40, 60), (0, 60, 60, 40), (60, 60, 40, 40)]
        self.tile_shape = (60, 60)
        self.tile_step = (60, 60)

    def test_tiling(self):
        tiles_rects = generate_tiles_rects(self.rect_shape, self.tile_shape, self.tile_step, False)
        self.assertSequenceEqual(self.true_tiles_rects, tiles_rects)

    def test_tiling_generator(self):
        tiles_generator = generate_tiles_rects(self.rect_shape, self.tile_shape, self.tile_step, True)
        for i, tile in enumerate(tiles_generator):
            self.assertEqual(self.true_tiles_rects[i], tile)


if __name__ == '__main__':
    unittest.main()
