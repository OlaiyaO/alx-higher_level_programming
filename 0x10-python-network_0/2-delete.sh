#!/bin/bash
# This script sends a DELETE request to the URL passed.
curl -s "$1" -X DELETE
