def anagrams(words: list[str]):
    def generate_signature(word: str):
        return ''.join(sorted(word))

    signature_to_words = dict()
    for word in words:
        signature = generate_signature(word)
        if signature not in signature_to_words:
            signature_to_words[signature] = set()
        signature_to_words[signature].add(word)

    # return only the anagrams
    return [anagrams for _, anagrams in signature_to_words.items() if len(anagrams) > 1]


def _main():
    print("complete")
    pass

if __name__ == "__main__":
    _main()

"""
Notes:
1. Brute force
- iterate over all words
- construct map from anagram map to words
- for each word, construct anagram map.
- Append each word to anagram_map_to_words value (list)
- return

analysis:
    - n is number of words
    - k is max lenght of words
O(nk + n).

constructing the map of all words i O(k), we do this for n words.
Not sure if the map is hashable in python?

2. super slow brute force (O(n^2k))
- For each word, iterate over the rest of the list to see if anagram is found.
- Can short circuit this by keeping the set of anagrams. keyed by the "root" word? then when anagram is found, check if root word is keyed to avoid duplicates

3. Preprocessing: sort by length?

4. After hinting runtime.
For each word, sort the words. anagrams are equivlant sorts.

- maintain a map of anagram with a root (sorted) word the anagram set
- traverse the list O(n)
-- for each word, sort it and see if exists in anagram map. the place it (O(klogk) + c)

Iterate over anagram_root_to_words, and print them out.

Misc:


Had to look at solution run time to tell.
Key idea: you can "sort" words instead of having generic "count". this is longer iteration on each word, but makes comparions better for MULTIPLE anagrams. Anagrams implies "ordering" -> sorting

Questions:

Not sure if the map is hashable in python? (anagram as a object)

Book solution
O(nklogk average, (n^2)klogk worst case)

you can use "sorted" directly on strings!
"""

