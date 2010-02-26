#!/usr/bin/env python
# -*- coding: utf-8 -*-

__ = 0

def test_None_is_an_object():
    assert __ == isinstance(None, object), "Unlike NULL in other languages"

def test_None_is_universal():
    """
    There is only one None.
    """
    assert None is __ 

def test_None_is_distinct():
    """
    None is distinct from other things which are False.
    """
    assert __ is not 0
    assert __ is not False

def test_what_exception_do_you_get_when_calling_nonexistent_methods_on_None():
    """
    What is the Exception that is thrown when you call a method that does
    not exist?
    
    Hint: launch python and try the code in the block below.
    
    Don't be confused by the code below yet.  It's using blocks which are
    explained later on in test_blocks.py.
    """
    # FIXME: best way to do assert_raises?
    #assert_raises(__, None.some_method_none_doesnt_know_about)
    
