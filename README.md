# popcorn
A polyrepo for a few in-house developed utilities and tools.

## Included tools

### Soda Opener

Soda Opener is a tiny PowerShell script which reads a text file for a list of URLs and opens them all in separate Google Chrome tabs. The following kinds of URLs are supported:

- apex domains (eg. shunyaek.se, google.com)
- www subdomain (eg. www.yahoo.com)
- full domains (eg. https://news.ycombinator.com)

Use `soda.txt` to list out the URLs and then run `opener.ps1` using Microsoft PowerShell:

```
PS C:\soda-opener> .\opener.ps1
```

**NOTE**: You should have Google Chrome installed on your computer for this to work!

**Coming soon**:

- Support for different browsers.
- A GUI for the same.
