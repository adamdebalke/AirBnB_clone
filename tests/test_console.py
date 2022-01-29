#!/usr/bin/python3
"""
The ``test_console`` module
==============================
Using ``test_console``
-------------------------
This is a test_console unittest file to test the console module.
"""
import unittest
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """Defines a class TestConsole.
    Test functionality of the console module.
    """
    help_quit = "Quit command to exit the program"
    help_EOF = "Exits the program"
    help_create = "Creates a new instance of a class, saves it to file\
 and prints the id"
    help_show = "Prints the string representation of an instance based\
 on the class name and id"
    help_destroy = "Deletes an instance based on the class name and id\
 and save the change into the JSON file"
    help_all = "Prints all string representation of all instances based\
 or not on the class name."
    help_update = "Updates an instance based on the class name and id by\
 adding or updating attribute and save the change into the JSON file"
    help_count = "Counts the number of instances of a certain class"

    all_classes_name = ["BaseModel", "User", "State", "City", "Amenity",
                        "Place", "Review"]
    all_classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def tearDown(self):
        """Remove storage file after test ends."""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_help_quit(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_quit)

    def test_help_EOF(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_EOF)

    def test_help_create(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_create)

    def test_help_show(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_show)

    def test_help_destroy(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_destroy)

    def test_help_all(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_all)

    def test_help_update(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_update)

    def test_help_count(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_count)

    def test_create(self):
        """Tests if the create command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                self.assertTrue(i + "." +
                                id_val in storage._FileStorage__objects.keys())

    def test_show(self):
        """Tests if the show command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("show" + " " + i + " " + id_val)
                str_obj = f.getvalue().strip()
                self.assertEqual(str(storage._FileStorage__objects
                                            .get(i + "." + id_val)), str_obj)

    def test_destroy(self):
        """Tests if the destroy command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                f.truncate(0)
                f.seek(0)
                self.assertTrue(i + "."
                                  + id_val in storage
                                ._FileStorage__objects.keys())
                HBNBCommand().onecmd("destroy" + " " + i + " " + id_val)
                self.assertTrue(i + "."
                                  + id_val not in storage
                                ._FileStorage__objects.keys())

    def test_all(self):
        """Tests if the all command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                HBNBCommand().onecmd("create" + " " + i)
            f.truncate(0)
            f.seek(0)
            lst_all = []
            for key in storage._FileStorage__objects.keys():
                lst_all.append(str(storage._FileStorage__objects[key]))
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), str(lst_all))

    def test_all_single(self):
        """Tests if the all with specific class command is
        functioning as expected.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                HBNBCommand().onecmd("create" + " " + i)
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("all" + " " + i)
                lst_all = []
                for key in storage._FileStorage__objects.keys():
                    if key.split('.')[0] == i:
                        lst_all.append(str(storage._FileStorage__objects[key]))
                self.assertEqual(f.getvalue().strip(), str(lst_all))

    def test_update_string(self):
        """Tests if the update command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                f.truncate(0)
                f.seek(0)
                self.assertTrue(i + "."
                                  + id_val in storage
                                ._FileStorage__objects.keys())
                HBNBCommand().onecmd("update" + " " + i + " "
                                              + id_val + '"first_name"'
                                              + '"Kidus Worku"')
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("show" + " " + i + " " + id_val)
                str_obj = f.getvalue().strip()
                self.assertEqual(str(storage._FileStorage__objects
                                            .get(i + "." + id_val)), str_obj)

    def test_update_int(self):
        """Tests if integer arguments are stored as int."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                f.truncate(0)
                f.seek(0)
                self.assertTrue(i + "."
                                  + id_val in storage
                                ._FileStorage__objects.keys())
                HBNBCommand().onecmd("update" + " " + i + " "
                                              + id_val + " "
                                              + "user_id" + " " + "89")
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("show" + " " + i + " " + id_val)
                str_obj = f.getvalue().strip()
                self.assertEqual(str(storage._FileStorage__objects
                                            .get(i + "." + id_val)), str_obj)
                self.assertTrue(type(storage._FileStorage__objects
                                     .get(i + "." + id_val)
                                     .user_id) is int)

    def test_update_float(self):
        """Tests if float arguments are stored as floats."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                f.truncate(0)
                f.seek(0)
                self.assertTrue(i + "." + id_val in storage
                                ._FileStorage__objects.keys())
                HBNBCommand().onecmd("update" + " " + i + " "
                                              + id_val + " " + "rating_value"
                                              + " " + "98.89")
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("show" + " " + i + " " + id_val)
                str_obj = f.getvalue().strip()
                self.assertEqual(str(storage._FileStorage__objects
                                            .get(i + "." + id_val)), str_obj)
                self.assertTrue(type(storage._FileStorage__objects
                                .get(i + "." + id_val)
                                .rating_value) is float)

    def test_count(self):
        """Tests if the count command is functioning as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                HBNBCommand().onecmd("create" + " " + i)
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("count" + " " + i)
                count = f.getvalue().strip()
                count_expected = 0
                for value in storage._FileStorage__objects.values():
                    if isinstance(value, TestConsole.all_classes[i]):
                        count_expected += 1
                self.assertEqual(int(count), count_expected)
