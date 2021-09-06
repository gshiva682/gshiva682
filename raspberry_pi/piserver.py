from socket import * 
from time import ctime

port=12345   
host=""
addr=(host,port) 

ser_soc=socket(AF_INET,SOCK_STREAM)
ser_soc.bind(addr) 
ser_soc.listen(5) 

while True:
    print("Waiting for connection") 
    cli_soc,cli_addr = ser_soc.accept() 
    print("...connected from :",cli_addr)
    cli_soc.send("Thank you".encode())
    ser_soc.close()
    break
    
