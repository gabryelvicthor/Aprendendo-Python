#Utilize alguma função da biblioteca temporal para apresentar de forma dinâmica o dia, mês, ano, hora
# e minutos atuais. a impressão deve ser feita da seguinte maneira:
# Hoje é dia XX do mês de XXXX, São XX horas e XX minutos#
from datetime import datetime

#Calculo
agora = datetime.now()


print("Hoje é dia {} do mês de {}. São {} horas e {} minutos.".format(agora.day, agora.month, agora.hour, agora.minute))