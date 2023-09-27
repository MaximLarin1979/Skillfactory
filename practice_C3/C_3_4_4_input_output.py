# f_input = open('input.txt', 'r')
# line_list = []
# for line in f_input:
#     line_list = line_list + [line]
# print (line_list)
# f_output = open('output.txt', 'w')
# f_output.writelines(line_list)
# f_output.close()

# f_numbers = open('numbers.txt', 'r')
# numbers_list = []
# for line in f_numbers:
#     numbers_list = numbers_list + [int(line)]
# f_input = open('input.txt', 'a')
# f_input.writelines(['\n', str(max(numbers_list)+min(numbers_list))])
# f_input.close()

f_students = open('students.txt', 'r')
low_score_list = []
for line in f_students:
    if int(line[len(line)-2::]) < 3:
        print(line[:len(line)-2:])

