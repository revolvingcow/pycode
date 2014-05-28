from utilities import execute, isGit, isMercurial, isBazaar

def rm(arguments):
    '''
    Remove file(s) from the pending changes.
    '''
    
    if isGit():
        command = ["git", "rm"]
        command.extend(arguments)
        execute(command)

    if isMercurial():
        command = ["hg", "rm"]
        command.extend(arguments)
        execute(command)

    if isBazaar():
        command = ["bzr", "rm"]
        command.extend(arguments)
        execute(command)
