# Michael Sarfati (michael.sarfati@utoronto.ca), June 20, 2015
# http://msarfati.wordpress.com

from hl7apy import parser
from hl7apy.exceptions import UnsupportedVersion

hl7 = open('sample.hl7', 'r').read()

try:
    m = parser.parse_message(hl7)
except UnsupportedVersion:
    m = parser.parse_message(hl7.replace("\n", "\r"))

import datetime
incoming_hl7 = {
    "type": m.msh.msh_9.value,
    "client_app": m.msh.msh_3.value,
    "client_fac": m.msh.msh_4.value,
    "control_id": m.msh.msh_10.value,
    "process_id": m.msh.msh_11.value,
    "timestamp": datetime.datetime.strptime(m.msh.msh_7.value, "%Y%m%d%H%M%S%f"),
    "hl7": m,
}
