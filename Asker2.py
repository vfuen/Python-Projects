import Asker

#asks 2 times becasue i call the function twice
Asker.asker()


# call it a third time using another import but just importing the function.
from Asker import asker

asker()

#Using 'as' method to import the function as a different name
from Asker import asker as askr

askr()

import Asker as a

a.asker()