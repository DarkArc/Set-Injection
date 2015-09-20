# Set Injection

This project is a very simple script for quickly generating text, given a collection of inputs.

# Configuration

There are two variables in the script which are of interest:
````python
separateFiles = False

gen = [
    ['a', 'dog'],
    ['my', 'cow'],
    ['a', 'dragon']
]
````

gen defines the list of outputs. Each sub list will create a new output.

As one might expect, if separateFiles is set, each output will be a new file. If seperateFiles is left at its default value, each output will be appended to the output file.

# Example

The default setup, is configured for function with Test.txt:
````
Hello {{0}} {{1}}
````

Which is translated to:
````
Hello a dog
Hello my cow
Hello a dragon
````

As you can see, the number inside of brackets correlates to the index of the value in the sub list. Thus, {{0}} is resolved to 'a', and {{1}} is resolved to 'dog' in the first output.
