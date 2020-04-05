#!/bin/bash

# Updates the container's timezone according to the provided environment
# variable DPS_TIMEZONE and sets UTC as default value.
#
# This script has to be run with root privileges in order to actually run
# `dpkg-reconfigure`.

set -euo pipefail

# check for the existence of DPS_TIMEZONE in environment
if [[ -v DPS_TIMEZONE ]]; then
    true \
    && echo ${DPS_TIMEZONE} > /etc/timezone \
    && ln -sf /usr/share/zoneinfo/${DPS_TIMEZONE} /etc/localtime;

# set UTC as default time zone
else
    # TODO: Untestested code! Verify that this is working! Verify the existence of path /usr/share/zoneinfo/Etc/UTC!
    true \
    && echo "Etc/UTC" > /etc/timezone \
    && ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime;
fi

# actually apply the timezone systemwide
dpkg-reconfigure -f noninteractive tzdata;
