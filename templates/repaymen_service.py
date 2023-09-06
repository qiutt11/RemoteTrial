from src.com.util.repaymen_select_mapper import Repaymen_s

#  loan_id 的状态需要判断   一个phone可能对应多个loan_id  但是只有一个状态是可用状态
class repaymentService():
   def repayment_success(self):
       u = Repaymen_s()
       ns = u.repayment_sl()