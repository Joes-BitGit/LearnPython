#!/usr/local/bin/python
# coding: UTF-8

'''

Write a short program that prints each number from 1 to 100 on a new line.

For each multiple of 3, print "Fizz" instead of the number.

For each multiple of 5, print "Buzz" instead of the number.

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

'''

def fizzBuzz(n: int):
    nums = []
    # hashmap to hold divisible numbers
    # makes it much easier to add any other numbers needed to be divisible
    fizzbuzz_dict = {3:'Fizz', 5:'Buzz', 7: 'Jazz'}
    # loop through until n
    for i in range(1,n+1):
        ans_str = ''
        # iterate over the dictionary to check if their are any numbers divisible
        for key in fizzbuzz_dict.keys():
            # concatenate if necessary
            # eg if n == 15
            # 3 -> 'Fizz' then ans_str = 'Fizz'
            # 5 -> 'Buzz' then ans_str = 'FizzBuzz'
            if i % key == 0:
                ans_str += fizzbuzz_dict[key]
        # if the string is empty then the number was not divisible
        # by anything in the hashmap
        if not ans_str:
            ans_str = str(i)

        nums.append(ans_str)
    return nums


if __name__ == '__main__':
    print(fizzBuzz(105))
