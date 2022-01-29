#!/usr/bin/python3
"""
This is the "console" file.

The console file contains the entry point of the command interpreter.
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines a class HBNBCommand.

    Attributes:
        prompt (str): prompt to display to the user
        all_classes (dict): list of all classes
    """
    prompt = "(hbnb) "
    all_classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    all_commands = ['create', 'show', 'destroy', 'all', 'update', 'count']

    error_occured = False

    def emptyline(self):
        """Do nothing if no command is entered."""
        pass

    def precmd(self, line):
        """Manipulate the user input before getting processed."""
        if '{' in line and '}' in line:
            args = re.findall(r"([^(,):{}]+)", line)
            args = [x.strip() for x in args]
            args[:] = [x for x in args if x]
            class_name = args[0].split('.')[0]
            cmd_name = args[0].split('.')[1]
            id_val = args[1].strip("'")
            del args[0]
            del args[0]
            print(args)
            j = 0
            for i in range(len(args) // 2):
                loop_line = ""
                key = args[j].strip("'")
                value = args[j + 1].strip("'")
                loop_line = cmd_name + " " + class_name + " "\
                                     + id_val.strip('"') + " "\
                                     + key.strip('"') + " "\
                                     + value
                j += 2
                cmd.Cmd.onecmd(self, loop_line)
                if HBNBCommand.error_occured:
                    break
            line = ""

        elif '.' in line and '(' in line and ')' in line:
            args = re.findall(r"([^(,):{}]+)", line)
            args = [x.strip() for x in args]
            args[:] = [x for x in args if x]
            class_name = args[0].split('.')[0]
            cmd_name = args[0].split('.')[1]
            if cmd_name not in HBNBCommand.all_commands:
                line = cmd_name
            elif len(args) > 1:
                id_val = args[1].strip('"')
                del args[0]
                del args[0]
                line = cmd_name + " " + class_name + " " + id_val
                for i in args:
                    line = line + " " + i
            else:
                line = cmd_name + " " + class_name
        return line

    def do_quit(self, arg):
        """Quits the command interpreter."""
        exit()

    def do_EOF(self, arg):
        """Quits the command interpreter."""
        print()
        exit()

    def do_create(self, arg):
        """Creates an instance from a class."""
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        else:
            if args[0] in HBNBCommand.all_classes.keys():
                obj = HBNBCommand.all_classes[args[0]]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows the string representation of the object."""
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key_obj = args[0] + "." + args[1]
            try:
                print(storage._FileStorage__objects[key_obj])
            except KeyError:
                print('** no instance found **')

    def do_destroy(self, arg):
        """Destroys the object passed."""
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key_obj = args[0] + "." + args[1]
            try:
                del storage._FileStorage__objects[key_obj]
                storage.save()
            except KeyError:
                print('** no instance found **')

    def do_all(self, arg):
        """Displays list of all objects in the application."""
        args = arg.split()
        if len(args) < 1:
            lst_all = []
            for key in storage._FileStorage__objects.keys():
                lst_all.append(str(storage._FileStorage__objects[key]))
            print(lst_all)
        else:
            if args[0] not in HBNBCommand.all_classes.keys():
                print("** class doesn't exist **")
            else:
                lst_all = []
                for key in storage._FileStorage__objects.keys():
                    if key.split('.')[0] == args[0]:
                        lst_all.append(str(storage._FileStorage__objects[key]))
                print(lst_all)

    def do_update(self, arg):
        """Updates an object with the values passed from the command line."""
        HBNBCommand.error_occured = False
        args = re.findall(r'[^\"\s]\S*|\".+?\"', arg)
        if len(args) < 1:
            print('** class name missing **')
            HBNBCommand.error_occured = True
        elif args[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            HBNBCommand.error_occured = True
        elif len(args) < 2:
            print('** instance id missing **')
            HBNBCommand.error_occured = True
        elif (args[0] + "." + args[1]) not in\
                storage._FileStorage__objects.keys():
            print('** no instance found **')
            HBNBCommand.error_occured = True
        elif len(args) < 3:
            print('** attribute name missing **')
            HBNBCommand.error_occured = True
        elif len(args) < 4:
            print('** value missing **')
            HBNBCommand.error_occured = True
        else:
            key_obj = args[0] + "." + args[1]
            selected_obj = storage._FileStorage__objects[key_obj]
            selected_obj_dict = selected_obj.to_dict()
            if '"' not in args[3] and "'" not in args[3]:
                if args[3].isdigit():
                    value = int(args[3])
                else:
                    value = float(args[3])
            else:
                value = args[3].strip('"')
            selected_obj_dict.update({args[2].strip('"'): value})
            updated_obj = HBNBCommand.all_classes[args[0]](**selected_obj_dict)
            storage._FileStorage__objects.update({key_obj: updated_obj})
            updated_obj.save()

    def do_count(self, arg):
        """Counts the number of instances of a class."""
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        else:
            if args[0] in HBNBCommand.all_classes.keys():
                count = 0
                for obj in storage._FileStorage__objects.values():
                    if isinstance(obj, HBNBCommand.all_classes[args[0]]):
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")

    def help_quit(self):
        """Displays the function of the quit command."""
        print('Quit command to exit the program')

    def help_EOF(self):
        """Displays the function of EOF."""
        print('Exits the program')

    def help_create(self):
        """Displays the function of the create command."""
        print('Creates a new instance of a class, saves it to file and prints\
 the id')

    def help_show(self):
        """Displays the function of the show command."""
        print('Prints the string representation of an instance based on the\
 class name and id')

    def help_destroy(self):
        """Displays the function of the destroy command."""
        print('Deletes an instance based on the class name and id and save the\
 change into the JSON file')

    def help_all(self):
        """Displays the function of the all command."""
        print('Prints all string representation of all instances based or\
 not on the class name.')

    def help_update(self):
        """Displays the function of the update command."""
        print('Updates an instance based on the class name and id by adding or\
 updating attribute and save the change into the JSON file')

    def help_count(self):
        """Displays the function of the count command."""
        print('Counts the number of instances of a certain class')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
