from utilities import execute, isGit, isMercurial, isBazaar

def merge(arguments):
    '''
    Merge incoming changes with the current branch.
    '''
    
    if isGit():
        command = ["git", "merge"]
        command.extend(arguments)
        execute(command)

    if isMercurial():
        command = ["hg", "merge"]
        command.extend(arguments)
        execute(command)

    if isBazaar():
        command = ["bzr", "merge"]
        command.extend(arguments)
        execute(command)
