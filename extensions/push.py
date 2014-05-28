from utilities import execute, isGit, isMercurial, isBazaar

def push(arguments):
    '''
    Push commits to target.
    '''
    
    if isGit():
        command = ["git", "push"]
        command.extend(arguments)
        execute(command)

    if isMercurial():
        command = ["hg", "push"]
        command.extend(arguments)
        execute(command)

    if isBazaar():
        command = ["bzr", "push"]
        command.extend(arguments)
        execute(command)
