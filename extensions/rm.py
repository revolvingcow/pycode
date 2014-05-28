import subprocess
from utilities import isGit, isMercurial, isBazaar

def rm(arguments):
    '''
    Remove file(s) from the pending changes.
    '''
    
    if isGit():
        command = ["git", "rm"]
        command.extend(arguments)
        executeCommand(command)

    if isMercurial():
        command = ["hg", "rm"]
        command.extend(arguments)
        executeCommand(command)

    if isBazaar():
        command = ["bzr", "rm"]
        command.extend(arguments)
        executeCommand(command)

def executeCommand(command):
    '''
    Execute the given command.
    '''

    subprocess.call(command)
