import csv

# Import tickets.csv file
with open("ticket_classifier/tickets.csv","r") as f:
    reader = csv.reader(f)
    tickets = list(reader)
    
total = len(tickets)
urgent_num = 0 


for ticket in tickets :
    if(ticket[1]) == "urgent" :
        urgent_num += 1
        
normal_num = 0

for ticket in tickets :
    if(ticket[1]) == "normal" :
        normal_num += 1


print("{:-^30}".format("REPORT"))
print("Total tickets : " + str(total))
print("Urgent :"  + str(urgent_num))
print("Normal :"   + str(normal_num))
print("{:-^30}".format(""))


dic = {"1":"network", "2":"password", "3":"printer", "4" :"software", "5":"hardware"}
print("{:-^30}".format("Please, Write down your ticket number"))
print("1.nework 2.password 3.printer 4.software 5.hardware")
ticket_num = str(input("=>"))

urgent_keywords = ["urgent", "not working", "down" , "failed" , "entire", "all","cannot access"]
print("{:-^30}".format("Please, Describe your problem"))
problem = str(input("=>"))

ticket_list = []

if ticket_num in dic :
    print(dic.get(ticket_num) + " problem")
    if any(keyword in problem for keyword in urgent_keywords)  :
        priority = "urgent"
        ticket_list.append([dic.get(ticket_num), priority])
    else :
        priority = "normal"
        ticket_list.append([dic.get(ticket_num), priority])

    # store csv 
    with open("tickets.csv", "a" , newline="") as f :
        writer = csv.writer(f)
        writer.writerow([dic.get(ticket_num),priority])
    
else :
    print("Worng ticket number, Please Try again")
    
    