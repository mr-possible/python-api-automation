class Resources:
    __addBookResource = 'Library/Addbook.php'
    __getBookResource = 'Library/GetBook.php'
    __deleteBookResource = 'Library/DeleteBook.php'

    def get_addBookResource(self):
        return self.__addBookResource

    def get_getBookResource(self):
        return self.__getBookResource

    def get_deleteBookResource(self):
        return self.__deleteBookResource
