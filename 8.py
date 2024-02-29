"""dictionaries
example_dict = {
    "name": [20, 11, 2003],
    "DOB": [30, 11, 2004]
}

values = example_dict['DOB']
print(example_dict["DOB"])"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
for x, y in student_marks.items():
    if x == query_name:
        pre_output = sum(y)/3
        print(f"{pre_output:.2f}")


