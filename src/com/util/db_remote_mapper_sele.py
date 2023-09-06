from src.config import dbconfig_remote

__author__ = 'CAI'

class playgame:
    def sel_ns(self,userid):
        conn = dbconfig_remote.pool_zdcd() #连接数据库
        sql = "SELECT id,user_phone FROM phapp_user WHERE id =('"+userid+"')" #查询
        cur = conn.cursor()
        cur.execute(sql)
        result=cur.fetchone()
        # print(type(result))
        # print(len(result))
        cur.close()
        conn.close()
        return result


# if __name__ == "__main__":
#     pg = playgame()
#     sel_content = pg.sel_ns('0349c1837a4247688ae445e2c2ae5162')
#     print (sel_content)



    def success_ns(self,ft,userid):
        conn = dbconfig_remote.pool_zdcd()
        sql="UPDATE phapp_user SET user_sex =('"+ft+"')  WHERE id in ('"+userid+"')"#更新通知状态为成功
        # sql="UPDATE trade SET face_trial ="+ft+"WHERE user_id in ("+userid+");"
        cur=conn.cursor()
        result = cur.execute(sql)
        # result=conn.commit()
        conn.commit()
        cur.close()
        conn.close()
        return result


# if __name__ == "__main__":
#     pg = playgame()
#     # sel_up_value =pg.success_ns('0',"222")
#     sel_nv_value = pg.sel_ns('222')
#     print (sel_nv_value[1])

    # sel_inse_value =pg.success_insert("cuixiaobo",str(18),str(3))
    # print(sel_nv_value)
