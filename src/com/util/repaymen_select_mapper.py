#-*-coding:utf-8-*-
from src.config import dbconfig_repayment


class Repaymen_s():
    #用手机号查userid
     def phone_sl(slef,iphone_no):
         conn = dbconfig_repayment.pool_zdcd1()  # 连接数据库
         sql = "SELECT id FROM phapp_user WHERE user_phone =('" + iphone_no + "')"  # 查询
         cur = conn.cursor()
         cur.execute(sql)
         result = cur.fetchone()
         # print(type(result))
         # print(len(result))
         cur.close()
         conn.close()
         return result
#
# if __name__ == "__main__":
#     pg = repayment_sl()
#     sel_content = pg.phone_sl('18137801502')
#     print (sel_content)

     #用userid查找loanid
     def orderid_sl(self,phone_sl):
         conn = dbconfig_repayment.pool_zdcd1()
         sql = "SELECT loan_id FROM jsd_loan_order WHERE user_id =('" + phone_sl[0]+ "')"
         cur = conn.cursor()
         cur.execute(sql)
         result = cur.fetchone()
         cur.close()
         conn.close()
         return result

# if __name__ == "__main__":
#      pg = repayment_sl()
#      sel_content = pg.phone_sl('18137801502')
#      sel_order = pg.orderid_sl(sel_content)
#      print (sel_order)
      #用loanid 查找接口需要的参数
     def repayment_sl(self,orderid_sl):
         conn = dbconfig_repayment.pool_zdcd1()
         # sql = "SELECT * FROM jsd_dh_repayment_presentation_temp  WHERE loan_id =('"+orderid_sl[0]+"')"
         # print(orderid_sl)
         # sql = "SELECT loan_id,presentation_amount,repay_time,the_stage_num,cont_code  FROM jsd_dh_repayment_presentation_temp  WHERE loan_id =('"+orderid_sl[0]+"')"
         sql = "SELECT loan_id,presentation_amount,repay_time,the_stage_num,cont_code  FROM jsd_dh_repayment_presentation_temp  WHERE loan_id =('"+orderid_sl+"')"
         cur = conn.cursor()
         cur.execute(sql)
         result = cur.fetchone()
         cur.close()
         conn.close()
         return result

     #查询提报数据
     def repayment_totb(self):
         conn = dbconfig_repayment.pool_zdcd1.connection()
         sql = "SELECT r.id, " \
               "r.plan_id, " \
               "r.loan_id, " \
               "r.user_id, " \
               "r.stage_num, " \
               "r.the_stage_num, " \
               "r.repay_amount, " \
               "r.repay_prin_inter_amount, " \
               "r.repay_principal_amount, " \
               "r.repay_service_amount, " \
               "r.repay_interest_amount, " \
               "r.manage_amount, " \
               "r.compensate_amount, " \
               "r.surplus_amount," \
               " r.one_payment_amount, " \
               "r.repay_time, " \
               "r.repay_type, " \
               "r.repay_sts, " \
               "r.create_time, " \
               "r.update_time, " \
               "r.sms_flag, " \
               "r.deal_times, " \
               "o.cont_code, " \
               "o.real_name, " \
               "o.id_card, " \
               "a.id accountId    " \
               "FROM jsd_dh_account a   " \
               "LEFT JOIN jsd_loan_repay_plan r ON a.loan_id = r.loan_id      " \
               "LEFT JOIN jsd_loan_order o ON a.loan_id = o.loan_id    " \
               "WHERE a.sts = 10210 AND r.repay_time = '2019-2-10'    " \
               "AND ( r.repay_sts = 20110 OR r.repay_sts = 20150       )   AND r.deal_times <= 10;"
         cur = conn.cursor()
         cur.execute(sql)
         result = cur.fetchone()
         cur.close()
         conn.close()
         return result

     #不需要提报的数据设置
     def repayment_totb(self, repay_p_id):
         conn = dbconfig_repayment.pool_zdcd1()
         sql = "update jsd_loan_repay_plan  set deal_times= '11' where id = ('" + repay_p_id + "')"
         cur = conn.cursor()
         cur.execute(sql)
         result = cur.fetchone()
         cur.close()
         conn.close()
         return result

     #修改提报结果
     def repayment_totb(self, loan_id):
         conn = dbconfig_repayment.pool_zdcd1()
         sql = "UPDATE jsd_dh_repayment_presentation_temp  set presentation_sts = '20160' where loan_id IN ('"+loan_id+"')"
         cur = conn.cursor()
         cur.execute(sql)
         result = cur.fetchone()
         cur.close()
         conn.close()
         return result

     # 查询还款结果
     def repayment_totb(self, loan_id):
         conn = dbconfig_repayment.pool_zdcd1()
         sql = "select repay_time,presentation_sts from jsd_dh_repayment_presentation where loan_id in ('"+loan_id+"') and repay_time = '2019-2-10'"
         cur = conn.cursor()
         cur.execute(sql)
         result = cur.fetchone()
         cur.close()
         conn.close()
         return result


     #查询生成贷后需要通知第三方数据记录    sts =10000 待通知
     def repayment_totb(self, loan_id):
         conn = dbconfig_repayment.pool_zdcd1()
         sql = "select *  from jsd_dh_channel_push_continual where loan_id = ('"+loan_id+"')"
         cur = conn.cursor()
         cur.execute(sql)
         result = cur.fetchone()
         cur.close()
         conn.close()
         return result

     #还款入账及通知第三方     sts =10001  通知完成
     def repayment_totb(self, loan_id):
         conn = dbconfig_repayment.pool_zdcd1()
         sql = "select *  from jsd_dh_channel_push_continual where loan_id = ('"+loan_id+"')"
         cur = conn.cursor()
         cur.execute(sql)
         result = cur.fetchone()
         cur.close()
         conn.close()
         return result

#
# if __name__ == "__main__":
#      pg = Repaymen_s()
#      sel_content = pg.phone_sl('15840005015')
#
#      sel_order = pg.orderid_sl(sel_content)
#      print(sel_order)
#      sel_rpm = pg.repayment_sl(sel_order)
#      print (sel_rpm)
#      print (type(sel_rpm[0]))
#      print (type(sel_rpm[1]))
#      print(type(sel_rpm[2]))
#      print(type(sel_rpm[3]))
#      print(type(sel_rpm[4]))


#
# if __name__ == "__main__":
#      pg = Repaymen_s()
#
#      sel_rpm = pg.repayment_sl("e81e5e89d22d4d6f8c5565b16f9b6174")
#      print (sel_rpm)
