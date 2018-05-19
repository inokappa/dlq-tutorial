import json
import unittest
import handler

class HelloTest(unittest.TestCase):
    def test_hello(self):
        event = {'hello': 'world'}
        context = ''
        self.assertEqual(handler.hello(event, context), 'hello world.')

    def test_hello_exception(self):
        event = {}
        context = ''
        with self.assertRaises(Exception):
            handler.hello(event, context)

    def test_hello_exception_message(self):
        event = {}
        context = ''
        with self.assertRaises(Exception) as ex:
            handler.hello(event, context)
        ex_message = ex.exception.args[0]
        self.assertEqual(ex_message, 'Noooooooooooooo eventtttttttttt.')

    def test_world(self):
        event = {'hello': 'world'}
        context = ''
        self.assertEqual(handler.world(event), 'hello world.')

    def test_world_exception(self):
        event = {}
        context = ''
        with self.assertRaises(Exception):
            handler.world(event)

    def test_world_exception_message(self):
        event = {}
        context = ''
        with self.assertRaises(Exception) as ex:
            handler.world(event)
        ex_message = ex.exception.args[0]
        self.assertEqual(ex_message, 'Erroooooooooooooooooooor.')
