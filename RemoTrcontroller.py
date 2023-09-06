import tkinter
from tkinter import messagebox
from flask import Flask, render_template, request
from src.com.util.db_remote_mapper_sele import playgame
from tkinter import *

app = Flask(__name__)
#
#
@app.route('/')
def hello_world():
    return 'Hello World!'

# #
@app.route('/index/retr')
# 跳转到首页
def index_retr():
    return render_template('/index/RemoteTrial.html')

@app.route('/retr_selectindex',methods=['POST', 'GET'])
def retr_sel():
    # 获取前台数据
    userids = request.form['userid']
    if userids == '':
        content = {'redCode':'0000','retInfo':'提示：请输入userid号'}
        print(content)
        return render_template('index/RemoteTrial.html')

    else:
        retr_data = playgame()
        date_ns = retr_data.sel_ns(userids) # 查询userid
        if date_ns == None:
            content = {'retCode':'0001','retInfo':'提示：userid不存在，请输入正确的userid'}
            print(content)
            return render_template('index/RemoteTrial.html', content=content)
        else:
            # return render_template('index/RemoteTrial.html', userider=date_ns[0], facetrialer=date_ns[1])
            content = {'retCode': '0002', 'retInfo': '提示：查询结果如下'}
            # content = {'retCode': '1010', 'retInfo': '提示：' + date_ns[0] + date_ns[1] }
            # return date_ns[0] + date_ns[1]
            return render_template('index/RemoteTrial.html', content=content,userider=date_ns[0], facetrialer=date_ns[1])

@app.route('/retr_updateindex', methods=['POST', 'GET'])
def retr_upd():
    userids = request.form['userid']
    facetrials = request.form['facetrial']
    retr_up_date = playgame()
    date_su_ns = retr_up_date.success_ns(facetrials,userids)
    if date_su_ns == 0 :
        content = {'retCode': '0002', 'retInfo': '提示：不需要更新'}
        return render_template('index/RemoteTrial.html',content=content)
    elif date_su_ns == 1:
        content = {'retCode': '0002', 'retInfo': '提示：更新成功'}
        return render_template('index/RemoteTrial.html' ,content=content)




    # if date_su_ns == 0 :
    #     updmess1 = Tk()
    #     mess1 = Message(updmess1, text='不需要修改')
    #     mess1.pack()
    #     mess1.mainloop()
    # elif date_su_ns == 0:
    #     updmess2 = Tk()
    #     mess2 = Message(updmess2, text='不需要修改')
    #     mess2.pack()
    #     mess2.mainloop()
    # return render_template('index/RemoteTrial.html')
#

if __name__ == '__main__':
    app.run()


