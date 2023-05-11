#!/usr/bin/python
"""
    Written by Gitahi
    Written on: March 31, 2022
    Inspired by: Adrian Kuboka's NGuard, he taught me a lot about many things including GCs
    Description: xguard is just another guard clause library, nothing new/big
"""

class Xguard:

    def not_null(self, arg):
        """
        Guard clause that raises an error if arg value is None.
        
        @param arg: The input value to check
        @type value: Any
        
        @raise ValueIsNoneError: if the input value is None. // #TODO: create custom errors
        """
        if arg is None:
            raise ValueError("Value cannot be None")

        return self

    def is_type(self, arg, argType):
        
        if not isinstance(arg, argType):
            raise TypeError(f"Value must be of type {argType}")

        return  self


    def is_gt(self, arg: int, argLim: int):
        if arg <= argLim:
            raise TypeError("Impossible")
        
        return self

    #TODO: add more checks
