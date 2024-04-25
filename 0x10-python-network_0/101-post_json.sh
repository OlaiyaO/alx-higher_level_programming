#!/bin/bash
# This script sends a JSON POST request to a URL passed.

curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
