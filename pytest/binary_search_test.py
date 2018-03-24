"""Tests for binary search function."""

import unittest

import binary_search

class TestBinarySearch(unittest.TestCase):
  def test_not_found(self):
    self.assertEqual(
        binary_search.binary_search([1, 2, 3, 4], 5),
        -1)

  def test_found(self):
    self.assertEqual(
        binary_search.binary_search([1, 2, 3, 4], 2),
        1)


if __name__ == '__main__':
  unittest.main()


