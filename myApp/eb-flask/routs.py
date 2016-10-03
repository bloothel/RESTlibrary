from flask import Flask
from RestServiceInfra import RestServiceInfra

books = {1:{"id": "1", "title": "sss", "description": "aaa", "create_date": "fff"}}

class getBook(RestServiceInfra):

    def get(self,bookID):
        return books[bookID]

    def put(self,bookID):
        args = self.argument_parser([['title',str,False],['description',str,False]])
        if args['title'] is not None:
            books[bookID]['title'] = args['title']
        if args['description'] is not None:
            books[bookID]['description'] = args['description']
        return {'Result' : 'Success'}

    def delete(self,bookID):
        try:
            del books[bookID]
        except KeyError:
            pass
        return {'Result' : 'Success'}
