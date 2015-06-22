# Michael Sarfati (michael.sarfati@utoronto.ca), June 21, 2015
# http://msarfati.wordpress.com

from hl7apy import core

## MSH Header ##
hl7 = core.Message("ORU_R01")

hl7.msh.msh_3 = "SendingApp"
hl7.msh.msh_4 = "SendingFac"
hl7.msh.msh_5 = "ReceivingApp"
hl7.msh.msh_6 = "ReceivingFac"
hl7.msh.msh_9 = "ORU^R01^ORU_R01"
hl7.msh.msh_10 = "168715"
hl7.msh.msh_11 = "P"

# PID - Patient Identification
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_3 = "1"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_PATIENT.PID.pid_5 = "SARFATI^MICHAEL"

# OBR Segment -- Patient details ##
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.OBR.obr_4 = "10000"

# OBX Segment -- Embedding the report
mri_b64 = open("./mri_scan_b64.txt", "r")

hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_1 = "1"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_2 = "ED"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_3 = "PDF"
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_5 = mri_b64.read()
hl7.ORU_R01_PATIENT_RESULT.ORU_R01_ORDER_OBSERVATION.ORU_R01_OBSERVATION.OBX.obx_11 = "F"  # Observ Result Status -- "F" meaning 'Final result'

# And finally
assert hl7.validate() is True
