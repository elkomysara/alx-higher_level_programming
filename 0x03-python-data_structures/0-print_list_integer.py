def print_list_integer(my_list=[]):
  """
  Prints all integers of a list on a separate line.

  Args:
      my_list (list, optional): The list of integers to print. Defaults to [].
  """
  for num in my_list:
    print("{:d}".format(num))

# Example usage
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
