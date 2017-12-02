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

        for index, number in enumerate(input_list, start=0):
            # We compare to the next item in the list.
            # If we aren't at the last element
            if (index + 1) < input_len:
                if number == input_list[index + 1]:
                    add_me.append(int(number))

            # It's a ring, so if we are at the last element
            # compare to the first element
            if index == (input_len - 1):
                if input_list[0] == number:
                    add_me.append(int(number))

        answer = sum(add_me)

        if answer != 0:
            print answer
        else:
            print 'Uh oh... The answer is 0'

if __name__ == "__main__":
    main()

