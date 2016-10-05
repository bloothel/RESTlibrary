from flask_restful import reqparse,  Resource
from flask_restful import abort



class RestServiceInfra(Resource):

    books = {1:{"id": "1", "title": "sss", "description": "aaa", "create_date": "fff"}}

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

