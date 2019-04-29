def nolist_clean(poem):
    poem_str = ' '.join(poem)
    return poem_str.lower().translate(str.maketrans('', '', ''.join(exclude)))
