# xguard

Xguard is yet another guard clause library.

## What are Guard Clauses
A guard clause is simply a check that immediately exits the function, either with a return statement or an exception. If you're used to writing functions that check to ensure everything is valid for the function to run, then you write the main function code, and then you write else statements to deal with error cases, this involves inverting your current workflow. The benefit is that your code will tend to be shorter and simpler, and less deeply indented. [Credit](https://deviq.com/design-patterns/guard-clause)

## How to use this package 
Using this package is easy. Just import the package, create an instance of the Xguard class, and start chaining your guard clauses together.

In dev mode, if you still encounter a lot of import errors, and you think you know what you are doing, try to add the xguard dir to the python path.
```
export PYTHONPATH=/path/to/parent/directory:$PYTHONPATH
```

Here's an example:
```python
from xguard import guard

def add_ten(number: int):
    guard = guard.Xguard()
    guard.not_null(number) \
         .is_type(number, int) \
         .is_gt(number, 0)

    # if we made it here, we have succeessfully used the guard clause, kudos!
    return number + 10;

res: int = add_ten(5) # 120
print(res)

# Good Issue: Try to use the guard clauses in a factorial function
```
See? Easy!

# For testing
``` python
python -m unittest discover tests/
```

## Why I wrote the library
I wrote xguard because I wanted to create something useful for other developers like myself. As someone who has written a lot of code, I know how frustrating it can be to spend time tracking down errors caused by bad inputs. I wanted to make it easier for developers to catch these issues early on and write more robust code.

It was also an opporuinty for me to improve on a similar project by Adrian without wrecking his original idea. I am adding some extra features like custom error messages to make it more powerful and flexible. With custom error messages, developers can quickly understand what went wrong when a guard clause fails.

Overall, my main motivation for creating xguard was to write something that I found useful and that I hope other developers will find useful as well. I believe in the power of open source software and I would love for others to contribute to the project. If you have any feedback or suggestions, please feel free to share them or even open a pull request on GitHub. Together, we can make xguard even better.

## Documentation
Each guard method is documented with a docstring that explains its purpose and usage, following the reST style. You can access the documentation for each method using Python's built-in `help` function

## License
This library is released under the GNU GPLv3 License. See the LICENSE file for details.

## Acknowledgements
This library is based on the ideas and code of Adrian's [similar project](https://github.com/veldfolds/NGuard). Thank you, Adrian!

