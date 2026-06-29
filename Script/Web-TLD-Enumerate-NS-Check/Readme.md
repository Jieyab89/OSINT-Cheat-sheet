# Tutorial 

## Tips 

Tips surface web tld domain enumeration:

First. If you have tried dorking but cannot find the target on the web, try a brute-force approach—similar to an email permutator, but applied to domain TLDs. What can you do? You can use the script below to parse domain extensions and perform a brute-force search. If that fails, try combining it with other search parameters—such as country of origin, language, username, or other indicators that could serve as clues—and then attempt to brute-force the extensions again, testing them either as double or single domain extension. It is possible that the site is not indexed and the developer has implemented strict controls for indexing bots, making it difficult to find. Try using a brute-force approach and adjust your search parameters or context

A second method is to perform a reverse IP lookup, provided you have identified the domains or IP addresses you wish to investigate. Check to see if there are any similarities to your target; if you are looking for new leads, try performing a reverse IP lookup

Third. After identifying a domain or IP address, try enumerating it using data aggregators like Censys, Shodan, or VirusTotal. Check the asset information and WHOIS history; you might uncover new information

Fourth, do not forget to check web archiving platforms—such as the Wayback Machine, Archive.today, or other services that store snapshots of web pages and URLs. This allows you to search for additional information in case anything was missed

## Reccon tld common domain 

```
python reccon-domain-tld.py --name <targetname> 
```

## Reccon tld domain brute 

```
python reccon-domain-tld.py --name pornhub --brute --brute-max-len 3
```

# Results 

## Common tld domain 

<img width="2559" height="1275" alt="image" src="https://github.com/user-attachments/assets/f48f1f4d-0356-4a8f-a693-421859174feb" />

## Brute tld domain

<img width="2559" height="1288" alt="image" src="https://github.com/user-attachments/assets/3e1632a0-3e90-4bb1-bbf0-2fc96cfda9d5" />

# Run local web server 

```
python -m http.server 8080
```

## Results viewer 

<img width="2559" height="1333" alt="image" src="https://github.com/user-attachments/assets/3a57d2d8-eb75-4082-8f41-2229f4cb62bf" />
