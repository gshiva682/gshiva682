from socket import * 

cli_soc=socket(AF_INET,SOCK_STREAM) 

port=12345 
ip=input("ENTER THE IP:")
cli_soc.connect((ip,port)) 
print(cli_soc.recv(1024).decode()) 
cli_soc.close()

