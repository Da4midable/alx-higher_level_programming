#!/usr/bin/python3
"""
  This function creates a copy of the string, removing the character at the
  specified position (C-style indexing, starting from 0).

  Args:
      string: The original string.
      n: The position of the character to remove (0-based indexing).

  Returns:
      A new string with the character at position n removed.
  """


def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n+1:]
