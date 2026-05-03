import csv
import datetime

# Set time
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Import tickets.csv file
with open("tickets.csv","r") as f:
    reader = csv.reader(f)
    # No counting empty row
    tickets = [row for row in reader if row]
    
total = len(tickets)

# Generate Ticket ID
ticket_id = "TKT-" + str(total +1).zfill(3)

urgent_num = 0 

for ticket in tickets :
    if len(ticket) < 2 :
        continue
    if ticket[2] == "urgent" :
        urgent_num += 1
        
normal_num = 0

for ticket in tickets :
    if len(ticket) < 2 :
        continue
    if ticket[2] == "normal" :
        normal_num += 1

# Counting Category         
network_count_num = 0
password_count_num = 0
printer_count_num = 0
software_count_num = 0
hardware_count_num = 0


for ticket in tickets :
    if ticket[1] == "network" :
        network_count_num +=1 
    elif ticket[1] == "password" :
        password_count_num +=1
    elif ticket[1] == "printer" :
        printer_count_num += 1
    elif ticket[1] == "software" :
        software_count_num += 1
    elif ticket[1] == "hardware" :    
        hardware_count_num += 1


# Report 
print("{:-^30}".format("REPORT"))
print("Total tickets : " + str(total))
print("Urgent :"  + str(urgent_num))
print("Normal :"   + str(normal_num))

# Category
print("{:-^30}".format("Category"))
print("Network : " + str(network_count_num))
print("Password :"  + str(password_count_num))
print("Printer :"   + str(printer_count_num))
print("Software :"   + str(software_count_num))
print("HardWare :"   + str(hardware_count_num))
print("{:-^30}".format(""))

# Search ID
search_id = str(input("Search ticekt ID (or press Enter to skip) : "))

if search_id : 
    for ticket in tickets :
        if ticket[0] == search_id:
            print("-> Category : " + ticket[1] + "| Priority :" + ticket[2] + "| Date :" + ticket[3])
            break
    else : 
            print("Ticket not found")
            
dic = {"1":"network", "2":"password", "3":"printer", "4" :"software", "5":"hardware"}
print("{:-^30}".format("Please, Write down your ticket number"))
print("1.nework 2.password 3.printer 4.software 5.hardware")

# Validation 
while True :
    ticket_num = str(input("=>"))
    if ticket_num in dic :
        break
    else : 
        print("Wrong number, Please try again")

urgent_keywords = ["urgent", "not working", "down" , "failed" , "entire", "all","cannot access"]
print("{:-^30}".format("Please, Describe your problem"))
problem = str(input("=>"))

ticket_list = []

if ticket_num in dic :
    if any(keyword in problem for keyword in urgent_keywords)  :
        priority = "urgent"
        ticket_list.append([dic.get(ticket_num), priority])
    else :
        priority = "normal"
        ticket_list.append([dic.get(ticket_num), priority])

    # Store csv 
    with open("tickets.csv", "a" , newline="") as f :
        writer = csv.writer(f)
        writer.writerow([ticket_id,dic.get(ticket_num),priority, today])
    
else :
    print("Worng ticket number, Please Try again")
    
    