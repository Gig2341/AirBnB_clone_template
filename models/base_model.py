#!/usr/bin/python3
import uuid
from datetime import datetime


'''this module represents the base model'''

class BaseModel:
	'''
		This class represents the base model
	'''
	def __init__(self, *args, **kwargs):
		"""
		Initializes the BaseModel class
		
		Args:
			id : unique string id of each instance
			created_at : current datetime when an instance is created
			updated_at :  current datetime when an instance is updated
		"""
		
		if len(kwargs) != 0:
			self.__dict__ = kwargs
			self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
			self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()


	def __str__(self):
		"""
			string representaion of the class
		"""
		return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""
			updates the public instance attribute updated_at with the current datetime
		"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""
			returns a dictionary containing all keys/values of __dict__ of the instance
		"""
		my_dict = self.__dict__
		my_dict["__class__"] = type(self).__name__
		my_dict["created_at"] = self.created_at.isoformat()
		my_dict["updated_at"] = self.updated_at.isoformat()
		return my_dict

