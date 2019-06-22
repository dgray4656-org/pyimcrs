from pprint import pprint

class ImcDevice():
	"""Class to represent Device managed by IMC
		properties TBD
	"""
	
	def __init__(self,id,label,ip,sysName,contact,location,sysOid,sysDescription):
		self.id=id
		self.label=label
		self.ip=ip
		self.sysName=sysName
		self.contact=contact
		self.location=location
		self.sysOid=sysOid
		self.sysDescription=sysDescription
		
	
	def spitout(self):
		pprint(self)
	