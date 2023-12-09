#!/bin/bash

mkdir -p /tmp/emacs-build

emacs -Q --batch --load init.el --execute "(org-publish-all)" --kill

cd /tmp/emacs-build
