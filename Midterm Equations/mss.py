# This program determines the nth TCP segment in a sequence number field


fileSize = int(input("Enter the file size in bytes: "))
MSS = int(input("Enter the MSS in bytes: "))
firstByte = int(input("Enter the first byte of data stream: "))
n = int(input("Enter the nth segment: "))

segment = fileSize/MSS

i=0
print("The first", n, "segments are:")
print(firstByte)
while i < n-1:
   firstByte += segment
   print(firstByte)
   i+=1
   

