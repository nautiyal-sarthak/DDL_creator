import os
import beeline # Beeline_create_table
import desc_tbl # use this in case the we recive the decribe table output. col_namedata_typecomment
import HiveGen #DDL_with_req
import Dsc_beeline #Beeline_desc.txt
# use this in case the we recive the beeline table output.


path = "C:/Users/1535141/Desktop/work/ddl/"
database = "schema"
outputFile = path + "ddl_out.txt"

format = "ROW FORMAT DELIMITED\nFIELDS TERMINATED BY '\\u0001'\nSTORED AS INPUTFORMAT\n" \
         "'org.apache.hadoop.mapred.TextInputFormat'\nOUTPUTFORMAT\n'" \
         "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'\nLOCATION\n" \
         "'hdfs://path/<db>/<tbl>'\ntblproperties ('skip.header.line.count'='1');\n"


if os.path.exists(outputFile):
    os.remove(outputFile)


def printOut(name,lst):
    with open(outputFile, "a") as output:
        output.write("Drop table " + database + "." + name + ";\n")
        output.write("\n" + "create external table " + database + "." + name + "(\n")
        for col_name in lst:
            if col_name == lst[len(lst) -1]:
                output.write(col_name + " " + "string)" + "\n")
            else:
                output.write(col_name + " " + "string" + ",\n")

        output.write(format.replace("<db>", database).replace("<tbl>", name))


#output = beeline.gen(path)
#output = HiveGen.gen(path)
output = Dsc_beeline.gen(path)


for tbls in output:
    printOut(tbls[0], tbls[1])

