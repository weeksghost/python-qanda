"""

Implement a function that uses a word list
to return the anagrams of a given word.

"""

def annograms(word):

    words = [w.rstrip() for w in open('WORD.LST')]
    sword = sorted(word)
    annogram = [w for w in words if sorted(w) == sword]
    if annogram:
        return annogram
    else:
        raise NotImplementedError

if __name__ == "__main__":

    print annograms("train")
    print '--'
    print annograms('drive')
    print '--'
    print annograms('python')

