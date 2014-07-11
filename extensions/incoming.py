from utilities import execute, executeAndReturnResponse, isGit, isMercurial, isBazaar

def incoming(arguments):
    '''
    Shows incoming commits.
    '''
    
    if isGit():
        out, err = executeAndReturnResponse(["git", "remote"])
        if not err and out:
            executeAndReturnResponse(["git", "remote", "update", "-p"])
            execute(["git", "log", "..@{u}"])

    if isMercurial():
        out, err = executeAndReturnResponse(["hg", "paths"])
        if not err and out:
            execute(["hg", "incoming"])

    if isBazaar():
        out, err = executeAndReturnResponse(["bzr", "missing"])
        if not err and out:
            execute(["bzr", "missing"])
