from collections import Counter


def get_shortest_unique_substring_reference(chars, string):
  """
  Finds the shortest substring within string that contains
  all elements in the array chars.
  Reference implementation based on the pramp.com solution

  Example
  -------
  string = 'xyyzyzyx'
  chars = ['x', y', 'z']
  
  Output: "zxy" (last 3 elements)
  """
  if not (string and chars):
    return ""
  
  # Default the result to the empty string, which we return in case we never
  # find a matching substring
  result = ""
  unique_counter = 0
  # Initialize the dict which we use to check if we've covered all
  # elements of the chars array
  chardict = dict()
  for ch in chars:
    chardict[ch] = 0
  
  left = 0
  for right in range(len(string)):
    right_char = string[right]
    # We skip over all chars that we're not interested in
    if right_char not in chardict:
      continue
      
    right_count = chardict[right_char]
    if right_count == 0:
      unique_counter += 1
    
    chardict[right_char] += 1
    
    while unique_counter == len(chars):
      length = right - left + 1
      if length == len(chars):
        return string[left:right+1]
      if (result == "") or (length < len(result)):
        result = string[left:right+1]
      
      left_char = string[left]
      if left_char in chardict:
        left_count = chardict[left_char] - 1
        if left_count == 0:
          unique_counter -= 1
      chardict[left_char] = left_count
      
      left += 1

  return result


def get_shortest_unique_substring(chars, string):
    """
    Finds the shortest substring within string that contains
    all elements in the array chars.

    Example
    -------
    string = 'xyyzyzyx'
    chars = ['x', y', 'z']

    Output: "zxy" (last 3 elements)
    """
    needed_dict = Counter(chars)
    n_missing = len(chars)
    
    i = start = end = 0
    for j, char in enumerate(string, 1):
        # We begin by extending the string
        n_missing -= needed_dict[char] > 0
        needed_dict[char] -= 1
        # If we've found enough characters, we now shrink the string again
        if not n_missing:
            while i < j and needed_dict[string[i]] < 0:
                needed_dict[string[i]] += 1
                i += 1
            # Now that we found a character that we need, we remove it and jump back into
            # the main loop
            needed_dict[string[i]] += 1
            n_missing += 1
            if end == 0 or j-i < end-start:
                start, end = i, j
            i += 1
    return string[start:end]


if __name__ == '__main__':
  # tail = right
  # head = left
  arr = ['x','y','z']
  string = "xyyzyzyx"
  
  print(get_shortest_unique_substring(arr, string))

  