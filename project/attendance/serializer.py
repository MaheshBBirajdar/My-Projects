from rest_framework import serializers
from .models import *

'''
def email_valid(value):                                      # 3) validators
	if not value.endswith('abc.com'):
		raise serializers.ValidationError("not valid")
	return value

class Attserializer(serializers.Serializer):
	stuid = serializers.IntegerField()
	stuname = serializers.CharField(max_length=100)
	stumail = serializers.EmailField(max_length=100, validators=[email_valid])


	def validate_stuid(self,value):                         # 1) Field Level Validation
		if value >= 100:
			raise serializers.ValidationError("Not Valid")
		return value


	def validate(self,data):                                # 2) Object Level Validation
		stuid = data.get('stuid')
		stumail = data.get('stumail')

		if stuid >= 100:
			raise serializers.ValidationError("Not Valid")

		if stumail.endswith("gmail.com"):
			raise serializers.ValidationError("Not valid Email")

		return data
		


	def create(self,validated_data):
		return Studentdata2.objects.create(**validated_data)



	def update(self,instance,validated_data):
		instance.stuname = validated_data.get('stuname',instance.stuname)
		instance.stumail = validated_data.get('stumail',instance.stumail)
		instance.save()
		return instance
'''


class Attserializer(serializers.ModelSerializer):
	#stumail = serializers.EmailField(max_length=100, validators=[email_valid])
	class Meta:
		model = Studentdata2
		fields = ['stuid','stuname','stumail']


