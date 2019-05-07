from json import JSONDecodeError

from rest_framework import viewsets
from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import json



from ET_App.models import User, Questions, Option
from ET_App.serializers import UserSerializer, QuestionsSerializer, OptionSerializer

"""
user1=User(1, "Sumuka", "G", 23, "male","Karnataka","sumuka@gmail.com")          #How do I make this Dynamic ?
user1.GetUsers()
print(user1)
"""

def AddUser(request):

   #Validate the email-Id sent by UI

   def authenticate(self, emailId,password):





    with open(request) as f:
        try:
            return json.load(f).get('user', [])  # put JSON-data to a variable
        except JSONDecodeError:
            return "Invalid JSON"

    Userlist = []

    for element in request:
        Userlist.append(User(element))
        print(element)
        #
        # '''
        # for u in UserList:
        #     # call api add method
        #
        # '''
        #
        # if request.method == 'POST':
        #      return Response({"message": "Got some data!", "data": request.data})
        # else:
        #     return Response({"message": "Hello, world!"})
        #


'''
user2 = User("3","Adarsh","R","25","male","Karnataka" , "ada@gmail.com","abcd")
user2.AddUser()
print(user2.Age)
'''




#Viewsets - API endpoint that allows messages to be viewed or edited

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def post(self, request, format='json'):
    #     serializer = UserSerializer(data = request.data, many = True)
    #     if serializer.is_valid():
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    #serializer_class = serializer.QuestionsSerializer
    serializer_class = QuestionsSerializer

class OptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer



# class UserDetailsSet(viewsets.ModelViewSet):
#     queryset = UserDetails.objects.all()
#     serializer_class = serializer.UserSerializer
#     serializer_class = serializer.UserSerializer




'''
question1=Question(1, "Choose for Question1","A","B","C","D")
question1.GetQuestions()
print(question1)
'''

'''
userdetail1=UserDetails(1, 1, 1)
userdetail1.GetUserDetails()
'''

