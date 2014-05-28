import subprocess
from utilities import isGit, isMercurial, isBazaar

def init(arguments):
    '''
    Initializes (or re-initializes) a repository.
    '''
    
    if "git" in arguments or isGit():
        executeCommand(["git", "init"])

    if "hg" in arguments or isMercurial():
        executeCommand(["hg", "init"])

    if "bzr" in arguments or isBazaar():
        executeCommand(["bzr", "init"])

def executeCommand(command):
    '''
    Execute the given command.
    '''

    subprocess.call(command)
