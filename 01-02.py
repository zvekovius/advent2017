#!/usr/bin/python

def main():
    with open('input', 'r') as numbers:
        add_me = []
        input_list = []
        answer = 0
        input_len = 0
        previous_number = None
        for line in numbers:
            for number in line.rstrip():
                input_list.append(number)

        input_len = len(input_list)

        half_len = input_len / 2
        len_check = input_len - 1

        for index, number in enumerate(input_list, start=0):
            # We compare to the next item in the list.
            # If we aren't at the last element
            if (index + half_len) <= len_check:
                if number == input_list[index + half_len]:
                    add_me.append(int(number))
            else:
                # How much of the list is left.
                remaining_index = len_check - index

                # get the index of looping back to element '0'
                # in the list
                new_half_len = half_len - remaining_index - 1

                if number == input_list[new_half_len]:
                    add_me.append(int(number))

        answer = sum(add_me)
        if answer != 0:
            print answer
        else:
            print 'Uh oh... The answer is 0'

if __name__ == "__main__":
    main()

