import requests
from requests.auth import HTTPDigestAuth

import json
import time
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#HEADERS={'Content-type':'application/json', 'Accept':'application/json'}

#VARIABLES FOR INTERFACE 'filterTrapStatus' SETTINGS
SYS_SETTINGS='0'
NO_FILTER='1'
FILTER='2'

#VARIABLES FOR URI CREATION
BASE_URL="https://hohpimcmaster01:8443/imcrs"
DEVICE_PATH="/plat/res/device"
MONITOR_PATH="/perf/monitor/device"
THRESHOLD_PATH="/perf/monitor/threshold"
ALARM_PATH="/fault/alarm"

class ImcSession():
	"""Class to Manage the Session with IMC and execute API calls"""

	def __init__(self, URL, u, p):
		self.s = requests.Session()
		self.s.headers.update({'Content-type':'application/json','Accept':'application/json'})
		self.s.verify=False
		try:
			x = self.s.get(BASE_URL,auth=HTTPDigestAuth(u,p))
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
			response=self.s.get(BASE_URL + DEVICE_PATH,params=myparams)
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
				response = self.s.get(BASE_URL + DEVICE_PATH,params=myparams)
				jres = response.json()
				jres2 = jres.get('device')
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

		target=BASE_URL + DEVICE_PATH + "/" + myparams['id'] + "/interface"

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
				jres2 = jres.get('interface')
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

