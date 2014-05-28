import os
import subprocess

def isGit():
    '''
    Determine if the current directory is part of a Git repository.
    '''

    return testRepository(["git", "branch"])

def isMercurial():
    '''
    Determine if the current directory is part of a Mercurial repository.
    '''

    return testRepository(["hg", "branch"])

def isBazaar():
    '''
    Determine if the current directory is part of the Bazaar repository.
    '''

    return testRepository(["bzr", "root"])

def testRepository(command):
    return subprocess.call(command, stderr=subprocess.STDOUT, stdout=open(os.devnull, 'w')) == 0
