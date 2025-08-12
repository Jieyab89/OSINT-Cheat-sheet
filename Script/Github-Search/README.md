# Tips Search on Github 

You are required to log in to get the best results

1. Navigate on Github search 
2. Search by "search qualifier." on Github, here the example qualifier 

Repository & Owner

> repo:owner/repo 
>
> user:username
> 
> org:orgname

File & Code 

> filename:name
>
> path:path
>
> extension:ext
> 
> language:lang

Text & Content

> in:name
>
> in:description
>
> in:readme
>
> in:file
> 
> in:path

Issue & PR

> is:issue
>
> is:pr
>
> is:open / is:closed
> 
> author:user
> 
> assignee:user
>
> mentions:user
>
> commenter:user
>
> label:label
> 
> milestone:name

Repo Metadata

> stars:>100
>
> forks:<50
>
> size:>1000
>
> created:>=2024-01-01
> 
> pushed:>2025-08-01
>
> archived:true

Example 

```
repo:olliebennett/getavatar.info path:*.js hash
```

![image](https://github.com/user-attachments/assets/550bd914-d29a-47fe-a5b3-12176322fbf8)
![image](https://github.com/user-attachments/assets/3fdf25a8-4e8d-463b-acc5-b61a6b705d11)

You can hunting for search initial access or something like username, mention or other things 

3. Or you can clone the repo target for deep analysis, because Github search have many factor: 

- Repo content changes

1. If there are new commits, files deleted, renamed, or added, the search results will change accordingly.
2. However, these changes don't appear immediately — GitHub needs time (sometimes minutes, sometimes hours) to update the index.

- Indexing delay & caching

1. GitHub doesn't read the repository contents directly from the disk every time we search.
2. It uses a search index that is periodically refreshed.
3. This means you can open a file directly in the repository and see the keyword there, but the search hasn't found it yet.

and other things, so you can analysis manual with command grep to gather information 

```
git -C ../<pathdir> grep -n "ip" -- '*.c'
```

![image](https://github.com/user-attachments/assets/1f0b081d-3906-48d4-96dc-75dd20f3a465)

4. There is another way, which is to search everything in the Github repo, but after I tried it, there were some shortcomings, such as the search results for each user being different because Github has its own way of indexing data, so there is a possibility of missing or not fetching something. However, this can still be used if you want to find initial access

![image](https://github.com/user-attachments/assets/9dae2d72-7c5d-43e8-80c3-1f94aaae6449)

Results 

![image](https://github.com/user-attachments/assets/8d247ce3-768d-407e-9577-e96d7ef246db)

5. You can also use the Github advanced search, its like Google dorking with fillter by paramater 

![image](https://github.com/user-attachments/assets/7f6a8956-64c7-40fc-8fbc-76d6b22e846d)

and analysis the results 

6. Happy hunting, soon i will added code search  

Endpoint list Github 

- https://github.com/search?q=<value>
- https://github.com/search?type=code&q=<value>
- https://github.com/search?type=repositories&q=<value>
- https://github.com/search?type=issues&q=<value>
- https://github.com/search?type=commits&q=<value>
- https://github.com/search/advanced