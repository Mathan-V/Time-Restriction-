from frappe.utils import getdate
from dateutil import parser
from datetime  import datetime
from datetime import date

def validate_current_date_1():
    a=self.posting_date
    #frappe.throw(_("date {0}").format(a))
    today = date.today()
    print(type(today))
    d1 = today.strftime("%Y/%m/%d")
    print(type(d1))
    now = datetime.now()
    print(now)
    now_time = now.strftime("%H:%M:%S")
    print(type(now_time))
    time = "10:30:59"
    print(type(time))
    #frappe.throw(_("time {0}").format(time))
    if(now_time > time and a <= d1):
        frappe.throw("Allow")


def validate_current_date_2(self):
    posting_date = str(self.posting_date)
    today = date.today()
    now_date = today.strftime("%Y-%m-%d")
    now = datetime.now()
    now_time = now.strftime("%H:%M:%S")
    time="10:59:59"
    #frappe.throw(_("posting date {0}, today {1}, ").format(posting,now_date))
    if(self.is_late_lpe_entry ==  1):
        pass
    else:
        if(now_date == posting_date):
            pass
        if(now_date != posting_date):
            if(now_time >= time):
                frappe.throw("For Late Entry,Fill up the Remark Field.")

def validate_for_late_lpe(self):
		posting_date = self.posting_date
		posting = str(posting_date)
		#frappe.throw(_("posting date {0}").format(posting))
		today = date.today()
		now_date = today.strftime("%Y-%m-%d")
		now = datetime.now()
		now_time = now.strftime("%H:%M:%S")
		time="11:59:59"
		if(self.is_late_lpe_entry ==  1):
			pass
		else:
			if(now_date == posting):
				pass
			elif(now_date != posting):
				if(now_time >= time):
					frappe.throw("For Late Entry,Fill up the Remark Field.")

def compareDates(curDate,post_date, postTime):
    noon = datetime.time(12,0,0)
    if (curDate ==  post_date) and (postTime <= noon):
        frappe.throw('Allow')
    else:
        frappe.throw("Don't allow")

def dateConvertion(strDate):
    date = datetime.datetime.strptime(strDate, '%d-%m-%Y').date()
    return date
date = datetime.datetime.now().date()
time = datetime.datetime.now().time()
conDate = dateConvertion(self.posting_date)
compareDates(date,conDate,time)


#Restriction For Labour Progress Entry
def validate_for_late_lpe(self):
    noon = datetime.time(12,0,0)
    posting_date = datetime.datetime.strptime(self.posting_date, '%Y-%m-%d').date()
    cur_date = datetime.datetime.now().date()
    cur_time = datetime.datetime.now().time()
    if(self.is_late_lpe_entry != 1) and (posting_date !=  cur_date) and (cur_time <= noon):
        frappe.throw("Mark the entry as late,then try submitting.")
