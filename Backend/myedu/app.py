from flask import Flask,render_template,session,request,redirect
import myedu

app = Flask(__name__)
app.secret_key="blahb"

data = {}
@app.route('/',methods=['GET','POST'])
def home():
    global data
    if request.method == 'GET':
        return render_template("test.html",data=data)

    if request.form['btn'] == "search":
        data['univ'] = myedu.uniSearch(request.form['search-field'])
        return render_template("test.html",data=data)

    if request.form['btn'].split(' ')[0] == "univ":
        value = int(request.form['btn'].split(' ')[1])
        data['dep'] = myedu.depSearch(data['univ'][value][2])
        data['info'] = myedu.imgSearch(data['univ'][value][0])
        return render_template("test.html",data=data)

    if request.form['btn'].split(' ')[0] == "dep":
        value = int(request.form['btn'].split(' ')[1])
        data['prof'] = myedu.profSearch(data['dep'][value][0])
        return render_template('test.html',data=data)

    if request.form['btn'].split(' ')[0] == "prof":
        value = int(request.form['btn'].split(' ')[1])
        data['courses'] = myedu.courseSearch(data['prof'][value][0])
        return render_template('test.html',data=data)
    return "didn't work :( "



if __name__ == "__main__":
    app.debug = True
    app.run()
