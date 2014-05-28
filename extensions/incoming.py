import os
import subprocess
from utilities import isGit, isMercurial, isBazaar

def incoming(arguments):
    '''
    Shows incoming commits.
    '''
    
    if isGit():
        out, err = executeCommandWithResponse(["git", "remote"])
        if not err and out:
            executeCommandWithResponse(["git", "remote", "update", "-p"])
            executeCommand(["git", "log", "..@{u}"])

    if isMercurial():
        out, err = executeCommandWithResponse(["git", "paths"])
        if not err and out:
            executeCommand(["hg", "incoming"])

    if isBazaar():
        out, err = executeCommandWithResponse(["bzr", "missing"])
        if not err and out:
            executeCommand(["bzr", "missing"])

def executeCommand(command):
    '''
    Execute the given command.
    '''

    subprocess.call(command, stderr=subprocess.STDOUT)

def executeCommandWithResponse(command):
    '''
    Execute the given command and return the output and errors.
    '''

    proc = subprocess.Popen(command, stderr=open(os.devnull, 'w'), stdout=subprocess.PIPE)
    return proc.communicate()
