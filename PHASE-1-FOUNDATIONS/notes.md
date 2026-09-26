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
