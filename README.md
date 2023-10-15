# Room Monitoring Node

Python script to run a temperature/humidity sensor and write the results to a index.html, which is server by a http server on port 8000. Designed to be easily extendable with more sensors, user interfaces, etc.

## Install requirements

Start by setting up your virtual environment

```python3 -m venv .venv```

Activate your virtual environment

```. .venv/bin/activate```

Install requirements

```pip install -r requirements.txt```

## Run the node

Run the node by running startNode.py

```python3 startNode.py```

Using C-c will kill the node and clean up the activated threads.

## Access results

Results are currently visible by accessing `http://<IP>:8000`

## Setup service (systemd)

Note that this may expose more files than you would like to. This is not secure(!!!) and will be changed in the near future.

Adjust `monitorNode.service.example` with the paths to your repository for ExecStart and ExecStop

i.e.

```
[Unit]
Description=Run Monitoring Node
After=multi-user.target

[Service]
Type=idle
ExecStart=/PATH/TO/YOUR/REPO/runAsService.sh
ExecStop=/PATH/TO/YOUR/REPO/stopService.sh

[Install]
WantedBy=multi-user.target
```

Then copy this file to /lib/systemd/system/monitorNode.service

```sudo cp ./monitorNode.service.example /lib/systemd/system/monitorNode.service```

To start the service, run

```sudo systemctl start monitorNode.service```

Enable the service

```sudo systemctl enable monitorNode.service```

Stop the service

```sudo systemctl stop monitorNode.service