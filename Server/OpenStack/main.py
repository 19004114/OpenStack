from flask import Flask, render_template, request, redirect, session, url_for, flash, json
from flask_mysqldb import MySQL
import MySQLdb.cursors
import variables
from datetime import datetime
import hashlib
import ast

app = Flask(__name__)
app.config['SECRET_KEY'] = "minh"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'openstack'

mysql = MySQL(app)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/login', methods =['GET', 'POST'])
def login():
    if 'loggedin' in session:
        return redirect(url_for('index'))
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = % s AND password = % s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('index'))
        else:
            msg = 'Thông tin đăng nhập không chính xác !'

    return render_template('login.html', msg=msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = % s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Tài khoản đã tồn tại !'
        elif not username or not password:
            msg = 'Xin hãy điền đủ thông tin !'
        else:
            cursor.execute('INSERT INTO users VALUES (NULL, % s, % s)', (username, password,))
            mysql.connection.commit()
            msg = 'Đăng ký thành công !'
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Xin hãy điền đủ thông tin !'
    return render_template('register.html', msg=msg)

@app.route('/')
def index():
    if 'loggedin' in session:
        data = variables.instances_details
        datalen = len(data)
        sidebar1 = "active"

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM quyentruycap')
        pms = cursor.fetchall()

        return render_template("index.html", data = data, datalen = datalen, sidebar1 = sidebar1, pms=pms)
    else:
        return redirect(url_for('login'))

@app.route('/pm', methods =['GET', 'POST'])
def pm():
    msg = ''
    sidebar2 = "active"
    if 'loggedin' in session:
        data = variables.instances_details

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM mayvatly')
        pms = cursor.fetchall()

        cursor.execute('SELECT * FROM quyentruycap')
        request_access = cursor.fetchall()

        if request.method == 'POST' and 'name' in request.form and 'MAC_addr' in request.form:
            name = request.form['name']
            MAC_addr = request.form['MAC_addr'].lower()
            hashMAC = hashlib.shake_256(MAC_addr.encode('utf-8')).hexdigest(10)

            print(MAC_addr)
            print(hashMAC)

            time_created = datetime.now()
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM mayvatly WHERE  MAC_addr = % s', (hashMAC,))
            account = cursor.fetchone()
            if account:
                msg = 'Máy tính vật lý đã tồn tại !'
            elif not name or not MAC_addr:
                msg = 'Xin hãy điền đủ thông tin !'
            else:
                cursor.execute('INSERT INTO mayvatly VALUES (NULL, %s, %s, %s)', (name, hashMAC,time_created))
                mysql.connection.commit()
                msg = 'Thêm thành công !'
        return render_template("PM.html", data = data, msg=msg, sidebar2 = sidebar2, pms = pms, request_access = request_access)
    else:
        return redirect(url_for('login'))

@app.route('/request_access', methods =['GET', 'POST'])
def request_access():
    if 'loggedin' in session:
        time_created = datetime.now()
        username = ""
        password = ""

        if request.method == 'POST' and 'select_VM' in request.form and 'select_PM' in request.form:
            select_VM = ast.literal_eval(request.form['select_VM'])
            VM_id = list(select_VM.keys())[0]
            obj_id = list(select_VM.values())[0]
            VM_name = obj_id[0]
            ip_addr = obj_id[1]

            select_PM = ast.literal_eval(request.form['select_PM'])
            mac_addr = list(select_PM.keys())[0]
            PM_name = list(select_PM.values())[0]

            print(mac_addr)

            if not select_VM:
                flash("Không có máy ảo để cấp quyền!")
                return redirect(url_for('pm'))
            elif not select_PM:
                flash("Không có máy vật lý để cấp quyền!")
                return redirect(url_for('pm'))

            account = {
                "FIT": "123456",
                "FIT2": "123456",
            }

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM quyentruycap WHERE VM_id = %s', (VM_id,))
            check_VM = cursor.fetchall()

            cursor.execute('SELECT * FROM quyentruycap WHERE mac_addr = %s', (mac_addr,))
            check_PM = cursor.fetchone()

            cursor.execute('SELECT * FROM quyentruycap WHERE VM_id = %s and mac_addr = %s', (VM_id, mac_addr))
            check_Request = cursor.fetchone()


            for i in range(len(list(account.keys()))):
                check_username = list(account.keys())[i]
                check_password = list(account.keys())[i]
                cursor.execute('SELECT * FROM quyentruycap WHERE username = %s and password = %s and VM_id = %s', (check_username, check_password, VM_id, ))
                check_Account = cursor.fetchone()
                if not check_Account:
                    username = list(account.keys())[i]
                    password = list(account.keys())[i]
            if len(check_VM) > 1 and username == "" and password == "":
                flash('Máy ảo đã cấp đủ tài khoản, Xin hãy chọn máy ảo khác!')
            elif check_Request:
                flash('Máy vật lý đã tồn tại quyền truy cập vào máy ảo này! Vui lòng thử lại!')
            elif check_PM:
                flash('Máy vật lý này đã được cấp quyền truy cập vào máy ảo! Hãy chọn máy vật lý khác')
            else:
                cursor.execute('INSERT INTO quyentruycap VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, NULL, %s)', (VM_id, VM_name, PM_name, username, password, ip_addr, mac_addr, time_created ))
                mysql.connection.commit()
                flash('Cấp quyền thành công !')
        elif 'select_VM' not in request.form:
            flash("Không tìm thấy máy ảo để cấp quyền!")
        elif 'select_PM' not in request.form:
            flash("Không tìm thây máy vật lý để cấp quyền!")
        return redirect(url_for('pm'))

@app.route('/delete_access_pm', methods =['GET', 'POST'])
def delete_access_pm():
    if request.method == 'POST' and 'id' in request.form:
        access_id = request.form['id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM quyentruycap WHERE id = %s', (access_id,))
        mysql.connection.commit()
        flash('Xóa thành công !')
    return redirect(url_for('pm'))

@app.route('/delete_access_vm', methods =['GET', 'POST'])
def delete_access_vm():
    if request.method == 'POST' and 'id' in request.form:
        access_id = request.form['id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM quyentruycap WHERE id = %s', (access_id,))
        mysql.connection.commit()
        flash('Xóa thành công !')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 400

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/select', methods=['GET', 'POST'])
def select():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        VM_id = request.form['VM_id']
        result = cursor.execute("SELECT * FROM quyentruycap WHERE VM_id = %s", [VM_id])
        PMs = cursor.fetchall()
        PM_list = []
        for pm in PMs:
            PM_dict = {
                    'id': pm['id'],
                    'PM_name': pm['PM_name'],
                    'username': pm['username'],
                    'password': pm['password'],
                    'mac_addr': pm['mac_addr']
            }
            PM_list.append(PM_dict)
        print(PM_list)
        return json.dumps(PM_list)