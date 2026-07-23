todayServer = {"servOne" , "servTwo" , "servThree" , "servFour" , "servFive" , "servSix" , "servSeven" , "servEight" , "servNine" , "servTen"}

yasterdayServer = {"servOne" ,  "servFour" , "servFive" ,  "servSeven" , "servEight" , "servNine" , "servTen"}

print(todayServer - yasterdayServer)#الservers that are in todayServer but not in yasterdayServer

print(todayServer & yasterdayServer)#the servers that are in both todayServer and yasterdayServer

for server in todayServer :
    print(server)
    #print the servers of todayServer's set



if "servOne" in yasterdayServer: 
    print('servOne is in yasterdayServer')
    #be sure to check if servOne is in yasterdayServer's set



list_servers = list(todayServer & yasterdayServer)

print(list_servers[0])