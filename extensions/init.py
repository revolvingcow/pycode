from utilities import execute, isGit, isMercurial, isBazaar

def init(arguments):
    '''
    Initializes (or re-initializes) a repository.
    '''
    
    if "git" in arguments or isGit():
        execute(["git", "init"])

    if "hg" in arguments or isMercurial():
        execute(["hg", "init"])

    if "bzr" in arguments or isBazaar():
        execute(["bzr", "init"])
