#!/bin/bash

emacs -Q --batch --load init.el --execute "(org-publish-project \"blog\" t)" --kill
