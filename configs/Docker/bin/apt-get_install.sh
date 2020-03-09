#!/bin/bash

set -euo pipefail

# This script is used to install packages into Debian-based images.
#
# It may be called with a list of Debian packages and will automatically
# perform the refresh of apt's list (apt-get upate) and then install the
# requested packages.
# To keep the Docker images small, apt's lists are removed.
#
# This sequence of action is found in many Debian-based images, usually
# implemented by a single RUN command with several '&&'-chained commands.
# This solution was discovered in Mozilla's bedrock repository[1]. It improves
# readability of the Dockerfile and is easy enough to provide.
#
# [1]: https://github.com/mozilla/bedrock


# stop the script, if any of the commands fails
set -e

# update apt's sources lists
apt-get update

# install the specified packages and their dependencies
# do NOT install 'recommended packages'
apt-get install -y --no-install-recommends "$@"

apt-get autoremove
apt-get clean

# remove apt's sources lists
rm -rf /var/lib/apt/lists/*
