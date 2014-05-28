import subprocess
from utilities import isGit, isMercurial, isBazaar

def push(arguments):
    '''
    Push commits to target.
    '''
    
    if isGit():
        command = ["git", "push"]
        command.extend(arguments)
        executeCommand(command)

    if isMercurial():
        command = ["hg", "push"]
        command.extend(arguments)
        executeCommand(command)

    if isBazaar():
        command = ["bzr", "push"]
        command.extend(arguments)
        executeCommand(command)

def executeCommand(command):
    '''
    Execute the given command.
    '''

    subprocess.call(command)
