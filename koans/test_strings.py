#!/usr/bin/env python
# -*- coding: utf-8 -*-

__ = None

def test_double_quoted_strings_are_strings():
    string = "Hello, world."
    assert isinstance(string, basestring) == __

def test_single_quoted_strings_are_also_strings():
    string = 'Goodbye, world.'
    assert isinstance(string, basestring) == __

def test_triple_quote_strings_are_also_strings():
    string = """Howdy, world!"""
    assert isinstance(string, basestring) == __
    
def test_use_double_quotes_to_create_strings_with_single_quotes():
    string = "Don't"
    assert string == __

def test_use_backslash_for_escaping_quotes_in_strings():
    a = "He said, \"Don't\""
    b = 'He said, "Don\'t'
    assert (a == b) == __

def test_triple_quoted_strings_can_span_lines():
    string = """
Howdy,
world!
"""
    assert len(string) == __

def test_triple_quoted_strings_need_less_escaping():
    a = "Hello \"world\"."
    b = """Hello "world"."""
    assert (a == b) == __

def test_you_still_have_to_be_careful_at_the_end_of_a_triple_quoted_string():
    string = """Hello "world\""""

def test_plus_concatenates_strings():
    string = "Hello, " + "world"
    assert string == __

def test_plus_will_not_modify_original_strings():
    hi = "Hello, "
    there = "world"
    string = hi + there
    assert hi == __
    assert there == __

def test_plus_equals_will_append_to_end_of_string():
    hi = "Hello, "
    there = "world"
    hi += there
    assert hi == __

def test_plus_equals_also_leaves_original_string_unmodified():
    original = "Hello, "
    hi = original_string
    there = "world"
    hi += there
    assert original == __

