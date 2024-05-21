# OSINT CHEAT SHEET - List OSINT Tools

[![Github Badge](https://img.shields.io/badge/-Jieyab89-black?style=flat&logo=github&logoColor=white&link=https://github.com/Jieyab89/)](https://github.com/Jieyab89)

Contains a list of OSINT tools, OSINT tips, datasets, Maltego transform and others. There are free and paid tools you can use and owner is not responsible, only for knowledge or educational purposes. Sorry if some of the resources have closed the service or error owner doesn't always check what's going on with the resources here, thank you

# Tips and trick safe guide using resources 

- Use virtual machine, fake host or docker image 
- Use private network e.g vpn, tor, p2p 
- Use second account (not you real account)
- Read ToS the resouces 
- Enable your firewall and IDS 
- Dont upload your private files make sure you have clean personal file in folder

# Linux Distribution for OSINT 

You can build it with VM or Live USB make sure you have sandbox machine 

- [tlosint-live](https://github.com/tracelabs/tlosint-live)
- [tails](https://tails.net/)
- [qubes](https://www.qubes-os.org/doc/)
- [parrot sec](https://www.parrotsec.org/)
- [csi linux](https://csilinux.com/csi-linux-downloads/)

# EXIF TOOL COMMAND

## Exif tag name and data type

> Artist                                        string
>
> Author                                        string
>
> Caption                                       string
>
> Categories                                    string
>
> Collections                                   string
>
> DateTime                                      date
>
> DPP                                           lang-alt
>
> EditStatus                                    string
>
> FixtureIdentifier                             string
>
> Keywords                                      string
>
> Notes                                         string
>
> ObjectCycle                                   string
>
> OriginatingProgram                            string
>
> Rating                                        real
>
> Rawrppused                                    boolean
>
> ReleaseDate                                   string
>
> ReleaseTime                                   string
>
> RPP                                           lang-alt
>
> Snapshots                                     string
>
> Tagged                                        boolean

More : man exiftool (Run on your terminal)

Site :

- [Exiftool](https://exiftool.org/)
- [List tagname](https://exiftool.org/TagNames/)
- [List tagnme 2](https://metacpan.org/dist/Image-ExifTool/view/lib/Image/ExifTool/TagNames.pod)
- [List tagname 3](https://manpages.org/imageexiftooltagnames/3)

## Write metadata

- exiftool -tagname="string" file
>
>example : exiftool -Author="Bayu" test.txt
>

you can add multiple tag and multiple file

## Delete metadata

- exiftool -tagname="" file
>
>example : exiftool -Author="" test.txt
>

## Delete mass metadata

- exiftool -all="" file
>
>example : exiftool -all="" file
>

#Usage : man exiftool or read documentation exiftool.org

> Not there are tag no writetable, make sure tagname can write
>

Automated tool by David Bombal

- [Exif python script remover](https://github.com/davidbombal/red-python-scripts/blob/main/remove_exif.py)

## !Note

> Use fresh file, if your file has been compressed or edit metadata you got a default metadata
> You can use xmp format for edit, write and delete metadata
> Check the documentation


# SOCMINT  

- [Instagram](https://github.com/Datalux/Osintgram)
Be carefull using this tool
- [Tinfoleak](https://github.com/vaguileradiaz/tinfoleak)
- [SOCMINT tool](https://osint.support/chrome-extensions/2019/09/29/osint-socmint-tooling.html)
- [Graph Search](http://socmint.tools/graph.htm)
- [Alfred](https://github.com/Alfredredbird/alfred)
- [Blackbird](https://github.com/p1ngul1n0/blackbird)

# Collection Dataset

- [Kaggle](https://www.kaggle.com/)
- [RAPID API Collection](https://rapidapi.com/hub)
- [Exploit Database](https://www.exploit-db.com/google-hacking-database)
- [AWS open data](https://registry.opendata.aws/)
- [Open Network](http://www.opendatanetwork.com/)
- [WHO Data](https://www.who.int/data/gho/)
- [Gpt OSINT](https://github.com/gigz/gpt-osint)
- [Humdata](https://data.humdata.org/dataset)
- [datasetsearch](https://datasetsearch.research.google.com/)
- [OSINT Collection](https://start.me/p/DPYPMz/the-ultimate-osint-collection)
- [Academic Torrent](https://academictorrents.com/)
- [Torrent API](https://github.com/Ryuk-me/Torrent-Api-py) 
- [API OSINT TORRENT](https://rapidapi.com/theoneappkh/api/torrent-search/) 
- [Microsoft Building Fingerprints](https://github.com/microsoft/GlobalMLBuildingFootprints)
- [MAXAR Satellite imagery](https://www.maxar.com/open-data)
- [Satellite Collection](https://www.nesdis.noaa.gov/real-time-imagery/imagery-collections)
- [Open measure](https://public.openmeasures.io/)
- [Fiugis](https://fiugis.maps.arcgis.com/home/search.html?restrict=false&sortField=relevance&sortOrder=desc&categories=%2FCategories%2FLocation#content)
- [Earth ESA](https://earth.esa.int/eogateway)
- [Google Public Data](https://www.google.com/publicdata/directory)
- [paperswithcode](https://paperswithcode.com/)
- [ID BPS](https://www.bps.go.id/id)
- [ID data Kementrian & Lembaha Dataset](https://data.go.id/home)
- [ShadowDragon](https://shadowdragon.io/)

# Forums & Sites

- [Bellingcat Discord](https://discord.com/invite/nTaNPmz)
- [Independent OSINT](https://discord.com/invite/2DGJ2EC)
- [OSINT.Team](https://osint.team)
- [Seccodeid Forum](https://forum.seccodeid.com/category/osint)
- [Reddit OSINT](https://www.reddit.com/r/OSINT)
- [TraceLabs Discord](https://discord.com/invite/Rn8z2QNAD9)
- [IntelTechniques](https://inteltechniques.com/)
- [Google Group](https://groups.google.com/?pli=1)
- [4Chan](https://4chansearch.com/)
- [boardreader](https://boardreader.com/)
- [maltego](https://www.maltego.com/categories/osint/)
- [offensiveosint](https://www.offensiveosint.io/)

# General Search

- [ASK](http://www.ask.com)
- [Baidu](http://www.baidu.com)
- [DuckDuckGo](https://duckduckgo.com)
- [Yandex](https://www.yandex.com)
- [Infospace](http://www.infospace.com)

# Meta Search

- [100SearchEngines](https://www.100searchengines.com)
- [Bing vs. Google](http://bvsg.org)
- [DADgogo](http://dadgogo.com)
- [Etools](http://www.etools.ch)
- [WebCrawler](http://www.webcrawler.com)

# Code Search

- [Chromium Code Search](https://source.chromium.org/chromium)
- [Android Code Search](https://cs.android.com)
- [Code Finder](http://codefinder.org)
- [CodeSeek](https://www.codeseek.co)
- [Debian Code Search](http://codesearch.debian.net)
- [Scala](https://www.programcreek.com/scala)
- [SearchCode](https://searchcode.com)
- [SourceCodeOnline](http://www.sourcecodeonline.com)
- [Woboq](https://code.woboq.org)
- [publicwww](https://publicwww.com/)
- [DevsecOps Secure Code](https://devsecopsguides.com/docs/rules)

# Competitive Programming

- [Hackerrank](https://www.hackerrank.com/)
- [Code chef](https://www.codechef.com/)
- [Code war](https://www.codewars.com/)

# File & FTP

- [Archie](http://archie.icm.edu.pl/archie_eng.html)
- [4shared](https://www.4shared.com)
- [FileSearching](http://www.filesearching.com)
- [File chef](https://www.filechef.com)
- [Global File Search](http://globalfilesearch.com)
- [Search Shared](https://www.searchshared.info)
- [MMNT](http://www.mmnt.ru)
- [Pdf analyzer](http://pdf-analyser.edpsciences.org/)
- [Tools pdf24](https://tools.pdf24.org/en/extract-images)

# Social Media Search and Monitoring

- [Awario](https://awario.com)
- [Brand24](https://brand24.com)
- [Samdesk](https://www.samdesk.io)
- [Maltego social links](https://www.maltego.com/transform-hub/social-links-ce/)
- [Maltego Social Links Pro](https://www.maltego.com/transform-hub/social-links-pro/)
- [Social Searcher](https://www.social-searcher.com/)
- [Social Analyzer](https://github.com/qeeqbox/social-analyzer)
- [SNSCRAPE - Scraper](https://github.com/JustAnotherArchivist/snscrape)
- [OSINT compass](https://osint-compass-portal.onrender.com/)
- [Phantom Buster](https://phantombuster.com/phantombuster)
- [Open measure](https://public.openmeasures.io/)
- [huntintel](https://www.huntintel.io/)
- [Sherlock Eye](https://sherlockeye.io/)
- [clauneck](https://github.com/serpapi/clauneck)
- [ShadowDragon](https://shadowdragon.io/)
- [sociallinks](https://sociallinks.io/)
- [Crimewall](https://sociallinks.io/products/sl-crimewall)

# Social Media Management and Content Discovery

- [Buffer](https://buffer.com)
- [Coosto](https://www.coosto.com)
- [Revive Social](https://revive.social)
- [Social Analyzer](https://github.com/qeeqbox/social-analyzer)
- [Gpt OSINT](https://github.com/gigz/gpt-osint)
- [SNSCRAPE - Scraper](https://github.com/JustAnotherArchivist/snscrape)
- [Phantom Buster](https://phantombuster.com/phantombuster)
- [huntintel](https://www.huntintel.io/)
- [Sherlock Eye](https://sherlockeye.io/)
- [clauneck](https://github.com/serpapi/clauneck)
- [ShadowDragon](https://shadowdragon.io/)
- [sociallinks](https://sociallinks.io/)
- [Crimewall](https://sociallinks.io/products/sl-crimewall)

# Web Intelligence

- [Better Whois](http://www.betterwhois.com)
- [whoishistory](https://osint.sh/whoishistory/)
- [DNS History](http://dnshistory.org)
- [DNS Spy](https://dnsspy.io)
- [DNS Checker](https://dnschecker.org)
- [HackerTarget](https://hackertarget.com/ip-tools)
- [RedHunt Labs Attack Surface Recon API](https://devportal.redhuntlabs.com/home)
- [Shodan](https://www.shodan.io)
- [Wappalyzer](https://www.wappalyzer.com/)
- [Sudomy](https://github.com/screetsec/Sudomy)
- [Testssl](https://testssl.sh/)
- [Nmap](https://nmap.org/)
- [builtwith](https://builtwith.com/)
- [VirusTotal](https://www.virustotal.com/gui/)
- [Nessus](https://www.tenable.com/products/nessus)
- [Nikto](https://cirt.net/Nikto2)
- [Webshag](https://github.com/wereallfeds/webshag)
- [wayback machine](https://archive.org/web/)
- [Whoxy](https://www.whoxy.com/)
- [Farsight DNSDB Transforms for Maltego](https://www.maltego.com/transform-hub/farsight-dnsdb/)
- [Web Screnshhot Maltego Transforms](https://github.com/TURROKS/Maltego_Web2Screenshot)
- [Nuclei](https://github.com/projectdiscovery/nuclei)
- [Netcraft](https://www.netcraft.com/tools/)
- [DNSX](https://github.com/projectdiscovery/dnsx)
- [cachedview](https://cachedview.com/)
- [Zoomeye](http://zoomeye.org/)
- [securitytrails](https://securitytrails.com/)
- [hakrawler](https://github.com/hakluke/hakrawler)
- [Dork Lab](https://github.com/rtwillett/DorkLab)
- [Websecreenshoot](https://github.com/maaaaz/webscreenshot)
- [Leakos](https://github.com/carlospolop/Leakos)
- [Pastos](https://github.com/carlospolop/Pastos)
- [SNYK](snyk.io)
- [Similar Sites](https://www.similarsites.com/)
- [Similar Web](https://www.similarweb.com/)
- [spyonweb](https://spyonweb.com/)
- [analyzeid](https://analyzeid.com/)
- [Zeus-Scanner](https://github.com/Ekultek/Zeus-Scanner)
- [CloudFail](https://github.com/m0rtem/CloudFail.git)
- [Real IP Discover](https://github.com/elefr3n/real_ip_discover.git)
- [Mend Io](https://www.mend.io/vulnerability-database)
- [whois request](whoisrequest.com)
- [completedns](completedns.com)
- [dnsdumper](dnsdumpster.com)
- [A href Backlink Checker](https://ahrefs.com/backlink-checker)
- [Neil Patel Backlink](https://neilpatel.com/backlinks/)
- [Semrush Backlink](https://www.semrush.com/analytics/backlinks/)
- [Small SEO Tool Backlink](https://smallseotools.com/backlink-checker/)
- [SEO Backlink Check](https://www.seobility.net/en/backlinkchecker/)
- [Moz Backlink](https://moz.com/link-explorer)
- [SPAM Check Score](https://www.dapachecker.org/spam-score-checker)
- [MOZ Spam Check](https://moz.com/help/link-explorer/link-building/spam-score)
- [WEB Check](https://web-check.xyz/)
- [brightcloud ip lookup](https://www.brightcloud.com/tools/url-ip-lookup.php)
- [Url Filltering](https://urlfiltering.paloaltonetworks.com/)
- [Katana](https://github.com/projectdiscovery/katana)
- [chiasmod0n](https://github.com/chiasmod0n/chiasmodon?tab=readme-ov-file)
- [redirectdetective](https://redirectdetective.com/)
- [wheregoes](https://wheregoes.com/)
- [spyoffers](https://www.spyoffers.com/)
- [Web Leaked Credentials](https://github.com/h4x0r-dz/Leaked-Credentials/)
- [host tracker](https://www.host-tracker.com/en)
- [crt.sh](https://crt.sh/)
- [view DNS](https://viewdns.info/)
- [visualping](https://visualping.io/)
- [jam dev browser extension](https://jam.dev/)
- [Whoxy Whois History](https://www.whoxy.com/whois-history/)
- [whoisfreaks Whois History](https://whoisfreaks.com/)
- [domaintools Whois History](https://research.domaintools.com/research/whois-history/)
- [whoisxmlapi Whois History](https://whois-history.whoisxmlapi.com/)

# Analysing URLs

- [Unfurl](https://github.com/obsidianforensics/unfurl)
- [VirusTotal](https://www.virustotal.com/gui/home/upload)
- [Archive Org](https://archive.org/web/)
- [Iplocation](https://iplocation.io/website-link-analyzer)
- [Smallseotools](https://smallseotools.com/website-link-analyzer-tool/)
- [Abuse IP](https://www.abuseipdb.com/)
- [Check Phish](https://checkphish.ai/)
- [Radar By Cloudflare](https://radar.cloudflare.com/)
- [Is it Phishing](https://isitphishing.org/)
- [Kaspersky](https://opentip.kaspersky.com/)
- [PolySwarm](https://polyswarm.network/)
- [Threat Miner](https://www.threatminer.org/)
- [Netcraft](https://www.netcraft.com/tools/)
- [Malwareworld](https://malwareworld.com/)
- [DNS TWIST](https://github.com/elceef/dnstwist)
- [URL CRAZY - Phishing detector](https://github.com/urbanadventurer/urlcrazy)
- [CRT - Find cert ssl and etc](https://crt.sh/)
- [Phishing catcher](https://github.com/x0rz/phishing_catcher)
- [Open Phish](https://openphish.com/phishing_feeds.html)
- [Phishtalk](https://www.phishtank.com/phish_archive.php)
- [URL Haus](https://urlhaus.abuse.ch/)
- [Expand Url](https://www.expandurl.net/)
- [Tiny Scan](https://www.tiny-scan.com)
- [redirectdetective](https://redirectdetective.com/)
- [wheregoes](https://wheregoes.com/)
- [spyoffers](https://www.spyoffers.com/)
- [vx-underground](https://vx-underground.org/)
- [ShadowDragon](https://shadowdragon.io/)

# Researching Cyber Threats

- [Apility.io](https://apility.io)
- [Alien Vault](https://otx.alienvault.com)
- [AutoShun](https://www.autoshun.org)
- [Blacklist Check Tool](http://www.blchecktool.com)
- [Censys](https://censys.io)
- [CVE Details](https://www.cvedetails.com)
- [IBM X-Force Exchange](https://exchange.xforce.ibmcloud.com)
- [JoeSandbox Cloud](https://www.joesandbox.com)
- [Is It Hacked?](http://www.isithacked.com)
- [Is It Phishing](https://isitphishing.org)
- [Kaspersky Threat](https://opentip.kaspersky.com)
- [Malware Domain List](http://www.malwaredomainlist.com/mdl.php)
- [Malware URL Website](https://www.malwareurl.com/listing-urls.php)
- [Quttera](https://quttera.com)
- [Virus total](https://www.virustotal.com/gui/home/upload)
- [Virus Share](https://virusshare.com)
- [Web Cookies Scanner](https://webcookies.org)
- [Yara](https://yara.readthedocs.io/en/stable/)
- [Spiderfoot](https://www.spiderfoot.net/)
- [NVD](https://nvd.nist.gov/search)
- [Seclist](https://seclists.org/fulldisclosure/)
- [CVE Mitre](https://cve.mitre.org/cve/search_cve_list.html)
- [Malicious Check](https://forum.seccodeid.com/d/phishing-email-analysis-tools)
- [Email Header Analysis](https://mxtoolbox.com/EmailHeaders.aspx)
- [Email-Analytics](https://emailanalytics.com/email-headers/)
- [Email Header Analisis Toolbox](https://toolbox.googleapps.com/apps/messageheader/)
- [Url Scan]( https://urlscan.io/ )
- [AnyRun](https://any.run/)
- [Hybrid Analysis](https://www.hybrid-analysis.com/)
- [VMRay Sandbox](https://www.vmray.com/)
- [Browser Sandbox](https://www.browserling.com/)
- [Fillter Bypass](https://www.filterbypass.me/id)
- [Abuse IP DB](https://www.abuseipdb.com/)
- [Talos CTI](https://www.talosintelligence.com/)
- [Phishing Analysis Tool](https://www.phishtool.com/)
- [Phish Verification System](https://phishtank.org/)
- [PolySwarm](https://www.maltego.com/transform-hub/polyswarm/)
- [ThreatCrowd](https://www.maltego.com/transform-hub/threatcrowd/)
- [HYAS Insight](https://www.maltego.com/transform-hub/hyas-insight/)
- [Phishstats](https://phishstats.info/)
- [GitGuardian](https://www.gitguardian.com/monitor-public-github-for-secrets)
- [Rescure](https://rescure.me/feeds.html)
- [PolySwarm](https://polyswarm.network/)
- [Darkfeed](https://darkfeed.io/)
- [Header Email](https://github.com/umair9747/headmail)
- [Badan Pemeriksa APK](https://apk.ibnux.com/?s=0)
- [SPAMHAUS](https://www.spamhaus.org/)
- [Spiderfoot HX](https://www.spiderfoot.net/open-source-vs-hx/) You must have account 
- [Flare](https://flare.io/)
- [Malwareworld](https://malwareworld.com/)
- [DNS TWIST](https://github.com/elceef/dnstwist)
- [URL CRAZY - Phishing detector](https://github.com/urbanadventurer/urlcrazy)
- [CRT - Find cert ssl and etc](https://crt.sh/)
- [Phishing catcher](https://github.com/x0rz/phishing_catcher)
- [Blackite](https://blackkite.com/community/)
- [Open Phish](https://openphish.com/phishing_feeds.html)
- [Phish Talk](https://www.phishtank.com/phish_archive.php)
- [Threat Feeds](https://threatfeeds.io/)
- [Threat Miner](https://www.threatminer.org/)
- [Intel OWL](https://github.com/intelowlproject/IntelOwl/)
- [RiskIQ](https://community.riskiq.com/)
- [LOKI](https://github.com/Neo23x0/Loki)
- [Mandiant](https://www.mandiant.com/advantage/threat-intelligence)
- [Mend Io](https://www.mend.io/vulnerability-database)
- [TRIAGE](https://tria.ge/reports/public)
- [EML Analyzer](https://eml-analyzer.herokuapp.com/#/)
- [Cyber Chef](https://gchq.github.io/CyberChef/)
- [Expand Url](https://www.expandurl.net/)
- [Wanna Browser Sandbox](https://www.wannabrowser.net/)
- [pestudio](https://www.winitor.com/download)
- [procmon](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [C2-Tracker](https://github.com/montysecurity/C2-Tracker)
- [malpedia](https://malpedia.caad.fkie.fraunhofer.de/)
- [vx-underground](https://vx-underground.org/)
- [shellpub](https://n.shellpub.com/en)
- [qianxin](https://ti.qianxin.com/en)
- [CAPA MANDIANT](https://github.com/mandiant/capa)
- [ShadowDragon](https://shadowdragon.io/)

# IoT Search Engines

- [LeakIX](https://leakix.net)
- [Binary Edge](https://www.binaryedge.io)
- [Shodan](https://www.shodan.io)
- [Shodan Filters](https://github.com/T43cr0wl3r/shodan-filters)
- [Shodan Scripts](https://github.com/random-robbie/My-Shodan-Scripts)
- [Kamerka](https://github.com/woj-ciech/Kamerka-GUI)
- [airportwebcams](https://airportwebcams.net/)
- [Earthcam](https://www.earthcam.com/#google_vignette)
- [tvway](http://tvway.ru/)
- [Cameraftp](https://www.cameraftp.com/cameraftp/publish/publishedcameras.aspx)
- [Insecam](http://Insecam.org)
- [Webcams](https://github.com/pbkompasz/webcams)
- [Molecool CCTV and Nearby](https://www.molecool.id/)
- [Calculator IPVM](https://calculator.ipvm.com/)
- [webcamtaxi](https://www.webcamtaxi.com/en/)
- [weatherbug](https://www.weatherbug.com/traffic-cam/)
- [CCTV location tracking](https://github.com/IvanGlinkin/CCTV)

# IP Addresses

- [Whats my ip](https://whatismyipaddress.com/)
This tools can show your ip address isp provider
- [Ip 2 location](https://www.ip2location.com/)
This tools can show your ip address isp provider and geo location  

# Wireless Network

- [Wigle](https://www.wigle.net/)
Maps and database of 802.11 wireless networks, with statistics, submitted by wardrivers, netstumblers, and
net huggers
- [Fing Net Scan](https://www.fing.com/)
- [Wifianalyzer](https://www.wifianalyzer.info/)
- [Signalmonitoring](https://signalmonitoring.com/)
- [Angry Ip](https://angryip.org/)
- [Advanced ip scanner](https://www.advanced-ip-scanner.com/)
- [Wifimap](https://www.wifimap.io/)
- [Fon](https://fon.com/maps/)
- [SolarWInds](https://www.solarwinds.com/network-performance-monitor/use-cases/wifi-monitor)

# SOC & Threat Hunting

Tips

You can find the file hash or other threat indicator

- [Alien Vault](https://otx.alienvault.com/)
- [Exploit db](https://www.exploit-db.com/)
- [AT&T](https://cybersecurity.att.com/resource-center#content_analyst-reports)
- [Yara](https://yara.readthedocs.io/en/stable/)
- [Virustotal](https://www.virustotal.com/gui/home/upload)
- [Joesandbox](https://www.joesandbox.com/#windows)
- [Spiderfoot](https://www.spiderfoot.net/)
- [Open CTI](https://github.com/OpenCTI-Platform/opencti)
- [Solarwinds](https://www.solarwinds.com/)
- [VMware Carbon Black Endpoint](https://www.vmware.com/products/carbon-black-cloud-endpoint.html)
- [Insightidr](https://www.rapid7.com/products/insightidr/)
- [MISP](https://www.misp-project.org/)
- [NVD](https://nvd.nist.gov/search)
- [Seclist](https://seclists.org/fulldisclosure/)
- [CVE Mitre](https://cve.mitre.org/cve/search_cve_list.html)
- [Whois Record](https://centralops.net/co/)
- [Abuse IP DB](https://www.abuseipdb.com/)
- [Talos CTI](https://www.talosintelligence.com/)
- [Darkfeed](https://darkfeed.io/)
- [Flare](https://flare.io/)
- [Mihari](https://github.com/ninoseki/mihari)
- [Processhacker](https://processhacker.sourceforge.io/)
- [Koodous](https://koodous.com/)
- [Blackite](https://blackkite.com/community/)
- [Open Phish](https://openphish.com/phishing_feeds.html)
- [Phish Talk](https://www.phishtank.com/phish_archive.php)
- [Sophos](https://www.sophos.com/en-us/intelix)
- [Signature Base](https://github.com/Neo23x0/signature-base) 
- [SIEM Rules](https://www.siemrules.com/)
- [Threat Feed](https://threatfeeds.io/)
- [Threat Connect](https://threatconnect.com/threat-intelligence-operations-platform/)
- [Threat Miner](https://www.threatminer.org/)
- [Virus Share](https://virusshare.com/)
- [Intel OWL](https://github.com/intelowlproject/IntelOwl/)
- [RiskIQ](https://community.riskiq.com/)
- [TypeDB](https://github.com/typedb-osi/typedb-cti)
- [Goosint](https://github.com/ciscocsirt/gosint)
- [Google APT search](https://cse.google.com/cse?cx=003248445720253387346:turlh5vi4xc)
- [LOKI](https://github.com/Neo23x0/Loki)
- [Mandiant](https://www.mandiant.com/advantage/threat-intelligence)
- [IoC Editor](https://fireeye.market/apps/S7cWpi9W)
- [CREST Threat Intel](https://www.crest-approved.org/wp-content/uploads/2022/04/CREST-Cyber-Threat-Intelligence.pdf?ref=secjuice.com)
- [Intel471](https://intel471.com/)
- [flashpoint](https://flashpoint.io/)
- [pestudio](https://www.winitor.com/download)
- [procmon](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [zerofox](https://www.zerofox.com/platform/)
- [malpedia](https://malpedia.caad.fkie.fraunhofer.de/)
- [vx-underground](https://vx-underground.org/)
- [shellpub](https://n.shellpub.com/en)
- [qianxin](https://ti.qianxin.com/en)
- [CAPA MANDIANT](https://github.com/mandiant/capa)
- [ShadowDragon](https://shadowdragon.io/)
- [sociallinks](https://sociallinks.io/)

# Automation Dorking 

- [Dorklab](https://github.com/rtwillett/DorkLab)
- [Ominis-Osint](https://github.com/AnonCatalyst/Ominis-Osint)
- [Go Dork](https://github.com/dwisiswant0/go-dork)
- [Dorkish](https://github.com/yousseflahouifi/dorkish)
- [Dork Collection](https://github.com/cipher387/Dorks-collections-list?tab=readme-ov-file)
- [Fast Dork Scan](https://github.com/IvanGlinkin/Fast-Google-Dorks-Scan.git)
- [Shodan Quries](https://github.com/jakejarvis/awesome-shodan-queries)
- [List Dork](https://github.com/BullsEye0/google_dork_list/blob/master/google_Dorks.txt)
- [CENSYS Queries](https://github.com/thehappydinoa/awesome-censys-queries)
- [Google Dork Simplified](https://github.com/dheerajydv19/Google-Dorks-Simplified)
- [Gdorks](https://github.com/Ishanoshada/GDorks)

# Github Dork

- [Advanced Search](https://github.com/search/advanced)
- [GitDorker](https://github.com/obheda12/GitDorker)
- [gitdorks_go](https://github.com/damit5/gitdorks_go)

# Dorking

Dorking is a wonderful thing, you can use this technique to search for anything such as index of a website, looking for live online camera server and other specifics, as for dorking commands that you can do for example

1. intitle: Search for specific titles
2. inurl: Search for specific urls or paths
3. intext: Search for specific words or contects
4. filetype: Search for files
5. site: Search from a specified target
6. Wildcard or symbol * (star) Find all web pages, for example: seccodeid*
7. Define:term Search for all things with specified terms, example define:seccodeid
8. cache page Take a snapshot of an indexed page. Google uses this to find the right page for the query you're looking for. Website or target specifically
9. allintext: Searches for specific text contained on a web page
10. allinurl: Find various keywords in a URL
11. allintitle: Restricts results to those containing all terms specified in a title
12. link: List of web pages that have links to the specified URL
13. (|) Pipe. This is a logical operator, | "tips" will show all the sites which contain either, or both words
14. (+) Used to concatenate words, useful to detect pages that use more than one specific key
15. (-) Minus operator avoids showing results that contain certain words, e.g. security -trails will show pages that use "security" in their text, but not those that have the word "trails"

Example
```
".mlab.com password"
"access_key"
"access_token"
"amazonaws"
"api.googlemaps AIza"
"api_key"
"api_secret"
"apidocs"
"apikey"
"apiSecret"
"app_key"
"app_secret"
"appkey"
"appkeysecret"
"application_key"
"appsecret"
"appspot"
"auth"
"auth_token"
"authorizationToken"
"aws_access"
"aws_access_key_id"
"aws_key"
"aws_secret"
"aws_token"
"AWSSecretKey"
"bashrc password"
"bucket_password"
"client_secret"
"cloudfront"
"codecov_token"
"config"
"conn.login"
"connectionstring"
"consumer_key"
"credentials"
"database_password"
"db_password"
"db_username"
"dbpasswd"
"dbpassword"
"dbuser"
"dot-files"
"dotfiles"
"encryption_key"
"fabricApiSecret"
"fb_secret"
"firebase"
"ftp"
"gh_token"
"github_key"
"github_token"
"gitlab"
"gmail_password"
"gmail_username"
"herokuapp"
"internal"
"irc_pass"
"JEKYLL_GITHUB_TOKEN"
"key"
"keyPassword"
"ldap_password"
"ldap_username"
"login"
"mailchimp"
"mailgun"
"master_key"
"mydotfiles"
"mysql"
"node_env"
"npmrc _auth"
"oauth_token"
"pass"
"passwd"
"password"
"passwords"
"pem private"
"preprod"
"private_key"
"prod"
"pwd"
"pwds"
"rds.amazonaws.com password"
"redis_password"
"root_password"
"secret"
"secret.password"
"secret_access_key"
"secret_key"
"secret_token"
"secrets"
"secure"
"security_credentials"
"send.keys"
"send_keys"
"sendkeys"
"SF_USERNAME salesforce"
"sf_username"
"site.com" FIREBASE_API_JSON=
"site.com" vim_settings.xml
"slack_api"
"slack_token"
"sql_password"
"ssh"
"ssh2_auth_password"
"sshpass"
"staging"
"stg"
"storePassword"
"stripe"
"swagger"
"testuser"
"token"
"x-api-key"
"xoxb "
"xoxp"
[WFClient] Password= extension:ica
access_key
bucket_password
dbpassword
dbuser
extension:avastlic "support.avast.com"
extension:bat
extension:cfg
extension:env
extension:exs
extension:ini
extension:json api.forecast.io
extension:json googleusercontent client_secret
extension:json mongolab.com
extension:pem
extension:pem private
extension:ppk
extension:ppk private
extension:properties
extension:sh
extension:sls
extension:sql
extension:sql mysql dump
extension:sql mysql dump password
extension:yaml mongolab.com
extension:zsh
filename:.bash_history
filename:.bash_history DOMAIN-NAME
filename:.bash_profile aws
filename:.bashrc mailchimp
filename:.bashrc password
filename:.cshrc
filename:.dockercfg auth
filename:.env DB_USERNAME NOT homestead
filename:.env MAIL_HOST=smtp.gmail.com
filename:.esmtprc password
filename:.ftpconfig
filename:.git-credentials
filename:.history
filename:.htpasswd
filename:.netrc password
filename:.npmrc _auth
filename:.pgpass
filename:.remote-sync.json
filename:.s3cfg
filename:.sh_history
filename:.tugboat NOT _tugboat
filename:_netrc password
filename:apikey
filename:bash
filename:bash_history
filename:bash_profile
filename:bashrc
filename:beanstalkd.yml
filename:CCCam.cfg
filename:composer.json
filename:config
filename:config irc_pass
filename:config.json auths
filename:config.php dbpasswd
filename:configuration.php JConfig password
filename:connections
filename:connections.xml
filename:constants
filename:credentials
filename:credentials aws_access_key_id
filename:cshrc
filename:database
filename:dbeaver-data-sources.xml
filename:deployment-config.json
filename:dhcpd.conf
filename:dockercfg
filename:environment
filename:express.conf
filename:express.conf path:.openshift
filename:filezilla.xml
filename:filezilla.xml Pass
filename:git-credentials
filename:gitconfig
filename:global
filename:history
filename:htpasswd
filename:hub oauth_token
filename:id_dsa
filename:id_rsa
filename:id_rsa or filename:id_dsa
filename:idea14.key
filename:known_hosts
filename:logins.json
filename:makefile
filename:master.key path:config
filename:netrc
filename:npmrc
filename:pass
filename:passwd path:etc
filename:pgpass
filename:prod.exs
filename:prod.exs NOT prod.secret.exs
filename:prod.secret.exs
filename:proftpdpasswd
filename:recentservers.xml
filename:recentservers.xml Pass
filename:robomongo.json
filename:s3cfg
filename:secrets.yml password
filename:server.cfg
filename:server.cfg rcon password
filename:settings
filename:settings.py SECRET_KEY
filename:sftp-config.json
filename:sftp-config.json password
filename:sftp.json path:.vscode
filename:shadow
filename:shadow path:etc
filename:spec
filename:sshd_config
filename:token
filename:tugboat
filename:ventrilo_srv.ini
filename:WebServers.xml
filename:wp-config
filename:wp-config.php
filename:zhrc
HEROKU_API_KEY language:json
HEROKU_API_KEY language:shell
HOMEBREW_GITHUB_API_TOKEN language:shell
jsforce extension:js conn.login
language:yaml -filename:travis
msg nickserv identify filename:config
org:Target "AWS_ACCESS_KEY_ID"
org:Target "list_aws_accounts"
org:Target "aws_access_key"
org:Target "aws_secret_key"
org:Target "bucket_name"
org:Target "S3_ACCESS_KEY_ID"
org:Target "S3_BUCKET"
org:Target "S3_ENDPOINT"
org:Target "S3_SECRET_ACCESS_KEY"
password
path:sites databases password
private -language:java
PT_TOKEN language:bash
redis_password
root_password
secret_access_key
SECRET_KEY_BASE=
shodan_api_key language:python
WORDPRESS_DB_PASSWORD=
xoxp OR xoxb OR xoxa
s3.yml
.exs
beanstalkd.yml
deploy.rake
.sls
AWS_SECRET_ACCESS_KEY
API KEY
API SECRET
API TOKEN
ROOT PASSWORD
ADMIN PASSWORD
GCP SECRET
AWS SECRET
"private" extension:pgp
```

> intext:"hacking" site:seccodeid.com
> 
> inurl:login site:seccodeid.com
>
> intext:username filetype:log
>
> site:www.github.com ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv  
>

# Dorking Other Search Engine 

- [YANDEX](https://seosly.com/blog/yandex-search-operators/)
- [BING](https://seosly.com/blog/bing-search-operators/)
- [mediasova](https://search.mediasova.com/en/index)

# Bash Dorking Script

PRO TIPS!

You can add other headers, regex and search engine endpoints for refinement and to encode queries

- BING SEARCH

WEB

```WEB
for ((i=1;i<=10;i++));do curl -i -s -k -L -X GET -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0" "https://www.bing.com/search?pglt=2081&q=.php?id=" | grep -Eo 'href="[^\"]+"' | grep -Po "(http|https)://[a-zA-Z0-9./?=_%:-]*" | grep ".php?id" | sort -u ;done
```

Hunt Username

```USERNAME
for ((i=1;1<=10;i++));do curl -i -s -k -L -X GET -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0;Accept: */*;Accept-Language: id,en-US;q-0.7,en;q-0.3;Accept-Encoding: gzip, deflate, br;Referer: https: //www.bing.com/;DNT: 1;Connection: keep-alive;Cookie: 1P_JAR=2023-11-05-19;Sec-Fetch-Dest:empty;Sec-Fetch-Mode:cors;Sec-Fetch-Site: same-origin;TE: trailers" "https://www.bing.com/search?pglt=2081&q=Jieyab89" | grep -Eo 'href="[^\"]+"' | grep -Po "(http|https)://[a-zA-Z0-9./?=_%:-]*" | grep -E "Jieyab89|github" | sort -u ;done
```

Hunt Username

```USERNAME
for ((i=1;1<=10;i++));do curl -i -s -k -L -X GET -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0;Accept: */*;Accept-Language: id,en-US;q-0.7,en;q-0.3;Accept-Encoding: gzip, deflate, br;Referer: https: //www.bing.com/;DNT: 1;Connection: keep-alive;Cookie: 1P_JAR=2023-11-05-19;Sec-Fetch-Dest:empty;Sec-Fetch-Mode:cors;Sec-Fetch-Site: same-origin;TE: trailers" "Your Bing Request URL Header" | grep -Eo 'href="[^\"]+"' | grep -Po "(http|https)://[a-zA-Z0-9./?=_%:-]*" | grep -E "Jieyab89|github" | sort -u ;done
```

- GOOGLE SEARCH

Hunt Username

```USERNAME
for ((i=1;1<=10;i++));do curl -i -s -k -L -X GET -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0;Accept: */*;Accept-Language: id,en-US;q-0.7,en;q-0.3;Accept-Encoding: gzip, deflate, br;Referer: https: //www.google.com/;DNT: 1;Connection: keep-alive;Cookie: 1P_JAR=2023-11-05-19;Sec-Fetch-Dest:empty;Sec-Fetch-Mode:cors;Sec-Fetch-Site: same-origin;TE: trailers" "https://www.google.com/search?sourceid=chrome-psyapi2&ion=1&espv=2&ie=UTF-8&start=${i}0&q=Jieyab89" | grep -Eo 'href="[^\"]+"' | grep -Po "(http|https)://[a-zA-Z0-9./?=_%:-]*" | grep -E "Jieyab89|github" | sort -u ;done
```

WEB

```WEB
for ((i=1;i<=10;i++));do curl -i -s -k -L -X GET -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0" "https://www.google.com/search?sourceid=chrome-psyapi2&ion=1&espv=2&ie=UTF-8&start=${i}0&q=.php?id=" | grep -Eo 'href="[^\"]+"' | grep -Po "(http|https)://[a-zA-Z0-9./?=_%:-]*" | grep ".php?id" | sort -u ;done
```

# Google Advanced Search Tools

- [Advanced google search](https://www.google.com/advanced_search)
- [Google Scholar](https://scholar.google.com)
- [Google Alerts](https://www.google.com/alerts)
- [Google Search History](https://myactivity.google.com/myactivity)

# Other Search Engines

- [us.searchboth.net](http://us.searchboth.net)
- [Archive.org](http://www.arhive.org)
- [Yandex](Yandex.com)
- [Pastebin](http://www.pastebin.com)
- [Topix.com](http://www.topix.com)
- [search.carrot2.org/stable/search](http://search.carrot2.org/stable/search)
- [Shodan](https://www.shodan.io/)
- [Piratebays](https://thepiratebays.com/)
- [Onesearch](https://www.onesearch.com/)
- [Searchencrypt](https://www.searchencrypt.com/home)
- [Duckgo](https://duckduckgo.com/)
- [Waymore](https://forum.seccodeid.com/d/waymore-find-way-more-from-the-wayback-machine)
- [StartPage](https://www.startpage.com/)
- [Searx](https://searx.space/)
- [CommonCrawl](https://commoncrawl.org/latest-crawl)
- [Similar Sites](https://www.similarsites.com/)
- [Zap Meta](https://www.zapmeta.com/)
- [Carrot Search](https://search.carrot2.org/#/search/web)
- [Goo Search](https://www.goo.ne.jp/)
- [swisscows](https://swisscows.com/en)
- [odp](http://www.odp.org/homepage.php)
- [Yiipy Search](https://www.yippysearchengine.com/)
- [webarchiveviewer](https://cybdetective.com/webarchiveviewer/)
- [duckduckgo Bangs](https://duckduckgo.com/bangs)
- [mediasova](https://search.mediasova.com/en/index)
- [mojeek](https://www.mojeek.com/)
- [boardreader](https://boardreader.com/)

# Internet Archive

- [DMCA](https://lumendatabase.org/)
- [Wayback Machine](https://web.archive.org/)
- [Intelligence X](https://intelx.io/)
- [Openlibrary](https://openlibrary.org/)
- [Archive Fo](https://archive.fo/)
- [UKWA](https://www.webarchive.org.uk/ukwa/)
- [Archive today](https://archive.vn/)
- [Waymore](https://forum.seccodeid.com/d/waymore-find-way-more-from-the-wayback-machine)
- [Cached Pages](http://www.cachedpages.com/)
- [cachedview](https://cachedview.com/)
- [ArchivEye](https://github.com/eastrd/ArchivEye)
- [Twitter Archive](https://github.com/humandecoded/twayback)
- [Archive Today](https://archive.is/)
- [Wayback Downloader](https://github.com/hartator/wayback-machine-downloader)
- [How to archive tele content](https://www.bellingcat.com/resources/how-tos/2022/03/08/how-to-archive-telegram-content-to-document-russias-invasion-of-ukraine/)
- [webarchiveviewer](https://cybdetective.com/webarchiveviewer/)
- [ShadowDragon](https://shadowdragon.io/)

# Data Breached OSINT

- [Dehashed](https://www.dehashed.com/)
- [Haveibeenpwned](https://haveibeenpwned.com/)
- [Intelligence X](https://intelx.io/)
- [Wiki Leaks](https://wikileaks.org/)
- [DDO Secrets](https://ddosecrets.com/wiki/Distributed_Denial_of_Secrets)
- [Breached](https://breached.to/) Availabe on Darkweb
- [Stealthmole](https://www.stealthmole.com/products/darkweb-tracker)
- [Doxbin](https://doxbin.com/)
- [Search0t](https://search.0t.rocks/)
- [Search0t MAP](https://search.0t.rocks/map)
- [What Breach](https://github.com/Ekultek/WhatBreach)
- [Breach Directory](https://breachdirectory.org/)
- [Snusbase](https://snusbase.com/)
- [Flare](https://flare.io/)
- [Leaklookup](https://leak-lookup.com/)
- [Pastos](https://github.com/carlospolop/Pastos)
- [Blackkite](https://blackkite.com/community/)
- [Facebook Data Breach Cheker](https://haveibeenzuckered.com/)
- [pwnedOrNot](https://github.com/thewhiteh4t/pwnedOrNot)
- [Intel471](https://intel471.com/)
- [Maltego Transform ShadowDragon](https://www.maltego.com/transform-hub/socialnet/)
- [offshoreleaks](https://offshoreleaks.icij.org/)
- [proxynova password breach](https://proxynova.com/tools/comb/)
- [WhiteIntel](https://whiteintel.io/)

# Crack Jurnals

- [SCI HUB](https://sci-hub.hkvisa.net/) This domain will always change
- [Z-Library](https://id.zlibrary-asia.se/s/?q=&type=phrase)
- [DOAJ (Directory of Open Access Journals)](https://doaj.org/)
- [LibGen (Library Genesis)](https://libgen.li/)
- [ScienceOpen](https://www.scienceopen.com/)
- [CORE](https://core.ac.uk/)
- [Unpaywall](https://unpaywall.org/)
- [Wiley Online Library](https://onlinelibrary.wiley.com/)
- [Open Access Button](https://openaccessbutton.org/)

# Search Jurnals

- [Libgen](https://libgen.is/)
- [Ieee](https://ieeexplore.ieee.org/Xplore/home.jsp)
- [Sciencedirect](https://www.sciencedirect.com/)
- [Sinta](https://sinta.kemdikbud.go.id/)
- [Scopus](https://www.scopus.com/)
- [Onesearch ID](https://onesearch.id/)
- [Z-Library](https://id.zlibrary-asia.se/s/?q=&type=phrase)
- [DOAJ (Directory of Open Access Journals)](https://doaj.org/)
- [LibGen (Library Genesis) 2](https://libgen.li/)
- [ScienceOpen](https://www.scienceopen.com/)
- [CORE](https://core.ac.uk/)
- [Springer Support](https://www.springeropen.com/journals)
- [Springer link 2](https://link.springer.com/)
- [Academia.edu](https://www.academia.edu/)
- [CyberLeninka](https://cyberleninka.org/)
- [Unpaywall](https://unpaywall.org/)
- [ResearchGate](https://www.researchgate.net/)
- [Wiley Online Library](https://onlinelibrary.wiley.com/)
- [Open Access Button](https://openaccessbutton.org/)

# Blogs Search Engine

- [Google Blog](www.google.com/blogsearch)
- [technorati](www.technorati.com)
- [omgili.com](http://omgili.com/)

# Darkweb Search Engines

- [Thehiddenwiki](http://thehiddenwiki.org)
- [Onion Link](http://www.onion.link)
- [MEMEX](https://memex.garden/)
- [Onion](https://onion.cab)
- [Onion city](https://onion.city/)
- [Ahmia](https://ahmia.fi/)
- [TorBot](https://github.com/DedSecInside/TorBot)
- [Darkfeed](https://darkfeed.io/)
- [Torch](xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega?P=)
- [Onionsearch](https://github.com/megadose/OnionSearch)
- [Darknet Book](https://github.com/darknet-book/tor-guide)
- [immuniweb](https://www.immuniweb.com/darkweb/)

# Tracking Website Changes

- [Changedetection](http://www.changedetection.com)
- [Followthatpage](http://www.followthatpage.com)
- [visualping](https://visualping.io/)

# Company Reconnaissance Sites (Passive)

- [whois](http://www.whois.net)
- [whois by hostinger](https://www.hostinger.co.id/whois)
- [Netcraft](http://www.netcraft.com)
- [Hunter](https://hunter.io/)
- [SignalHire](https://www.signalhire.com/)
- [Spiderfoot](https://www.spiderfoot.net/) 
- [Spiderfoot HX](https://www.spiderfoot.net/open-source-vs-hx/) You must have account
- [Rocket Reach](https://rocketreach.co/)
- [Glasdoor](https://www.glassdoor.com/)
- [Linkedin](https://www.linkedin.com/)
- [Indeed](https://www.indeed.com/companies?from=gnav-title-webapp)
- [ZoomInfo](https://www.zoominfo.com/)
- [Crunchbase](https://www.crunchbase.com/)
- [Apolo](https://www.apollo.io/)
- [Lusha](https://www.lusha.com/)
- [Jobstreet](https://www.jobstreet.com.ph/)
- [BOTW](https://botw.org/)
- [opencorporates](https://opencorporates.com/)
- [Data OCCRP](https://data.occrp.org/)
- [OSINT Maps](https://cybdetective.com/osintmap/)
- [Tripadvisor](https://www.tripadvisor.com/)
- [Trustindex](https://www.trustindex.io/)
- [G Map Review](https://www.google.com/maps/)
- [Provenexpert](https://www.provenexpert.com/)
- [SIMPU RI](https://umrahcerdas.kemenag.go.id/)
- [collegerecruiter](https://www.collegerecruiter.com/)
- [corporationwiki](https://www.corporationwiki.com/)
- [Maltego social links](https://www.maltego.com/transform-hub/social-links-ce/)
- [indokontraktor ID](https://indokontraktor.com/)
- [opentender ID](https://opentender.net/)
- [lpse lkpp ID](https://lpse.lkpp.go.id/eproc4)
- [ahu ID](https://ahu.go.id/pencarian/profil-pt)
- [Minerba ESDM ID](https://momi.minerba.esdm.go.id/gisportal/home/)
- [MODI ID](https://modi.esdm.go.id/portal/dataPerusahaan)
- [Minerba ESDM ID Map](https://momi.minerba.esdm.go.id/public/)
- [HAKI ID](https://pdki-indonesia.dgip.go.id/search?type=trademark&keyword=)
- [Email Format](https://www.email-format.com/i/search/)
- [opensanctions](https://www.opensanctions.org/)
- [ALEPT OCCRP](https://aleph.occrp.org/)
- [offshoreleaks](https://offshoreleaks.icij.org/)
- [gajiterbaru](https://gajiterbaru.id/)
- [sociallinks](https://sociallinks.io/)

# People Searching

- [spokeo](http://www.spokeo.com)
- [123people](http://www.123people.com)
- [peepdb](http://www.peepdb.com)
- [reversegeni](http://www.reversegenie.com/plate.php)
- [PDDIKTI](https://pddikti.kemdikbud.go.id/)
- [IDEBKU OJK ID](https://idebku.ojk.go.id/Public/HomePage)
- [SINTA](https://sinta.kemdikbud.go.id/)
- [Social Searcher](https://www.social-searcher.com/)
- [Pimeyes](https://pimeyes.com/en)
- [Rocketreach](https://rocketreach.co/)
- [SignalHire](https://www.signalhire.com/)
- [Thatsthem](https://thatsthem.com/)
- [Freepeoplesearch](https://freepeoplesearch.com/)
- [Epios](https://epieos.com/)
- [anymailfinder](https://anymailfinder.com/)
- [getprospect](https://getprospect.com/)
- [ZoomInfo](https://www.zoominfo.com/)
- [Apolo](https://www.apollo.io/)
- [Family Tree](https://www.familytreenow.com/)
- [Radaris](https://radaris.com/)
- [beenverified](https://www.beenverified.com/people/)
- [bandcamp](https://bandcamp.com/)
- [Sherlock Eye](https://sherlockeye.io/)
- [NIK PARSE](https://github.com/bachors/nik_parse.js?tab=readme-ov-file#nik_parsejs)
- [Maltego Social Links Pro](https://www.maltego.com/transform-hub/social-links-pro/)
- [hertz](https://www.hertz.com/rentacar/receipts/request-receipts.do)
- [fastpeoplesearch](https://www.fastpeoplesearch.com/)
- [fastpeoplesearch.info](https://fastpeoplesearch.info/)
- [intelius](https://www.intelius.com/)
- [recruitin](https://recruitin.net/)
- [recruitmentgeek](https://recruitmentgeek.com/tools/linkedin#gsc.tab=0)

# Family People Search 

- [Delpher](https://www.delpher.nl/)
- [Myheritage](https://www.myheritage.com/)
- [Myheritage NL](https://www.myheritage.nl/)
- [FamilySearch](https://www.familysearch.org/id/indonesia/)
- [genealogieonline](https://www.genealogieonline.nl/en/)
- [geneanet](https://en.geneanet.org/)

# Phone Numbers

- [argali](http://www.argali.com)
- [ciddb](http://www.ciddb.com/index.php)
- [cellrevealer](http://www.cellrevealer.com)
- [spydialer](http://www.spydialer.com)
- [Twilio](https://www.twilio.com/lookup)
- [Reverse lookup](https://www.reversephonelookup.com/)
- [PhoneInfoga](https://github.com/sundowndev/PhoneInfoga)
- [Sync](https://sync.me/)
- [National cell](https://www.nationalcellulardirectory.com/)
- [Getcontact](https://www.getcontact.com/id/)
- [Moriarty-Project](https://github.com/AzizKpln/Moriarty-Project)
- [Get Contact](https://www.getcontact.com/en/)
- [True Caller](https://www.truecaller.com/)
- [Cell Id Lookup](https://www.reskrim.com/cek.php)
- [Device Info](https://www.deviceinfo.me/)
- [Cell Finder](https://cellidfinder.com/)
- [Unkownphone](https://www.unknownphone.com/)
- [Whocallsme](https://whocallsme.com/)
- [elenchitelefonici](https://www.elenchitelefonici.it/)
- [nationalcellulardirectory](https://www.nationalcellulardirectory.com/)
- [phonebooks](https://www.phonebooks.com/)
- [International Phone Directories](https://www.thisnumber.com/)
- [PhoneInfoga](https://demo.phoneinfoga.crvx.fr/#/)
- [Spy Dialer](https://spydialer.com/)
- [Phone Validator](https://www.phonevalidator.com/)
- [Fone finder](https://www.fonefinder.net/)
- [411 reverse phone](https://www.411.com/reverse-phone)
- [Number guru](https://www.numberguru.com/)
- [Zaba reverse phone](https://www.zabasearch.com/reverse-phone-lookup/)
- [FullContact](https://www.maltego.com/transform-hub/full-contact/)
- [HLR Lookup](https://www.hlrlookup.com/)
- [Ceebydith HLR Lookup](https://ceebydith.com/cek-hlr-lokasi-hp.html)
- [Free HLR](https://www.free-hlr.com/)
- [HLR Lookup API](https://www.hlr-lookups.com/)
- [Maltego Phone Search](https://www.maltego.com/transform-hub/phonesearch/)
- [SignalHire](https://www.signalhire.com/)
- [Emobiletracker](https://www.emobiletracker.com/)
- [OpenCNAM](https://docs.maltego.com/support/solutions/articles/15000045282-maltego-opencnam-transforms)
- [Fullcontact](https://www.fullcontact.com/)
- [seon](https://seon.io/resources/the-ultimate-guide-to-free-email-lookup-and-reverse-email-lookup-tools/)
- [Thatsthem](https://thatsthem.com/)
- [Freepeoplesearch](https://freepeoplesearch.com/)
- [Epios](https://epieos.com/)
- [anymailfinder](https://anymailfinder.com/)
- [getprospect](https://getprospect.com/)
- [ZoomInfo](https://www.zoominfo.com/)
- [Spam Calls](https://spamcalls.net/en/)
- [inteltechniques](https://inteltechniques.com/tools/Telephone.html)
- [pipl](https://pipl.com/)
- [phonebook](https://phonebook.cz/)

# Public Records

- [Public Record](http://publicrecords.searchsystems.net)
- [Fam Watchdog](http://Familywatchdog.us)
- [Crime Reports](http://www.crimereports.com)

# Finding Usernames

- [Namechk](http://www.namechk.com)
- [Knowem](http://www.knowem.com)
- [Nexfil](https://github.com/thewhiteh4t/nexfil)
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [Instantusername](https://instantusername.com/#/)
- [Snitch](http://snitch.name/)
- [Checkusernames](https://checkusernames.com/)
- [Maigret](https://github.com/soxoj/maigret)
- [Picuki](https://www.picuki.com/)
- [ZoomInfo](https://www.zoominfo.com/)
- [Alfred](https://github.com/Alfredredbird/alfred)
- [Blackbird](https://github.com/p1ngul1n0/blackbird)
- [Bellingcat Username](https://bellingcat.github.io/name-variant-search/#gsc.tab=0)
- [whatsmyname](https://whatsmyname.app/)
- [holehe](https://github.com/megadose/holehe)
- [hertz](https://www.hertz.com/rentacar/receipts/request-receipts.do)

# Social Networks

- [Facebook](https://facebook.com/livemap)
- [Facebook lookup id](https://lookup-id.com/#)
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [Socialsearcher Users](https://www.social-searcher.com/)
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [Nexfil](https://github.com/thewhiteh4t/nexfil)
- [Googlesocialsearch](https://www.social-searcher.com/google-social-search/)
- [Google Social Network Transforms](https://www.maltego.com/transform-hub/google-programmable-search-engine-transforms/)
- [FullContact](https://www.maltego.com/transform-hub/full-contact/)
- [maigret](https://github.com/soxoj/maigret)
- [Blackbird](https://github.com/p1ngul1n0/blackbird)

# Google Queries for Facebook

> Group Search: site:facebook.com inurl:group
>
> Group Wall Posts Search: site:facebook.com inurl:wall
>
> Pages Search: site:facebook.com inurl:pages
>
> Public Profiles: allinurl: people ‘‘name’’ site:facebook.com
>

# Facebook Query Language (FQL)

- [Findmyfbid](http://www.findmyfbid.com/)
- [Lists FB Query Endpoint](https://gist.github.com/nemec/2ba8afa589032f20e2d6509512381114)

> Photos By - https://www.facebook.com/search/taget_id/photos-by
>  
> Photos Liked - https://www.facebook.com/search/taget_id/photos-liked
>  
> Photos Of - https://www.facebook.com/search/taget_id/photos-of
>  
> Comments - https://www.facebook.com/search/taget_id/photos-commented
>  
> Friends - https://www.facebook.com/search/taget_id/friends
>  
> Videos Tagged - https://www.facebook.com/search/taget_id/videos
>  
> Videos By - https://www.facebook.com/search/taget_id/videos-by
>  
> Videos Liked - https://www.facebook.com/search/taget_id/videos-liked
>  
> Videos Commented - https://www.facebook.com/search/taget_id/videos-commented
>  
> Events Attended - https://www.facebook.com/search/taget_id/events-joined
>  
> Relatives - https://www.facebook.com/search/taget_id/relatives
>  

or you can use dork for spesific example

> id <this id facebook> site:facebook.com
>  
> page site: facebook.com
>
> id <this id facebook> site:facebook.com *
>
> page site: facebook.com *
>

# The Ultimate Facebook Investigation Tool

- [Intel Technique](https://inteltechniques.com/osint/facebook.html)
- [DumpItBlue](http://le-tools.com/DumpItBlue.html)
- [Facebook Search](http://search.fb.com/)
- [Fb-sleep-stats](https://github.com/sqren/fb-sleep-stats)
- [Lookup-ID.com](https://lookup-id.com)
- [SearchIsBack](https://searchisback.com)
- [Wolfram Alpha Facebook Report](http://www.wolframalpha.com/input/?i=facebook+report)
- [Facebook Recover Lookup](https://web.facebook.com/login/identify?ctx=recover&_rdc=1&_rdr)
- [Who posted facebook](https://whopostedwhat.com/)
- [sowsearch](https://www.sowsearch.info/)
- [Hastag Analzer](https://www.hashatit.com/)
- [Export comment](https://exportcomments.com/)
- [Facebook endpoint](https://plessas.net/facebookmatrix)
- [Facebook Graph](https://graph.tips/facebook.html) 
- [Facebook live](https://www.facebook.com/watch/live/?ref=live_delegate)
- [Facebook vid downloader](https://fdown.net/)
- [Fb Sleep Stats](https://github.com/sorenlouv/fb-sleep-stats)
- [Skopenow FB Hunter](https://www.skopenow.com/)
- [Facebook Data Breach Cheker](https://haveibeenzuckered.com/)

# OnlyFans

- [fansmetrics](https://fansmetrics.com/)
- [onlysearch](https://onlysearch.co/)
- [onlyfinder](https://onlyfinder.com/)
- [onlyfans search](https://hubite.com/en/onlyfans-search/)
- [fansearch](https://www.fansearch.com/)

# Steam 

- [STEAM DB](https://steamdb.info/calculator/)
- [Steam OSINT tool](https://github.com/matiash26/Steam-OSINT-TOOL)

# Slack 

- [SlackPirate](https://github.com/emtunc/SlackPirate)

# Office365

- [Oh365UserFinder](https://github.com/dievus/Oh365UserFinder)
- [o365chk](https://github.com/nixintel/o365chk)

# Instagram

- [Hashtagify](http://hashtagify.me)
- [Iconosquare](http://iconosquare.com)
- [Picodash](https://www.picodash.com)
- [Toutatis](https://github.com/megadose/toutatis)
- [SearchMyBio](https://www.searchmy.bio/)
- [Dumpor](https://dumpor.com/)
- [Hookgram](https://hookgram.com/)
- [Picuki](https://www.picuki.com/)
- [Inflact](https://inflact.com/)
- [Greatfon](https://greatfon.com/)
- [Save Free](https://www.save-free.com/)
- [Insta Location Search](https://github.com/bellingcat/instagram-location-search)
- [Insta story visual maps](https://github.com/Jasawn/python-instagram-story-visualiser)
- [Snap Insta](https://snapinsta.app/)
- [Insta Profiler](https://imginn.io/)
- [Insta Loader](https://github.com/instaloader/instaloader)
- [Storistalker](https://storistalker.com/#back)
- [instahunt](https://instahunt.co/)
- [Sterraxcyl IG Profiler](https://github.com/novitae/sterraxcyl)

# Microsoft OneDrive 

- [Onedrive enum](https://github.com/nyxgeek/onedrive_user_enum)

# Pinterest

- [Pingroupie](http://pingroupie.com)
- [Pinterest Downloader](https://www.expertsphp.com/pinterest-photo-downloader.html)
- [Pinterset Guest](https://addons.mozilla.org/en-US/firefox/addon/pinterest-guest/)
- [Pinterest search](https://sourcinglab.io/search/pinterest)

# Reddit 

- [karmadecay](http://karmadecay.com/)
- [reddit post analyser](https://www.osintcombine.com/reddit-post-analyser)
- [Archive Reddit](https://www.redditarchive.com/)
- [Reddit Search](https://redditcommentsearch.com/)
- [Vizit](https://redditstuff.github.io/sna/vizit/)
- [Sub reddit](https://subreddits.org/)
- [RedActive](https://www.redective.com/)
- [f5bot](https://f5bot.com/)

# Youtube 

- [citizenevidence](https://citizenevidence.amnestyusa.org/)
- [watchframebyframe](http://www.watchframebyframe.com/)
- [YT Mtedata](https://mattw.io/youtube-metadata/)
- [TY Geo Find](https://mattw.io/youtube-geofind/)
- [YT chat downloader](https://github.com/xenova/chat-downloader)

# Twitter

- [search.twitter.com](https://twitter.com/search-home)
- [twitter advanced](https://www.twitter.com/search-advanced)
- [twitter who_to_follow](https://www.twitter.com/who_to_follow)
- [Backtweets](http://backtweets.com) BackTweets is a Twitter analytics tool that allows users to search through a Tweet archive.
- [First Tweet](http://ctrlq.org/first)
- [Foller.me](http://foller.me)
- [Followerwonk](http://followerwonk.com)
- [GeoSocial Footprint](http://geosocialfootprint.com)
- [Gigatweeter](http://gigatweeter.com)
- [Harvard TweetMap](http://worldmap.harvard.edu/tweetmap)
- [Hashtagify](http://hashtagify.me)
- [Hashtags.org](http://www.hashtags.org)
- [MyTweetAlerts](https://www.mytweetalerts.com/) A tool to create custom email alerts based on Twitter search.
- [OneMillionTweetMap](http://onemilliontweetmap.com)
- [SnapBird](http://snapbird.org)
- [Social Bearing](http://www.socialbearing.com)
- [Social Rank First Follower](http://socialrank.com/firstfollower)
- [Spoonbill](http://spoonbill.io)
- [Tagdef](https://tagdef.com)
- [TeachingPrivacy](http://app.teachingprivacy.com)
- [Tinfoleak](https://tinfoleak.com)
- [Trends24](http://trends24.in)
- [TrendsMap](http://trendsmap.com)
- [Ttrends](https://ttrends.co)
- [twbirthday](http://twbirthday.com)
- [TwChat](http://twchat.com)
- [tweepsect](http://tweepsect.com)
- [TweetArchivist](http://www.tweetarchivist.com)
- [TweetDeck](https://www.tweetdeck.com)
- [Tweeten](http://tweeten.xyz)
- [TweetMap](http://mapd.csail.mit.edu/tweetmap)
- [TweetMap](http://worldmap.harvard.edu/tweetmap)
- [TweetPsych](http://tweetpsych.com)
- [Tweetreach](http://tweetreach.com)
- [TweetStats](http://www.tweetstats.com)
- [TweetTunnel](http://tweettunnel.com)
- [Twellow](http://www.twellow.com)
- [Tweriod](http://www.tweriod.com)
- [Twiangulate](http://www.twiangulate.com)
- [Twilert](http://www.twilert.com)
- [Twipho](http://www.twipho.net)
- [Twitonomy](http://www.twitonomy.com)
- [TwitRSS](https://twitrss.me)
- [Twitter Advanced Search](https://twitter.com/search-advanced?lang=en)
- [Twitter Audit](https://www.twitteraudit.com)
- [Twitter Chat Schedule](http://tweetreports.com/twitter-chat-schedule)
- [Twitter Counter](http://twittercounter.com)
- [Twitterfall](http://twitterfall.com)
- [Twitter Search](http://search.twitter.com)
- [TWUBS Twitter Chat](http://twubs.com/twitter-chats)
- [Schedule Warble](https://warble.co)
- [Twint](https://github.com/twintproject/twint)
- [Twitwork](https://github.com/atmoner/TwitWork)
- [Twitter Account Profiler](https://www.sotwe.com/)
- [Twitter Account Profiler](https://twstalker.com/)
- [Twitter Archive](https://github.com/humandecoded/twayback)
- [History Twitter](https://memory.lol/app/)
- [Wayback Twitter](https://waybacktweets.streamlit.app/)
- [Twitter BOT](https://botometer.osome.iu.edu/)
- [Treverse](https://github.com/paulgb/Treeverse/blob/master/README.md?utm_content=buffer33d48&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer#readme)
- [Tweetbinder](https://www.tweetbinder.com/)
- [onemilliontweetmap](https://onemilliontweetmap.com/)
- [birdhunt](https://birdhunt.co/)

# Github 

- [Github search name](https://caius.github.io/github_id/)
- [Github Archive](https://www.gharchive.org/)
- [Github Dork](https://github.com/techgaun/github-dorks)
- [Fdupes](https://github.com/adrianlopezroche/fdupes)

# Snapchat 

- [Snapchat MAP](https://map.snapchat.com/)
- [Snapchat Map scrapping](https://github.com/nemec/snapchat-map-scraper)
- [SnapIntel](https://github.com/Kr0wZ/SnapIntel)

# Twitter Search Engines

- [tweetpaths](http://www.tweetpaths.com)
- [allmytweets](http://www.allmytweets.com)
- [Twimemachine](https://www.twimemachine.com)
- [inteltechniques](http://inteltechniques.com/osint/twitter.html)

# LinkedIn

Google queries for LinkedIn
> Public Profiles: site:linkedin.com inurl:pub
>  
> Updated Profiles: site:linkedin.com inurl:updates
>  
> Company Profiles: site:linkedin.com inurl:companies
>  

- [LinkedInDumper](https://github.com/l4rm4nd/LinkedInDumper)
- [Weakestlink](https://github.com/shellfarmer/WeakestLink)
- [GatherContacts](https://github.com/clr2of8/GatherContacts)
- [Rocket reach](https://rocketreach.co/person)
- [Phantom Buster](https://phantombuster.com/phantombuster)
- [reversecontact](https://www.reversecontact.com/)
- [Linkedin Search OSINT](https://cse.google.com/cse?cx=daaf18e804f81bed0)
- [Linkedin Overlay Remover](https://addons.mozilla.org/nl/firefox/addon/linkedin-overlay-remover/)

# MySpace

Google queries for MySpace

> Profiles: site: myspace.com inurl:profile
>  
> Blogs: site:myspace.com inurl:blogs
>  
> Videos: site:myspace.com inurl:vids
>  
> Jobs: site:myspace.com inurl:jobs
>  
> Videos: site:myspace.com ‘‘TARGET NAME’’ ‘‘videos’’
>  
> Comments: site:myspace.com ‘‘TARGET NAME’’ ‘‘comments’’
>  
> Friends: site:myspace.com ‘‘TARGET NAME’’ ‘‘friends’’
>  

# Tiktok

- [tiktok-hashtag-analysis](https://github.com/bellingcat/tiktok-hashtag-analysis)
- [tiktok-downloader](https://github.com/Gimenz/tiktok-downloader)
- [tiktok API](https://pypi.org/project/TikTokApi/)
- [tiktok date extract](https://bellingcat.github.io/tiktok-timestamp/)
- [Gimenz tiktok downloader](https://github.com/Gimenz/tiktok-downloader)

# Parler 

- [Parler Vidio Map](https://kylemcdonald.net/parler/map/)
- [Open Measures](https://public.openmeasures.io/)

# Monitoring & Alerting

- [Pastebin Alerts](http://pastebin.com/u/alerts)
- [HaveIBeenPwned](http://www.haveIbeenpwned.com)
- [Hudson Rock Cybercrime Intelligence Free Tools](https://www.hudsonrock.com/threat-intelligence-cybercrime-tools)
- [breachorclear](http://breachorclear.jesterscourt.cc)

# EXIF Analysis

- [regex](http://regex.info/exif.cgi)
- [FindExif](http://www.findexif.com)
- [metapicz](http://metapicz.com)
- [imageforensic](http://www.imageforensic.org)
- [metapicz](http://metapicz.com)
- [jimpl](https://jimpl.com/)
- [pic2map](https://www.pic2map.com/)
- [labs.tib.eu](https://labs.tib.eu/geoestimation/)
- [imago-forensics](https://github.com/redaelli/imago-forensics)
- [Renrot Exif](https://github.com/andy-shev/RenRot)
- [Geotag](https://vsudo.net/tools/geotag)
- [PhotOSINT Browser Extension](https://chrome.google.com/webstore/detail/photosint/gonhdjmkgfkokhkflfhkbiagbmoolhcd/related?hl=nl)
- [Python exif extractor](https://github.com/davidbombal/red-python-scripts/blob/main/exif.py)

# Documents

- [Metashield Analyzer](https://metashieldanalyzer.elevenpaths.com/)
- [foca](https://github.com/ElevenPaths/FOCA)
- [Psbdmp](https://psbdmp.ws/)
- [Find PDF Doc](http://www.findpdfdoc.com/)
- [Pdf analyzer](http://pdf-analyser.edpsciences.org/)
- [Tools pdf24](https://tools.pdf24.org/en/extract-images)
- [ArchivEye](https://github.com/eastrd/ArchivEye)
- [Fdupes](https://github.com/adrianlopezroche/fdupes)
- [kaseware search query](https://www.kaseware.com/search-query)

# Email Tracking

- [ip-adress](http://www.ip-adress.com/trace_email/)
- [whatismyipaddress](http://www.whatismyipaddress.com/trace-email)
- [hunter](https://hunter.io/)
- [email-checker](https://email-checker.net/)
- [verifyemailaddress](https://www.verifyemailaddress.org/)
- [SignalHire](https://www.signalhire.com/)
- [Holehe](https://github.com/megadose/holehe)
- [Holehe Maltego Transforms](https://github.com/megadose/holehe-maltego)
- [Spokeo](https://www.spokeo.com/email-search)
- [Mx Toolbox - Header Email](https://mxtoolbox.com/EmailHeaders.aspx)
- [getnotify](http://www.getnotify.com)
- [epieos](https://epieos.com/)
- [seon](https://seon.io/resources/the-ultimate-guide-to-free-email-lookup-and-reverse-email-lookup-tools/)
- [Eye](https://github.com/N0rz3/Eyes)
- [Thatsthem](https://thatsthem.com/)
- [Freepeoplesearch](https://freepeoplesearch.com/)
- [Headmail](https://github.com/umair9747/headmail)
- [Poastal](https://github.com/jakecreps/poastal)
- [anymailfinder](https://anymailfinder.com/)
- [getprospect](https://getprospect.com/)
- [Email Hippo](https://tools.emailhippo.com/)
- [Buster](https://github.com/sham00n/buster)
- [Gravatar Email Cheker](https://gravatar.com/site/check/)
- [EmailRep](https://emailrep.io/)
- [pwnedOrNot](https://github.com/thewhiteh4t/pwnedOrNot)
- [Email-Analytics](https://emailanalytics.com/email-headers/)
- [Email Header Analisis Toolbox](https://toolbox.googleapps.com/apps/messageheader/)
- [Sherlock Eye](https://sherlockeye.io/)
- [Ghunt](https://github.com/mxrch/GHunt)
- [Email Format](https://www.email-format.com/i/search/)
- [predictasearch](https://www.predictasearch.com/)

# Shodan Query Options

> https://pen-testing.sans.org/blog/2015/12/08/effective-shodan-searches
>  
> https://danielmiessler.com/study/shodan/#gs.VBVsyo0
>  

# Capturing Information

- [DownloadHelper](https://www.downloadhelper.net/)
Firefox plugin that will assist in downloading all media from a website
- [Exif Viewer](https://addons.mozilla.org/en-US/firefox/addon/exif-viewer/)
- [HTTrack](https://www.httrack.com/)
- [Wayback Machine](https://archive.org/web/)
- [cachedview](https://cachedview.com/)
- [url png](https://www.url2png.com/) 

# OSINT TOOLS

- [bbot](https://github.com/blacklanternsecurity/bbot)
- [Meta OSINT](https://metaosint.github.io/)
- [Shrelock](https://github.com/sherlock-project/sherlock)
- [Maltego](https://www.maltego.com/)
- [OSINT Framework](https://osintframework.com/)
- [Twint](https://forum.seccodeid.com/d/twint-twitter-intelligence-tool)
- [Telegram OSINT](https://forum.seccodeid.com/d/telegram-nearby-map)
- [Recon-Ng](https://github.com/lanmaster53/recon-ng)
- [tinfoleak](https://github.com/vaguileradiaz/tinfoleak)
- [maigret](https://github.com/soxoj/maigret)
- [mosint](https://github.com/alpkeskin/mosint)
- [osint_stuff_tool_collection](https://github.com/cipher387/osint_stuff_tool_collection)
- [instaloctrack](https://github.com/bernsteining/instaloctrack)
- [SpyScrap](https://github.com/RuthGnz/SpyScrap)
- [osintteye](https://github.com/rlyonheart/osinteye)
- [metagoofil](https://github.com/kurobeats/metagoofil)
- [Harvester](https://github.com/laramies/theHarvester)
- [Geo creepy](http://www.geocreepy.com/)
- [trape](https://github.com/jofpin/trape)
- [ReconDog](https://github.com/s0md3v/ReconDog)
- [iKy](https://github.com/kennbroorg/iKy)
- [Ghunt](https://github.com/mxrch/GHunt)
- [Moriarty-Project](https://github.com/AzizKpln/Moriarty-Project)
- [Mr.Holmes](https://github.com/Lucksi/Mr.Holmes)
- [octosuite Advanced Github OSINT Framework](https://github.com/rly0nheart/octosuite.git)  
- [Toutatis](https://github.com/megadose/toutatis)  
- [A tool for OSINT based threat hunting](https://github.com/ninoseki/mihari)
- [K𝚊𝚛𝚖𝚊 𝚟𝟸 is a Passive Open Source Intelligence](https://github.com/Dheerajmadhukar/karma_v2)  
- [Secure ELF parsing/loading library for forensics reconstruction of malware, and robust reverse engineering tools](https://github.com/elfmaster/libelfmaster)  
- [OSINT tool that allows you to find a person's accounts and emails + breached email](https://github.com/Greyjedix/Profil3r)  
- [A tool to search Aviation-related intelligence from public sources](https://github.com/n0skill/AVOSINT)
- [PoC OSINT Discord user and guild information harvester](https://github.com/V3ntus/darvester)  
- [Automate downloading archived deleted Tweets](https://github.com/Mennaruuk/twayback)
- [Discover the location of nearby Telegram users](https://github.com/tejado/telegram-nearby-map)
- [OSINT Tool on Twitter and Instagram](https://github.com/xadhrit/terra)  
- [The World's simplest facial recognition api for python and the command line](https://github.com/ageitgey/face_recognition)
- [Automation and automation of digital forensic tools](https://github.com/google/turbinia)  
- [E4GL30S1NT](https://github.com/C0MPL3XDEV/E4GL30S1NT)
- [Commit stream finding Github repositories by extracting commit](https://github.com/x1sec/commit-stream)
- [SingleFile copy of an entire web page in a single HTML file](https://github.com/gildas-lormeau/SingleFile)
- [Photon Incredibly fast crawler designed for OSINT](https://github.com/s0md3v/Photon)
- [infoooze](https://github.com/devXprite/infoooze)
- [Eye](https://github.com/N0rz3/Eyes)
- [More](https://forum.seccodeid.com/?q=osint)

# OSINT Online Tool  

- [Echosec](https://www.echosec.net/)
- [Foller](https://foller.me/)
- [Tweet Deck](https://tweetdeck.twitter.com/)
- [Tweet Trips](https://www.tweetedtrips.com/)
- [Tweet Tonomy](http://www.twitonomy.com/)
- [Twinangulate](https://www.twiangulate.com/search/)
- [Geosocial](http://geosocialfootprint.com/)
- [Hash tracking](https://www.hashtracking.com/)
- [Socmint tool](http://socmint.tools/)
- [Spyse](https://spyse.com/)
- [OSINT Combine](https://www.osintcombine.com/tools)
- [Cell Id Lookup](https://www.reskrim.com/cek.php)
- [Device Info](https://www.deviceinfo.me/)
- [Cell Finder](https://cellidfinder.com/)
- [GRABIFY IP](https://grabify.link/)
- [Cek Rekening](https://cekrekening.id/home)
- [Thatsthem](https://thatsthem.com/)
- [IntelligenceX](https://intelx.io/tools)

# Telegram Tool

Search channel, username anymore

- [Telegago](https://cse.google.com/cse?cx=006368593537057042503:efxu7xprihg#gsc.tab=0)
- [TelegramDB](http://www.telegramdb.org/)
- [Telegram Search Engine](https://xtea.io/)
- [Telegram Database: channels, groups and users](https://t.me/s/privatelinks)
- [Telegram channels and groups catalog](https://tgstat.com/)
- [Telegago](https://cse.google.com/)
- [Social Finder](https://socialfinder.app/list/Telegram)
- [Lyzem Search](https://lyzem.com/)
- [Discover The Best Telegram Channels](https://telegramchannels.me/)
- [Tele Channel Overiview](https://telemetr.io/)
- [Telepathy](https://github.com/proseltd/Telepathy)
- [Telemetr](https://telemetr.io/)
- [Telegramtrac](https://github.com/claromes/telegramtrac)
- [TGDev](https://tgdev.io/)
- [IntelX Telegram](https://intelx.io/tools?tab=telegram)
- [Tele Geo Int](https://github.com/Alb-310/Geogramint)
- [Tele Phone Number Checker - Bellingcat](https://github.com/bellingcat/telegram-phone-number-checker)
- [Telegram Geogramint](https://github.com/Alb-310/Geogramint)
- [Telegram-Trilateration](https://github.com/jkctech/Telegram-Trilateration)
- [TeleTracker by Tsale](https://github.com/tsale/TeleTracker)

# Document and Slides Search

- [Authorstream](http://www.authorstream.com)
- [Find-pdf-doc](http://www.findpdfdoc.com)
- [Free Full PDF](http://www.freefullpdf.com)
- [PDF Search Engine](http://www.pdfsearchengine.info)
- [RECAP](http://archive.recapthelaw.org)
- [SlideShare](http://www.slideshare.net)
- [Scribd](http://www.scribd.com)
- [soPDF.com](http://www.sopdf.com)
- [FileChef](https://www.filechef.com/)
- [File Search Engine](https://www.filesearch.link/)
- [FilePursuit](https://filepursuit.com/)
- [NAPALM FTP Indexer](https://www.searchftps.net/)
- [Cryptome](https://cryptome.org/)
- [Finda PDF](https://www.findapdf.com/)
- [Find PDF Doc](http://www.findpdfdoc.com/)
- [Pdf analyzer](http://pdf-analyser.edpsciences.org/)
- [Tools pdf24](https://tools.pdf24.org/en/extract-images)
- [ArchivEye](https://github.com/eastrd/ArchivEye)

# Real-Time Search, Social Media Search, and General Social Media Tools

- [Buffer](https://buffer.com)
- [Hashtatit](http://www.hashatit.com)
- [Rival IQ](https://www.rivaliq.com)
- [SocialBakers](http://www.socialbakers.com)
- [SociaBlade](http://socialblade.com)
- [Social Searcher](http://www.social-searcher.com)
- [Mail.Ru Social Network Search](https://go.mail.ru/search_social)
- [WATools](https://watools.io/)
- [Profil3r](https://github.com/Rog3rSm1th/Profil3r)
- [Oblivion](https://github.com/loseys/Oblivion)
- [Social Analyzer](https://github.com/qeeqbox/social-analyzer)
- [Snsscrape](https://github.com/JustAnotherArchivist/snscrape)
- [stratosphere](https://github.com/elehcimd/stratosphere)
- [OSINT compass](https://osint-compass-portal.onrender.com/)
- [Sherlock Eye](https://sherlockeye.io/)
- [ShadowDragon](https://shadowdragon.io/)
- [sociallinks](https://sociallinks.io/)
- [Crimewall](https://sociallinks.io/products/sl-crimewall)

# Image Search

- [7Photos](http://7photos.net)
- [Baidu Images](http://image.baidu.com)
- [Bing Images](http://www.bing.com/images)
- [Clarify](http://clarify.io)
- [Flickr](https://secure.flickr.com)
- [GoodSearch Image Search](http://www.goodsearch.com/search-image)
- [Google Image](https://images.google.com)
- [Image Identification Project](https://www.imageidentify.com)
- [MyPicsMap](http://www.mypicsmap.com)
- [PhotoBucket](http://photobucket.com)
- [Picsearch](http://www.picsearch.com)
- [PicTriev](http://www.pictriev.com)
- [StolenCameraFinder](http://www.stolencamerafinder.co.uk)
- [TinEye](https://tineye.com) - Reverse image search engine.
- [Worldcam](http://www.worldc.am)
- [Yahoo Image Search](https://images.search.yahoo.com)
- [Yandex Images](https://www.yandex.com/images)
- [Betaface](https://www.betaface.com/demo.html)
- [Search4faces](https://search4faces.com/)
- [Pimeyes](https://pimeyes.com/en)
- [Reminiai](https://remini.ai/)
- [Search4face](https://search4faces.com/en/)
- [Vkfacewatch](https://vk.watch/)
- [Facecheck](https://facecheck.id/)
- [Findmyclone](https://www.findmyclone.com/)
- [Face++](https://www.faceplusplus.com/)
- [AWS-Recon](https://aws.amazon.com/rekognition/)
- [Azure vidio indexer](https://vi.microsoft.com/en-us)
- [Webcams](https://github.com/pbkompasz/webcams)
- [Mever](https://mever.iti.gr/forensics/)
- [InVID Verification](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/)
- [Google Lens](https://lens.google.com/)
- [Robots Verify](https://www.robots.ox.ac.uk/~vgg/software/vff/)
- [Amazon Face Recon](https://aws.amazon.com/getting-started/hands-on/detect-analyze-compare-faces-rekognition/)
- [VGG Image Search Engine (VISE)](https://robots.ox.ac.uk/~vgg/software/vise/)
- [Fake face detector](https://seintpl.github.io/AmIReal/)
- [Telegram Face Match Bot](https://t.me/facematch_bot)
- [berify](https://berify.com/)
- [shutterstock](https://www.shutterstock.com/royalty-free/reverse-image-search-for-video)

# Image Analysis

- [ExifTool](https://exiftool.org/)
- [Exif Search](http://www.exif-search.com)
- [FotoForensics](http://www.fotoforensics.com)
- [Gbimg.org](http://gbimg.org)
- [Ghiro](http://www.getghiro.org)
- [ImpulseAdventure](http://www.impulseadventure.com/photo/jpeg-snoop.html)
- [Jeffreys Image Metadata Viewer](http://exif.regex.info/)
- [JPEGsnoop](https://sourceforge.net/projects/jpegsnoop)
- [Metapicz](http://metapicz.com/)
- [Forensically](https://29a.ch/photo-forensics/)
- [DiffChecker](https://www.diffchecker.com/image-diff/)
- [ImgOps](https://imgops.com/)
- [Pimeyes](https://pimeyes.com/en)
- [Reminiai](https://remini.ai/)
- [Search4face](https://search4faces.com/en/)
- [Vkfacewatch](https://vk.watch/)
- [Facecheck](https://facecheck.id/)
- [Findmyclone](https://www.findmyclone.com/)
- [Face++](https://www.faceplusplus.com/)
- [AWS-Recon](https://aws.amazon.com/rekognition/)
- [Image Analyzer](https://www.maltego.com/transform-hub/image-analyzer/)
- [Pelock](https://www.pelock.com/products/steganography-online-codec)
- [OCR Image](https://www.newocr.com/)
- [labs.tib.eu](https://labs.tib.eu/geoestimation/)
- [Webcams](https://github.com/pbkompasz/webcams)
- [imago-forensics](https://github.com/redaelli/imago-forensics)
- [Face recon](https://github.com/ageitgey/face_recognition)
- [Cleanup pictures](https://cleanup.pictures/)
- [Mever](https://mever.iti.gr/forensics/)
- [InVID Verification](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/)
- [Google Lens](https://lens.google.com/)
- [Exif Purge](https://www.exifpurge.com/)
- [VGG Image Classification](https://www.robots.ox.ac.uk/~vgg/software/vic/)
- [VGG Image Search Engine (VISE)](https://robots.ox.ac.uk/~vgg/software/vise/)
- [Fake face detector](https://seintpl.github.io/AmIReal/)
- [GeoSpy](https://geospy.web.app/)
- [DiffChecker](https://www.diffchecker.com/image-diff/)
- [ImgOps](https://imgops.com/)
- [Telegram Face Match Bot](https://t.me/facematch_bot)
- [picarta](https://picarta.ai/)
- [huggingface](https://huggingface.co/)
- [ID KTP OCR](https://github.com/fauzantaqiyuddin/fastapi-ocr-ktp)
- [Python exif extractor](https://github.com/davidbombal/red-python-scripts/blob/main/exif.py)

# Stock Images

- [AlltheFreeStock](http://allthefreestock.com)
- [Death to Stock](http://deathtothestockphoto.com)
- [Freeimages](http://www.freeimages.com)
- [Freestocks.org](http://freestocks.org)
- [Gratisography](http://www.gratisography.com)
- [IM Free](http://www.imcreator.com/free)
- [ISO Republic](http://isorepublic.com)
- [iStockphoto](http://www.istockphoto.com)
- [Kaboompics](http://kaboompics.com)
- [LibreStock](https://librestock.com)
- [Life of Pix](http://www.lifeofpix.com)
- [NegativeSpace](http://negativespace.co)
- [New Old Stock](http://nos.twnsnd.co)
- [Pixabay](https://pixabay.com)
- [Pexels](https://www.pexels.com)
- [Stocksnap](https://stocksnap.io)
- [Shutterstock](http://www.shutterstock.com)
- [tookapic](https://stock.tookapic.com)
- [Unsplash](https://unsplash.com)
- [Pimeyes](https://pimeyes.com/en)

# Video Search and Other Video Tools

- [Aol Videos](http://on.aol.com)
- [Bing Videos](http://www.bing.com/?scope=video)
- [Blinkx](http://www.blinkx.com)
- [Clarify](http://clarify.io)
- [Clip Blast](http://www.clipblast.com)
- [DailyMotion](http://www.dailymotion.com)
- [Deturl](http://deturl.com)
- [DownloadHealper](http://www.downloadhelper.net)
- [Earthcam](http://www.earthcam.com)
- [Insecam](http://insecam.org/)
- [Frame by Frame](https://chrome.google.com/webstore/detail/frame-by-frame/cclnaabdfgnehogonpeddbgejclcjneh/)
Browser plugin that allows you to watch YouTube videos frame by frame.
- [Geosearch](http://www.geosearchtool.com)
- [Internet Archive: Open Source Videos](https://archive.org/details/opensource_movies)
- [LiveLeak](http://www.liveleak.com)
- [Metacafe](http://www.metacafe.com)
- [Metatube](http://www.metatube.com)
- [Montage](https://montage.storyful.com)
- [Veoh](http://www.veoh.com)
- [Vimeo](https://vimeo.com)
- [Voxalead](http://voxalead.labs.exalead.com)
- [Yahoo Video Search](http://video.search.yahoo.com)
- [YouTube](https://www.youtube.com)
- [YouTube Data Viewer](https://www.amnestyusa.org/citizenevidence)
- [ccSUBS](http://ccsubs.com/) Download Closed Captions & Subtitles from YouTube
- [YouTube Metadata](https://mattw.io/youtube-metadata/)
- [YouTube Geofind](https://mattw.io/youtube-geofind/)
- [Video Stabilization Methods](https://github.com/yaochih/awesome-video-stabilization)
- [Azure vidio indexer](https://vi.microsoft.com/en-us)
- [Bilibili scraper](https://github.com/yixiangyin/bilibili-scraper)
- [Webcams](https://github.com/pbkompasz/webcams)
- [Kamerka](https://github.com/woj-ciech/Kamerka-GUI)
- [airportwebcams](https://airportwebcams.net/)
- [airportwebcams](https://airportwebcams.net/)
- [Earthcam](https://www.earthcam.com/#google_vignette)
- [tvway](http://tvway.ru/)
- [unscreen](https://www.unscreen.com/)
- [shutterstock](https://www.shutterstock.com/royalty-free/reverse-image-search-for-video)

# Geospatial Research and Mapping Tools

- [Atlasify](http://www.atlasify.com)
- [Batchgeo](http://batchgeo.com)
- [Bing Maps](http://www.bing.com/maps)
- [CartoDB](https://cartodb.com)
- [Colorbrewer](http://colorbrewer2.org)
- [CrowdMap](https://crowdmap.com)
- [Dominoc925](https://dominoc925-pages.appspot.com/mapplets/cs_mgrs.html)
- [DualMaps](https://www.mapchannels.com/dualmaps7/map.htm)
- [GeoGig](http://geogig.org)
- [GeoNames](http://www.geonames.org)
- [Esri](http://www.esri.com)
- [Flash Earth](http://www.flashearth.com)
- [Google Earth](http://www.google.com/earth)
- [Google Earth Pro](https://www.google.com/intl/en/earth/versions/#earth-pro)
- [Google Maps](https://www.google.com/maps)
- [Google Maps Streetview Player](http://brianfolts.com/driver)
- [Google My Maps](https://www.google.com/maps/about/mymaps)
- [GPSVisualizer](http://www.gpsvisualizer.com)
- [GrassGIS](http://grass.osgeo.org)
- [Here](http://here.com)
- [Hyperlapse](https://github.com/TeehanLax/Hyperlapse.js)
- [Inspire Geoportal](http://inspire-geoportal.ec.europa.eu)
- [InstantAtlas](http://www.instantatlas.com)
- [Instant Google Street View](http://www.instantstreetview.com)
- [Kartograph](http://kartograph.org)
- [Leaflet](http://leafletjs.com)
- [MapAList](http://mapalist.com)
- [MapBox](https://www.mapbox.com)
- [Mapbuildr](https://mapbuildr.com)
- [Mapchart.net](https://mapchart.net)
- [Maperitive](http://maperitive.net)
- [MapHub](https://maphub.net)
- [MapJam](http://mapjam.com)
- [Mapline](https://mapline.com)
- [Map Maker](https://maps.co)
- [Mapquest](https://www.mapquest.com)
- [Modest Maps](http://modestmaps.com)
- [NGA GEOINT](https://github.com/ngageoint)
- [OpenLayers](http://openlayers.org)
- [Polymaps](http://polymaps.org)
- [Perry Castaneda Library](https://www.lib.utexas.edu/maps)
- [Open Street Map](http://www.openstreetmap.org)
- [QGIS](http://qgis.org)
- [QuickMaps](https://chrome.google.com/webstore/detail/quick-maps/bgbojmobaekecckmomemopckmeipecij)
- [Scribble Maps](http://scribblemaps.com)
- [Terrapattern](http://www.terrapattern.com)
- [Tableau](http://www.tableausoftware.com)
- [Timescape](https://www.timescape.io)
- [View in Google Earth](http://www.mgmaps.com/kml/#view)
- [Wikimapia](http://wikimapia.org)
- [World Aeronautical Database](http://worldaerodata.com)
- [WorldMap Harvard](http://worldmap.harvard.edu)
- [ViaMichelin](http://www.viamichelin.com)
- [Yahoo Maps](https://maps.yahoo.com)
- [Zeemaps](https://www.zeemaps.com)
- [Sentinel Hub](https://www.sentinel-hub.com/explore/sentinelplayground/)
- [Maxar](https://discover.digitalglobe.com/)
- [USGS (EarthExplorer)](https://earthexplorer.usgs.gov/)
- [Zoom Earth](https://zoom.earth/)
- [Remote Pixel](https://remotepixel.ca/projects/index.html)
- [SunCalc](https://www.suncalc.org/)
- [ArcGIS](https://livingatlas.arcgis.com/en/browse/)
- [Pic2Map](https://www.pic2map.com/)
- [Mapillary](https://www.mapillary.com/app/)
- [KartaView](https://kartaview.org/map/)
- [Satellites Pro](https://satellites.pro/)
- [Liveuamap](https://liveuamap.com/)
- [Descartes Labs](https://maps.descarteslabs.com/)
- [Baidu Maps](https://map.baidu.com/)
- [MapChecking](https://www.mapchecking.com/)
- [Windy](https://www.windy.com/)
- [SOAR](https://soar.earth/)
- [digiKam](https://www.digikam.org/)
- [geoq](https://github.com/ngageoint/geoq)
- [gvision](https://github.com/GONZOsint/gvision)
- [OSM Bellingcat](https://osm-search.bellingcat.com/)
- [labs.tib.eu](https://labs.tib.eu/geoestimation/)
- [sketchmapper](https://sketchmapper.cellgrid.co/)
- [github sketchmapper](https://github.com/mlkin/sketchmapper)
- [byt-georagging](https://github.com/Yachay-AI/byt5-geotagging)
- [CSIS maps](https://amti.csis.org/maps/)
- [Humdata maps](https://data.humdata.org/group)
- [Planet - satellite maps](https://www.planet.com/products/)
- [OSM Finder](https://github.com/Xetnus/osm-finder)
- [OSM Finder - Web based](https://osm-finder.netlify.app/)
- [Wayback Geospatial](https://livingatlas.arcgis.com/wayback)
- [Twitter Geo](http://geosocialfootprint.com/)
- [Insta Geo](https://github.com/bellingcat/instagram-location-search)
- [NASA EARTH](https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms)
- [EARTH DATA NASA](https://wvs.earthdata.nasa.gov/)
- [peakvisor](https://peakvisor.com/)
- [peakfinder](https://www.peakfinder.com/) 
- [Calc Map Coordinate](https://www.calcmaps.com/map-coordinates/)
- [Latlong Calc](https://www.latlong.net/)
- [Gps Visualizer](https://www.gpsvisualizer.com/calculators)
- [Iq Air](https://www.iqair.com/id/)
- [NASA Earth Data](https://search.earthdata.nasa.gov/search)
- [NASA World View](https://worldview.earthdata.nasa.gov/)
- [Earth Exploer](https://earthexplorer.usgs.gov/)
- [Sky Watch Earth Cache](https://skywatch.com/earthcache/)
- [Sentinel Hub](https://www.sentinel-hub.com/)
- [Skylens](https://app.skylens.io/)
- [Geocreepy](https://www.geocreepy.com/)
- [garmin](https://www.garmin.co.id/products/outdoor/gpsmap64s-sea/)
- [Corona Atlsa](https://corona.cast.uark.edu/)
- [BMKG RI](https://www.bmkg.go.id/)
- [GIS INA](https://tanahair.indonesia.go.id/portal-web/)
- [Kpler](https://www.kpler.com/)
- [wanderlog review on Google maps](https://wanderlog.com/)
- [planet](https://www.planet.com/)
- [NBR Map](https://map.nbr.org/interactivemap/)
- [geohints](https://geohints.com/)
- [geotips](https://geotips.net/)
- [shademap](https://shademap.app/)
- [shadowmap](https://shadowmap.org/)
- [livingatlas wayback](https://livingatlas.arcgis.com/wayback)
- [livingatlas wayback Guide](https://www.esri.com/arcgis-blog/products/arcgis-living-atlas/mapping/use-world-imagery-wayback/)
- [supermapol](https://www.supermapol.com/)
- [supermapol docs](https://doc.supermapol.com/en/Introduction/Introduction.html)
- [gpsjam](https://gpsjam.org/)
- [freemaptools](https://www.freemaptools.com/)
- [bbbike](https://mc.bbbike.org/mc/)
- [geojson](https://geojson.io/)
- [mooncalc](https://www.mooncalc.org/)
- [moon timeanddate](https://www.timeanddate.com/)
- [urbanaccessregulations](https://urbanaccessregulations.eu/userhome/map)
- [mapsm](https://mapsm.com/)
- [picarta](https://picarta.ai/)
- [Kaseware Geospatial](https://www.kaseware.com/geospatial-analysis-software)

# Nearby Map From Geospatial

- [foursquare](https://location.foursquare.com/)
- [tripadvisor](https://www.tripadvisor.com/)
- [booking](booking.com)
- [agoda](agoda.com)
- [wanderlog review on Google maps](https://wanderlog.com/)

# Fact Checking

- [About Urban Legends](http://urbanlegends.about.com)
- [Captin Fact](https://captainfact.io/)
- [Check](https://meedan.com/check)
- [Citizen Desk](https://www.sourcefabric.org/en/citizendesk)
- [Emergent](http://www.emergent.info)
- [Fact Check](http://www.factcheck.org)
- [Full Fact](https://fullfact.org)
- [MediaBugs](http://mediabugs.org)
- [Snopes](http://www.snopes.com)
The definitive Internet reference source for urban legends, folklore, myths, rumors, and misinformation.
- [Verification Handbook](http://verificationhandbook.com)
- [Verification Junkie](http://verificationjunkie.com)
- [Verily](https://veri.ly)
- [Google Fact](https://toolbox.google.com/factcheck/explorer)
- [Open Measures](https://openmeasures.io/)
- [Hoaxy](https://hoaxy.osome.iu.edu/)
- [FEAT](https://github.com/GONZOsint/FEAT)

# Server Information Gathering

- [Testssl](https://testssl.sh/)
- [Nesus](https://www.tenable.com/products/nessus)
- [securitytrails](https://securitytrails.com/)
- [SSL Scan](https://www.kali.org/tools/sslscan/)

# CTF Analysis & Exploit

- [Cybercheff](https://gchq.github.io/CyberChef/) The Cyber Swiss Army Knife - a web app for encryption, encoding, compression and data analysis
- [Bettercap](https://github.com/bettercap/bettercap)
Framework to perform MITM (Man in the Middle) attacks.
- [Yersinia](https://github.com/tomac/yersinia)
A framework for layer 2 attacks
- [FeatherDuster](https://github.com/nccgroup/featherduster)
An automated, modular cryptanalysis tool
- [Hash Extender](https://github.com/iagox86/hash_extender)
A utility tool for performing hash length extension attacks
- [Hashcat](https://hashcat.net/hashcat/)
Password cracking
- [DLLInjector ](https://github.com/OpenSecurityResearch/dllinjector)
Inject dlls in processes
- [Metasploit](https://www.metasploit.com/)
Penetration testing software and exploit
- [Pwntools](https://github.com/Gallopsled/pwntools)
CTF framework and exploit development library
- [ROPgadget](https://github.com/JonathanSalwan/ROPgadget)
Framework for ROP exploitation
- [Exiftool](https://exiftool.org/)
Read, write and edit file metadata
- [Malzilla](https://malzilla.sourceforge.net/downloads.html)
Malware hunting tool
- [Zmap](https://zmap.io/)
An open-source network scanner.
- [Nmap](https://nmap.org/)
Net mapping and port scanner
- [Wireshark](https://www.wireshark.org/)
Analyze the network dumps
- [Apktool](https://ibotpeaches.github.io/Apktool/)
Android Decompiler
- [Ninja Binary](https://binary.ninja/)
Binary analysis framework
- [Binwalk](https://github.com/ReFirmLabs/binwalk)
Analyze, reverse engineer, and extract firmware images
- [GDB](https://www.sourceware.org/gdb/)
The GNU project debugger
- [GEF](https://github.com/hugsy/gef)
Advanced debugging capabilities for exploit devs & reverse engineers on Linux
- [IDA](https://www.hex-rays.com/ida-pro/)
Most used Reversing software
- [PEDA](https://github.com/longld/peda)
Python Exploit Development Assistance for GDB
- [Radare2](https://github.com/radareorg/radare2)
UNIX-like reverse engineering framework and command-line toolset
- [Windbg](http://www.windbg.org/)
Windows debugger distributed by Microsoft
- [Boomerang](https://github.com/BoomerangDecompiler/boomerang)
Decompile x86 binaries to C
- [Detox](http://relentless-coding.org/projects/jsdetox/install)
A Javascript malware analysis tool
- [SmartDeblur](https://github.com/Y-Vladimir/SmartDeblur)
Restoration of defocused and blurred photos/images
- [HitPaw](https://online.hitpaw.com/online-photo-enhancer.html?linksource=header)
Enhance image, video and media quality with AI is free and paid
- [ImageMagick](http://www.imagemagick.org/script/index.php)
Tool for manipulating images
- [Exiv2](https://exiv2.org/manpage.html)
Image metadata manipulation tool
- [Stegbreak](https://linux.die.net/man/1/stegbreak)
Launches brute-force dictionary attacks on JPG image
- [Steghide](https://steghide.sourceforge.net/)
Hide data in various kind of images
- [Stegsolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)
Apply various steganography techniques to images
- [SearchSploit](https://www.exploit-db.com/searchsploit)
Command line search tool for Exploit-DB
- [Exploitalert](https://www.exploitalert.com/browse-exploit.html)
List exploiting and vuln
- [Lollabs](https://lolbas-project.github.io/)
Windows exploiting
- [GtfoBins](https://gtfobins.github.io/)
Linux exploiting
- [Hacktricks](https://book.hacktricks.xyz/welcome/readme)
List exploit and vuln cheat sheet walkthrough
- [Payload all the things](https://github.com/swisskyrepo/PayloadsAllTheThings)
Example and payload injection
- [All about bug bounty](https://github.com/daffainfo/AllAboutBugBounty)
Bypasses, payloads, Reconnaissance and etc
- [Bug Bounty](https://github.com/Yudha-ard/Bug-Bounty) Tips bug bounty reconnaissance
- [DnsSpy](https://github.com/dnSpy/dnSpy)
Desktop NET debugger and assembly editor

# Zero Day

- [0day](https://0day.today/)
- [Zerodium](https://zerodium.com/)
- [0day fans](https://0dayfans.com/)

# Cryptocurrency Investigation

- [Blockchain](https://www.blockchain.com/)
- [Flashpoint](https://flashpoint.io/resources/research/flashpoint-and-chainalysis-investigate-hydra-where-cryptocurrency-cybercrime-goes-dark/)
- [Intel471](https://intel471.com/)
- [Tatum](https://tatum.io/)
- [Ciphertrace](https://ciphertrace.com/)
- [Bitcoin Abuse](https://www.bitcoinabuse.com/)
- [GraphSense](https://github.com/INTERPOL-Innovation-Centre/GraphSense-Maltego-transform)
- [Blockhain Explorer](https://www.blockexplorer.com/l/en-US/)
- [blockcypher](https://live.blockcypher.com/)
- [BTC Scan](https://btcscan.org/)
- [TON of privacy](https://github.com/aaarghhh/a_TON_of_privacy)
- [OXT](https://oxt.me/)
- [etherscan](https://etherscan.io/)
- [Maltego Transform ShadowDragon](https://www.maltego.com/transform-hub/socialnet/)
- [Maltego Social Links Pro](https://www.maltego.com/transform-hub/social-links-pro/)
- [trackenn](https://github.com/kennbroorg/trackenn?tab=readme-ov-file)

# Cell Investigation

- [Opencellid](https://opencellid.org/)
- [CellTower Locator - Cell2gps](http://www.cell2gps.com/)
- [Cell-id Query](https://www.cell-id.info/?lang=en)
- [Location API](unwiredlabs)
- [Cell Mapping](https://www.cellmapper.net/)
- [Global Internet Infrastructure Map](https://www.infrapedia.com/)
- [Spy Dialer](https://spydialer.com/)
- [Phone Validator](https://www.phonevalidator.com/)
- [Free Operator Search](https://freecarrierlookup.com/)
- [HLR Lookup](https://www.hlrlookup.com/)
- [Ceebydith HLR Lookup](https://ceebydith.com/cek-hlr-lokasi-hp.html)
- [Free HLR](https://www.free-hlr.com/)
- [HLR Lookup API](https://www.hlr-lookups.com/)
- [Maltego Phone Search](https://www.maltego.com/transform-hub/phonesearch/)
- [Emobiletracker](https://www.emobiletracker.com/)
- [Phone Validator](https://www.phonevalidator.com/index.aspx)
- [Reverse Phone](https://www.reversephonecheck.com/)
- [Reverse Phone Lookup](https://www.reversephonelookup.com/)
- [OpenCNAM](https://docs.maltego.com/support/solutions/articles/15000045282-maltego-opencnam-transforms)
- [Search Country Operator (IMSI)](https://www.heicard.com/en/operator.html)
- [Analysis of IMSI numbers](https://www.numberingplans.com/?page=analysis&sub=imsinr)
- [World MCC & MNC Code](https://en.wikipedia.org/wiki/Mobile_country_code)
- [World MCC & MNC Code 2](https://www.mcc-mnc.com/)
- [World Mobile Network Code](https://en.wikipedia.org/wiki/Mobile_network_codes_in_ITU_region_5xx_(Oceania))
- [World Network Coverage](https://www.nperf.com/en/map/ID/-/-/signal/?ll=-2.5678942164342513&lg=118.01999999999998&zoom=5)
- [Profone GSM Tracker](https://cellphonetrackers.org/gsm/gsm-tracker.php)
- [Thatsthem](https://thatsthem.com/)
- [Freepeoplesearch](https://freepeoplesearch.com/)
- [IMSI imei info](https://www.imei.info/imsi/)
- [cellebrite](https://cellebrite.com/en/ufed/)
- [LIST MCC & MNC World](https://docs.routee.net/docs/list-of-mccmnc-codes)
- [Cell Global Identity World](https://en.wikipedia.org/wiki/Cell_Global_Identity)
- [MCC MNC World Net](https://mcc-mnc.net/)
- [Cell Global Identity Article](https://medium.com/@fthcknmz/cell-global-identity-cgi-407ea0288943)
- [GSM Cell ID](https://en.wikipedia.org/wiki/GSM_Cell_ID)
- [predictasearch](https://www.predictasearch.com/)

# IMEI Investigation

- [SNDeepinfo](https://sndeep.info/)
- [Imei Numbers](http://imei-number.com/)
- [Nobbi](http://www.nobbi.com/)
- [IMEI Info](https://www.imei.info/)
- [International Numberingplans](https://www.numberingplans.com/)
- [IPhone IMEI](https://iunlocker.com/en/check_imei.php)

# Chat Apps Investigation

WhatsApp

- [Analyze your WhatsApp Chat](https://whatsanalyze-80665.web.app/)
- [Chat Visualizer](https://chatvisualizer.com/)
- [WhatsApp Group Links](https://whatsgrouplink.com/)
- [Download WhatsApp Profile Picture](https://watools.io/download-profile-picture)
- [WhatsApp Group Links 2](https://whatsappgroup.info/)
- [Wa tools](https://watools.io/)
- [whatsanalyze](https://whatsanalyze.com/)
- [chatvisualizer](https://chatvisualizer.com/)
- [WaGpScraper](https://github.com/riz4d/WaGpScraper)

Telegram

- [TelegramDB](http://www.telegramdb.org/)
- [Telegram Search Engine](https://xtea.io/)
- [Telegram Database: channels, groups and users](https://t.me/s/privatelinks)
- [Telegram channels and groups catalog](https://tgstat.com/)
- [Telegago](https://cse.google.com/)
- [Social Finder](https://socialfinder.app/list/Telegram)
- [Lyzem Search](https://lyzem.com/)
- [Discover The Best Telegram Channels](https://telegramchannels.me/)
- [Tele Channel Overiview](https://telemetr.io/)
- [Telegramtrac](https://github.com/claromes/telegramtrac)
- [TGDev](https://tgdev.io/)
- [Telegram Geogramint](https://github.com/Alb-310/Geogramint)
- [Telegram-Trilateration](https://github.com/jkctech/Telegram-Trilateration)
- [TeleTracker by Tsale](https://github.com/tsale/TeleTracker)

# Build Sockpuppet Accounts

Build your sockpuppet account and proctect your privacy

- [Roop Image face swap from AI](https://github.com/s0md3v/roop)
- [Thispersondoesnotexist](https://www.thispersondoesnotexist.com/)
- [Protonmail](https://protonmail.com/)
- [Nordvpn](https://nordvpn.com/)
- [NOX](https://www.bignox.com/)
- [Browser Extension](https://nordvpn.com/blog/use-these-browser-extensions-for-your-privacy/)
- [Burner Phone Number](https://www.mintmobile.com/)
- [Phone Burner](https://www.phoneburner.com/)
- [Hushed](https://hushed.com/)
- [Temp Phone Number](https://temporary-phone-number.com/)
- [Temp Phone Number and SMS activate](https://sms-activate.org/en)
- [Temp Mail 1](https://mail.tm/en/)
- [Temp Mail 2](https://temp-mail.org/en/)
- [Temp Mail 3](https://tempmailo.com/)
- [Cryptocurrency Payment Monero](https://www.getmonero.org/)
- [Cryptocurrency Payment Bitcoin](https://bitcoin.org/en/)
- [Openpgp](https://www.openpgp.org/)
- [Operating System](https://tails.boum.org/)
- [Zmail](https://zmail.sourceforge.net/)
- [Open DNS](https://www.opendns.com/home-internet-security/)
- [I2P](https://geti2p.net/en/)
- [TOR](https://www.torproject.org/download/)
- [Apple Kuncitara](https://support.apple.com/id-id/guide/iphone/iph049680987/ios)
- [AI Vidio Maker](https://www.synthesia.io/free-ai-video-demo#OptimizedForSharing_New)
- [deepfakesweb](https://deepfakesweb.com/)
- [DeepFaceLive](https://github.com/iperov/DeepFaceLive)
- [fakeinfo](https://fakeinfo.net/)
- [Online SMS](https://online-sms.org/)

Social Network and blogging

- Wordpress
- Blogger
- Medium  
- Facebook
- Instagram
- Linkedin 

# Enhance Image Quality

- [Letsenhance](https://letsenhance.io/)
- [Cutout](https://www.cutout.pro/photo-enhancer-sharpener-upscaler)
- [Upscale](https://upscalepics.com/)
- [Canva](https://www.canva.com/features/image-enhancer/)
- [Adobe](https://www.adobe.com/express/feature/image/enhance)
- [Picwish](https://picwish.com/unblur-image-portrait)
- [Fotor](https://www.fotor.com/features/unblur-image/)
- [SIUN](https://github.com/minyuanye/SIUN)
- [DPED](https://github.com/aiff22/DPED)
- [neural-enhance](https://dockship.io/model/neural-enhance/5de4333901afe15d4ec10393)
- [neural-enhance](https://github.com/alexjc/neural-enhance)
- [Reminiai](https://remini.ai/)
- [Depix](https://github.com/beurtschipper/Depix)
- [Realesrgan](https://replicate.com/xinntao/realesrgan)  
- [HitPaw](https://online.hitpaw.com/online-photo-enhancer.html?linksource=header)
- [Cleanup Pictures](https://cleanup.pictures/)
- [Gfpgan](https://replicate.com/tencentarc/gfpgan)
- [Realesrgan Playground](https://real-esrgan.com/#Playground)
- [waifu2x](https://waifu2x.org/)
- [imglarger](https://imglarger.com/Anime16K)
- [imageupscaler](https://imageupscaler.com/deblurring/)

# Locations Data Mapping

- [Google maps](https://www.google.co.id/maps)
- [Social geo lens](https://www.osintcombine.com/social-geo-lens)
- [Open street map](https://www.openstreetmap.org/)
- [Google Maps Geocoding](https://www.maltego.com/transform-hub/google-maps-geocoding-transforms/)
- [Googleearthengine](https://earthengine.google.com/#intro)
- [OSM Bellingcat](https://osm-search.bellingcat.com/)
- [byt5-geotagging](https://github.com/Yachay-AI/byt5-geotagging)
- [CSIS maps](https://amti.csis.org/maps/)
- [Humdata maps](https://data.humdata.org/group)
- [Planet - satellite maps](https://www.planet.com/products/)
- [OSM Finder](https://github.com/Xetnus/osm-finder)
- [OSM Finder - Web based](https://osm-finder.netlify.app/)
- [wanderlog review on Google maps](https://wanderlog.com/)

# Discord Server Search  

- [Discord servers](https://discordservers.com/)
- [Discover servers](https://disboard.org/)
- [Discord history tracker](https://www.dht.chylex.com/)  
- [Darvester](https://github.com/darvester/darvester)
- [Discord Leaks](https://discordleaks.unicornriot.ninja/discord/server/)

# Darkweb Intelligence

- [Stealthmole](https://www.stealthmole.com/products/darkweb-tracker)
- [Darkweb bookmarks](https://www.osintcombine.com/dw-osint-bookmarks)
- [Maltego digital shadows transform](https://www.maltego.com/transform-hub/digital-shadows/)
- [Maltego cybersixgill transform](https://www.maltego.com/transform-hub/cybersixgill/)
- [Doge Darknet Osint Graph Explorer](https://github.com/pielco11/DOGE)
- [Maltego social links professional transform](https://www.maltego.com/transform-hub/social-links-pro/)
- [TorBot](https://github.com/DedSecInside/TorBot)
- [Darkfeed](https://darkfeed.io/)
- [Flare](https://flare.io/)
- [pryingdeep](https://github.com/iudicium/pryingdeep)
- [Maltego](https://www.maltego.com/)
- [Darknet Book](https://github.com/darknet-book/tor-guide)
- [Onios Scan](https://github.com/s-rah/onionscan)
- [Cyber Int Darkweb Intel Platform](https://cyberint.com/platform/threat-intelligence/)
- [SOC Radar Darkweb Int Monitoring](https://socradar.io/products/dark-web-monitoring/)
- [I2P Download](https://geti2p.net/en/)
- [zerofox](https://www.zerofox.com/platform/)
- [ShadowDragon](https://shadowdragon.io/)
- [sociallinks](https://sociallinks.io/)
- [Crimewall](https://sociallinks.io/products/sl-crimewall)

# Digital Forensics

- [Yggdrasil](https://github.com/Jarl-Bjoern/Yggdrasil/)
- [MISP](https://www.misp-project.org/)
- [Maltego](https://www.maltego.com/)
- [Filesec](https://filesec.io/)
- [Logstash kibana](https://www.elastic.co/logstash/)
- [Kibana](https://www.elastic.co/kibana/)
- [Extundelete Ext3 or ext4 partition recovery](https://extundelete.sourceforge.net/)
- [TestDisk](https://www.cgsecurity.org/wiki/TestDisk_Download)
- [VirusTotal](https://www.virustotal.com/gui/home/upload)
- [Avilla Forensics](https://forum.seccodeid.com/d/avillaforensics-mobile-digital-forensics)
- [Autopsy](https://www.autopsy.com/)
- [Recuva](https://www.ccleaner.com/recuva)
- [Magnetforensics](https://www.magnetforensics.com/free-tools/)
- [Opentxt](https://www.opentext.com/products/security-cloud)
- [Ntfstool Forensics](https://forum.seccodeid.com/d/ntfstool-forensics-tool-for-ntfs-parser-mft-bitlocker-deleted-files)
- [Sleuthkit](https://www.sleuthkit.org/sleuthkit/)
- [SIFT SANS](https://www.sans.org/tools/sift-workstation/)
- [SIFT CLI](https://github.com/teamdfir/sift-cli/releases/tag/v1.8.5)
- [HYAS Insight](https://www.maltego.com/transform-hub/hyas-insight/)
- [imago-forensics](https://github.com/redaelli/imago-forensics)
- [SimpleImager](https://github.com/QXJ6YW4/SimpleImager)
- [Processhacker](https://processhacker.sourceforge.io/)
- [Koodous](https://koodous.com/)
- [Nirsoft Bwowsing History](https://www.nirsoft.net/utils/browsing_history_view.html)
- [dfrlab.org](https://dfrlab.org/research/)
- [atlanticcouncil](https://www.atlanticcouncil.org/)
- [Mever](https://mever.iti.gr/forensics/)
- [cellebrite](https://cellebrite.com/en/ufed/)
- [MOBSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) 
- [RMS - Mobile Pentest](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) 
- [APK Leaks](https://github.com/dwisiswant0/apkleaks)
- [forensictools](https://github.com/cristianzsh/forensictools)
- [VolWeb](https://github.com/k1nd0ne/VolWeb)
- [C2-Tracker](https://github.com/montysecurity/C2-Tracker)
- [Wanna Browser Sandbox](https://www.wannabrowser.net/)
- [pestudio](https://www.winitor.com/download)
- [procmon](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [IoC Editor](https://fireeye.market/apps/S7cWpi9W)
- [Gfobins](https://gtfobins.github.io/)
- [Lolbas](https://lolbas-project.github.io/)
- [Loonbins](https://www.loobins.io/tactics/collection/)
- [sociallinks](https://sociallinks.io/) 

# Write Your Investigation

- [Yoga](https://github.com/WebBreacher/yoga)
- [Malteo CaseFile](https://docs.maltego.com/support/solutions/articles/15000018948-what-is-maltego-casefile-)

# Securing Your Privacy

- [Eraser](https://eraser.heidi.ie/)
- [Thunderbird](https://www.thunderbird.net/en-US/)
- [Ublock origin](https://github.com/gorhill/uBlock)
- [Zmail](https://zmail.sourceforge.net/)
- [Open DNS](https://www.opendns.com/home-internet-security/)
- [I2P](https://geti2p.net/en/)
- [Gnupg](https://gnupg.org/)
- [HTTPS Everywhere](https://www.eff.org/https-everywhere/)
- [Pelock](https://www.pelock.com/products/steganography-online-codec)
- [Tails OS](https://tails.boum.org/)
- [WOT](https://www.mywot.com/)
- [Temp Mail 1](https://mail.tm/en/)
- [Temp Mail 2](https://temp-mail.org/en/)
- [Temp Mail 3](https://tempmailo.com/)
- [Phone Burner](https://www.phoneburner.com/)
- [Hushed](https://hushed.com/)
- [Privacy Badger](https://privacybadger.org/)
- [Blur IMG Extension](https://chromewebstore.google.com/detail/blur-the-image-and-video/aikjogmpaoaookmacnkbenekcnkjlkmi?hl=en-US&authuser=0)
- [Apple Kuncitara](https://support.apple.com/id-id/guide/iphone/iph049680987/ios)
- [Apple Focus Mode](https://support.apple.com/id-id/guide/iphone/iphd6288a67f/17.0/ios/17.0)

Payment

- [Bitcoin](https://bitcoin.org/id/)
- [Monero](https://www.getmonero.org/)

Password Manager

- [Keepas](https://keepass.info/)
- [Dashlane](https://www.dashlane.com/)
- [Nordpass](https://nordpass.com/)
- [Securing your email](https://cybernews.com/secure-email-providers/find-all-accounts-linked-to-email-address/)

# Fraud Checker

- [Cek Rekening](https://cekrekening.id/home) - Indonesian By Kominfo
- [Kredibel](https://www.kredibel.com/) - Indonesian
- [Verihub](https://verihubs.com/) - Indonesian
- [Scamadviser](https://www.maltego.com/transform-hub/scamadviser/)
- [Ipqualityscore](https://docs.maltego.com/support/solutions/articles/15000041408-maltego-ipqualityscore-transforms#overview-0-0)
- [OpenCNAM](https://docs.maltego.com/support/solutions/articles/15000045282-maltego-opencnam-transforms)
- [Fullcontact](https://www.fullcontact.com/)
- [Spam Calls](https://spamcalls.net/en/)
- [Maltego Transform ShadowDragon](https://www.maltego.com/transform-hub/socialnet/)
- [Crimewall](https://sociallinks.io/products/sl-crimewall)

# Content Removal & Strict Media Content

Search people missing and abuse, strict content, removing, takedown and minimize your data on the internet

- [Google image removal](https://support.google.com/websearch/answer/4628134)
Remove your image from Google
- [Stopncii](https://stopncii.org)
Free tool designed to support victims of Non-Consensual Intimate Image (NCII) abuse
- [Bing content removal](www.bing.com/webmasters/tools/contentremoval)
Chech the detail on [here](https://www.bing.com/webmasters/help/bing-content-removal-tool-cb6c294d)
- [Google content removal](https://search.google.com/search-console/remove-outdated-content)
Check the detail on [here](https://support.google.com/websearch/troubleshooter/3111061?hl=id)
- [Web archiver remover](https://help.archive.org/help/how-do-i-request-to-remove-something-from-archive-org/)
Check the detail [here](https://help.archive.org/help/removing-your-item-pages-from-archive-org/) and [here](https://www.joshualowcock.com/guide/how-to-delete-your-site-from-the-internet-archive-wayback-machine-archive-org/) view detail on [Help web archive](https://help.archive.org/)
- [Facebook Privacy](https://www.facebook.com/help/124518907626945)
Strict and disable bot crawl search engine index account
- [zerofox](https://www.zerofox.com/) From threat intelligence to brand and domain protection to rapid response DISRUPTION & TAKEDOWNS
- [Instagram Privacy](https://help.instagram.com/147542625391305)
Strict and disable bot crawl search engine index account
- [Missing Kids](https://www.missingkids.org/gethelpnow/isyourexplicitcontentoutthere) Remove nudes or sexually-exploitive images or videos taken when you were a child out there on the internet
- [Takeit Down](https://takeitdown.ncmec.org/) Help remove online nude, partially nude
- [Inhope](https://www.inhope.org/EN#hotlineReferral) Report suspected child sexual abuse images or videos
- [ReportIWF Indonesia](https://report.iwf.org.uk/id) Proctect and remove sexualy, nudes on internet
- [ReportIWF](https://www.iwf.org.uk/our-technology/report-remove/) Proctect and remove sexualy, nudes on internet
- [kemenpppa Indonesia](https://www.kemenpppa.go.id/) Kementrian perlindungan anak dan perempuan
- [National Center for Missing and Exploited Children](https://report.cybertip.org/) Report the content to the appropriate authorities around the world
- [Inhope](https://inhope.org/) Find your country listed, contact INHOPE abuse internet  
- [cybertip US](https://report.cybertip.org/) National Center for Missing and Exploited Children
- [cybertip Canada](https://www.cybertip.ca/en/) National Center for Missing and Exploited Children
- [internethotline Japan](https://www.internethotline.jp/)  Internet Hotline Center Japan
- [safekaznet Kazakhstan](http://www.safekaznet.kz/en/report-2) Internet Association of Kazakhstan
- [Liga Internet Russia](https://ligainternet.ru/hotline/) Safe Internet League
- [Kocs Korean](https://www.kocsc.or.kr/mainPage.do) Korea Communication Standards Commission
- [Thailand Internet Hotline](https://www.thaihotline.org/) Internet Foundation for the Development of Thailand
- [Jugendschutz Germany](https://www.jugendschutz.net/) Internet Foundation Germany
- [FSM Germany](https://www.fsm.de/) Internet Foundation Germany
- [ECO Germany](https://www.internet-beschwerdestelle.de/de/index.html) Internet Foundation Germany
- [NCOSE](https://endsexualexploitation.org/about/) National Center on Sexual Exploitation (NCOSE) exists because people should be free to live and love without sexual abuse and exploitation.
- [More info all region](https://support.google.com/websearch/answer/148666?hl=id) Check available internet hotline around world 
- [411](https://www.whitepages.com/suppression-requests) Request for remove your data from this site
- [411 Info](https://411.info/manage/) Request for remove your data from this site
- [Absolute People Search](https://absolutepeoplesearch.com/optout) Request for remove your data from this site
- [Acxiom](https://isapps.acxiom.com/optout/optout.aspx) Request for remove your data from this site
- [Addresses](https://www.intelius.com/opt-out/submit/) Request for remove your data from this site
- [Address Search](https://addresssearch.com/remove-info.php) Request for remove your data from this site
- [Archives](https://archives.com/optout) Request for remove your data from this site
- [Apollo](https://www.apollo.io/privacy-policy/remove/) Request for remove your data from this site
- [Arivify](https://www.arivify.com/removal) Request for remove your data from this site
- [Azerch](https://www.azerch.com/Policies/Privacy) Request for remove your data from this site
- [Background Alert](https://www.backgroundalert.com/optout/) Request for remove your data from this site
- [Background Check](https://backgroundcheck.run/ng/control/privacy) Request for remove your data from this site
- [Background Checkers](https://www.backgroundcheckers.net/optOut/name/landing) Request for remove your data from this site
- [BatchSkipTracing](https://batchskiptracing.com/personal-information) Request for remove your data from this site
- [BatchLeads](https://batchleads.io/personal-information) Request for remove your data from this site
- [BatchDialer](https://batchdialer.com/personal-information) Request for remove your data from this site
- [BatchDriven](https://batchdriven.com/personal) Request for remove your data from this site
- [Been Verified](https://www.beenverified.com/faq/opt-out/) Request for remove your data from this site
- [Buzzfile](http://www.buzzfile.com/Company/Remove) Request for remove your data from this site
- [Call Truth](https://www.calltruth.com/opt_out.php) Request for remove your data from this site
- [Caller Smart](https://www.callersmart.com/opt-out) Request for remove your data from this site
- [Centeda](https://centeda.com/ng/control/privacy) Request for remove your data from this site
- [Check People](https://www.checkpeople.com/opt-out) Request for remove your data from this site
- [Check Secrets](https://www.checksecrets.com/optOut/name/landing) Request for remove your data from this site
- [Checkr](https://candidate.checkr.com/privacy/delete) Request for remove your data from this site
- [City-Data](https://www.city-data.com/privacy-form.php?w=usget) Request for remove your data from this site
- [ClickSearch](https://clicksearch.us/optout) Request for remove your data from this site
- [Clustr Maps](https://clustrmaps.com/bl/opt-out) Request for remove your data from this site
- [Complete Investigation Services](http://www.cisworldwide.com/search/index.php?xpath=lp_optout) Request for remove your data from this site
- [Confidential Phone Lookup](https://www.confidentialphonelookup.com) Request for remove your data from this site
- [Contact Out](https://contactout.com/optout) Request for remove your data from this site
- [Connected Investors](https://connectedinvestors.com/content/do-not-sell) Request for remove your data from this site
- [Corporation Wiki](https://www.corporationwiki.com/profiles/public) Request for remove your data from this site
- [Councilon](https://councilon.com/ex/control/privacy) Request for remove your data from this site
- [Cyber Background Checks](https://www.cyberbackgroundchecks.com/removal) Request for remove your data from this site
- [Data Axle](https://www.data-axle.com/do-not-sell-my-data/) Request for remove your data from this site
- [DataVeria](https://dataveria.com/ng/control/privacy) Request for remove your data from this site
- [DataChk](https://www.datacheckinc.com/contact/) Request for remove your data from this site
- [Dehashed](https://dehashed.com/) Request for remove your data from this site
- [DelvePoint](https://www.delvepoint.com) Request for remove your data from this site
- [DexKnows](https://tinyurl.com/dexknowscom) Request for remove your data from this site
- [DirectMail](https://www.directmail.com/mail_preference/) Request for remove your data from this site
- [DMA Choice](https://www.ims-dm.com/cgi/dncc.php) | [DMA Choice](https://www.ims-dm.com/cgi/optoutemps.php) Request for remove your data from this site
- [Epsilon-Main](https://www.epsilon.com/privacy-policy/) Request for remove your data from this site
- [Epsilon-Abacus](https://www.epsilon.com/privacy-policy/) Request for remove your data from this site
- [Epsilon-CFD](https://www.epsilon.com/privacy-policy/) Request for remove your data from this site
- [Epsilon-Shopper](https://www.epsilon.com/privacy-policy/) Request for remove your data from this site
- [Fama](https://fama.io/privacy/) Request for remove your data from this site
- [FamilySearch](https://familysearch.org/privacy) Request for remove your data from this site
- [Family Tree Now](https://www.familytreenow.com/optout) Request for remove your data from this site
- [Fast People Fast](https://findpeoplefast.net/company/remove-my-info) Request for remove your data from this site
- [Fast People Search](https://www.fastpeoplesearch.com/removal) Request for remove your data from this site
- [Fax VIN](https://www.faxvin.com/company/privacy) Request for remove your data from this site
- [Find People Search](https://findpeoplesearch.com/customerservice/) Request for remove your data from this site
- [Free Background Checks](https://www.infopay.com/privacy) Request for remove your data from this site
- [Free People Directory](https://www.freepeopledirectory.com/optout) Request for remove your data from this site
- [Free Phone Tracer](https://www.beenverified.com/app/optout/search) Request for remove your data from this site
- [Free Public Profile](https://www.freepublicprofile.com/Removal) Request for remove your data from this site
- [FindRec](https://findrec.com/ng/control/privacy) Request for remove your data from this site
- [Glad I Know](https://gladiknow.com/opt-out) Request for remove your data from this site
- [GoLookup](https://golookup.com/support/optout) Request for remove your data from this site
- [Grey Pages](https://www.grey-pages.com/removal) Request for remove your data from this site
- [Haines & Company](https://www.haines.com/privacy-policy/) Request for remove your data from this site
- [Hometry](https://homemetry.com/control/privacy) Request for remove your data from this site
- [HPCC-USA](https://www.hpcc-usa.org/research/change-listing.html) Request for remove your data from this site
- [ID Crawl](https://www.idcrawl.com/opt-out) Request for remove your data from this site
- [ID True](https://www.idtrue.com/optout/) Request for remove your data from this site
- [Infopay](mailto:privacy@infopay.com) Request for remove your data from this site
- [Infospace](https://infospace.intelius.com/optout.php) Request for remove your data from this site
- [Infotracer](https://infotracer.com/optout) Request for remove your data from this site
- [Infotracer UK](https://infotracer.com/optout/) Request for remove your data from this site
- [Instant Check Mate](https://instantcheckmate.com/optout) Request for remove your data from this site
- [InstantPeopleFinder](https://www.intelius.com/opt-out) Request for remove your data from this site
- [Intelius](https://www.intelius.com/opt-out) Request for remove your data from this site
- [IntelligenceX](https://intelx.io/abuse) Request for remove your data from this site
- [IRBSearch](mailto:customercare@irbsearch.com) Request for remove your data from this site
- [Kiwi Searches](https://kiwisearches.com/optout) Request for remove your data from this site
- [LexisNexis/Accurint](https://optout.lexisnexis.com) Request for remove your data from this site
- [LexisNexis Direct Marketing](https://www.lexisnexis.com/privacy/directmarketingopt-out.aspx) Request for remove your data from this site
- [Locate Family](https://www.locatefamily.com/removal2.html) Request for remove your data from this site
- [Locate People](https://www.locatepeople.org/optout) Request for remove your data from this site
- [MashPanel](https://www.mashpanel.com/remove.php) Request for remove your data from this site
- [Mastercard](https://www.mastercard.us/en-us/vision/corp-responsibility/commitment-to-privacy/privacy/data-analytics-opt-out.html) Request for remove your data from this site
- [Mastercard](https://www.mastercard.us/en-us/vision/corp-responsibility/commitment-to-privacy/privacy/email-opt-out.html) Request for remove your data from this site
- [MugshotLook](https://www.mugshotlook.com/optOut/name/landing) Request for remove your data from this site
- [MyHeritage](https://faq.myheritage.com/en/article/how-do-i-delete-my-account-on-myheritage) Request for remove your data from this site
- [MyLife](https://www.mylife.com/ccpa/index.pubview) Request for remove your data from this site
- [National Cellular Directory](https://www.nationalcellulardirectory.com/optout/) Request for remove your data from this site
- [Neighbor Report](https://neighbor.report/remove) Request for remove your data from this site
- [NewEnglandFacts](https://newenglandfacts.com/ng/control/privacy) Request for remove your data from this site
- [Number Guru](https://www.beenverified.com/app/optout/search) Request for remove your data from this site
- [Numberville](https://numberville.com/opt-out.html) Request for remove your data from this site
- [Nuwber](https://nuwber.com/removal/link) Request for remove your data from this site
- [Official USA](https://www.officialusa.com/opt-out) Request for remove your data from this site
- [Old Friends](https://old-friends.co/) Request for remove your data from this site
- [Ownerly](https://www.beenverified.com/app/optout/search) Request for remove your data from this site
- [PeekYou](https://www.peekyou.com/about/contact/optout/) Request for remove your data from this site
- [Peep Lookup](https://www.peeplookup.com/opt_out) Request for remove your data from this site
- [PeopleBackgroundCheck](https://people-background-check.com/ng/control/privacy) Request for remove your data from this site
- [People By Name](https://www.peoplebyname.com/remove.php) Request for remove your data from this site
- [People By Phone](https://www.peoplebyphone.com/remove-my-number/) Request for remove your data from this site
- [People Data Labs](https://www.peopledatalabs.com/opt-out-form) Request for remove your data from this site
- [People Finder](https://peoplefinder.com/optout.php) Request for remove your data from this site
- [People Finders](https://www.peoplefinders.com/opt-out#IT) Request for remove your data from this site
- [People Looker](https://www.peoplelooker.com/f/optout/search) Request for remove your data from this site
- [People Search 123](https://www.peoplesearch123.com/optOut/name/landing) Request for remove your data from this site
- [People Search Expert](https://www.peoplesearchexpert.com) Request for remove your data from this site
- [People Finder](https://peoplefinder.com/optout.php) Request for remove your data from this site
- [People Finders](https://www.peoplefinders.com/opt-out#IT) Request for remove your data from this site
- [People Looker](https://www.peoplelooker.com/f/optout/search) Request for remove your data from this site
- [People Search 123](https://www.peoplesearch123.com/optOut/name/landing) Request for remove your data from this site
- [People Search Now](https://www.peoplesearchnow.com/opt-out) Request for remove your data from this site
- [People Searcher](https://www.peoplesearcher.com/optOut/name/landing) Request for remove your data from this site
- [People Smart](https://www.peoplesmart.com/app/optout/search) Request for remove your data from this site
- [People Trace UK](https://www.peopletraceuk.com/RequestRecordRemoval.asp) Request for remove your data from this site
- [People’s Check](https://www.peoplescheck.com/optout/) Request for remove your data from this site
- [People Whiz](https://www.peoplewhiz.com/remove-my-info) Request for remove your data from this site
- [Phonebook BT](https://www.productsandservices.bt.com/consumer/edw/privacypolicy/copyform/bt/#/) Request for remove your data from this site
- [Pub360](https://pub360.com/ng/control/privacy) Request for remove your data from this site
- [Public Data Digger](https://publicdatadigger.com/removeprofile) Request for remove your data from this site
- [Public Data USA](https://publicdatausa.com/optout.php) Request for remove your data from this site
- [Public Info Services](https://www.publicinfoservices.com/help-center/remove-my-public-record) Request for remove your data from this site
- [Public Records](https://publicrecords.directory/contact.php) Request for remove your data from this site
- [Public Records Now](https://www.publicrecordsnow.com/static/view/optout/) Request for remove your data from this site
- [Quick People Trace](https://www.peoplefinders.com/opt-out#IT) Request for remove your data from this site
- [Radaris](https://radaris.com/control/privacy) Request for remove your data from this site
- [Reveal Name](https://www.revealname.com/opt_out) Request for remove your data from this site
- [Reveal Phone Owner](https://www.revealphoneowner.com/data-removal) Request for remove your data from this site
- [Sales Spider](http://salespidermedia.com/opt-out-and-information-removal.php) Request for remove your data from this site
- [Search Bug](https://www.searchbug.com/peoplefinder/how-to-remove.aspx) Request for remove your data from this site
- [Search People Free](https://www.searchpeoplefree.com/opt-out) Request for remove your data from this site
- [Selfie Systems](https://www.spokeo.com/optout) Request for remove your data from this site
- [Smart Background Checks](https://www.smartbackgroundchecks.com/optout) Request for remove your data from this site
- [Social Catfish](https://socialcatfish.com/opt-out/) Request for remove your data from this site
- [Spy Dialer](https://www.spydialer.com/optout.aspx) Request for remove your data from this site
- [Spokeo](https://www.spokeo.com/optout) Request for remove your data from this site
- [SpyFly](https://www.spyfly.com/help-center/remove-info) Request for remove your data from this site
- [Spytox](https://www.spytox.com/opt_out) Request for remove your data from this site
- [State Records](https://infotracer.com/optout/) Request for remove your data from this site
- [Super Pages](https://tinyurl.com/dexknowscom) Request for remove your data from this site
- [Sync Me](https://sync.me/optout/) Request for remove your data from this site
- [Telephone Directories](https://www.telephonedirectories.us/Edit_Records) Request for remove your data from this site
- [Tenn Help](https://www.tennhelp.com/public-resources/change-listing.html) Request for remove your data from this site
- [That’s Them](https://thatsthem.com/optout) Request for remove your data from this sitef
- [The Real Yellow Pages](https://tinyurl.com/dexknowscom) Request for remove your data from this site
- [Thomson Reuters/Westlaw/CLEAR](https://privacyportal-cdn.onetrust.com/dsarwebform/dbf5ae8a-0a6a-4f4b-b527-7f94d0de6bbc/5dc91c0f-f1b7-4b6e-9d42-76043adaf72d.html) Request for remove your data from this site
- [TLO](https://service.transunion.com/dss/ccpa_optout.page) Request for remove your data from this site
- [Tower Data](https://dashboard.towerdata.com/optout/) Request for remove your data from this site
- [True Caller](https://www.truecaller.com/unlisting) Request for remove your data from this site
- [True People Search](https://www.truepeoplesearch.com/removal) Request for remove your data from this site
- [True People Search.net](https://truepeoplesearch.net/remove-my-info) Request for remove your data from this site
- [Truth Finder](https://www.truthfinder.com/opt-out/) Request for remove your data from this site
- [United States Phonebook](http://www.unitedstatesphonebook.com/contact.php) Request for remove your data from this site
- [Unmask](https://unmask.com/opt-out) Request for remove your data from this site
- [USA People Search](https://www.usa-people-search.com/manage/) Request for remove your data from this site
- [US Phone Pro](https://www.usphonepro.com/opt_out) Request for remove your data from this site
- [US Phonebook](https://www.usphonebook.com/opt-out) Request for remove your data from this site
- [USA Trace](https://www.peoplefinders.com/opt-out#IT) Request for remove your data from this site
- [US Search](https://www.ussearch.com/opt-out/submit/) Request for remove your data from this site
- [Valassis](https://valassis.com/do-not-sell-my-personal-information/) Request for remove your data from this site
- [Valpak/Cox](https://www.valpak.com/coupons/show/mailinglistsuppression) Request for remove your data from this site
- [Verecor](https://findrec.com/page/privacy) Request for remove your data from this site
- [Vericora](https://vericora.com/ng/control/privacy) Request for remove your data from this site
- [Veriforia](https://veriforia.com/ng/control/privacy) Request for remove your data from this site
- [Veripages](https://veripages.com/page/contact) Request for remove your data from this site
- [Verispy](https://www.dataaccessmanagement.com/verispy/) Request for remove your data from this site
- [Veritora](https://federal-data.com/control/profile?url=) Request for remove your data from this site
- [Visa](https://marketingreportoptout.visa.com/OPTOUT/request.do) Request for remove your data from this site
- [Voter Records](https://voterrecords.com/faq) Request for remove your data from this site
- [White Pages](http://www.whitepages.com/suppression_requests) Request for remove your data from this site
- [WYTY](https://www.wyty.com/remove/) Request for remove your data from this site
- [XLEK](https://www.xlek.com/optout.php) Request for remove your data from this site
- [Yellow Book](https://www.beenverified.com/app/optout/search) Request for remove your data from this site
- [Yellow Pages](https://tinyurl.com/dexknowscom) Request for remove your data from this site
- [ZoomInfo](https://www.zoominfo.com/about-zoominfo/privacy-manage-profile) Request for remove your data from this site
- [Get Contact Unlisting](https://getcontact.com/en/manage) Request for remove your data from this site

*NB : Please read carefully and check the ToS or privacy statment. Its taking to long, you need to patiently. For this point, your data is not guaranteed to be lost 100% on the internet, but this is to minimize the spread of your data and data breaches

# Vehicle OSINT

- [licenseplatemania](https://licenseplatemania.com/)
- [platesmania](https://platesmania.com/uk/search?&lang=en)
- [findbyplate](https://findbyplate.com/)
- [google image](https://www.google.com/imghp?hl=en)
- [Wiki Routes](https://wikiroutes.info/en/padang)
- [Carnet](https://carnet.ai/)
- [ID number plate](https://auto2000.co.id/berita-dan-tips/plat-nomor-seluruh-indonesia)
- [ID number wikipedia](https://id.wikipedia.org/wiki/Tanda_Nomor_Kendaraan_Bermotor_Indonesia)
- [World Car Brand Wikipedia](https://en.wikipedia.org/wiki/List_of_car_brands)
- [carlogos](https://www.carlogos.org/car-brands/)
- [commercialtrucktrader](https://www.commercialtrucktrader.com/)
- [License Plate AI Recognition](https://github.com/winter2897/Real-time-Auto-License-Plate-Recognition-with-Jetson-Nano)
- [vehicleregistrationapi](https://www.vehicleregistrationapi.com/)
- [vehiclehistory](https://www.vehiclehistory.com/license-plate-search)
- [faxvin](https://www.faxvin.com/license-plate-lookup)
- [worldlicenseplates](http://www.worldlicenseplates.com/)
- [autotraveler](https://autotraveler.ru/en/spravka/vehicle-registration-codes-in-the-world.html#.Y3R6BnbMJPY)
- [cipher387](https://cipher387.github.io/venicle_number_search_toolbox/)
- [inteltechniques](https://inteltechniques.com/tools/Vehicle.html)
- [avtocod](https://avtocod.ru/)
- [dmvcivls.gov](https://dmvcivls-wselfservice.ct.gov/Registration/VerifyRegistration)
- [etimspayments](https://prodpci.etimspayments.com/pbw/include/dc_parking/input.jsp?ticketType=P)

VIN Checker 

- [faxvin](https://www.faxvin.com/)
- [vehiclehistory](https://www.vehiclehistory.com/)
- [vindecoderz](https://www.vindecoderz.com/)
- [fordvinlookup](https://www.fordvinlookup.com/)
- [chevroletforum](https://chevroletforum.com/forum/vindecoder.php)
- [hyundaiforum](https://www.hyundaiforum.com/forum/vindecoder.php)
- [nissanusa](https://www.nissanusa.com/recalls-vin.html)
- [cadillacforum](https://www.cadillacforum.com/forum/vindecoder.php)
- [dodgeforum](https://dodgeforum.com/forum/vindecoder.php)
- [toyota](https://www.toyota.com/owners/my-vehicle/vehicle-specification.html)
- [audiworld](https://www.audiworld.com/forums/vindecoder.php)
- [vinpit](https://vinpit.com/vin-decoder/yamaha)
- [scionlife](https://www.scionlife.com/forums/vindecoder.php)
- [nhtsa](https://www.nhtsa.gov/vin-decoder)
- [bigrigvin](https://bigrigvin.com/)
- [cartell Japan](https://www.cartell.ie/japanese-import/)
- [carvx JP](https://carvx.jp/)
- [cyclevin](https://cyclevin.com/)

# Aircraft Tracking

- [flightradar24](https://www.flightradar24.com/)
- [flightaware](https://www.flightaware.com/)
- [planefinder](https://planefinder.net/)
- [flightaware](https://www.flightaware.com/live/)
- [radarbox](https://www.radarbox.com/)
- [adsbexchange](https://globe.adsbexchange.com/)
- [Planefinder](https://planefinder.net/)
- [Live ATC](https://www.liveatc.net/)
- [planespotters](https://www.planespotters.net/)
- [globe plane](https://globe.adsbexchange.com/)
- [theaviationist](https://theaviationist.com/)
- [airrecognition](https://airrecognition.com/index.php)
- [gpsjam](https://gpsjam.org/)

# Ship Tracking

- [shiptracker](https://shiptracker.live/)
- [marinetraffic](https://www.marinetraffic.com/)
- [vesselfinder](https://www.vesselfinder.com/)
- [gisis](https://gisis.imo.org/Public/Default.aspx)
- [WindWard](https://windward.ai/)
- [Kpler](https://www.kpler.com/)
- [Container tracking](http://container-tracking.org/)
- [marineteacher](https://www.marineteacher.com/)

# Railways

- [Open Railways](https://wiki.openstreetmap.org/wiki/OpenRailwayMap)
- [Train Tracker](https://mobility.portal.geops.io/world.geops.transit?lang=en&layers=strassennamen,haltekanten,haltestellen,pois,world.geops.traviclive&x=810000&y=5900000&z=5.5)
- [Yandex Train Map](https://rasp.yandex.ru/map/trains/)
- [KAI ID](https://penumpang.kai.id/daop)
- [KAI ID Map Railway](https://www.arcgis.com/apps/View/index.html?appid=27b7119dc6754d3e9e584a4fa71e5744)
- [World Railway Train](https://mobility.portal.geops.io/world.geops.transit?layers=paerke,strassennamen,haltekanten,haltestellen,pois,world.geops.traviclive&x=12003263.13&y=-842145.41&z=7.98)
- [Railway zugfinder](https://www.zugfinder.net/)

# GPT OSINT 

- [Gpt osint](https://github.com/gigz/gpt-osint)

# OSINT for Red Team 

- [Phishious](https://github.com/CanIPhish/Phishious) 
Secure Email Gateway (SEG) for phishing email header (escape detection)
- [Operative framework](https://github.com/gaulliath/operative-framework/releases/tag/2.0a) investigation OSINT framework, you can interact with multiple targets
- [Mod Login](https://github.com/clong/ModLogin) Credentials reuse
- [Cr3dOv3r](https://github.com/D4Vinci/Cr3dOv3r) Credential reuse
- [Crackmapexec](https://www.kali.org/tools/crackmapexec/) Password Spray 
- [Datasploit](https://github.com/datasploit/datasploit) OSINT Framework to perform various recon techniques on Companies, People, Phone Number, Bitcoin Addresses, etc
- [CloudFail](https://github.com/m0rtem/CloudFail) DNS and old database records to find hidden IP's behind the CloudFlare network
- [cloudgazer](https://github.com/Aidennnn33/cloudgazer) Find Real IPs hidden behind Cloudflare with Criminal IP(criminalip.io), security OSINT Tool
- [Rustcan](https://github.com/RustScan/RustScan) Port scanner 
- [NMAP](https://nmap.org/) Port scanner 
- [Getrails](https://pypi.org/project/getrails/) Dork hacking that work with Google, Duckduckgo and Torch
- [OWASP Maryam](https://owasp.org/www-project-maryam/) open-source framework based on OSINT and data gathering
- [Metabigor](https://github.com/j3ssie/metabigor?tab=readme-ov-file)  Intelligence tool, its goal is to do OSINT tasks and more but without any API key
- [OSINT BBOT](https://github.com/blacklanternsecurity/bbot) A recursive internet scanner for hackers.
- [Spiderfoot](https://github.com/smicallef/spiderfoot) A Scrapping web tool 
- [Zeus-Scanner](https://github.com/Ekultek/Zeus-Scanner) A web scanner 
- [Zenrows](https://www.zenrows.com/) Bypassing captcha and WAF 
- [Scrapfly](https://scrapfly.io/) Bypassing captcha and WAF 
- [capsolver](https://www.capsolver.com/id) Bypassing captcha and WAF 
- [2captcha](https://2captcha.com/) Bypassing captcha and WAF 
- [Puppeter](https://www.npmjs.com/package/puppeteer-extra-plugin-stealth) For web scrapper and info gath 
- [MOBSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) Mobile Pentest Tool 
- [RMS - Mobile Pentest](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) Mobile Pentest Tool 
- [Mortar](https://github.com/0xsp-SRD/mortar) Mortar evasion technique to defeat and divert detection and prevention of security products (AV/EDR/XDR)
- [APK Leaks](https://github.com/dwisiswant0/apkleaks) Decompile APK and find the sensitive info
- [Web copilot](https://github.com/h4r5h1t/webcopilot) An automation tool that enumerates subdomains then filters out xss, sqli, open redirect, lfi, ssrf and rce parameters
- [Nuclei template js template](https://github.com/ayadim/Nuclei-bug-hunter/blob/main/file/web/js/js-analyse.yaml) Nuclei template. Extract Data From JS ffile e.g key, endpoint, etc 
- [Atlas Sql Tamper Suggester](https://github.com/m4ll0k/Atlas) Open source tool that can suggest sqlmap tampers to bypass WAF/IDS/IPS, the tool is based on returned status code
- [Go Phish](https://getgophish.com/) Gophish is a powerful, open-source phishing framework that makes it easy to test your organization's exposure to phishing.
- [Advanced SQL Injection](https://github.com/kleiton0x00/Advanced-SQL-Injection-Cheatsheet) A cheat sheet that contains advanced queries for SQL Injection of all types.
- [Payload all the things](https://github.com/swisskyrepo/PayloadsAllTheThings) A list of useful payloads and bypass for Web Application Security and Pentest/CTF 
- [Hack Tricks](https://book.hacktricks.xyz/) The great sites for pentesting and recon cheat sheet
- [GAP-Burp-Extension](https://github.com/xnl-h4ck3r/GAP-Burp-Extension) Burp Extension to find potential endpoints, parameters, and generate a custom target wordlist
- [Cloundflare](https://github.com/greycatz/CloudUnflare) Reconnaissance Real IP address for Cloudflare Bypass
- [Cloudmare](https://github.com/MrH0wl/Cloudmare) Cloudflare, Sucuri, Incapsula real IP tracker.
- [emkei](https://emkei.cz/) Free online fake mailer with attachments spoof email 
- [GraphSpy](https://github.com/RedByte1337/GraphSpy) Initial Access and Post-Exploitation Tool for AAD and O365 with a browser-based GUI
- [revshells](https://www.revshells.com/) Reverse Shell Generator
- [enum4linux](https://github.com/CiscoCXSecurity/enum4linux) Linux alternative to enum.exe for enumerating data from Windows and Samba hosts
- [vulmap](https://github.com/zhzyker/vulmap) Vulmap - Web vulnerability scanning and verification tools
- [Active-Directory-Exploitation-Cheat-Sheet](https://github.com/S1ckB0y1337/Active-Directory-Exploitation-Cheat-Sheet) A cheat sheet that contains common enumeration and attack methods for Windows Active Directory.
- [HPING](https://github.com/antirez/hping) Hping network tool
- [AlliN](https://github.com/P1-Team/AlliN) A flexible scanner
- [KUNYU](https://github.com/knownsec/Kunyu) Kunyu, more efficient corporate asset collection
- [jwt tool](https://github.com/ticarpi/jwt_tool)  A toolkit for testing, tweaking and cracking JSON Web Tokens
- [jwt-secrets-list](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list) possible to help developers and DevOpses identify it by traffic analysis at the Wallarm NGWAF level 
- [aparoid](https://github.com/stefan2200/aparoid) Static and dynamic Android application security analysis
- [Active Directory Cheat](https://github.com/esidate/pentesting-active-directory) Active Directory Pentesting Mind Map 
- [sploitus](https://sploitus.com/) Awesome exploit list like Exploit DB
- [thehacker recipe](https://www.thehacker.recipes/) Awesome pentesting checklist and cheat 
- [OPSEC](https://github.com/WesleyWong420/OPSEC-Tradecraft) Collection of OPSEC Tradecraft and TTPs for Red Team Operations
- [CSAF CSLAB](https://github.com/csalab-id/csaf) Cyber Security Awareness Framework (CSAF)
- [hakoriginfinder](https://github.com/hakluke/hakoriginfinder) Tool for discovering the origin host behind a reverse proxy. Useful for bypassing cloud WAFs! 
- [gmapsapiscanner](https://github.com/ozguralp/gmapsapiscanner) Used for determining whether a leaked/found Google Maps API Key is vulnerable to unauthorized access by other applications or not
- [jsluice](https://github.com/BishopFox/jsluice) Extract URLs, paths, secrets, and other interesting bits from JavaScript
- [DisableFlagSecure](https://github.com/LSPosed/DisableFlagSecure) Disable FLAG_SECURE on all windows, enabling screenshots in apps that normally wouldn't allow it, and disabling screenshot detection on Android 14+
- [trufflehog](https://github.com/trufflesecurity/trufflehog) Find leaked credentials and Find and verify secrets
- [SecretFinder](https://github.com/m4ll0k/SecretFinder) SecretFinder - A python script for find sensitive data (apikeys, accesstoken,jwt,..) and search anything on javascript files
- [uproot-JS](https://github.com/0xDexter0us/uproot-JS) Extract JavaScript files from burp suite project with ease
- [JS beautify vscode extension](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify) Beautify javascript, JSON, CSS, Sass, and HTML in Visual Studio Code
- [Bug bounty hunter javascript reccon](https://www.bugbountyhunter.com/guides/?type=javascript_files) Awesome trick and tips reccon web assets  
- [Javascript reccon](https://gist.github.com/fuckup1337/49484c35c8ad8ae1d165ffe7d71375eb) This is a simple guide to perform javascript recon in the bugbounty
- [Nuclei OSINT Templates](https://github.com/cipher387/juicyinfo-nuclei-templates) Awesome list nuclei template for OSINT and reccon from web pages
- [Official Nuclei Templates](https://github.com/projectdiscovery/nuclei-templates) List official nuclei templates available for pentesting 
- [XRAY](https://github.com/chaitin/xray/blob/master/README_ID.md) A powerful security assessment tool 
- [villain](https://www.kali.org/tools/villain/) C2 framework that can handle multiple TCP socket & HoaxShell-based reverse shells *maybe FUD
- [aquasecurity vuln list](https://github.com/aquasecurity/vuln-list) Collect vulnerability information and save it in parsable format automatically
- [trivy](https://github.com/aquasecurity/trivy) Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more 
- [aquasecurity Redhat vuln list](https://github.com/aquasecurity/vuln-list-redhat) Red Hat security advisories 
- [Vuls](https://vuls.io/docs/en/abstract.html) Vulnerability scanner for Linux/FreeBSD, agent-less, written in Go
- [OneForAll](https://github.com/shmilylty/OneForAll/blob/master/docs/en-us/README.md) Awesome web reccon and subdomain, DNS reccon
- [Can I Take Over xyz](https://github.com/EdOverflow/can-i-take-over-xyz) A list of services and how to claim (sub)domains with dangling DNS records
- [Can I Take Over DNS](https://github.com/indianajson/can-i-take-over-dns) A list of DNS providers and how to claim (sub)domains via missing hosted zones
- [DevsecOps Secure Code](https://devsecopsguides.com/docs/rules) Resource for developers, security professionals, and operations teams who want to learn about the world of DevSecOps
- [dwisiswant0 Nuceli Template Dir](https://github.com/dwisiswant0/nuclei-templates-dir) Awesome list and easy for search nuclei templates 
- [dwisiswant0 CF-CHECK](https://github.com/dwisiswant0/cf-check/releases) CloudFlare Checker written in Go
- [HTTP Docs](https://devdoc.net/web/developer.mozilla.org/en-US/docs/HTTP.1.html) Awesome guides protocol for transmitting hypermedia documents for pentester and developer
- [Devoper Mozila](https://developer.mozilla.org/en-US/) Awesome resouces guides protocol for transmitting hypermedia documents for pentester and developer
- [List Red Team Tool Cheat Sheet](https://highon.coffee/blog/) List cheat sheet for red team tools 
- [Red Team Notes](https://notes.benheater.com/) Good notes for red team  
- [OSCP NOTES](https://github.com/0xsyr0/OSCP) Awesome OSCP notes cheat sheet for your labs and exam or CTF

Social Engineering

- [social engineering](https://www.social-engineer.org/)
- [emkei](https://emkei.cz/)
- [Phishious](https://github.com/CanIPhish/Phishious) 

Active Directory

- [BloodHound](https://github.com/BloodHoundAD/BloodHound)
- [Certify](https://github.com/GhostPack/Certify)
- [Certipy](https://github.com/ly4k/Certipy)
- [certi](https://github.com/zer1t0/certi)
- [PKINITtools](https://github.com/dirkjanm/PKINITtools)
- [ADCSPwn](https://github.com/bats3c/ADCSPwn)
- [PassTheCert](https://github.com/AlmondOffSec/PassTheCert)
- [kerbrute](https://github.com/ropnop/kerbrute)
- [Adinfo](https://github.com/lzzbb/Adinfo)
- [SharpADWS](https://github.com/wh0amitz/SharpADWS) via Active Directory Web Services (ADWS) protocol
- [SOAPHound](https://github.com/FalconForceTeam/SOAPHound) via Active Directory Web Services (ADWS) protocol
- [SharpHostInfo](https://github.com/shmilylty/SharpHostInfo)

Webshell Bypass

- [WebShell-Bypass-Guide](https://github.com/AabyssZG/WebShell-Bypass-Guide)
- [bypass.tidesec.com/web/](http://bypass.tidesec.com/web/)

Credential Access

- [LaZagne](https://github.com/AlessandroZ/LaZagne)
- [WirelessKeyView](https://www.nirsoft.net/utils/wireless_key.html)
- [Windows credential manager](https://www.nirsoft.net/utils/credentials_file_view.html)
- [Pillager](https://github.com/qwqdanchun/Pillager/)
- [searchall](https://github.com/Naturehi666/searchall)

Post Exploitation

- [metasploit-framework](https://github.com/rapid7/metasploit-framework)
- [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec)
- [impacket](https://github.com/fortra/impacket)
- [wmiexec-Pro](https://github.com/XiaoliChan/wmiexec-Pro)
- [pstools](https://docs.microsoft.com/en-us/sysinternals/downloads/pstools)
- [Rubeus](https://github.com/GhostPack/Rubeus)
- [Powermad](https://github.com/Kevin-Robertson/Powermad)
- [PowerSploit](https://github.com/PowerShellMafia/PowerSploit)
- [Responder](https://github.com/lgandx/Responder)
- [Responder-Windows](https://github.com/lgandx/Responder-Windows)

Credential Dumping

- [LaZagne](https://github.com/AlessandroZ/LaZagne)
- [WirelessKeyView](https://www.nirsoft.net/utils/wireless_key.html)
- [Windows credential manager](https://www.nirsoft.net/utils/credentials_file_view.html)
- [Pillager](https://github.com/qwqdanchun/Pillager/)
- [searchall](https://github.com/Naturehi666/searchall)

Password crack 

- [hashcat](https://github.com/hashcat/hashcat) A tool brute and crack password hash
- [john](https://github.com/openwall/john) A tool brute and crack password hash 
- [thc hydra](https://github.com/vanhauser-thc/thc-hydra) A tool brute and crack password 
- [CiLocks](https://github.com/tegal1337/CiLocks) Crack Interface lockscreen, Metasploit and More Android/IOS Hacking

Wordlists for all

- [SecLists](https://github.com/danielmiessler/SecLists) 
- [SecDictionary](https://github.com/SexyBeast233/SecDictionary) 
- [ffuf](https://github.com/ffuf/ffuf)
- [Dictionary-Of-Pentesting](https://github.com/insightglacier/Dictionary-Of-Pentesting)
- [fuzzDicts](https://github.com/TheKingOfDuck/fuzzDicts)
- [Web-Fuzzing-Box](https://github.com/gh0stkey/Web-Fuzzing-Box)
- [PentesterSpecialDict](https://github.com/ppbibo/PentesterSpecialDict)
- [fuzz.txt](https://github.com/Bo0oM/fuzz.txt)
- [wordlists](https://github.com/assetnote/wordlists)

Web fuzz wordlists

- [top25-parameter](https://github.com/lutfumertceylan/top25-parameter)

Generate wordlists

- [weakpass.com/generate](https://weakpass.com/generate)

Generate subdomains and wordlists

- [weakpass.com/generate/domains](https://weakpass.com/generate/domains)

Private Deployment

- [weakpass](https://github.com/zzzteph/weakpass)

Generate subdomains and wordlists(offline)

- [probable_subdomains](https://github.com/zzzteph/probable_subdomains)

Kali/Linux

- [crunch-wordlist](https://sourceforge.net/projects/crunch-wordlist)

Windows

- [Windows-Crunch](https://github.com/shadwork/Windows-Crunch)

Default Credentials

- [DefaultCreds-cheat-sheet](https://github.com/ihebski/DefaultCreds-cheat-sheet)
- [datarecovery](https://datarecovery.com/rd/default-passwords/)
- [cirt.net](https://cirt.net/passwords)
- [routerpasswords](https://www.routerpasswords.com/)
- [portforward](https://portforward.com/router-password/)
- [cleancss](https://www.cleancss.com/router-default/)
- [toolmao](https://www.toolmao.com/baiduapp/routerpwd/)
- [datarecovery](https://datarecovery.com/rd/default-passwords/)

Local Enumeration

- [HackBrowserData](https://github.com/moonD4rk/HackBrowserData)
- [BrowserGhost](https://github.com/QAX-A-Team/BrowserGhost)
- chrome: [chromepass](http://www.nirsoft.net/utils/chromepass.html)
- [firefox_decrypt](https://github.com/unode/firefox_decrypt)
- foxmail: [foxmail-password-decryptor](https://securityxploded.com/foxmail-password-decryptor.php)
- [how-does-MobaXterm-encrypt-password](https://github.com/HyperSine/how-does-MobaXterm-encrypt-password)
- [navicat_password_decrypt](https://github.com/Zhuoyuan1/navicat_password_decrypt)
- [how-does-navicat-encrypt-password](https://github.com/HyperSine/how-does-navicat-encrypt-password)
- [Sunflower_get_Password](https://github.com/wafinfo/Sunflower_get_Password)
- [shcrt](https://github.com/depau/shcrt)
- [SharpDecryptPwd decrypt locally](https://github.com/RowTeam/SharpDecryptPwd)
- [SharpXDecrypt](https://github.com/JDArmy/SharpXDecrypt)

Privilage Escalation Cheat and check

- [Gfobins](https://gtfobins.github.io/) Awesome privilage escalation cheat and checklist
- [Lolbas](https://lolbas-project.github.io/) Awesome privilage escalation cheat and checklist
- [Loonbins](https://www.loobins.io/tactics/collection/) Awesome privilage escalation cheat and checklist
- [Mac OS privilage escalation](https://book.hacktricks.xyz/macos-hardening/macos-security-and-privilege-escalation) Awesome privilage escalation cheat and checklist
- [PEASS NG](https://github.com/peass-ng/PEASS-ng) Awesome automatic enum for privilage escalation cheat and checklist
- [wadcoms](https://wadcoms.github.io/#+Windows) WADComs is an interactive cheat sheet, offensive security tools and their respective commands, to be used against Windows/AD environments
- [g0tmi1k linux priv esc](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/) Basic Linux Privilege Escalation
 
# Audio OSINT 

- [Audio metadata](https://github.com/tmont/audio-metadata)
- [Google Translate by speech](https://support.google.com/translate/answer/6142468?hl=en&co=GENIE.Platform%3DDesktop)
- [Microsoft Translator](https://play.google.com/store/apps/details?id=com.microsoft.translator&hl=en&gl=US)
- [Yandex Translate](https://play.google.com/store/apps/details?id=ru.yandex.translate&hl=en&gl=US)
- [Apple Translate by speech](https://apps.apple.com/us/app/translate/id1514844618)
- [translatedlabs](https://translatedlabs.com/spoken-language-identifier)
- [Adobe Audition](https://www.adobe.com/id_en/products/audition.html)
- [Sound classification with YAMNet](https://www.tensorflow.org/hub/tutorials/yamnet)
- [Praat](https://www.fon.hum.uva.nl/praat/)
- [phonexia](https://www.phonexia.com/use-case/audio-forensics-software/)
- [SoundScrape](https://github.com/Miserlou/SoundScrape)
- [Online loudness meter](https://youlean.co/online-loudness-meter/)
- [soundeffectssearch](https://www.soundeffectssearch.com/advanced-search/)
- [vocalremover](https://vocalremover.org/)

Audio enchange quality  

- [boom](https://www.globaldelight.com/boom/)
- [fxsound](https://www.fxsound.com/)

# OSINT Network 

Detect a fake network and VPN

- [Spur](https://spur.us/)
- [FocSec](https://focsec.com/)
- [IP VPN detector](https://ip.teoh.io/vpn-detection)
- [IPQS](https://www.ipqualityscore.com/vpn-ip-address-check)

# Medical OSINT 

- [WHO](https://www.who.int/)
- [PUB MED](https://pubmed.ncbi.nlm.nih.gov/)

# OSINT Military

- [militaryfactory](https://www.militaryfactory.com/)
- [Military and other uniform badges](https://www.uniforminsignia.net/)
- [SMALL ARMS SURVEY](https://www.smallarmssurvey.org/resource/introductory-guide-identification-small-arms-light-weapons-and-associated-ammunition)
- [dfrlab.org](https://dfrlab.org/research/)
- [atlanticcouncil](https://www.atlanticcouncil.org/)
- [NASA EARTH](https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms)
- [EARTH DATA NASA](https://wvs.earthdata.nasa.gov/)
- [peakvisor](https://peakvisor.com/)
- [peakfinder](https://www.peakfinder.com/) 
- [Geoconfirmed](https://geoconfirmed.org/)
- [Air Wars](https://airwars.org/)
- [Copernicus](https://atmosphere.copernicus.eu/charts/packages/cams/?facets=%7B%22Family%22%3A%5B%22Fires%22%5D%7D)
- [Ej Atlas](https://ejatlas.org/)
- [Intro OSINT Military](https://www.linkedin.com/pulse/mastering-military-osint-comprehensive-guide-modern-niels-groeneveld)
- [Telegram Geogramint](https://github.com/Alb-310/Geogramint)
- [Skylens](https://app.skylens.io/)
- [Geocreepy](https://www.geocreepy.com/)
- [Kamerka](https://github.com/woj-ciech/Kamerka-GUI)
- [Earthcam](https://www.earthcam.com/#google_vignette)
- [onemilliontweetmap](https://onemilliontweetmap.com/)
- [birdhunt](https://birdhunt.co/)
- [garmin](https://www.garmin.co.id/products/outdoor/gpsmap64s-sea/)
- [SALW](https://salw-dashboard.electrifai.net/analytics/main)
- [Earth ESA](https://earth.esa.int/eogateway)
- [APP Sentinel](https://apps.sentinel-hub.com/)
- [NASA Fire Dataset](https://firms.modaps.eosdis.nasa.gov/)
- [Google Earth Pro](https://earth.google.com/web/)
- [CIA GOV](https://www.cia.gov/the-world-factbook/)
- [Acleddata](https://acleddata.com/)
- [Global Conflict](https://www.cfr.org/global-conflict-tracker)
- [Google Public Data](https://www.google.com/publicdata/directory)
- [huntintel](https://www.huntintel.io/)
- [planet](https://www.planet.com/)
- [NBR Map](https://map.nbr.org/interactivemap/)
- [ADS B](https://www.ads-b.nl/)
- [itamilradar](https://www.itamilradar.com/)
- [info-res](https://www.info-res.org/)
- [syria.liveuamap](https://syria.liveuamap.com/)
- [NATO INT](https://www.nato.int/nato-on-the-map/)
- [understandingwar](https://www.understandingwar.org/map-room)
- [worldbeyondwar](https://worldbeyondwar.org/no-bases/)
- [planefinder](https://planefinder.net/)
- [WEB SDR](http://websdr.ewi.utwente.nl:8901/)
- [Bellingcat Radar](https://ollielballinger.users.earthengine.app/view/bellingcat-radar-interference-tracker)
- [airrecognition](https://airrecognition.com/index.php)
- [gpsjam](https://gpsjam.org/)
- [freemaptools](https://www.freemaptools.com/)
- [earthobservatory NASA](https://earthobservatory.nasa.gov/global-maps)
- [mooncalc](https://www.mooncalc.org/)

# Academic Search Tools

- [Base Search](https://www.base-search.net/)
- [SCI HUB](https://www.sci-hub.se/)
- [msearch](https://msearch.io/)
- [Google scholar](https://scholar.google.com/)
- [Jstor](https://www.jstor.org/)

Academic Literature

- [Academic Literature on Open Source Research & Methods](https://docs.google.com/document/d/1uqzGi9asZZlaEs8syHbh3AsizVccU-IKJp4zPufaaBk/edit#heading=h.s9zomzvdp109)
- [OSINT ethics](https://stanleycenter.org/publications/osint-applied-ethics-workbook/)
- [G Drive - Navigating digital media](https://drive.google.com/drive/folders/1eF9FE-2B-bVciTCbajMR_f1Q7fHZl0s5)

# Web Directory 

- [Vlib](https://vlib.org/)
- [Dmoz](https://web.archive.org/web/20240000000000*/http:/www.dmoz.org/)

# Torrent

- [utorrent](https://www.utorrent.com/) 
- [bittorrent](https://www.bittorrent.com/) 
- [Jacket](https://github.com/Jackett/Jackett)
- [API OSINT TORRENT](https://github.com/cipher387/API-s-for-OSINT/blob/main/README.md) 
- [torrentinim](https://github.com/sergiotapia/torrentinim)

# SDR OSINT 

- [map sdr points](https://rx-tx.info/map-sdr-points) 
- [Airspy SDR RADIO](https://www.sdr-radio.com/airspy-server) 
- [AirSpy MAP](https://airspy.com/directory/)
- [WEB SDR](http://websdr.ewi.utwente.nl:8901/)
- [Bellingcat Radar](https://ollielballinger.users.earthengine.app/view/bellingcat-radar-interference-tracker)

# API for OSINT 

Resources and collection for your make tool OSINT 

- [API Resoruces OSINT - For Your Private Tool](https://github.com/cipher387/API-s-for-OSINT/blob/main/README.md) 
- [API for OSINT](https://github.com/cipher387/API-s-for-OSINT)

# Data Visualization

- [Maltego](https://www.maltego.com/)
- [Mgrs Mapper](https://mgrs-mapper.com/app)
- [Neo4j](https://neo4j.com/)
- [Kepler Mapping](https://kepler.gl/demo/) 
- [Google Chart](https://developers.google.com/chart)
- [Chart JS](https://www.chartjs.org/)
- [fiugis](https://fiugis.maps.arcgis.com/home/index.html)
- [Map Hub](https://maphub.net/map)
- [Maltego Casefile](https://docs.maltego.com/support/solutions/articles/15000018948-what-is-maltego-casefile-)
- [Any Chart](https://www.anychart.com/)
- [High Charts](https://www.highcharts.com/)
- [Any Logic](https://anylogic.help/)
- [GO js Charts](https://gojs.net/)
- [cytoscape](https://js.cytoscape.org/)
- [sigmajs](https://www.sigmajs.org/)
- [graph-gallery](https://d3-graph-gallery.com/network.html)

# Emoji Investigation

- [dutchosintguy](https://www.dutchosintguy.com/post/cryptography-osint-can-you-read-emoji)
- [Emoji Wiki](https://emojis.wiki/)
- [Emoji Guide](https://emojiguide.com/)
- [Emoji Tracker](https://emojitracker.com/details/1F44F)

# OSINT Branding & Verify 

- [Trus Pilot](https://www.trustpilot.com/)
- [Google Alert](https://www.google.com/alerts)
- [White Pages](https://www.whitepages.com/)
- [Tripadvisor](https://www.tripadvisor.com/)
- [Trustindex](https://www.trustindex.io/)
- [G Map Review](https://www.google.com/maps/)
- [Provenexpert](https://www.provenexpert.com/)
- [SIMPU RI](https://umrahcerdas.kemenag.go.id/)
- [Jobstreet.co.id](https://www.jobstreet.co.id/)
- [WEB Check](https://web-check.xyz/)
- [brightcloud ip lookup](https://www.brightcloud.com/tools/url-ip-lookup.php)
- [Url Filltering](https://urlfiltering.paloaltonetworks.com/)
- [A href Backlink Checker](https://ahrefs.com/backlink-checker)
- [Neil Patel Backlink](https://neilpatel.com/backlinks/)
- [Semrush Backlink](https://www.semrush.com/analytics/backlinks/)
- [Small SEO Tool Backlink](https://smallseotools.com/backlink-checker/)
- [SEO Backlink Check](https://www.seobility.net/en/backlinkchecker/)
- [Moz Backlink](https://moz.com/link-explorer)
- [SPAM Check Score](https://www.dapachecker.org/spam-score-checker)
- [MOZ Spam Check](https://moz.com/help/link-explorer/link-building/spam-score)
- [NIK PARSE](https://github.com/bachors/nik_parse.js?tab=readme-ov-file#nik_parsejs)
- [Maltego Transform ShadowDragon](https://www.maltego.com/transform-hub/socialnet/)
- [Kaseware](https://www.kaseware.com/link-analysis)
- [opentender ID](https://opentender.net/)
- [lpse lkpp ID](https://lpse.lkpp.go.id/eproc4)
- [ahu ID](https://ahu.go.id/pencarian/profil-pt)
- [Minerba ESDM ID](https://momi.minerba.esdm.go.id/gisportal/home/)
- [MODI ID](https://modi.esdm.go.id/portal/dataPerusahaan)
- [HAKI ID](https://pdki-indonesia.dgip.go.id/search?type=trademark&keyword=)
- [Katadata ID](https://databoks.katadata.co.id/)
- [pddikti ID](https://pddikti.kemdikbud.go.id/)
- [pipl](https://pipl.com/)
- [ipqs](https://www.ipqualityscore.com/)
- [sociallinks](https://sociallinks.io/)

# NEWS OSINT

Search News Journalist and Documentary Sites 

- [Glanlaw](https://www.glanlaw.org/)
- [Bellingcat](bellingcat.com)
- [The Guardians](https://www.theguardian.com/international)
- [Drone Emprit](https://pers.droneemprit.id/)
- [Google News](https://news.google.com/)
- [MagPortal](http://www.magportal.com/)
- [Flipboard](https://flipboard.com/)
- [aljazeera](https://www.aljazeera.com/)
- [apnews](https://apnews.com/hub/israel-hamas-war)
- [unocha](https://www.unocha.org/)
- [narasi ID](https://narasi.tv/)
- [katadata ID](https://katadata.co.id/)
- [ID BRIN](https://brin.go.id/)
- [ShadowDragon](https://shadowdragon.io/)
- [Delpher](https://www.delpher.nl/)

# OSINT Keyword 

- [Google Trends](https://trends.google.com/trends/)
- [keyworddiscovery](https://www.keyworddiscovery.com/)
- [Yandex Trends](https://wordstat.yandex.com/)
- [Wordtracker](https://www.wordtracker.com/)

# Threat Actor & Criminal 

- [eumostwanted EU](https://eumostwanted.eu/)
- [nationalcrimeagency UK](https://www.nationalcrimeagency.gov.uk/most-wanted)
- [FBI Most Wanted](https://web.archive.org/web/20030315000000*/https://www.fbi.gov/wanted/cyber)
- [FBI](https://www.fbi.gov/wanted)
- [secretservice](https://www.secretservice.gov/investigations/mostwanted)
- [pusiknas Polri ID](https://pusiknas.polri.go.id/dpo)
- [kejaksaan ID](https://pelayanan.kejaksaan.go.id/layanan/permohonan/dpo)
- [reskrimum Polri ID](https://web.archive.org/web/20220124010657/https://reskrimum.metro.polri.go.id/dpo/)
- [reskrimum Metro Polri ID](https://reskrimum.metro.polri.go.id/dpo/)
- [Maltego Transform ShadowDragon](https://www.maltego.com/transform-hub/socialnet/)
- [stealthmole](https://www.stealthmole.com/)
- [NCA most wanted](https://nationalcrimeagency.gov.uk/most-wanted-search)
- [ShadowDragon](https://shadowdragon.io/)
- [sociallinks](https://sociallinks.io/)
- [Crimewall](https://sociallinks.io/products/sl-crimewall)

# OSINT for Politics and Geopolitics

OSINT politics and geopolitics, risk crisis

- [civicus](https://monitor.civicus.org/)
- [freedomhouse](https://freedomhouse.org/countries/freedom-world/scores)
- [hunger map](https://hungermap.wfp.org/)
- [native-land](https://native-land.ca/)
- [riskmap](https://www.riskmap.com/)
- [splcenter](https://www.splcenter.org/hate-map)
- [safeairspace](https://safeairspace.net/)
- [globaldetentionproject](https://www.globaldetentionproject.org/detention-centres/map-view)
- [tasteatlas](https://www.tasteatlas.com/)
- [global terrorism database](https://www.start.umd.edu/gtd/)
- [start global terrorism database](https://www.start.umd.edu/)
- [datasets global terrorism database Kaggle](https://www.kaggle.com/datasets/START-UMD/gtd)

# Maltego Transform List 

- [Offical Maltego Transform List](https://www.maltego.com/transform-hub/)
- [Github cipher387 maltego transforms list](https://github.com/cipher387/maltego-transforms-list)

# OSINT Wildlife 

- [SIKU](https://siku.org/project-management)

# OSINT Satellite

- [ESRI](https://geoxc-apps.bd.esri.com/)
- [n2yo](https://www.n2yo.com/)
- [satellitemap](https://satellitemap.space/?constellation=starlink)
- [planet](https://www.planet.com/)
- [space track](https://www.space-track.org/auth/login)
- [google earth](https://earth.google.com/)
- [satellitetracker](https://satellitetracker.net/)

# OSINT for Scraping and Data Collection

- [Zenrows](https://www.zenrows.com/) Bypassing captcha and WAF 
- [Scrapfly](https://scrapfly.io/) Bypassing captcha and WAF 
- [capsolver](https://www.capsolver.com/id) Bypassing captcha and WAF 
- [2captcha](https://2captcha.com/) Bypassing captcha and WAF 
- [Puppeter](https://www.npmjs.com/package/puppeteer-extra-plugin-stealth) For web scrapper and info gath
- [spiderfoot](https://github.com/smicallef/spiderfoot) Automates OSINT for threat intelligence and mapping your attack surface.

# OSINT IRC Chat

- [netsplit](https://netsplit.de/channels/)
- [kiwiirc](https://kiwiirc.com/search)

# OSINT Art Collection

- [Getty Edu](https://www.getty.edu/art/collection/)
- [graphicsatlas](http://www.graphicsatlas.org/)
- [NPG UK](https://www.npg.org.uk/collections/)
- [Artnet](https://www.artnet.com/artists/)
- [NGV AU](https://www.ngv.vic.gov.au/explore/collection/)
- [DAAO AU](https://www.daao.org.au/)
- [Old Indiana Photo](https://www.oldindianphotos.in/)
- [Lostart DE](https://www.lostart.de/en/start)

# OSINT The Artists 

- [Artnet](https://www.artnet.com/artists/)
- [NGV AU](https://www.ngv.vic.gov.au/explore/collection/)
