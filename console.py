#!/usr/bin/python3
'''
program that contains the entry
point of the command interpreter
'''
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models import storage


class HBNBCommand(cmd.Cmd):
    '''
    entry point of the command
    interpreter
    '''
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State",
                     "Place", "Amenity", "Review", "City"]

    def emptyline(self):
        '''
        shouldn’t execute anything
        '''
        pass

    def do_quit(self, arg):
        '''
        Quits the program
        '''
        return True

    def help_quit(self, arg=None):
        '''
        provides the help instructions for the
        quit command
        '''
        print("Quit command to exit the program")

    def do_EOF(self, line):
        '''
        exits the program
        '''
        return True

    def do_create(self, arg):
        '''
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        '''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        '''
        Prints the string representation of an
        instance based on the class name and id
        '''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        '''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        '''
        Prints all string representation of all
        instances based or not on the class name.
        '''
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class
        usage: <class name>.count()
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if arg:
            cls_nm = commands[0]

        count = 0

        if commands:
            if cls_nm in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == cls_nm:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        '''
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        '''
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)

                obj.save()

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid
        """
        arg_list = arg.split('.')

        cls_nm = arg_list[0]  # incoming class name

        command = arg_list[1].split('(')

        cmd_met = command[0]  # incoming command method

        e_arg = command[1].split(')')[0]  # extra arguments

        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmd_met in method_dict.keys():
            if cmd_met != "update":
                return method_dict[cmd_met]("{} {}".format(cls_nm, e_arg))
            else:
                if not cls_nm:
                    print("** class name missing **")
                    return
                try:
                    obj_id, arg_dict = split_curly_braces(e_arg)
                except Exception:
                    pass
                try:
                    call = method_dict[cmd_met]
                    return call("{} {} {}".format(cls_nm, obj_id, arg_dict))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
