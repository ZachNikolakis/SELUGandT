---
title: LONI Login Activity
teaching: 0
exercises: 0
questions:
  - "What is a high-performance cluster computer?"
  - "Why is this useful for our work?"
objectives:
  - "Set up an account on the LONI computer."
  - "Log In to LONI."
  - "Understand how to use software on this machine."
---

# Making a LONI Account

LONI (Louisiana Optic Network Infrastructure) is a supercomputing network available to public institutions in Louisiana. 

Supercomputers, or high-performance cluster computers, are really just networks of computers that allow users to access enough processor power to do long jobs. Several of the computations we do this semester will be too complex or will take too long to run on your personal laptop or classroom machine, so we will send these computations to LONI.

LONI's main advantages:

* Free for use if you are an LA public institution student.
* Available on all platforms.
* Flexible to multiple software installations.
* Supports multiple programming paradigms.
* Very large community with good documentation.

## Making a LONI Account

I have already set up allocations for this course. But each of you needs to have an independent way to access those allocations. To do this, you will create a user account [here](https://allocations.loni.org/login_request.php). Please use your SELU email address for this step. Work through the steps. You should receive a confirmation email shortly about your account being set up. 

## Joining the Class Allocations

Once you have received an email confirming your account creation, go [here](https://allocations.loni.org/allocations.php?only_mach=Dell_Cluster). You will click on "Join an existing allocation," and enter my email (april.wright@selu.edu). Join the correct one for the class.

## Joining the Class Allocations

Logging in to LONI. Now, we will use our command line interfaces to log into the LONI cluster.

## Introduction to Python built-in data types

### Strings, integers and floats

Python has built-in numeric types for integers, floats, and complex numbers.
Strings are a built-in textual type.:

```python
text = "Data Carpentry"
number = 42
pi_value = 3.1415
```

Here we've assigned data to variables, namely `text`, `number` and `pi_value`,
using the assignment operator `=`. The variable called `text` is a string which
means it can contain letters and numbers. Notice that in order to define a
string you need to have quotes around your text. To print out the value
stored in a variable we can simply type the name of the variable into the
interpreter:

```python
>>> text
"Data Carpentry"
```

However, in a script, a `print` function is needed to output the `text`:

*example.py*
```python
# A Python script file
# Comments in Python start with #
# The next line uses the print function to print out the text string
print(text)
```
*Running the script*
```bash
$ python example.py
Data Carpentry
```

**Tip**: The `print` function is a built-in function in Python. Later in this
lesson, we will introduce methods and user-defined functions. The Python
documentation is excellent for reference on the differences between them.

### Operators

We can perform mathematical calculations in Python using the basic operators
 `+, -, /, *, %`:

```python
>>> 2 + 2   #  addition
4
>>> 6 * 7   #  multiplication
42
>>> 2 ** 16  # power
65536
>>> 13 % 5  # modulo
3
```

We can also use comparison and logic operators:
`<, >, ==, !=, <=, >=` and statements of identity such as
`and, or, not`. The data type returned by this is
called a _boolean_.


```python
>>> 3 > 4
False
>>> True and True
True
>>> True or False
True
```

## Sequential types: Lists and Tuples

### Lists

**Lists** are a common data structure to hold an ordered sequence of
elements. Each element can be accessed by an index.  Note that Python
indexes start with 0 instead of 1:

```python
>>> numbers = [1, 2, 3]
>>> numbers[0]
1
```

A `for` loop can be used to access the elements in a list or other Python data
structure one at a time:

```python
>>> for num in numbers:
...     print(num)
...
1
2
3
>>>
```

**Indentation** is very important in Python. Note that the second line in the
example above is indented. Just like three chevrons `>>>` indicate an
interactive prompt in Python, the three dots `...` are Python's prompt for
multiple lines. This is Python's way of marking a block of code. [Note: you
do not type `>>>` or `...`.]

To add elements to the end of a list, we can use the `append` method. Methods
are a way to interact with an object (a list, for example). We can invoke a
method using the dot `.` followed by the method name and a list of arguments
in parentheses. Let's look at an example using `append`:

```python
>>> numbers.append(4)
>>> print(numbers)
[1, 2, 3, 4]
>>>
```

To find out what methods are available for an
object, we can use the built-in `help` command:

```python
help(numbers)

Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 ...
```

### Tuples

A tuple is similar to a list in that it's an ordered sequence of elements.
However, tuples can not be changed once created (they are "immutable"). Tuples
are created by placing comma-separated values inside parentheses `()`.

```python
# tuples use parentheses
a_tuple= (1, 2, 3)
another_tuple = ('blue', 'green', 'red')
# Note: lists use square brackets
a_list = [1, 2, 3]
```

> ## Challenge - Tuples
> 1. What happens when you type `a_tuple[2]=5` vs `a_list[1]=5` ?
> 2. Type `type(a_tuple)` into python - what is the object type?
>
{: .challenge}


## Dictionaries

A **dictionary** is a container that holds pairs of objects - keys and values.

```python
>>> translation = {'one': 1, 'two': 2}
>>> translation['one']
1
```
Dictionaries work a lot like lists - except that you index them with *keys*.
You can think about a key as a name for or a unique identifier for a set of values
in the dictionary. Keys can only have particular types - they have to be
"hashable". Strings and numeric types are acceptable, but lists aren't.

```python
>>> rev = {1: 'one', 2: 'two'}
>>> rev[1]
'one'
>>> bad = {[1, 2, 3]: 3}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

In Python, a "Traceback" is an multi-line error block printed out for the
user.

To add an item to the dictionary we assign a value to a new key:

```python
>>> rev = {1: 'one', 2: 'two'}
>>> rev[3] = 'three'
>>> rev
{1: 'one', 2: 'two', 3: 'three'}
```

Using `for` loops with dictionaries is a little more complicated. We can do
this in two ways:

```python
>>> for key, value in rev.items():
...     print(key, '->', value)
...
1 -> one
2 -> two
3 -> three
```

or

```python
>>> for key in rev.keys():
...     print(key, '->', rev[key])
...
1 -> one
2 -> two
3 -> three
>>>
```

> ## Challenge - Can you do reassignment in a dictionary?
> 
> 1. First check what `rev` is right now (remember `rev` is the name of our dictionary). 
>     
>    Type:
> ```python
> >>> rev
> ```
>
> 2. Try to reassign the second value (in the *key value pair*) so that it no longer reads "two" but instead reads "apple-sauce". 
>
> 3. Now display `rev` again to see if it has changed. 
>
{: .challenge}

It is important to note that dictionaries are "unordered" and do not remember
the sequence of their items (i.e. the order in which key:value pairs were
added to the dictionary). Because of this, the order in which items are
returned from loops over dictionaries might appear random and can even change
with time.



## Functions

Defining a section of code as a function in Python is done using the `def`
keyword. For example a function that takes two arguments and returns their sum
can be defined as:

```python
def add_function(a, b):
    result = a + b
    return result

z = add_function(20, 22)
print(z)
42
```

Key points about functions are:

* definition starts with `def`
* function body is indented
* `return` keyword precedes returned value