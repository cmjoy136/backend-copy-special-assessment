#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "cmjoy136"

# Write functions and modify main() to call them
def get_special_paths(dir):
    """searches through directory to find __filename__ files"""
    result = []
    for filename in os.listdir(dir):
        match_obj = re.search(r'__\w+__', filename)
        if match_obj is not None:
            result.append(os.path.abspath(os.path.join(dir, filename)))
    return result

def copy_to(paths, dir):
    """takes files from get_special_paths and copies them to existing or  created directory"""
    if not os.path.exists(dir):
        os.mkdir(dir)
    for path in paths:
        shutil.copy(path, dir)

def zip_to(paths, zippath):
    """creates zipfile and places files into zip"""
    zip_command = ['zip', '-j', zippath ]
    for path in paths:
        zip_command.append(path)
    print("command im about to do")
    print(' '.join(zip_command))
    subprocess.call(zip_command)
    

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory to read from', default='.')
    args = parser.parse_args()
    paths = get_special_paths(args.from_dir)

    if args.todir:
        copy_to(paths, args.todir)

    if args.tozip:
        zip_to(paths, args.tozip)

if __name__ == "__main__":
    main()
