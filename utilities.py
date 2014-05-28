import os
import subprocess

def isGit():
    '''
    Determine if the current directory is part of a Git repository.
    '''

    return executeCheckingForErrors(["git", "branch"])

def isMercurial():
    '''
    Determine if the current directory is part of a Mercurial repository.
    '''

    return executeCheckingForErrors(["hg", "branch"])

def isBazaar():
    '''
    Determine if the current directory is part of the Bazaar repository.
    '''

    return executeCheckingForErrors(["bzr", "root"])

def execute(command):
    '''
    Execute the given command.
    '''

    subprocess.call(command, stderr=subprocess.STDOUT)

def executeCheckingForErrors(command):
    '''
    Execute the given command and return whether any errors were found.
    '''

    return subprocess.call(command, stderr=subprocess.STDOUT, stdout=open(os.devnull, 'w')) == 0

def executeAndReturnResponse(command):
    '''
    Execute the given command and return the output and errors.
    '''

    proc = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return proc.communicate()
