import string

a_to_z = string.lowercase

def is_pangram(self):
    return set(string.lowercase).issubset(set(self.lower()))
