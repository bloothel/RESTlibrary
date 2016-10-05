from flask import Flask, abort
from RestServiceInfra import RestServiceInfra


class getBook(RestServiceInfra):

    def get(self,bookID):
        if bookID in self.books:
            return self.books[bookID]
        else:
            abort(404)

    def put(self,bookID):
        args = self.argument_parser([['title',str,False],['description',str,False],['create_date',str,False]],'form')
        if bookID in self.books:
            if args['title'] is not None:
                self.books[bookID]['title'] = args['title']
            if args['description'] is not None:
                self.books[bookID]['description'] = args['description']
            if args['create_date'] is not None:
                self.books[bookID]['create_date'] = args['create_date']
        else:
            self.books[bookID] = {"id": str(bookID), "title": args['title'], "description": args['description'], "create_date": args['create_date']}
        return {'Result' : 'Success'}

    def delete(self,bookID):
        del self.books[bookID]
        return {'Result' : 'Success'}
