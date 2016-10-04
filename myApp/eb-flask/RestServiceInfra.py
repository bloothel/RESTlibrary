import os
import sys
from flask_restful import reqparse,  Resource
from flask_restful import abort
from flask_httpauth import HTTPBasicAuth
import datetime
import zipfile

# The application context is created and destroyed as necessary.
# It never moves between threads and it will not be shared between requests.
# As such it is the perfect place to store database connection information and other things
from flask import g



class RestServiceInfra(Resource):

    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','csv','zip','gz','json'])
    auth = HTTPBasicAuth()
    sqlPath=""
    project_path = ""
    books = {1:{"id": "1", "title": "sss", "description": "aaa", "create_date": "fff"}}

    def __init__(self):
        self.project_path = os.path.dirname(os.path.dirname(__file__))

    def get(self):pass

    def put(self):pass

    def argument_parser(self, arg, location='args'):
        parser = reqparse.RequestParser()
        for argument in arg:
            parser.add_argument(argument[0], type=argument[1], location=location,
                                help='%s argument have to contains %s type' %(argument[0],argument[1]), required=argument[2])
        parsed_args=parser.parse_args()
        if location=='files':
            for name,arg in parsed_args.iteritems():
                if not self.allowed_file(arg):
                    abort(http_status_code=409, errors="File type of file %s not authorized" %(argument[0]))
        return parsed_args

    @property
    def fullSqlPath(self):
        return os.path.normcase ( self.project_path + self.sqlPath)

    def convertToJson(self,result):pass

    def allowed_file(self,file):
        if file.filename.rsplit('.', 1)[1] == 'zip':
            zip_ref = zipfile.ZipFile(file)
            for z in zip_ref.infolist():
                if '.' in z.filename and not z.filename.rsplit('.', 1)[1] in self.ALLOWED_EXTENSIONS:
                    return False
            return True
        return '.' in file.filename and file.filename.rsplit('.', 1)[1] in self.ALLOWED_EXTENSIONS
