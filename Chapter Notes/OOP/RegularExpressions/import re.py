import re

l = "Beautiful is better than ugly"

matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

string = "Two too."

m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

line = "123?34 hello?"

m = re.findall("\d", line, re.IGNORECASE)
print(m)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)

for match in found:
    print(match)

text = """
Giraffes have aroused the curiosity of __PLURAL_NOUN__ since the earliest times. The giraffe is the tallest of 
all living __PLURAL_NOUN__, but scientists are unable to explain how it got its long __PART_OF_THE_BODY__. 
The giraffe's tremedous height, which might not reach __NUMBER__ __PLURAL_NOUN__, 
comes from its legs and __BODYPART__"""

def mad_libs(mls):
    """
    :param mls: STring with parts the user should fill out surrounded by double underscores.
    Underscores cannot be insidew hint. e.g., no __hint_hint__ only __hint__"""
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("Invalid mls")
mad_libs(text)
    
line = "I Love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)