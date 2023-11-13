# serializers are used for transfer data of our models to other languages like in case we return the dictionary of the 
# languages which are the json objects





# class Meta:: In Django and Django REST Framework, the Meta class is used to provide additional information 
# about the configuration of a model or serializer. It's a container for various metadata.
# model = Languages: This line specifies the model that the serializer is associated with. In this case, 
# the model is assumed to be named Languages. This means that this serializer will be used to convert 
# instances of the Languages model to and from JSON.
# fields = ('id', 'name', 'paradigm'): This line specifies which fields from the associated 
# model (Languages in this case) should be included in the serialized representation. In 
# other words, when an instance of the Languages model is serialized using this serializer,
#  only the fields listed here (id, name, paradigm) will be included in the output.

from rest_framework import serializers
from .models import Languages
# serializers.ModelSerializer this will show the information about the model
class LanguageSerializer(serializers.HyperlinkedModelSerializer):# this will show the information about the model with 
    class Meta:
        model=Languages
        fields=('id','url','name','paradigm')