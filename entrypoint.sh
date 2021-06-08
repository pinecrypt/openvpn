#!/bin/bash
set -e
CONFIG=/server-secrets/openvpn-$1.conf
while [ ! -e $CONFIG ]; do
  sleep 1
done
curl -X DELETE http://127.0.0.1:2001/api/by-service/openvpn-$1
openvpn --config $CONFIG
