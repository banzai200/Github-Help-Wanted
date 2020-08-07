#!/usr/bin/python
import argparse
import re
import sys
from github import Github

gf = False
gh = Github()

def exe():
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
    parse.add_argument("--login", help="Search using login and password",
                       action="store", dest='login', nargs='+')
    parse.add_argument("--token", help="Search using token",
                       action="store", dest='token')
    parse.add_argument("-c", "--count", help="Limit number of repositories",
                       action="store", dest="number", type=int, default=60)

    return parse


def search(args):
    arg = args.parse_args()
    pages = (arg.number / 30) + (arg.number % 30 > 0)
    language = ''
    pagenum = 1
    repos = []
    global gh
    if arg.login:
        gh = Github(arg.login[0], arg.login[1])
    elif arg.token:
        gh = Github(arg.token)
    if arg.language:
        language = ' language:' + arg.language
    if arg.gf:
        global gf
        gf = True
    query = arg.gf + arg.query + language
    if not query:
        args.print_help(sys.stderr)
        exit()
    while pagenum <= int(pages):
        for repo in gh.search_repositories(query='help-wanted-issues:>1 ' + query, sort=arg.sort, order=arg.d).get_page(pagenum):
            repos.append(repo)
        pagenum = pagenum + 1
    print(repos[:arg.number])
    return repos[:arg.number]


def get_issue(repolist):
    good = ''
    repoq = []
    if gf:
        good = 'label:"good first issue"'
    for repo in repolist:
        repoq.append('repo:' + repo.full_name)
    repoq = re.sub(r'\[|\]|,|\'', '', str(repoq))
    query = repoq + ' is:open label:"help wanted" ' + good
    issue_list = gh.search_issues(query=query)
    return issue_list


def main():
    args = exe()
    issues = get_issue(search(args))
    for issue in issues:
        print(issue.repository.full_name)
        print(issue.repository.html_url)
        print(issue.title)
        print(issue.html_url)
        print(issue.body)
        print('\n')

main()
