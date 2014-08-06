# -*- coding: utf-8 -*-

import unittest
from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_root(self):
        from .views import root
        request = testing.DummyRequest()
        info = root(request)
        self.assertEqual(info['project'], 'pipette')
