# for question 1



myObejct = {
    'name' : 'Alon',
     'age' : 57,
    'bith date': '1975/01/05'

}





# for question 2
myObejct = {
    'name' : 'Alon',
     'age' : 57,
    'birth date': '1975/01/05'

}

myObejct['lastName'] = 'vilces'





# for question 3

myObejct = {
    'name' : 'Alon',
     'age' : 12,
    'birth date': '1975/01/05'

}

myObejct['Hobbies'] =  'Drink Coffe' , 'Playing video games' , 'Watching a movie','Soccer'

#for question 4

def Object():
    myObejct = {
        'name': 'Alon',
        'age': 12,
        'birth date': '1975/01/05'

    }

 #   if  'name' in myObejct:
    #    return True
#
 #   else:
   #     return False

#for question 5

def Object():
    myObejct = {
        'name': 'Alon',
        'age': 6,
        'birth date': '2002/01/05'

    }

  #  if  myObejct['age'] == 6:
  #      return True

  #  else:
   #     return False


print(Object())

#for question 6


myObejct = {
    'name': 'Alon',
    'age': 6,
    'birth date': '2002/01/05',
    'equal' : 12
}

#if myObejct['age'] == myObejct['equal']:
   # print(True)

#else:
    #print(False)

#for question 7

myObejct = {
    'name': 'Alon',
    'age': 6,
    'birth date': '1975/01/05',
    'equal' : 12
}

myObejct2 = {
    'name': 'Alon',
    'age': 6,
    'birth date': '2002/01/05',
    'equal' : 12
}


objectSet = set(myObejct)
objectSet2 = set(myObejct2)

#for i in objectSet.intersection(objectSet2):
    #print(i)

#for question 8

myObejct = {
    'name1': 'Alon',
    'age2': 6,
    'birth date3': '2002/01/05',
    'equal' : 12
}

myObejct2 = {
    'name': 'Alon',
    'age': 6,
    'birth date': '2002/01/05',
    'equal' : 12
}

objectSet = set(myObejct)
objectSet2 = set(myObejct2)

#for i in objectSet.intersection(objectSet2):
    #print(i)

#for question 9

#def Comparing_keys(myObejct,name):
  #  if name in myObejct.keys():
   #     return True
   # else:
   #     return False

myObejct = {
        'name': 'Alon',
        'age2': 6,
        'birth date3': '2002/01/05',
        'equal': 12
    }

#for question 10

#def Comparing_values(myObejct,age):
    # if age in myObejct.values():
      #  return True
    #else:
     #   return False

#myObejct = {
    #    'name': 'Alon',
   #     'age2': 6,
   #     'bith date3': '1975/01/05',
  #      'equal': 12
  #  }

#for question 11
myObejct = {
    'name': 1,
    'age2': 6,
    'birth date3': 85,
    'equal': 12
}

convertObjec=list(myObejct.items())
convertObjec.sort()

#for question 12

def update_dict(myObejct,key,value):
      myObejct[key] = value
      return myObejct

myObejct = {
    'name': 1,
    'age2': 6,
    'birth date3': 63,
    'equal': 12
}

#for question 13

def build_dict_from_list(list1,list2):
    dict = {}
    if len(list1) == len(list2):
        for i in range(len(list1)):
            dict[list1[i]] = list2[i]
        return dict
    else:
        return None
