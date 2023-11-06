# Sort My Animals Kata
# https://www.codewars.com/kata/58ff1c8b13b001a5a50005b4
def sort_animals(input):
    return sorted(input,key=lambda x: (x.number_of_legs, x.name))

 
