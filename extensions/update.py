from utilities import execute, isGit, isMercurial, isBazaar

def pull(arguments):
    '''
    Pull the latest changes.
    '''
    
    if isGit():
        command = ["git", "pull"]
        command.extend(arguments)
        execute(command)

    if isMercurial():
        command = ["hg", "pull", "-u"]
        command.extend(arguments)
        execute(command)

    if isBazaar():
        command = ["bzr", "update"]
        command.extend(arguments)
        execute(command)
