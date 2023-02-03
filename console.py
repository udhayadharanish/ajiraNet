computer = []
repeater = []
link = []

while(True):
    l = input().split()
    if(l[0] == "q"):
        print("Computers:",computer)
        print("Repeaters : ",repeater)
        print("Connections : ",link)
        break
    # print(l)
    if(l[0] == "ADD"):
        if(len(l) != 3):
            print("Error : Invalid command syntax.")
        elif(l[1] == "COMPUTER"):
            if(l[2] in computer ):
                print("Error : That name already exists")
            else:
                computer.append(l[2])
                print(f"Successfully added {l[2]}")
        
        elif(l[1] == "REPEATER"):
            repeater.append(l[2])
            print(f"Successfully added {l[2]}")

        else:
            print("Error : Invalid command syntax.")
    if(l[0]== "CONNECT"):
        # print(l[1] in computer,l[2] in computer)
        if(len(l) != 3):
            print("Error : Invalid command syntax.")
        elif(l[1] == l[2]):
            print("Cannot connect device to itself")
        
        elif((l[1] in computer or l[1] in repeater) and (l[2] in computer or l[2] in repeater)):
            if(l[1:] in link):
                print("Error: Devices are already Connected.")
            else:
                link.append(l[1:])
                print("Sucessfully Connected")
        
        else:
            print("Node not found.")
    if(l[0] == "INFO_ROUTE"):
        if(len(l) != 3):
            print("Error : Invalid Command syntax.")
        else:
            r = ""
            target = l[1]
            count = 0
            k = 0
            r = l[1]
            s = l[2]
            while(target != s):
                for i in range(len(link)):
                    if(target == link[i][0]):
                        target = link[i][1]
                    
                r+= target


                
            print(r)





            
    # print(link)


        
  

    


