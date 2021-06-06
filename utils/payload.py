def addBookPayload(bookName, isbn, aisle, authorName):
    """
    @return: Returns the json payload required for adding a book to the database.
    """
    content = {
        'name': bookName,
        'isbn': isbn,
        'aisle': aisle,
        'author': authorName
    }
    return content


def deleteBookPayload(bookId):
    """
    @return: Returns the json payload required for deleting a book based on @param: bookId from the database.
    """
    content = {
        'ID': bookId
    }
    return content
