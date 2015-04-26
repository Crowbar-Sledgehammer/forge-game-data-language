#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import os
import subprocess

INPUT_FILE = 'fgd.YAML-tmLanguage'
OUTPUT_FILE = 'build/fgd.tmLanguage'

# Dynamic Imports
sys.path.append('./deps/AAAPackageDev/')

sys.modules['sublime'] = object

class _sublime_lib (object):
    ST2 = object()
sys.modules['sublime_lib'] = _sublime_lib

class _sublime_lib_view(object):
    OutputPanel = object
    coorded_substr = object
    base_scope = object
    @staticmethod
    def get_text(*_):
        with open(INPUT_FILE,'r') as file_handle:
            return file_handle.read()
sys.modules['sublime_lib.view'] = _sublime_lib_view

class _sublime_lib_path(object):
    file_path_tuple = object
sys.modules['sublime_lib.path'] = _sublime_lib_path

class mockWindow(object):
    pass

class outputPath(str):
    def set_path(*_):
        pass
    def write_line(*_):
        print(_)
    def show(*_):
        pass


from fileconv import dumpers, loaders

def _mkdirp(path):
    if not os.path.exists(path):
        os.mkdir(path)

def _call(command_string):
    print('{}\033[1;30m'.format(command_string))
    return_code = subprocess.call(command_string)
    print('\033[0m')
    if return_code > 0:
        exit(return_code)

def main():
    data = loaders.YAMLLoader(mockWindow, None, file_path=INPUT_FILE, output=outputPath(INPUT_FILE)).load()
    dumpers.PlistDumper(None, None, OUTPUT_FILE, file_path=OUTPUT_FILE, output=outputPath(OUTPUT_FILE)).dump(data)

if __name__ == '__main__':
    main()
