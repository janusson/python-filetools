#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
Description:
A collection of helpful file handling functions in Python.
'''

import os

def check_for_dir(directory):
    '''
    simple check for directory presence on filesystem.

    Args:
        directory (pathlike): 

    Returns:
        bool: [description]
    '''
    if os.path.exists():
        print(f'{directory} - present.')
        return True
    else:
        print(f'{directory} - directory not found.')
        return False

def check_subdir(maybe_subdir, directory):
    '''
    checks if mayvbe_subdir is a sub-directory of 'directory'

    Args:
        maybe_subdir (pathlike): the possible sub-directory
        directory (pathlike): the possible parent-directory

    Returns:
        bool: True if sub-directory
    '''
    path = os.path.realpath(maybe_subdir)
    directory = os.path.realpath(directory)
    rel_path = os.path.relpath(path, directory)
    if rel_path.startswith(os.pardir):
        return False
    else:
        return True

def get_files_indir(data_dir = r'C:\User\Documents'):
    '''
    Search directory subdirectories experiment file folders of specified ext.
    Searches topdown from directory given.
    
    Args:

    Returns:
        list: path_list is a list of full .raw directories.
    '''
    
    data_dir = 
    print('>>>program searches topdown from directory given.')
    print(f'>>>enter data directory or use default: {data_dir}.')
    user_choice = input()
    if len(user_choice)<2:
        print(f'using default dir.')
    else:
        data_dir = user_choice
    path_list = [x[0] for x in os.walk(data_dir, 1) if x[0][-4:] == '.csv']
    print(f'Processing {len(path_list)} .csv experiment files.')

    return path_list
