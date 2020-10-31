# InvMirror
 
 Firstly I apologize for the poor wording.
 
 Purpose of Application
 - In hospitals that use ADS(automated dispensing system) devices, there is a need to standardize stock of medications in sets of devices occupying the same floor(mirroring). This prevents direct patient care staff from having to guess where each of their medications are stored. Consequently it also enables better care as it doubles the stock of a medication on the floor. This ultimately drives pharmacy performance as it lowers the need for "immediate" refills or creating adhoc dispenses from the main pharmacy.
 
Use
- This application works in conjuction with inventory reports in ADS system to identify which medications in a specific location are not mirrored correctly. Essentially this helps cut down the need for independent review on the technician's part to identify and replace medications. Another aim of this application is to provide context as well to the technician to be able to answer some of the questions such as if something should be removed/replaced.

How?
- Utilizes the jinja templating with html to pdf libs as well as a simple PANDAS function alongside PYSIMPLEGUI to be able to create a nice user experience.
- Final pdf is stored on the desktop, works on Windows so far, testing on Mac/Linux is not conducted. Most of the computers in hospital setting run on Windows.


