from flask import Flask, render_template, request, redirect, url_for
import sys

app = Flask(__name__)

todo_list_global=[]
count=0

class Todo:
    def __init__(self, num, title):
        self.id = num
        self.title = title
        self.complete = False
    
    def __str__(self):
        return f"{self.title}"
    
    def updateComplete(self):
        self.complete = True
        return self.complete
    
    def updateNotComplete(self):
        self.complete = False
        return self.cpmplete
    
    def updateid(self, newid):
        self.id = newid
@app.route("/")
def hello_world():
    global todo_list_global
    return render_template("index.html", todo_list = todo_list_global)

@app.route("/add",methods=["POST"])
def add():
    global todo_list_global
    global count
    count = count + 1

    title = request.form.get("title")

    new_todo = Todo(num=count,title=title)
    todo_list_global.append(new_todo)

    return redirect("/")
