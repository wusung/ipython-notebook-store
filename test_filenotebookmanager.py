#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for bookstore
"""

from unittest import TestCase
import doctest

from bookstore.filenotebookmanager import FileNotebookManager

class TestFileNotebookManager(TestCase):
    def setUp(self):
    	pass

    def tearDown(self):
        pass

    def test_entry_points(self):
        pass
    
    def test_nb_dir(self):
    	pass

    def test_create_checkpoint(self):
    	filenotebookManager = FileNotebookManager()
        FileNotebookManager.create_checkpoint(name='test1', path='')
