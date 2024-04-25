#!/bin/bash
# This script takes a URL, sends a GET request with a custom header.
curl -s -H "X-School-User-Id: 98" "$1"
