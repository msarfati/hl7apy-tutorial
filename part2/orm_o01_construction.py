# Michael Sarfati (michael.sarfati@utoronto.ca), June 21, 2015
# http://msarfati.wordpress.com
"""
This script constructs an HL7 ORM^O01 message of the following form:

MSH|^~\&|SendingApp|SendingFac|ReceivingApp|ReceivingFac|20150414173000||ORM^O01^ORM_O01|168715|P|2.5
PID|1|A-10001||B-10001|Doe^John
ORC|||||||||20150414120000
OBR|1|1|1100|||||||||||

"""

from hl7apy import core

hl7 = core.Message("ORM_O01")

hl7.msh.msh_3 = "SendingApp"
hl7.msh.msh_4 = "SendingFac"
hl7.msh.msh_5 = "ReceivingApp"
hl7.msh.msh_6 = "ReceivingFac"
hl7.msh.msh_9 = "ORM^O01^ORM_O01"
hl7.msh.msh_10 = "168715"
hl7.msh.msh_11 = "P"

# PID
hl7.add_group("ORM_O01_PATIENT")
hl7.ORM_O01_PATIENT.pid.pid_2 = "1"
hl7.ORM_O01_PATIENT.pid.pid_3 = "A-10001"
hl7.ORM_O01_PATIENT.pid.pid_5 = "B-10001"
hl7.ORM_O01_PATIENT.pid.pid_6 = "DOE^JOHN"

# ORC
hl7.ORM_O01_ORDER.orc.orc_1 = "1"
hl7.ORM_O01_ORDER.ORC.orc_10 = "20150414120000"

# OBR
# We must explicitly add the OBR segment, then populate fields
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.ORM_O01_ORDER_CHOICE.add_segment("OBR")

hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.ORM_O01_ORDER_CHOICE.OBR.obr_2 = "1"
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.ORM_O01_ORDER_CHOICE.OBR.obr_3 = "2"
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_OBSERVATION.ORM_O01_ORDER_CHOICE.OBR.obr_4 = "1100"

assert hl7.validate() is True
# Returns True
