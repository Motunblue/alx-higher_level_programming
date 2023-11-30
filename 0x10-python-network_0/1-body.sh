#!/bin/bash
# Takes a url and send GET request to the URL
curl -sI http://"$1" | grep 'HTTP/1.' | awk '{print $2}' | grep -q "200" && curl -s http://$1 
