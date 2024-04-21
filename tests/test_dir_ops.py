import unittest
from src.dir_ops import get_subdirs

class TestGetSubdirs(unittest.TestCase):

    def test_get_subdirs_normal(self):
        dirs = ['dir1', 'dir2', 'file.txt']
        expected = ['dir1', 'dir2']
        actual = get_subdirs(dirs)
        self.assertEqual(expected, actual)

    def test_get_subdirs_empty(self):
        dirs = []
        expected = []
        actual = get_subdirs(dirs)
        self.assertEqual(expected, actual)

    def test_get_subdirs_no_subdirs(self):
        dirs = ['file1.txt', 'file2.txt']
        expected = []
        actual = get_subdirs(dirs)
        self.assertEqual(expected, actual)

