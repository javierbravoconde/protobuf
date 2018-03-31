import person_pb2
from google.protobuf.json_format import MessageToJson, Parse

person = person_pb2.Person()

person.name = "name"
person.id=1
person.email = "email@email.com"

json_string = MessageToJson(person)

print(json_string)



person_parsed = Parse(json_string, person_pb2.Person())
print(person_parsed.SerializeToString())
