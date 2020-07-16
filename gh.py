#!/usr/bin/python
from github import Github
import argparse, sys
gh = Github()
gf = False


def main():
    parse = argparse.ArgumentParser(description="Search issues within repos on Github")
    parse.add_argument(action='store', dest='query', nargs='?', const=1, default='')
    parse.add_argument("-gf", help="Search good-first-issue", action="store_const",
                       const='good-first-issues:>1 ', default='')
    parse.add_argument("-s", help="Sort [forks, stars]", action="store",
                       dest='sort', nargs='?', const=1, default='updated')
    parse.add_argument("-l", help="Search by programming language", action="store",
                       dest='language', nargs='?', const=1, default='')
    parse.add_argument("-d", help="Order by descendant", action="store_const",
                       const='desc', default='asc')

    return parse


def search(args):
    arg = args.parse_args()
    language = ''
    if arg.language:
        language = ' language:' + arg.language
    if arg.gf:
        global gf
        gf = True
    query = arg.gf + arg.query + language
    if not query:
        args.print_help(sys.stderr)
        exit()
    return gh.search_repositories(query='help-wanted-issues:>1 ' + query, sort=arg.sort, order=arg.d)


def get_issue(repolist):
    for repo in repolist:
        good = ''
        if gf:
            good = 'label:"good first issue"'
        query = 'repo:' + repo.full_name + ' is:open label:"help wanted" ' + good
        issue_list = gh.search_issues(query=query)
    return issue_list


issues = get_issue(search(main()))
for issue in issues:
    print(issue.repository.full_name)
    print(issue.repository.html_url)
    print(issue.title)
    print(issue.html_url)
    print(issue.body)
    print('\n')