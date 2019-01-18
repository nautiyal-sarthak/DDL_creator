import glob

def gen(path):
    out = []

    for file in glob.glob(path + "*ddl.txt"):
        collst = []
        tblname = ""

        for line in open(file).readlines():
            line = line.lower()
            if "createtab_stmt" in line:
                continue

            if "create external table" in line:
                txt = line.split("`")[1].split(".")
                tblname = txt[1]
                continue

            if "row format serde" in line:
                out.append([tblname, list(collst)])
                tblname = ""
                collst.clear()
                break

            if tblname != "":
                if len(line.split("`")) >= 2 :
                    collst.append(line.split("`")[1])

    return out
