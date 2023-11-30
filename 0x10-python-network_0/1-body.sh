#!/usr/bin/env bash
# Takes a url and send GET request to the URL
# Display the body of the reponse with 200 status code

url="http://$1"
status=$(curl -sI $url | grep 'HTTP/1.' | awk '{print $2}')

if [ "$status" -eq 200 ]; then
    curl $url
fi

