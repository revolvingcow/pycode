from utilities import execute, isGit, isMercurial, isBazaar

def mv(arguments):
    '''
    Move file(s)
    '''
    
    if isGit():
        command = ["git", "mv"]
        command.extend(arguments)
        execute(command)

    if isMercurial():
        command = ["hg", "mv"]
        command.extend(arguments)
        execute(command)

    if isBazaar():
        command = ["bzr", "mv"]
        command.extend(arguments)
        execute(command)
