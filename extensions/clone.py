from utilities import executeAndReturnResponse

def clone(arguments):
    '''
    Clone a repository.
    '''

    commandSets = [
        ["git", "clone"],
        ["hg", "clone"],
        ["bzr", "branch"]
        ]

    for commandSet in commandSets:
        command = commandSet
        command.extend(arguments)
        out, err = executeAndReturnResponse(command)

        if err:
            print("{0}: repository not found".format(command[0]))
        else:
            print("{0}: repository cloned!".format(command[0]))
            break
