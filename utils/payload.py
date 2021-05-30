def addBookPayload():
    """
    @return: Returns the json payload required for adding a book to the database.
    """
    content = {
        'name': 'Learn Basics of API Automation',
        'isbn': '67767676',
        'aisle': '22',
        'author': 'Mark Manson'
    }
    return content
