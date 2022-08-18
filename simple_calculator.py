import re


def add(str):
    if len(str) == 0:
        return 0

    elif str.startswith("//"):
        if len(str) == 2:
            return -1

        first_line = []
        second_line = []



        if str.find("\n")  != -1 and str.find("\n") + 1 >= len(str):
            return 0

        for index in range(len(str)):
            if str[index] == "\n":
                first_line = str[2:index]
                second_line = str[index + 1:]
                break
        
        # first_line = re.sub(r'(.)\1+', r'\1', first_line)[1:-1]
        first_line = first_line[1:-1]
        delimiter_list = []

        if len(first_line) == 1:
            delimiter_list = list(first_line)
        else:
            delimiter_list = first_line.split("][")            
            for d in delimiter_list:
                if len(d) > 0:
                    second_line = second_line.replace(d, d[0])

        numbers = second_line
        for item in delimiter_list:
            if len(item) > 0:
                numbers = numbers.split(item[0])
                numbers = ','.join(numbers)
        numbers = numbers.split(",")


        is_there_neg_nums = False
        is_valid = True
        raised_error = "negatives not allowed"
        neg_nums = ""


        for item in numbers:
            if item.startswith("-"):
                if len(item) > 1 and item[1:].isnumeric():
                    neg_nums += " " + item[1:]
                    is_there_neg_nums = True
                else:
                    is_valid = False
            elif not item.isnumeric():
                is_valid = False

        if not is_valid:
            return -1

        if is_there_neg_nums:
            if len(neg_nums.split(" ")) > 2:
                raise ValueError(raised_error + "".join(neg_nums))
            else:
                raise ValueError(raised_error)

        result = 0
        for num in numbers:
            if int(num) <= 1000:
                result += int(num)
        return result


    else:
        # or replace \n with , and then split based on ,
        numbers = re.split(',|\n', str)

        is_there_neg_nums = False
        is_valid = True
        raised_error = "negatives not allowed"
        neg_nums = ""
        for item in numbers:
            if item.startswith("-"):
                if len(item) > 1 and item[1:].isnumeric():
                    neg_nums += " -" + item[1:]
                    is_there_neg_nums = True
                else:
                    is_valid = False
            elif not item.isnumeric():
                is_valid = False

        if not is_valid:
            return -1

        if is_there_neg_nums:
            if len(neg_nums.split(" ")) > 2:
                raise ValueError(raised_error + "".join(neg_nums))
            else:
                raise ValueError(raised_error)

        result = 0
        for num in numbers:
            if int(num) <= 1000:
                result += int(num)

        
        return result
