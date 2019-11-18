txt_file = open("sun.txt", mode="r+")
#
# for i in range(1000):
#     txt_file.writelines(str(random.randint(1, 1000)) + "\n")

result_set = set(txt_file.readlines())
for i in result_set:
    print(i.replace("\n", ""))
