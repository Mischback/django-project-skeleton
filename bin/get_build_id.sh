#!/bin/sh

if git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
	sha=$(git rev-parse --short HEAD);
	if test -n "$(git status --porcelain)"; then
		/usr/bin/printf "%s-dirty\n" $sha;
	else
		/usr/bin/printf "%s\n" $sha;
	fi
else
	date +%Y%m%d-%H%M 2>/dev/null;
fi
