FROM python:3-alpine
RUN apk add --update --no-cache openvpn curl bash
RUN pip install requests
ADD helpers /helpers
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT /entrypoint.sh
