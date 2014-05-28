import subprocess
from utilities import isGit, isMercurial, isBazaar

def pull(arguments):
    '''
    Pull the latest changes.
    '''
    
    if isGit():
        command = ["git", "fetch"]
        command.extend(arguments)
        executeCommand(command)

    if isMercurial():
        command = ["hg", "pull"]
        command.extend(arguments)
        executeCommand(command)

    if isBazaar():
        command = ["bzr", "pull"]
        command.extend(arguments)
        executeCommand(command)

def executeCommand(command):
    '''
    Execute the given command.
    '''

    subprocess.call(command)
