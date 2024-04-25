#!/bin/bash
# This script takes a URL, sends a request to it.
curl -s "$1" | wc -c
