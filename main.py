from miio import ViomiVacuum
import os


IP = os.environ.get("VACCUUM_IP_ADDRESS")
TOKEN = os.environ.get("VACCUUM_TOKEN")

vaccuum = ViomiVacuum(IP, TOKEN)


print(vaccuum.status())


