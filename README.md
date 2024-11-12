# Nmap-as-a-service
Nmap service using Flask & Redis to implement a worker that waits for scanning jobs requested.

# Installation
```shell
sudo apt update && sudo apt install -y nmap redis python3-venv
```

```shell
python3 -m venv .venv
. .venv/bin/activate
sudo pip install flask rq python3-nmap
```

- Start the worker
```shell
rq worker
```

- Start the flask server
```shell
python3 flask-server.py
```
