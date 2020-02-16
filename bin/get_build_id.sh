#!/bin/sh

# This script is part of django-project-skeleton and is used to determine an
# identifier to tag Docker images.
#
# The project's Makefile will call this script and then use its output, beside
# other values/constants to construct the image's tag.
#
# Preferably the project is version controlled by git. The script will
# determine the latest commit sha1 hash (referenced by HEAD) and will also
# determine, if there are unstaged/uncommitted changes in the repository.
# The sha1 hash will be used to tag the image (see Makefile), optionally with
# an indicator for an dirty repository (during testing/staging/deployment you
# will not want 'dirty' images, because they are not deterministically
# reproducible. Nonetheless, those images will be created and may be used).
#
# If the project is not version controlled, a timestamp will be used instead.
# This is *not* recommended, because it will not allow you to recreate a
# specific image, making debugging nearly impossible.
# Additionally, the timestamp depends on the build system's timezone,
# introducing further problems, especially if the image should be used by
# people based in other timezones.
#
# TL;DR:
#   - use git to version control your project
#   - use the provided Makefile to build your Docker images
#   - profit

# determine, if the project is under version control by git
if git rev-parse --is-inside-work-tree > /dev/null 2>&1; then

    # get most recent git commit sha1 hash
	sha=$(git rev-parse --short HEAD -- 2>/dev/null);

    # use the porcelain of git status to determine, if there a unstaged
    # changes in the repository
    # TODO: How portable is this? Should this be switched to a plumbing cmd?
	if test -n "$(git status --porcelain -- 2>/dev/null)"; then
		/usr/bin/printf "%s-dirty\n" $sha;
	else
		/usr/bin/printf "%s\n" $sha;
	fi
# Oh noooo, git is not used... Provide a timestamp to identify the image!
# This should be the absolutely last resort to tag an image and is *not*
# recommended. You should really be using a VCS!
else
    # YYYYmmdd-HHMM -> 20200212-1953
    # Please note, that this depends on your system's timezone, which makes
    # identifying the resulting image *really* hard.
    # Additionally, this will *not* allow rebuilding images in a deterministic
    # way.
	date +%Y%m%d-%H%M 2>/dev/null;
fi
