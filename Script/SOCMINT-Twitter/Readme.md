# Jieyab ft Xquik 

## Data Source 

1. Xquik API 
2. Cookie (your account cookie session) 
3. Wayback Machine (Cdx API)

## Update Note

1. Update infinity scroll and load new data 
2. Update data corelation 
3. Fix business logic flow 
4. Monitoring (Soon)
5. MCP (Soon)
6. Add more parameter for enrichment 
7. Add no rate limit (throttle)

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