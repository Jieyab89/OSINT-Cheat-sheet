# OSINT CHEAT SHEET

[![Github Badge](https://img.shields.io/badge/-Jieyab89-black?style=flat&logo=github&logoColor=white&link=https://github.com/Jieyab89/)](https://github.com/Jieyab89)

OSINT RESOURCES DATASET 

- [Join Telegram channel](https://t.me/seccodeid)
- [OSINT beginner](https://t.me/seccodeid/38)
- [OSINT handbook 2022 OSINT information gathering and threat intel](https://t.me/seccodeid/87)

# EXIF TOOL COMMAND 

#Exif tag name and data type

> Author                                        string/
> 
> Caption                                       string/
> 
> Categories                                    string/
> 
> Collections                                   string/
> 
> DateTime                                      date/
> 
> DPP                                           lang-alt/
> 
> EditStatus                                    string/
> 
> FixtureIdentifier                             string/
> 
> Keywords                                      string/+
> 
> Notes                                         string/
> 
> ObjectCycle                                   string/
> 
> OriginatingProgram                            string/
> 
> Rating                                        real/
> 
> Rawrppused                                    boolean/
> 
> ReleaseDate                                   string/
> 
> ReleaseTime                                   string/
> 
> RPP                                           lang-alt/
> 
> Snapshots                                     string/+
> 
> Tagged                                        boolean/

More : man exiftool 

Site : 

- [Exiftool](https://exiftool.org/)
- [List tagname](https://exiftool.org/TagNames/)
- [List tagnme 2](https://metacpan.org/dist/Image-ExifTool/view/lib/Image/ExifTool/TagNames.pod)
- [List tagname 3](https://manpages.org/imageexiftooltagnames/3)

#Write metadata 

- exiftool -tagname="string" file 
>
>example : exiftool -Author="Bayu" test.txt 
>

you can add multiple tag and multiple file 

#Delete metadata 

- exiftool -tagname="" file 
>
>example : exiftool -Author="" test.txt 
>

#Delete mass metadata 

- exiftool -all="" file 
>
>example : exiftool -all="" file 
>

#Usage : man exiftool or read documentation exiftool.org 

> Not there are tag no writetable, make sure tagname can write 
>

#!Note 

> Use fresh file, if your file has been compressed or edit metadata you got a default metadata
> You can use xmp format for edit, write and delete metadata 
> Check the documentation 


# SOCMINT  

- [Instagram](https://github.com/Datalux/Osintgram) 
Be carefull using this tool

- [SOCMINT tool](https://osint.support/chrome-extensions/2019/09/29/osint-socmint-tooling.html)
- [Graph Search](http://socmint.tools/graph.htm)

# Collection Dataset 

- [Kaggle](https://www.kaggle.com/)


# Forums 

- [Bellingcat Discord](https://discord.com/invite/nTaNPmz)
- [Independent OSINT](https://discord.com/invite/2DGJ2EC)
- [OSINT.Team](https://osint.team)
- [Seccodeid](https://forum.seccodeid.com)
- [/r/OSINT](https://www.reddit.com/r/OSINT)
- [TraceLabs Slack](https://tracelabs.slack.com)


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

# Social Media Search and Monitoring

- [AIDR](http://aidr.qcri.org)
- [Awario](https://awario.com)
- [Brand24](https://brand24.com)
- [Mention](https://mention.com)
- [Samdesk](https://www.samdesk.io)
- [Social Links](https://www.mtg-bi.com)

# Social Media Management and Content Discovery

- [Agora pulse](https://www.agorapulse.com)
- [Buffer](https://buffer.com)
- [Coosto](https://www.coosto.com)
- [Falcon](https://www.falcon.io)
- [tailwind](https://www.tailwindapp.com)
- [Revive Social](https://revive.social)

# Web Intelligence 

- [Better Whois](http://www.betterwhois.com)
- [DNS History](http://dnshistory.org)
- [DNS Spy](https://dnsspy.io)
- [DNS Checker](https://dnschecker.org)
- [HackerTarget](https://hackertarget.com/ip-tools)
- [Shodan](https://www.shodan.io)

# Analysing URLs 

- [unfurl](https://github.com/obsidianforensics/unfurl)

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

# IoT Search Engines

- [LeakIX](https://leakix.net)
- [Binary Edge](https://www.binaryedge.io)
- [Purplepee.com](https://purplepee.co)
- [Shodan](https://www.shodan.io)
- [Shodan Filters](https://github.com/T43cr0wl3r/shodan-filters)
- [Shodan Scripts](https://github.com/random-robbie/My-Shodan-Scripts)

# IP Addresses 

- [Whats my ip](https://whatismyipaddress.com/)
This tools can show your ip address isp provider 
- [Ip 2 location](https://www.ip2location.com/)
This tools can show your ip address isp provider and geo location  

# Wireless Network 

- [Wigle](https://www.wigle.net/)
Maps and database of 802.11 wireless networks, with statistics, submitted by wardrivers, netstumblers, and 
net huggers

# SOC or Threat Hunting 

- [Alien Vault](https://otx.alienvault.com/)
- [Exploit db](https://www.exploit-db.com/)
- [AT&T](https://cybersecurity.att.com/resource-center#content_analyst-reports)

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

example 
> intext:"hacking" site:seccodeid.com
> site:www.github.com ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv  

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

# Jurnals 

- [sciencedirect](https://www.sciencedirect.com/)
- [Scopus](https://www.scopus.com/)
- [Sinta](https://sinta.kemdikbud.go.id/)
- [ieeexplore](https://ieeexplore.ieee.org)

# Crack Jurnals 

- [SCI HUB](https://sci-hub.hkvisa.net/)
This domain will always change

# Blogs Search Engine 

- [Google Blog](www.google.com/blogsearch)
- [technorati](www.technorati.com)
- [omgili.com](http://omgili.com/)

# DeepWeb Search Engines

- [thehiddenwiki](http://thehiddenwiki.org)
- [onion link](http://www.onion.link)
- [MEMEX]()
- [onion](https://onion.cab)

# Tracking Website Changes 

- [Changedetection](http://www.changedetection.com)
- [Followthatpage](http://www.followthatpage.com)

# Company Reconnaissance Sites (Passive) 

- [whois](http://www.whois.net)
- [Netcraft](http://www.netcraft.com)

# People Searching 

- [spokeo](http://www.spokeo.com)
- [123people](http://www.123people.com)
- [zoominfo](http://www.zoominfo.com)
- [peepdb](http://www.peepdb.com)
- [reversegeni](http://www.reversegenie.com/plate.php)
- [PDDIKTI](https://pddikti.kemdikbud.go.id/)
- [SINTA](https://sinta.kemdikbud.go.id/)

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

# Public Records 

- [Public Record](http://publicrecords.searchsystems.net)
- [Fam Watchdog](http://Familywatchdog.us)
- [Crime Reports](http://www.crimereports.com)

# Finding Usernames 

- [Namechk](http://www.namechk.com)
- [Knowem](http://www.knowem.com)

# Social Networks 

- [Facebook](https://facebook.com/livemap)
- [Facebook lookup id](https://lookup-id.com/#)
- [Sherlock](https://github.com/sherlock-project/sherlock)

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
- [Agora Pulse](http://barometer.agorapulse.com)
- [Commun.it](http://commun.it)
- [DumpItBlue](http://le-tools.com/DumpItBlue.html)
- [Fanpage Karma](http://www.fanpagekarma.com)
- [Facebook Search](http://search.fb.com/)
- [Facebook Search Tool](http://netbootcamp.org/facebook.html)
- [Fb-sleep-stats](https://github.com/sqren/fb-sleep-stats)
- [Find my Facebook ID](https://findmyfbid.in)
- [Lookup-ID.com](https://lookup-id.com)
- [SearchIsBack](https://searchisback.com)
- [Wolfram Alpha Facebook Report](http://www.wolframalpha.com/input/?i=facebook+report)

# Instagram 

- [Hashtagify](http://hashtagify.me)
- [Iconosquare](http://iconosquare.com)
- [Picodash](https://www.picodash.com)
- [SnapMap](https://snapmap.knightlab.com/)
- [Social Rank](https://www.socialrank.com)
- [Toutatis](https://github.com/megadose/toutatis)
- [Worldcam](http://worldc.am)
- [SearchMyBio](https://www.searchmy.bio/)

# Pinterest 

- [Pingroupie](http://pingroupie.com)

# Twitter 

- [search.twitter.com](https://twitter.com/search-home)
- [twitter advanced](https://www.twitter.com/search-advanced)
- [twitter who_to_follow](https://www.twitter.com/who_to_follow)
- [Alldaytrends](https://alldaytrends.com) A website where you can find trending hashtags.
- [Backtweets](http://backtweets.com) BackTweets is a Twitter analytics tool that allows users to search through a Tweet archive.
- [Blue Nod](http://bluenod.com)
- [burrrd.](https://burrrd.com)
- [doesfollow](https://doesfollow.com)
- [Fake Follower Check](https://fakers.statuspeople.com)
- [First Tweet](http://ctrlq.org/first)
- [Foller.me](http://foller.me)
- [FollowCheck](http://followcheck.com)
- [Followerwonk](http://followerwonk.com)
- [Geochirp](http://www.geochirp.com)
- [GeoSocial Footprint](http://geosocialfootprint.com)
- [GetTwitterID](http://gettwitterid.com)
- [Gigatweeter](http://gigatweeter.com)
- [Ground Signal](https://www.groundsignal.com)
- [HappyGrumpy](https://www.happygrumpy.com)
- [Harvard TweetMap](http://worldmap.harvard.edu/tweetmap)
- [Hashtagify](http://hashtagify.me)
- [Hashtags.org](http://www.hashtags.org)
- [ManageFlitter](http://manageflitter.com)
- [Mentionmapp](http://mentionmapp.com)
- [MyTweetAlerts](https://www.mytweetalerts.com/) A tool to create custom email alerts based on Twitter search.
- [Nations24](https://nations24.com)
- [OneMillionTweetMap](http://onemilliontweetmap.com)
- [Queryfeed](https://queryfeed.net)
- [Rank Speed](http://www.rankspeed.com)
- [Riffle](http://crowdriff.com/riffle/)
- [RiteTag](https://ritetag.com)
- [Sentiment140](http://www.twittersentiment.appspot.com)
- [SnapBird](http://snapbird.org)
- [Sleeping Time](http://sleepingtime.org)
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
- [Twicsy](http://twicsy.com)
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

# Twitter Search Engines 

- [tweetpaths](http://www.tweetpaths.com)
- [allmytweets](http://www.allmytweets.com)
- [Sleepingtime](http://www.sleepingtime.org)
- [twicsy](http://www.twicsy.com)
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

# Social Network Search Engines

- [kurrently](http://www.kurrently.com)
- [socialmention](http://www.socialmention.com)
- [whostalkin](http://www.whostalkin.com)
- [twoogel](http://www.twoogel.com)
- [social mention](http://www.mention.com)
- [whostalkin](http://www.whostalkin.com)

# Monitoring & Alerting 

- [Pastebin Alerts](http://pastebin.com/u/alerts)
- [HaveIBeenPwned](http://www.haveIbeenpwned.com)
- [breachorclear](http://breachorclear.jesterscourt.cc)

# Images Search Engine 

- [Images google](https://images.google.com)
- [Facesaerch](http://facesaerch.com/)
- [Tineye](http://www.tineye.com)
- [Flickr](http://Flickr.com/map)
- [7photos](http://www.7photos.net)
- [Worldc](http://www.worldc.am)
- [Yandex](https://yandex.com/images/)

# EXIF Analysis 

- [regex](http://regex.info/exif.cgi)
- [FindExif](http://www.findexif.com)
- [metapicz](http://metapicz.com)
- [imageforensic](http://www.imageforensic.org)
- [metapicz](http://metapicz.com)
- [jimpl](https://jimpl.com/)
- [pic2map](https://www.pic2map.com/)

# Documents 

- [Metashield Analyzer](https://metashieldanalyzer.elevenpaths.com/)
- [forensicswiki](http://www.forensicswiki.org/wiki/Document_Metadata_Extraction)
- [foca](https://www.elevenpaths.com/labstools/foca/index.html)

# Email Tracing 

- [ip-adress](http://www.ip-adress.com/trace_email/)
- [whatismyipaddress](http://www.whatismyipaddress.com/trace-email)

# Tracking People 

- [getnotify](http://www.getnotify.com)

# IoT – Internet of Things 

- [Insecam](http://Insecam.org)
- [Shodan](https://Shodan.io)

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

# OSINT TOOLS 

- [Shrelock]()
- [Maltego](https://www.maltego.com/)
- [OSINT Framework](https://osintframework.com/)
- [Creepy](https://www.geocreepy.com/)
- [Twint](https://forum.seccodeid.com/d/twint-twitter-intelligence-tool)
- [Telegram OSINT](https://forum.seccodeid.com/d/telegram-nearby-map)
- [Recon-Ng](https://github.com/lanmaster53/recon-ng)
- [Metagoofil](https://www.kali.org/tools/metagoofil/)
- [More](https://forum.seccodeid.com/?q=osint)

# OSINT Github Tool  

- [tinfoleak](https://github.com/vaguileradiaz/tinfoleak)
- [migret](https://github.com/soxoj/maigret)
- [mosint](https://github.com/alpkeskin/mosint)
- [osint_stuff_tool_collection](https://github.com/cipher387/osint_stuff_tool_collection)
- [instaloctrack](https://github.com/bernsteining/instaloctrack)
- [SpyScrap](https://github.com/RuthGnz/SpyScrap)
- [osintteye](https://github.com/rlyonheart/osinteye)
- [metagofil](https://github.com/kurobeats/metagoofil)
- [recon-ng](https://github.com/lanmaster53/recon-ng)
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
  
# OSINT Online Tool  

- [Echosec](https://www.echosec.net/)
- [Foller](https://foller.me/)
- [Tweet Deck](https://tweetdeck.twitter.com/)
- [Tweet Trips](https://www.tweetedtrips.com/)
- [Tweet Tonomy](http://www.twitonomy.com/)
- [Twinangulate](https://www.twiangulate.com/search/)
- [Geosocial](http://geosocialfootprint.com/)
- [Hash tracking](https://www.hashtracking.com/)
- [Bellingcat](https://www.bellingcat.com/)
- [Socmint tool](http://socmint.tools/)
- [Spyse](https://spyse.com/)

# Telegram Tool  

Search channel, username anymore 

- [Telegago](https://cse.google.com/cse?cx=006368593537057042503:efxu7xprihg#gsc.tab=0)

# Linkedin 

Extension find email, people on profile Linkedin 

- [Find that lead](https://chrome.google.com/webstore/detail/findthatlead/lkpekgkhmldknbcgjicjkomphkhhdkjj?hl=en-GB)

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

# Real-Time Search, Social Media Search, and General Social Media Tools

- [Audiense](https://www.audiense.com)
- [Bottlenose](http://bottlenose.com)
- [Buffer](https://buffer.com)
- [Hootsuite](http://hootsuite.com)
- [Hashtatit](http://www.hashatit.com)
- [Rival IQ](https://www.rivaliq.com)
- [SocialBakers](http://www.socialbakers.com)
- [SociaBlade](http://socialblade.com)
- [Social Searcher](http://www.social-searcher.com)
- [Mail.Ru Social Network Search](https://go.mail.ru/search_social)
- [WATools](https://watools.io/)
- [Profil3r](https://github.com/Rog3rSm1th/Profil3r)
- [Oblivion](https://github.com/loseys/Oblivion) 

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
- [Websta](http://websta.me)
- [Worldcam](http://www.worldc.am)
- [Yahoo Image Search](https://images.search.yahoo.com)
- [Yandex Images](https://www.yandex.com/images)
- [Betaface](https://www.betaface.com/demo.html)
- [Search4faces](https://search4faces.com/)

# Image Analysis

- [ExifTool](http://www.sno.phy.queensu.ca/~phil/exiftool)
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

# Geospatial Research and Mapping Tools

* [Atlasify](http://www.atlasify.com)
* [Batchgeo](http://batchgeo.com)
* [Bing Maps](http://www.bing.com/maps)
* [CartoDB](https://cartodb.com)
* [Colorbrewer](http://colorbrewer2.org)
* [CrowdMap](https://crowdmap.com)
* [CTLRQ Address Lookup](https://ctrlq.org/maps/address)
* [Dominoc925](https://dominoc925-pages.appspot.com/mapplets/cs_mgrs.html)
* [DualMaps](https://www.mapchannels.com/dualmaps7/map.htm)
* [GeoGig](http://geogig.org)
* [GeoNames](http://www.geonames.org)
* [Esri](http://www.esri.com)
* [Flash Earth](http://www.flashearth.com)
* [Google Earth](http://www.google.com/earth)
* [Google Earth Pro](https://www.google.com/intl/en/earth/versions/#earth-pro)
* [Google Maps](https://www.google.com/maps)
* [Google Maps Streetview Player](http://brianfolts.com/driver)
* [Google My Maps](https://www.google.com/maps/about/mymaps)
* [GPSVisualizer](http://www.gpsvisualizer.com)
* [GrassGIS](http://grass.osgeo.org)
* [Here](http://here.com)
* [Hyperlapse](https://github.com/TeehanLax/Hyperlapse.js)
* [Inspire Geoportal](http://inspire-geoportal.ec.europa.eu)
* [InstantAtlas](http://www.instantatlas.com)
* [Instant Google Street View](http://www.instantstreetview.com)
* [Kartograph](http://kartograph.org)
* [Leaflet](http://leafletjs.com)
* [MapAList](http://mapalist.com)
* [MapBox](https://www.mapbox.com)
* [Mapbuildr](https://mapbuildr.com)
* [Mapchart.net](https://mapchart.net)
* [Maperitive](http://maperitive.net)
* [MapHub](https://maphub.net)
* [MapJam](http://mapjam.com)
* [Mapline](https://mapline.com)
* [Map Maker](https://maps.co)
* [Mapquest](https://www.mapquest.com)
* [Modest Maps](http://modestmaps.com)
- [NGA GEOINT](https://github.com/ngageoint)
- [OpenLayers](http://openlayers.org)
- [Polymaps](http://polymaps.org)
- [Perry Castaneda Library](https://www.lib.utexas.edu/maps)
- [Open Street Map](http://www.openstreetmap.org)
- [QGIS](http://qgis.org)
- [QuickMaps](https://chrome.google.com/webstore/detail/quick-maps/bgbojmobaekecckmomemopckmeipecij)
- [StoryMaps](http://storymaps.arcgis.com/en)
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
