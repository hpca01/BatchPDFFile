import pandas as pd
import os
from xhtml2pdf import pisa
from jinja2 import Environment, FileSystemLoader
import datetime

class Mirror():

	def __init__(self, file_in, *args, **kwargs):
	    self.file_loc = file_in

	def getDF(self):
		self.df = pd.read_csv(self.file_loc)
		columns = ['Device', 'MedDescription', 'MedID','CurrentQuantity', 'Min', 'Max', 'DaysUnused', 'ActiveOrders']
		self.df.reset_index(inplace=True)
		self.df = self.df[columns]
		self.num_devices = len(self.df.Device.unique())
		return None

	def getUniqueDevices(self):
		'''
		create devices list generator obj
		'''
		self.devices_list = (device for device in self.df.Device.unique())
		return self.devices_list

	def getMirroredList(self):
		try:
			if not self.devices_list:
				self.getUniqueDevices()
		except AttributeError:
			self.getUniqueDevices()

		#need to wrap this is a forloop
		device1 = str(next(self.devices_list))
		device2 = str(next(self.devices_list))
		self.intermdf = self.df[(self.df['Device'] == device1) | (self.df['Device'] == device2)]
		self.intermdf = self.intermdf.groupby('MedDescription').filter(lambda x: x['Device'].nunique() == 1).set_index('Device')
		return self.intermdf

	def writePdf(self,  df):
		html = Environment(
			loader = FileSystemLoader(searchpath='.', followlinks=True)).get_template('template.html').render(df = df,
				date_generated = datetime.datetime.now())

		#print(html)
		dev1,dev2 = [*[device.replace('/', '') for device in list(df.index.unique())]]

		file_name = "Mirror List for {dev1} and {dev2}.pdf".format(dev1= dev1, dev2 = dev2)
		with open(file_name, "w+b") as write:
				pisa.CreatePDF(src=html, dest = write)
		return file_name		

class GetResource():
	
	def resource_path(relative_path):
	    """ Get absolute path to resource, works for dev and for PyInstaller """
	    try:
	        # PyInstaller creates a temp folder and stores path in _MEIPASS
	        base_path = sys._MEIPASS
	    except Exception:
	        base_path = os.path.abspath(".")

	    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
	
	ob = Mirror(file_in = r"Station Inventory By Station %28Standard Size%29.csv")
	ob.getDF()
	for dev_pair in range(0, ob.num_devices, 2):
		os.startfile(GetResource.resource_path(ob.writePdf(ob.getMirroredList())))

	
	
	
	

