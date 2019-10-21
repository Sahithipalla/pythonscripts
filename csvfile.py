pwd
import csv
data=open("test.csv")
data
csv_data=csv.reader(data)
csv_data
data_lines=list(csv_data)
data_lines
#create or overwrite a csv.file
file_output=open("new_file.csv","w",newline="")
csv_writer=csv.writer(file_output,delimiter=",")
csv_writer.writerow(["col1","col2","col3"])
csv_writer.writerows([[1,2,3],[4,5,6],[7,8,9]])
file_out.close()
data=open("new_file.csv")
data
csv_data=csv.reader(data)
data_lines=list(csv_data)
data_lines
#edit the file
f=open("new_file.csv","a",newline="")
csv_writer=csv.writer(f)
csv_writer.writerow([12,34,56])
csv_writer.writerows([[10,20,30],[40,50,60],[70,80,90]])
f.close()
data=open("new_file.csv")
data
csv_data=csv.reader(data)
data_lines=list(csv_data)
data_lines

