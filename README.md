# DDL_creator
This python Code will help in reading the beline output in various formats and create the ddls

# Sample Inputs

1. 
show create table schema.tbl; (Multiple tabls in one file)                        
+-----------------------------------------------------
|                                                     
+-----------------------------------------------------
| CREATE EXTERNAL TABLE `schema.tbl`(                 
|   col1)                                             
| PARTITIONED BY (                                    
|   `col2` string)                                    
| ROW FORMAT SERDE                                    
|   'org.apache.hadoop.hive.ql.io.orc.OrcSerde'       
| STORED AS INPUTFORMAT                               
|   'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat' 
| OUTPUTFORMAT                                        
|   'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
| LOCATION                                            
|   'hdfs://dotopal/hdata/Schema/tbl'                 


2. 
desc schema.tbl ; (Multiple tabls in one file) 
+--------------------------+-----------------------+-----------------------+
|         col_name         |       data_type       |        comment        |
+--------------------------+-----------------------+-----------------------+
| col1                    | string                |                       |
| col2                | string                |                       |
| s_starttime              | string                |                       |


3.
use schema; (Multiple tabls in one file) 
No rows affected (0.844 
show columns in tbl;
+---------------------+-
|        field        |
+---------------------+-
| col1               |
| col2           |
 | s_starttime         |
 
 4.
 (1 file for 1 each table)
createtab_stmt
CREATE EXTERNAL TABLE `schema.tbl`(
  `col1` string, 
  `col2` string, 
 )
PARTITIONED BY ( 
  `col3` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.orc.OrcSerde' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
LOCATION
  'path'


 
