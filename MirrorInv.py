import os
import jinja2 as jinja
import xhtml2pdf as html_to_pdf
import PySimpleGUI as sg
import time
from format import Mirror
from format import GetResource

def run_form():
	with sg.FlexForm("Mirror Tool", auto_size_text=True) as form:
		msg_elm = sg.Text('',  size = (40, 4) ,auto_size_text=True,font = ('Helvetica', 10))
		file_in = sg.Input('Select csv file...')
		form_rows= [
			[sg.Text('Mirror Tool for Pyxis ES v 1.5', font = ('Helvetica', 15))],
			[file_in, sg.FileBrowse()],
			[msg_elm],
			[sg.Submit(), sg.Cancel()]
		]

		form.LayoutAndRead(form_rows, non_blocking=True)

		for i in range(0,100000000):
			msg_elm.Update("Waiting for file to be selected")
			button, values = form.ReadNonBlocking()
			if button == 'Cancel':
				time.sleep(.01)
				break
			elif values is not None and button == "Submit":
				val = file_in.Get()
				create_pdfs(val)
				time.sleep(1)
			time.sleep(1)
		form.CloseNonBlockingForm()

def create_pdfs(file):
	path = file
	ob = Mirror(file_in = file)
	ob.getDF()
	for dev_pair in range(0, ob.num_devices, 2):
		os.startfile(GetResource.resource_path(ob.writePdf(ob.getMirroredList())))

if __name__ == '__main__':
	run_form()