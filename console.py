#!/usr/bin/python3
'''
program that contains the entry
point of the command interpreter
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    entry point of the command
    interpreter
    '''
    prompt = "(hbnb) "

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

    def do_EOF(self, arg):
        '''
        exits the program
        '''
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
