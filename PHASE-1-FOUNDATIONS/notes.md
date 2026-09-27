## Phase 1 — Foundations

1. Environment Setup
2. Numbers & Strings
3. Collections — lists, tuples, sets, dictionaries
4. Variables & Operators

# Numbers

int, float, and complex
#Integers (int) have arbitrary precision; isn't stored in a fixed number of bits like 32 or 64.
#Floats (float) stored using IEEE 754(international standard almost every language uses for decimal numbers — 64 bits per number);
-it stores numbers in binary fractions, not decimal ones. In Dosage or measurement math, these tiny errors can silently accumulate.
-Numbers are objects (a value bundled with a type and identity) like everything else in python.
-numbers are immutable, trying it creates brand new object and re-points the var name to it.

#Operators
#rounding

# Strings

-A string (str) is an ordered sequence of Unicode characters.
-strings are immutable — .upper(), .replace(), slicing, all of it returns a new string; nothing modifies the original object in place.

#Indexing & slicing
-str[index] gets one character
-str[start,stop] gets a slice (start included, stop excluded)
-str[-1] gets the last character
-str[::2] steps by 2

#Core methods
.strip() (removes leading/trailing whitespace)
.split(sep) (breaks a string into a list at each occurrence of sep)
.join(iterable) (the reverse — glues a list of strings back together with a separator)
.replace(old, new),
.upper()/.lower()

#f-strings(formatted string literals — f"text {expression}")
-modern way to build strings from values.
-They also support format specs: f"{value: format_specifier}. e.g f"{value:.2f}" forces 2 decimal places and f"{name:<10}" left-pads to width 10.

#Comparison is lexicographic- compared character by character using each character's underlying numeric code.
It's case-sensitive — 'A' < 'a' is True.
Every uppercase letter has a lower code point than every lowercase letter.
If neither string finds a differing character and one just runs out first, the shorter one wins as "lesser": "cat" < "catalog" is True — they match for 3 characters, then "cat" simply ends.
sorted() and .sort() use exactly this rule internally

#Method chaining: each method returns a new string, and the next method runs on that result.

## Collections- lists, tuples, sets and dictionaries.

##Lists
-A list is an ordered, mutable sequence collecting items not merely of the same type.
-Indexing and slicing work identically to strings.
The real difference: can change an item in place — my_list[0] = "new value"— no new object gets created, the same list object is mutated.
#Core methods:
1 .append(x) (add to the end)
2 .insert(i, x)
3 .remove(x) (removes by value x inside the list),
4 .pop(i) (removes and returns the item at index i, defaults to the last item),
5 .sort() (sorts in place, returns None),
6 .reverse(),
7 .extend() (merges another list in)
8 .sorted(my_list) is different from .sort() — it returns a new sorted list and leaves the original untouched.
#list_b = list_a does not copy anything — both names now point at the same list object. Mutate one, and the other changes too, because there's only one list, with two names for it.
A real independent copy needs .copy(), list(list_a), or list_a[:].

##Tuple
-ordered like a list, but immutable
-No .append(), no item assignment — once built, it's fixed.
-Used for things that are conceptually a single fixed unit (a coordinate, a fixed-format row)
-single-item tuple needs a trailing comma — (5,), not (5) (which is just the integer 5 in parentheses).
-Syntax=> () not []

##Sets
-unordered, and every item is unique
-no duplicates, ever — adding a duplicate is silently ignored
-No indexing, since "unordered" means there's no position to index.
Written {1, 2, 3} — but {} alone makes an empty dict, not a set; empty set is set().
| (union — everything from both)
& (intersection — only what's in both)
-(difference — in this one but not the other).

##Dictionary(dict)
-key-value pairs, like a labeled record.
-{"name": "Moyo", "age": 34}
-Access by key, not position: record["name"]
-.get(key, default) is the safe version — returns default instead of crashing if the key doesn't exist.
-Mutable, just like lists;
-record["age"] = 35 updates it in place; record["ward"] = "ICU" adds a brand-new key.

## Operators Roundup

-Augmented assignment — x += 1 is shorthand for x = x + 1
-Same for -=, multiplication, /=, //=, %=, modulus
#Logical operators
and (both sides must be true),
or (at least one side true),
not (flips a boolean)
#Truthiness — every value has an implicit True/False-ness, even outside actual booleans.
-0, 0.0, "", [], {}, set(), and None are all "falsy."
-Almost everything else is "truthy."
#Membership- in / not in
-check whether something exists inside a list, set, string, or dict (checks the keys for a dict, not the values).
