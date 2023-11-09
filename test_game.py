import unittest
import tkinter as tk

import game


class TestCreateMenu(unittest.TestCase):
    def test__create_menu(self):
        root = tk.Tk()
        app = (root)
        app._create_menu()

        self.assertIsNotNone(app._create_menu())


if __name__ == '__main__':
    unittest.main()

