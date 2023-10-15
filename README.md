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