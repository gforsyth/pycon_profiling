def third(poem):
    poem2 = []
    for line in poem:
        poem2.append(re.sub("[^a-z\s]", "", line.lower()))
    return poem2
