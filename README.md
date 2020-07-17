## Github Help Wanted

A program for fetching Github issues with the 'help-wanted' tag

## Installation
```
pip install github-help-wanted
```

## Usage
```
gh [-h] [-gf] [-s [SORT]] [-l [LANGUAGE]] [-d] [query]
```

### Search issues with the 'good-first' tag
```
gh repo -gf
```
### Search by programming language
```
gh -l piglatin
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
```
$ gh nice -gf -l python
rootzoll/raspiblitz
https://github.com/rootzoll/raspiblitz
[solved] unable to recover backup due to character limitations
https://github.com/rootzoll/raspiblitz/issues/783
I was unable to restore an old wallet and `channels.backup` due to the restricted character set for `Password D`  – which was introduced after i created the wallet – via the interface.
My wallet recovery was in the end successful after bypassing the check and setting `passwordD` directly to the correct value in https://github.com/rootzoll/raspiblitz/blob/5a501e65211c4d62286c551a87742fd304cbc1b7/home.admin/70initLND.sh#L345

So if someone stumbles over the same issue, this might be a solution – otherwise it might be an idea to allow all characters for restoring purposes.

Thanks for the great work!!!



mjec/rc-niceties
https://github.com/mjec/rc-niceties
Put warning up until niceties is fixed
https://github.com/mjec/rc-niceties/issues/21
Until the issues that are preventing staff from using niceties.recurse.com are resolved, it would be useful to have a disclaimer on the site warning users to only submit niceties via the most recent Google form.

Suggested by @rhonorv on [RC Zulip :lock:](https://recurse.zulipchat.com/#narrow/stream/19042-397-Bridge/topic/Niceties.3F.3F.3F/near/172773838).

```
## Limitations

Since it uses the Github Search API, it has a rate limitation on multipage searches, being limited to [60 searches per hour](https://developer.github.com/v3/#rate-limiting)

On the more ambiguous terms of search, for example, searching all the Python issues without a query, the program crashes with an exception, blowing the limitation, since PyGithub searches everytime there's a page on the search results

## TODO

- Limit results for the search API
- Implement a Auth option for queries
- Make a better usage guide
