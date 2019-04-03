============
zotero-tools
============


Tools for working with Zotero API

Installation
============

> python3 -m pip install -U git+https://github.com/bjohas/zotero-tools.git

Set up your API key for Zotero and save to api_settings.sh. Then, e.g.,

> . ./api_settings.sh
> zotero-get --api_key=${API_KEY} --library_id=${LIBRARY_ID} --library_type=group --tag=retrieve_pdf_tag | jq .

Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
