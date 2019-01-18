import glob
import os

# use this in case the we recive the decribe table output.

path = "C:/Users/1535141/Desktop/work/SAIL EDM/dotopal/NG/Nov/ddls"
database = "dotopal_ng_sri_open"
outputFile = "C:/Users/1535141/Desktop/work/SAIL EDM/dotopal/NG/Nov/ddls/output.ddl"

format = "ROW FORMAT DELIMITED\nFIELDS TERMINATED BY '\u0001'\nSTORED AS INPUTFORMAT\n" \
         "'org.apache.hadoop.mapred.TextInputFormat'\nOUTPUTFORMAT\n'" \
         "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'\nLOCATION\n" \
         "'hdfs://nnscbhaastest/apps/hive/warehouse/<db>/<tbl>'\ntblproperties ('skip.header.line.count'='1');\n"


#os.remove(outputFile)
for file in glob.glob(path + "/*.txt"):
    print("converting: " + file)

    tablename = file.split("\\")[1].split(".")[0].lower()

    with open(outputFile,"a") as output:
        for line in open(file).readlines():
            line = line.lower()
            if "col_namedata_typecomment" in line:
                output.write("Drop table " + database + "." + tablename + ";\n")
                output.write("\n" + "create external table " + database + "." + tablename + "(\n")
                continue

            split = line.split("")
            col_name, data_type = split[0],split[1]

            if col_name == "ods":
                output.write(col_name + " " + data_type + "\n")
                output.write(")\n")
                break
            else:
                output.write(col_name + " " + data_type + ",\n")

        output.write(format.replace("<db>", database).replace("<tbl>", tablename))
