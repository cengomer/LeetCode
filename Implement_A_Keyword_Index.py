def keyword_index(docs):
    index = {}
    for doc_idx, doc in enumerate(docs):
        for word in doc.split():
            if word in index:
                index[word].append(doc_idx)
            else:
                index[word] = [doc_idx]
    return index