i = 0
if __name__ == '__main__':
    for line in open("JavaEntityFiled.filed"):
        # print line,
        print "private String " + line.strip("\n") + ";"
        i = i+1
print i