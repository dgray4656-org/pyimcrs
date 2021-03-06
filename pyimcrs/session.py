import requests
from requests.auth import HTTPDigestAuth

import json
import time
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from pyimcrs import util

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ImcSession():
	"""Class to Manage the Session with IMC and execute API calls"""

	def __init__(self, URL, u, p):
		self.target = URL
		self.user = u
		self.s = requests.Session()
		self.s.headers.update({'Content-type':'application/json','Accept':'application/json'})
		self.s.verify=False
		try:
			x = self.s.get(URL,auth=HTTPDigestAuth(u,p))
			x.raise_for_status()
		except Exception as e:
			print(e)
			self.s=None

	def get_device_list(self,resPrivilegeFilter=False,start=0,size=10,
					orderby='id',desc=False,total=False,exact=False,
					operator=None, category=None, label=None, ip=None, 
					mac=None, status=None, series=None, contact=None,
					location=None):
		"""get_device function"""

		output_list=[]

		myparams={'resPrivilegeFilter':resPrivilegeFilter,
					'start':start, 
					'size': size,
					'orderby':orderby,
					'desc': desc,
					'total': total,
					'exact': exact}

		if operator is not None:
			myparams.update({'operator': operator})
		if category is not None:
			myparams.update({'category' : category})
		if label is not None:
			myparams.update({'label' : label})
		if ip is not None:
			myparams.update({'ip' : ip})
		if mac is not None:
			myparams.update({'mac' : mac})
		if status is not None:
			myparams.update({'status' : status})
		if series is not None:
			myparams.update({'series' : series})
		if contact is not None:
			myparams.update({'contact' : contact})
		if location is not None:
			myparams.update({'location' : location})

		myparams.update({'total':True})

		try:
			response=self.s.get(self.target + util.DEVICE_PATH,params=myparams)
			count = response.headers['Total']
		except Exception as e:
			print(e)
			count = 0

		if count == 0:
			return output_list
		else:
			myparams.update({'total':False})
			myparams.update({'size':count})
			try:
				response = self.s.get(self.target + util.DEVICE_PATH,params=myparams)
				jres = response.json()
				jres2 = jres.get('data')
			except Exception as e:
				print(e)
				return output_list

			if type(jres2) is dict:
				output_list.append(jres2)
			elif type(jres2) is list:
				for x in jres2:
					output_list.append(x)

			return output_list

	def get_device_interfaces(self, devid):
		myparams={'id':devid,
				'start':0,
				'size':10,
				'desc':False,
				'total':False}

		output_list=[]

		target=self.target + util.DEVICE_PATH + "/" + str(myparams['id']) + "/interface"

		myparams.update({'total':True})

		try:
			response = self.s.get(target, params=myparams)
			count = response.headers['Total']
		except Exception as e:
			print("Error getting count of interfaces for device", myparams['id'])
			print(e)
			count=0

		if count == 0:
			return output_list
		else:
			myparams.update({'total':False,'size':count})
			try:
				response = self.s.get(target, params=myparams)
				jres = response.json()
				jres2 = jres.get('data')
			except Exception as e:
				print("Error getting interfaces for device", myparams['id'])
				print(e)
				return output_list

			if type(jres2) is dict:
				output_list.append(jres2)
			elif type(jres2) is list:
				for x in jres2:
					output_list.append(x)

			return output_list

	def get_alarm_list(self, operatorName='a030147', total=False, start=0, size=10, orderby='faultTime', desc=False,
					alarmLevel=None, recStatus=None, ackStatus=None, timeRange=None, startAlarmTime=None, endAlarmTime=None, startAlarmAckTime=None,
					endAlarmAckTime=None, startAlarmDuration=None, endAlarmDuration=None, alarmDesc=None, descRelationship=None, acker=None,
					userAcker=None, paras=None, customView=None, deviceIp=None, deviceId=None, ifIndex=None, id=None, alarmCategory=None,
					faultOid=None, faultOidFuzzyQuery=False, originalType=None, holdInfo=None):
		myparams={'operatorName':operatorName,
				'total':total,
				'start':start,
				'size':size,
				'orderby':orderby,
				'desc':False}

		if alarmLevel is not None:
		    myparams.update({'alarmLevel':alarmLevel})
		if recStatus is not None:
		    myparams.update({'recStatus':recStatus})
		if ackStatus is not None:
		    myparams.update({'ackStatus':ackStatus})
		if timeRange is not None:
		    myparams.update({'timeRange':timeRange})
		if startAlarmTime is not None:
		    myparams.update({'startAlarmTime':startAlarmTime})
		if endAlarmTime is not None:
		    myparams.update({'endAlarmTime':endAlarmTime})
		if startAlarmAckTime is not None:
		    myparams.update({'startAlarmAckTime':startAlarmAckTime})
		if endAlarmAckTime is not None:
		    myparams.update({'endAlarmAckTime':endAlarmAckTime})
		if startAlarmDuration is not None:
		    myparams.update({'startAlarmDuration':startAlarmDuration})
		if endAlarmDuration is not None:
		    myparams.update({'endAlarmDuration':endAlarmDuration})
		if alarmDesc is not None:
		    myparams.update({'alarmDesc':alarmDesc})
		if descRelationship is not None:
		    myparams.update({'descRelationship':descRelationship})
		if acker is not None:
		    myparams.update({'acker':acker})
		if userAcker is not None:
		    myparams.update({'userAcker':userAcker})
		if paras is not None:
		    myparams.update({'paras':paras})
		if customView is not None:
		    myparams.update({'customView':customView})
		if deviceIp is not None:
		    myparams.update({'deviceIp':deviceIp})
		if deviceId is not None:
		    myparams.update({'deviceId':deviceId})
		if ifIndex is not None:
		    myparams.update({'ifIndex':ifIndex})
		if id is not None:
		    myparams.update({'id':id})
		if alarmCategory is not None:
		    myparams.update({'alarmCategory':alarmCategory})
		if faultOid is not None:
		    myparams.update({'faultOid':faultOid})
		if faultOidFuzzyQuery is not False:
		    myparams.update({'faultOidFuzzyQuery':faultOidFuzzyQuery})
		if originalType is not None:
		    myparams.update({'originalType':originalType})
		if holdInfo is not None:
		    myparams.update({'holdInfo':holdInfo})

		output_list=[]

		myparams.update({'total':True})

		target=self.target + util.ALARM_PATH
		
		try:
			response=self.s.get(target,params=myparams)
			count = response.headers['Total']
		except Exception as e:
			print(e)
			count = 0

		if count==0:	
			return output_list
		else:
			myparams.update({'total':False})
			myparams.update({'size':count})
			try:
				response = self.s.get(target,params=myparams)
				jres = response.json()
				jres2 = jres.get('data')
			except Exception as e:
				print(e)
				return output_list

			if type(jres2) is dict:
				output_list.append(jres2)
			elif type(jres2) is list:
				for x in jres2:
					output_list.append(x)

			return output_list