import random

def generatePeopleList(seed=None):
    """
    Esta función genera una lista de diccionarios con ID y edad para 10 personas.    
    """
    if seed is not None:
        random.seed(seed)
    people_list = []
    for _ in range(10):
        person = {'id':len(people_list), 'age': random.randint(1,120)}
        people_list.append(person)
    return people_list

def orderPeopleListByAge(people_list):
    """
    Esta funcion ordena por edad una lista que tenga el campo "age" (edad).
    En el proceso, también imprime el ID de la persona más joven y el ID de la persona más vieja.
    >>> unsorted_list = generatePeopleList(22)
    >>> print(unsorted_list)
    [{'id': 0, 'age': 117}, {'id': 1, 'age': 18}, {'id': 2, 'age': 32}, {'id': 3, 'age': 4}, {'id': 4, 'age': 79}, {'id': 5, 'age': 58}, {'id': 6, 'age': 24}, {'id': 7, 'age': 90}, {'id': 8, 'age': 16}, {'id': 9, 'age': 95}]
    >>> sorted_list = orderPeopleListByAge(unsorted_list)
    ID de persona más joven:  3
    ID de persona más vieja:  0
    >>> print(sorted_list)
    [{'id': 0, 'age': 117}, {'id': 9, 'age': 95}, {'id': 7, 'age': 90}, {'id': 4, 'age': 79}, {'id': 5, 'age': 58}, {'id': 2, 'age': 32}, {'id': 6, 'age': 24}, {'id': 1, 'age': 18}, {'id': 8, 'age': 16}, {'id': 3, 'age': 4}]
    """
    people_list.sort(key=lambda x: x['age'], reverse = True)
    print('ID de persona más joven: ', people_list[-1]['id'])
    print('ID de persona más vieja: ', people_list[0]['id'])
    return people_list

if __name__ == "__main__":
    import doctest
    doctest.testmod()
