import git
import sys, os
import getopt

try:
    repo = git.Repo(os.getcwd())
except git.errors.InvalidGitRepositoryError:
    print 'Error: Not a git repository'

def findChangedFiles(commit):
    '''
    Finds all of the affected files within a given commit
    '''
    return ['%s' % diff.a_path for diff in repo.commit(commit).diffs]

def getCommitMessage(commit):
    '''
    Finds the commit message for the specified commit
    '''
    try:
        commit = repo.commit(commit)

        return {'hash' : commit.id,
                'message' : commit.message}
    except git.errors.GitCommandError:
        print 'Error: Commit not found'
        return False

def getCommitsSinceTag(tag):
    '''
    Returns all commits since the given tag
    '''
    try:
        commitList = repo.commits_between(tag, 'HEAD')
        result = [commit.id for commit in commitList]
    except git.errors.GitCommandError:
        print 'Error: Commit not found'
        return False

    return result
    
def main():
    options, remainder = getopt.getopt(sys.argv[1:], 'c:', 'commit=');

    for opt, arg in options:
        if (opt in ('-c', '--commit')):
            commit = arg

    try:
    	print "\n".join(["%s" % x for x in findChangedFiles(commit)])
    except UnboundLocalError:
        print 'Usage: git_handler.py ([-c|--commit][-t|--tag]) <commit|tag>'
    except TypeError:
        print 'Commit not found'

if __name__ == '__main__':
    main()
