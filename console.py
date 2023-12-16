#!/usr/bin/python3
"""
This script defines a command-line interpreter using the `cmd` module.
The interpreter allows users to interact with it through a command prompt
and execute specific commands.
"""
import cmd
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    is a command-line interpreter class that inherits from `cmd.Cmd`.
    It provides a prompt and specific commands for user interaction.
    """
    prompt = '(hbnb)'
    valid_classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
        ]

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        print("")
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Called when the user inserts an empty line.
        It does nothing in this case.
        """
        pass

    def do_create(self, line):
        """
        Create a new instance of a specified class
        """
        if not line:
            print("** class name missing **")
        elif line not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Print the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            instances = []
            for obj_key, obj in models.storage.all().items():
                if obj.__class__.__name__ == args[0]:
                    instances.append(str(obj))
            if not instances:
                print("** instance id missing **")
            else:
                print(instances)
        else:
            insts_key = f'{args[0]}.{args[1]}'
            obj_dict = models.storage.all()

            if insts_key not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[insts_key])

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            insts_key = f'{args[0]}.{args[1]}'
            obj_dict = models.storage.all()

            if insts_key not in obj_dict.keys():
                print("** no instance found **")
            else:
                del obj_dict[insts_key]
                models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based on the class name
        """
        args = line.split()
        if len(args) > 0 and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            instances = []
            obj_dict = models.storage.all()
            for obj in obj_dict.values():
                if len(args) == 0 or obj.__class__.__name__ == args[0]:
                    instances.append(str(obj))
            print(instances)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by
        adding or updating an attribute
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            insts_key = f'{args[0]}.{args[1]}'
            obj_dict = models.storage.all()

            if insts_key not in obj_dict:
                print("** no instance found **")
            else:
                instance = obj_dict[insts_key]
                attr_name = args[2]
                attr_val = args[3].strip('"')

                if (attr_name == "id" or
                        attr_name == "created_at" or
                        attr_name == "updated_at"):
                    print("** cannot update '{}' attr **".format(attr_name))
                else:
                    setattr(instance, attr_name, attr_val)
                    instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
