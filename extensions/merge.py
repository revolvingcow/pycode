import subprocess
from utilities import isGit, isMercurial, isBazaar

def merge(arguments):
    '''
    Merge incoming changes with the current branch.
    '''
    
    if isGit():
        command = ["git", "merge"]
        command.extend(arguments)
        executeCommand(command)

    if isMercurial():
        command = ["hg", "merge"]
        command.extend(arguments)
        executeCommand(command)

    if isBazaar():
        command = ["bzr", "merge"]
        command.extend(arguments)
        executeCommand(command)

def executeCommand(command):
    '''
    Execute the given command.
    '''

    subprocess.call(command)
