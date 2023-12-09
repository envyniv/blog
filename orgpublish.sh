#!/bin/bash

HOME=/tmp/emacs-build


mkdir -p $HOME
cp -r "$(pwd)/init.el" $HOME

emacs -Q --batch --load $HOME/init.el --execute "(org-publish-all)" --kill
