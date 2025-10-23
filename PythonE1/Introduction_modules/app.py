# import helper_str
from utils.helper_str import upperString, firstLetterUpper
from models.students import students

from models.glaces import glaces 

"""
Une autre manière de faire plus explicite mais plus verbeuse :
import models.glaces
print(models.glaces.glaces)
"""

print( upperString("hello world") )
print( firstLetterUpper("alan") )

print(students)

print(glaces)

