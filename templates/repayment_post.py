import json
import http.client
from src.com.util.repaymen_select_mapper import Repaymen_s
import datetime

def repayment_po(sel_rpm):
    host = "10.100.19.110"
    port = "8445"
    headers = "{\"Content-type\": \"form-data;charset=UTF-8\"}"
    zdcdUrl = "/jsd/late/jsdRepayFundNotice"
    all = Repaymen_s().repayment_sl(sel_rpm)
    status = '1'      #写死的，就是还款成功状态
    cid = 'H'+str(all[0])
    reason = '还款成功'    #写死的，就是还款成功原因
    repaymoney = str(all[1])
    repaytime = all[2].strftime('%Y-%m-%d')   #date_time.strftime('%Y-%m-%d')
    # print(repaytime)
    term = str(all[3])
    contnum = str(all[4])
    # print(contnum)
    # 0-loan_id, 1-presentation_amount, 2-repay_time, 3-the_stage_num, 4- cont_code
    jsonParams = {
        "status":""+status+"",
        "cid":""+(cid)+"",
        "reason":""+reason+"",
        "repaymoney":""+repaymoney+"",
        "repaytime":""+repaytime+"",
        "term":""+term+"",
        "contnum":""+contnum+""
    }
    print (jsonParams)
    strs = json.dumps(jsonParams)
    headers = eval(headers)
    conn = http.client.HTTPConnection(host,port)
    conn.request('POST', zdcdUrl, strs, headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    OrderInfor = json.loads(data)
    return OrderInfor
    conn.close()

# HY179FG25pM0000110


if __name__ == "__main__":
    pg = Repaymen_s()
    # sel_content = pg.phone_sl('18401573054')
    # sel_order = pg.orderid_sl(sel_content)
    # sel_rpm = pg.repayment_sl('e81e5e89d22d4d6f8c5565b16f9b6174')
    p = repayment_po('e81e5e89d22d4d6f8c5565b16f9b6174')
    print (p)