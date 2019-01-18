import glob

def gen(path):
    out = []
    for file in glob.glob(path + "*.txt"):
        inCol = False
        collst = []
        tblname = ""
        for line in open(file).readlines():
            if "|         col_name         |" in line:
                continue

            if "/> desc " in line:
                tblname = (line.split(".")[1].split(";")[0]).strip()
                continue

            if tblname != "":
                if "rowid" in line:
                    inCol = True

                if inCol and len(line.split("|")) >= 2:
                    colname = line.split("|")[1].strip()
                    collst.append(colname)

                if "ods" in line:
                    out.append([tblname, list(collst)])
                    tblname = ""
                    collst.clear()
                    inCol = False
    return out
