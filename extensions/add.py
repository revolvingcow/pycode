from utilities import execute, isGit, isMercurial, isBazaar

def add(arguments):
    '''
    Add file(s) to the pending changes.
    '''
    
    if isGit():
        # If no additional arguments were passed assume
        # we want to add all pending changes.
        if len(arguments) == 0:
            arguments.append(".")

        command = ["git", "add"]
        command.extend(arguments)
        execute(command)

    if isMercurial():
        command = ["hg", "add"]
        command.extend(arguments)
        execute(command)

    if isBazaar():
        command = ["bzr", "add"]
        command.extend(arguments)
        execute(command)
