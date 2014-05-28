#!/usr/bin/env python

import os
import subprocess
import argparse
import importlib

from utilities import isGit, isMercurial, isBazaar

class CodeRepository:
    def __init__(self):
        '''
        Initialize the code repository class.
        '''

        self.currentDirectory = os.getcwd()
        self.executingDirectory = os.path.dirname(os.path.realpath(__file__))
        self.extensionDirectory = os.path.join(self.executingDirectory, "extensions")

    def run(self, args):
        '''
        Run the given command and arguments against the current working directory.
        '''
        
        executed = self.executeExtension(args[0], args[1:])

        # If no extension was found then we execute the command as if
        # it was naturally called.
        if not executed:
            commandWithArgs = args[:]
            commandWithArgs.insert(0, "vcs")

            if isGit():
                commandWithArgs[0] = "git"
                subprocess.call(commandWithArgs)
                executed = True
            
            if isMercurial():
                commandWithArgs[0] = "hg"
                subprocess.call(commandWithArgs)
                executed = True

            if isBazaar():
                commandWithArgs[0] = "bzr"
                subprocess.call(commandWithArgs)
                executed = True

        if not executed:
            print("No repository found")
            exit(3)

    def executeExtension(self, extension, arguments):
        '''
        Find the named extension and attempt to execute it with the given arguments.
        '''
        
        extensionPath = "extensions.{0}".format(extension)
        extensionExecuted = False
        
        try:
            module = importlib.import_module(extensionPath)
            method = getattr(module, extension)
            method(arguments)
            
            extensionExecuted = True
        except ImportError:
            pass
        finally:
            pass

        return extensionExecuted 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("commands", metavar="commands", nargs="+")
    args = parser.parse_args()

    repo = CodeRepository()
    repo.run(args.commands)
