#!/bin/bash

if [[ -v DPS_TIMEZONE ]]; then

    true \
    && echo ${DPS_TIMEZONE} > /etc/timezone \
    && ln -sf /usr/share/zoneinfo/${DPS_TIMEZONE} /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata;

fi

# actually execute the provided command, but drop privileges using gosu
exec gosu pythonuser "$@"
