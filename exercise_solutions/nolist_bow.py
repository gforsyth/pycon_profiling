def bag_of_words_nolist(poem):
    poem_str = nolist_clean(poem)
    counter = collections.Counter(poem_str.split(' '))
    return counter
