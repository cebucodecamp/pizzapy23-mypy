#!/bin/bash

if [[ -z "$1" ]]; then
  echo "Please specify the tag."
  echo "Usage: $0 tagname"
  exit 4
fi

docker build -t cebucodecamp/pizzapy23-mypy:$1 .
