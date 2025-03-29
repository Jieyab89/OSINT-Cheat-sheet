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