def fun(n):
    # generate the combinations (we can use module for this)
    lis = []
    allowed_continue_leaves = 4
    out_counter = 0
    for z in range(n, 0, -1):
        inlis = []
        for a in range(2 ** out_counter):
            for x in ["a", "p"]:
                counter = 2 ** (z - 1)
                for y in range(counter):
                    inlis.append(x)
        lis.append(inlis)
        out_counter += 1
    # convert to structured string (we can use numpy for restructuring)
    st = ""
    for x in range(2 ** n):
        for y in lis:
            st += y[x]
        st += "\n"
    # we can use regular expression to get continious 4 or more time absent pattern but we will not use it we will do it manually
    require = 0
    unuttended = 0
    for x in st.split():
        # check for rejected
        rejected_flag = False
        counter = 0
        for y in x:
            if y == "a":
                counter += 1
                if counter >= allowed_continue_leaves:
                    rejected_flag = True
                    break
            else:
                counter = 0
        if not rejected_flag:
            require += 1
            if x[-1] == "a":
                unuttended += 1
    return f"{unuttended}/{require}"


print(f"testcase1 {fun(5)}")
print(f"testcase2 {fun(10)}")
