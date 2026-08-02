# Jieyab ft Xquik 

<img width="2553" height="1218" alt="Image" src="https://github.com/user-attachments/assets/eb01c1ca-c577-432d-a266-5533b5b71ce0" />

# Sett up 

1. Config your Google api console here, enable and manage API Custom Search by Google  

<img width="2536" height="1210" alt="enable" src="https://github.com/user-attachments/assets/17aca5db-9869-40f0-8a9b-58eae51dce6c" />

2. Sett the api key in web console Google 

<img width="891" height="1354" alt="g-api" src="https://github.com/user-attachments/assets/1df5201e-9d8d-4450-9c46-cc83cb35eaba" />

Check the result in the table 

<img width="2121" height="1218" alt="g - api result" src="https://github.com/user-attachments/assets/1763dc2f-2382-4c94-8973-90f98678d477" />

3. Settings CSE Google to put the cx key 

<img width="2533" height="1254" alt="cx key" src="https://github.com/user-attachments/assets/b8d04387-2ac9-4302-8b04-2ea1873e610a" />

4. Add site want to crawll e.g twitter.com and x.com 

<img width="868" height="886" alt="add host and domain twitter" src="https://github.com/user-attachments/assets/caecb9d5-85c7-4fdb-8e38-e4acfc55630e" />

## Data Source 

1. Xquik API (subs there is a price)
2. Cookie (your account cookie session)  
3. Wayback Machine (Cdx API)
4. Goole CSE API (free quota 100 per day u can increase u limit with buy the service)

## Update Note

1. Update infinity scroll and load new data for twitter reply and retweets  
2. Update data corelation 
3. Fix business logic flow 
4. Monitoring (Soon)
5. MCP (Soon)
6. Add more parameter for enrichment 
7. Add no rate limit (throttle)
8. Add Google CSE data source 

## Setup

```bash
pip install -r requirements.txt
```

Edit `config.ini.example` to config.ini 

## Run Local Web Server 

```bash
python app.py
```

Open `http://127.0.0.1:5000`

# Results 

Xquik Dashboard 

<img width="2556" height="1193" alt="image" src="https://github.com/user-attachments/assets/51e9d0f3-d079-44ce-9841-378a3e1ad7e4" />

Dasboard Home 

<img width="2545" height="1085" alt="image" src="https://github.com/user-attachments/assets/232e02de-4587-4b15-be28-01e09f0e367f" />

Archive 

<img width="2556" height="1108" alt="image" src="https://github.com/user-attachments/assets/a80b4211-d1a8-4a84-9f11-64df3d878372" />

<img width="2551" height="1118" alt="image" src="https://github.com/user-attachments/assets/27c554c0-3c3e-4fae-818d-f9f5aa076fcb" />

Graph

<img width="2560" height="1098" alt="image" src="https://github.com/user-attachments/assets/0c5710e8-26eb-4c25-9bd0-4385053e2cb8" />

Vidio 

<img width="2556" height="1243" alt="image" src="https://github.com/user-attachments/assets/c40bae79-7dd5-48fb-9642-17f27bf06d18" />

Dir Output 

<img width="2131" height="1065" alt="image" src="https://github.com/user-attachments/assets/22c8900f-1418-45aa-a773-f85ac0f3f8a3" />

# Help 

About SnowflakeID -> Twitter userid : https://en.wikipedia.org/wiki/Snowflake_ID

About paramater was provided in data and dump with json file type 

<img width="2555" height="1105" alt="image" src="https://github.com/user-attachments/assets/0646b1e8-c46e-49d5-a29f-f511cea9ee47" />

Xquik API DOC

Offc doc: https://docs.xquik.com/api-reference/overview

Soon i will check more detail about Twitter or X mechanism and business logic also endpoint API was listed in Mobile and Web 

Wayback archive data source 

The server connection to the Wayback Machine archive is often down, so try bumping the thread and don't set the throttle too high, and try checking the connection manually using curl.