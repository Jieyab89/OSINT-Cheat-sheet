# Tutorial and about darkweb intel 

You can visit my Gitbook 

https://jieyab89-osint.gitbook.io/jieyab89-osint-cheat-sheet-wiki-tips/osint-tool-resouces-usage/all-about-darkweb-tips-darkweb-osint-assessments 

# Upgrade libary in pip 

Knowing security issue report by Dependabot

> lxml: Default configuration of iterparse() and ETCompatXMLParser() allows XXE to local files 
>
> Link: https://bugs.launchpad.net/lxml/+bug/2146291

> Requests has Insecure Temp File Reuse in its extract_zipped_paths() utility function
>
> Remarks Upgrade to at least Requests 2.33.0, where the library now extracts files to a non-deterministic location
> 
> If developers are unable to upgrade, they can set TMPDIR in their environment to a directory with restricted write access

Upgrade libary with pip

```
pip install -r requirements.txt --upgrade
```