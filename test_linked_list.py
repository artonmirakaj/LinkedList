#!/usr/bin/env python

import os
import sys
import unittest

bin_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(bin_dir)

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
	def test_stack_methods(self):
		stack = LinkedList()
		stack.push(1)
		stack.push(2)
		stack.push(3)
		self.assertEqual(stack.pop(), 3)
		self.assertEqual(stack.pop(), 2)
		self.assertEqual(stack.pop(), 1)
		self.assertEqual(stack.pop(), None)

if __name__ == '__main__':
	unittest.main()