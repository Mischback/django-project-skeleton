#!/bin/bash

# determine the scripts current working directory (CWD)
CWD="${BASH_SOURCE%/*}";
if [[ ! -d "$CWD" ]]; then CWD="$PWD"; fi

# include the script for setting the timezone
source "$CWD/set_timezone.sh"

exec "$@"
