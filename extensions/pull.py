from utilities import execute, isGit, isMercurial, isBazaar

def pull(arguments):
    '''
    Pull the latest changes.
    '''
    
    if isGit():
        command = ["git", "fetch"]
        command.extend(arguments)
        execute(command)

    if isMercurial():
        command = ["hg", "pull"]
        command.extend(arguments)
        execute(command)

    if isBazaar():
        command = ["bzr", "pull"]
        command.extend(arguments)
        execute(command)
