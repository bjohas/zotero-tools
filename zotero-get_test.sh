#!/bin/sh

. ./api_settings.sh

zotero-get --api_key=${API_KEY} --library_id=${LIBRARY_ID} --library_type=group --tag=retrieve_pdf | jq .
