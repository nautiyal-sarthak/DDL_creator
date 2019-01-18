def gen(path):
    with open(path) as f:
        my_lines = f.readlines()

    tblname = ""
    collst = []

    out = []

    for line in my_lines:
        if "CREATE EXTERNAL TABLE" in line:
            tblname = line.split("`")[1].split(".")[1]
            continue

        if tblname != "":
            if "`" in line:
                colname = line.split("`")[1]
                collst.append(colname)
            elif "ROW FORMAT SERDE" in line:
                out.append([tblname, list(collst)])
                tblname = ""
                collst.clear()

    return out
