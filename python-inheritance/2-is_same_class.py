#!/usr/bin/python3
''' Check if the object is an exact instance of the specified class '''


def is_same_class(obj, a_class):
    '''Check if the object is an instance of the class given'''
    return type(obj) is a_class
