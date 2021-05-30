def addBookPayload():
    """
    @return: Returns the json payload required for adding a book to the database.
    """
    content = {
        'name': 'Life Lessons from Rajni',
        'isbn': 'abght865',
        'aisle': '89',
        'author': 'Rajnikanth'
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