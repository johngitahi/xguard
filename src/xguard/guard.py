#!/usr/bin/python
"""
Written by Gitahi
Written on: March 31, 2022
Inspired by: Adrian Kuboka's NGuard, he taught me a lot about many things including GCs
Description: xguard is just another guard clause library, nothing new/big
"""


class Xguard:
    """
    A guard clause library for checking input values
    """

    def not_null(self, arg):
        """
        Guard clause that raises an error if arg value is None.

        @param arg: The input value to check
        @type arg: Any

        @raise ValueError: if the input value is None. // #TODO: create custom errors
        """
        if arg is None:
            raise ValueError("Value cannot be None")

        return self

    def is_type(self, arg, arg_type):
        """
        Guard clause that raises an error if arg type is not of the
        specified type(arg_type)

        @param arg: The input value to check
        @type arg: Any

        @param arg_type: The type to check against
        @type arg_type: type

        @raise TypeError: if the input value is not of the specified type.
        """
        if not isinstance(arg, arg_type):
            raise TypeError(f"Value must be of type {arg_type}")

        return self

    def is_gt(self, arg: int, arg_lim: int):
        """
        Guard clause that raises an error if arg value is less than or equal to the specified limit.

        @param arg: The input value to check
        @type arg: int

        @param arg_lim: The limit to check against
        @type arg_lim: int

        @raise TypeError: if the input value is less than or equal to the specified limit.
        """
        if arg <= arg_lim:
            raise TypeError("Impossible")

        return self
