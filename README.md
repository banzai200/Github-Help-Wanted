## Github Help Wanted

A python command for fetching github issues with the 'help-wanted' tag

## Usage
```
gh.py [-h] [-gf] [-s [SORT]] [-l [LANGUAGE]] [-d] [query]
```

### Search issues with the 'good-first' tag
```
gh.py repo -gf
```
### Search by programming language
```
gh.py -l piglatin
```

Response will be printed to stdout on the following format:

```
Repository Full Name
Repository Url
Issue Title
Issue Url
Issue Body
```

## Example

## Limitations

Since it uses the Github Search API, it has a rate limitation on multipage searches, being limited to [60 searches per hour](https://developer.github.com/v3/#rate-limiting)

On the more ambiguous terms of search, for example, searching all the Python issues without a query, the program crashes with an exception, blowing the limitation, since PyGithub searches everytime there's a page on the search results

## TODO

- Package into a executable
- Limit results for the search API
- Implement a Auth option for queries
- Write an example
- Make a better usage guide
