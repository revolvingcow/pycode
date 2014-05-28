import os
import subprocess
from utilities import isGit, isMercurial, isBazaar

def clone(arguments):
    '''
    Clone a repository.
    '''

    commandSets = [
        ["git", "clone"],
        ["hg", "clone"],
        ["bzr", "branch"]
        ]

    for commandSet in commandSets:
        command = commandSet
        command.extend(arguments)
        out, err = executeCommandWithResponse(command)

        if err:
            print("{0}: repository not found".format(command[0]))
        else:
            print("{0}: repository cloned!".format(command[0]))
            break

def executeCommand(command):
    '''
    Execute the given command.
    '''

    subprocess.call(command, stderr=subprocess.STDOUT)

def executeCommandWithResponse(command):
    '''
    Execute the given command and return the output and errors.
    '''

    proc = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return proc.communicate()
