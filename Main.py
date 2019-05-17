from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
connection = AuthorizedConnection('http://admin:admin@192.168.1.1/')
client = Client(connection)
print(client.device.signal())
print(client.device.information())
print(client.diagnosis.diagnose_ping())
print(client.device.basic_information())
print(client.diagnosis.diagnose_traceroute())