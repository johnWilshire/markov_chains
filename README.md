The program in `markov.py` is a markov text generator and will generate a sentence from an input file.

For example:
``` python markov.py --filename news.txt```

Could generate:

```Delivered senator will be known mr shorten said mr abbott out.```

It works by generating a graph of word transitions and freqencies.
It then picks a random node to start on and chooses the next word based off of words that appeared next to it in the input text.
This process is repeated until either a word is reached that has no transitions, or until an arbitrary sentance length is reached.
