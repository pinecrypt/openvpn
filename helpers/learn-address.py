#!/usr/bin/env python
import os
import sys
import requests

# TODO: Replace with curl based script

operation, addr = sys.argv[1:3]
if operation == "delete":
    pass
else:
    common_name = sys.argv[3]
    requests.post("http://127.0.0.1:2001/api/by-serial/%d" %
      int(os.environ["tls_serial_0"]),
      data={
        "service": os.environ["service"],
        "internal_addr": addr,
        "remote_addr": os.environ["untrusted_ip"],
        "remote_port": os.environ["untrusted_port"]
    })
