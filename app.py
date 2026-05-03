from flask import Flask, render_template, request, redirect
import csv
import datetime

app = Flask(__name__)

dic = {"1":"network", "2":"password", "3":"printer", "4":"software", "5":"hardware"}
urgent_keywords = ["urgent", "not working", "down", "failed", "entire", "all", "cannot access"]

def load_tickets():
    with open("tickets.csv", "r") as f:
        reader = csv.reader(f)
        return [row for row in reader if row]

@app.route("/")
def index():
    tickets = load_tickets()
    total = len(tickets)
    urgent_num = sum(1 for t in tickets if len(t) > 2 and t[2] == "urgent")
    normal_num = sum(1 for t in tickets if len(t) > 2 and t[2] == "normal")
    return render_template("index.html", total=total, urgent=urgent_num, normal=normal_num)

@app.route("/submit", methods=["POST","GET"])
def submit():
    ticket_num = request.form["ticket_num"]
    problem = request.form["problem"]
    
    tickets = load_tickets()
    ticket_id = "TKT-" + str(len(tickets) + 1).zfill(3)
    category = dic[ticket_num]
    priority = "urgent" if any(k in problem for k in urgent_keywords) else "normal"
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("tickets.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ticket_id, category, priority, today])
    
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)