from flask_restful import Resource,Api,reqparse,marshal_with,fields
from.models import db,StudyResource,Role,User

api = Api(prefix='/api')
parser = reqparse.RequestParser()

parser.add_argument('topic',type=str,help='Topic Can be String only' ,required = True)
parser.add_argument('description',type=str,help='Description Can be String only' ,required = True)
parser.add_argument('resource_link',type=str,help='Resource link Can be String only',required = True)

Study_Material_field = {
    'id' : fields.Integer,
    'topic' : fields.String,
    'description' : fields.String,
    'resource_link' : fields.String
}

class StudyMaterial(Resource):
    @marshal_with(Study_Material_field)
    def get(self):
        pass
    def post(self):
        args = parser.parse_args()
        studyresource = StudyResource(**args)
        db.session.add()
        db.session.commit()
        return studyresource
        return {'message':"Study Resources Created"}
        pass
api.add_resource(StudyMaterial,'/Study_material')