import subprocess
from utilities import isGit, isMercurial, isBazaar

def mv(arguments):
    '''
    Move file(s)
    '''
    
    if isGit():
        command = ["git", "mv"]
        command.extend(arguments)
        executeCommand(command)

    if isMercurial():
        command = ["hg", "mv"]
        command.extend(arguments)
        executeCommand(command)

    if isBazaar():
        command = ["bzr", "mv"]
        command.extend(arguments)
        executeCommand(command)

def executeCommand(command):
    '''
    Execute the given command.
    '''

    subprocess.call(command)
