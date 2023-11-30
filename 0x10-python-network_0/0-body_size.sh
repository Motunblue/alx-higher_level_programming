#!/bin/bash
# Send a request to display the size of the body of the response
curl -sI http://"$1" | grep 'Content-Length' | awk '{print $2}'
