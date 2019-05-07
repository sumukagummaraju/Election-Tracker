from rest_framework import serializers
from ET_App.models import User,Questions,Option,UserSelectedOption
#for serialization
                                                                                 #for deserialization

#Serializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #fields = ('userId', 'firstName', 'lastName', 'age','gender','state','email')



class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields='__all__'
        #fields = ('questionId','question')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('option1','option2','option3','option4')
        fields = '__all__'



"""
class UserSelectedOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSelectedOption
        fields = ('userId','questionId','optionId','timeRegistered')
"""







