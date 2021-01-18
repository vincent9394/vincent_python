
# 寫入檔案 - write()
with open("result.txt", "wt", encoding="utf8") as f:
    f.write('00001.hk,13.0,2018-01-01 13:00\n00001.hk,13.5,2018-01-01 14:00')
    


	
# 讀取檔案 - read()
with open("result.txt", "rt", encoding="utf8") as f:
    x = f.read()

	


# 在f.read()運用.split()函數後，會以\n作為分隔定位，然後返回一個list。
with open("result.txt", "rt", encoding="utf8") as f:
    x = f.read().split('\n')



	
# for i in f 
with open("result.txt", "rt", encoding="utf8") as f:
    for line in f:
        print(line)




# 匯入 csv 函式庫
import csv



# csv.writer()
with open("result.csv", "wt", newline="", encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerow(["股票號", "現價", "抓取時間"])
    writer.writerow(["00004", "30.0", "2018-01-01 00:00:00"])
    writer.writerow(["00005", "20.0", "2018-01-01 00:00:00"])
    writer.writerow(["00006", "10.0", "2018-01-01 00:00:00"])

	

# csv.reader()
with open("result.csv", "rt", newline="", encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        print( row )
		
		
		
# csv.reader() - save data to list
with open("result.csv", "rt", newline="", encoding="utf8") as f:
    reader = csv.reader(f)
	data = []
    for row in reader:
        data.append( row )
        
    
        
# csv.DictWriter()        
with open("result2.csv", "wt", newline="", encoding="utf8") as f:
    writer = csv.DictWriter(f, ["股票號", "現價", "抓取時間"])
    writer.writeheader()
    writer.writerow({"股票號": "00001",  "抓取時間": "2018-01-01 00:00:00","現價": "30.0"})
    writer.writerow({ "現價": "20.0", "抓取時間": "2018-01-01 00:00:00","股票號": "00002"})
    writer.writerow({"股票號": "00003", "現價": "10.0", "抓取時間": "2018-01-01 00:00:00"})
    
	
	
# csv.DictReader()
with open("result2.csv", "rt", newline="", encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
		
		
	
# csv.DictReader() - save data to list
with open("result2.csv", "rt", newline="", encoding="utf8") as f:
    reader = csv.DictReader(f)
	data = []
    for row in reader:
        data.append(row)
 
 

# append mode 續寫檔案 
with open("result3.csv", "at", newline="", encoding="utf8") as f:
    writer = csv.DictWriter(f, ["股票號", "現價", "抓取時間"])
    writer.writeheader()
    writer.writerow({"股票號": "00001",  "抓取時間": "2018-01-01 00:00:00","現價": "330.0"})
    writer.writerow({ "現價": "330.0", "抓取時間": "2018-01-01 00:00:00","股票號": "00002"})
    writer.writerow({"股票號": "00003", "現價": "330.0", "抓取時間": "2018-01-01 00:00:00"})

	
	
# f.tell() 檢查檔案大小
with open("result3.csv", "at", newline="", encoding="utf8") as f:
    print( f.tell() )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
