#!/usr/bin/python3
"""
HBNBCommand class
"""
import cmd
import json
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    command interpreter for HBNB
    """

    prompt = '(hbnb) '
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """
        quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        exit the program at EOF
        """
        print("")
        return True

    def emptyline(self):
        """do nothing on empty line"""
        pass

    def do_create(self, arg):
        """create a new instance, save it, and print the id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        instance = HBNBCommand.class_dict[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """print the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in FileStorage._FileStorage__objects:
            print("** no instance found **")
            return
        print(FileStorage._FileStorage__objects[key])

    def do_destroy(self, arg):
        """delete an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in FileStorage._FileStorage__objects:
            print("** no instance found **")
            return
        del FileStorage._FileStorage__objects[key]
        FileStorage().save()

    def do_all(self, arg):
        """print all string representation of all instances"""
        args = shlex.split(arg)
        if not args:
            inst = FileStorage._FileStorage__objects.values()
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
                return
            inst = [v for k, v in FileStorage._FileStorage__objects.items()
                    if k.split(".")[0] == class_name]
        print([str(obj) for obj in inst])

    def do_update(self, arg):
        """update an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in FileStorage._FileStorage__objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]
        instance = FileStorage._FileStorage__objects[key]
        setattr(instance, attribute_name, value)
        instance.save()

    def default(self, arg):
        """Call on an input line when the command prefix is not recognized"""
        print("*** Unknown syntax: {}".format(arg))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
