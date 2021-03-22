data_hoje = input('Data de hoje: ')
calorias_pequeno_almoco = int(input('Calorias do pequeno almoço: '))
calorias_almoco = int(input('Calorias do almoço: '))
calorias_lanche = int(input('Calorias do lanche: '))
calorias_jantar = int(input('Calorias do jantar: '))
total_calorias = calorias_pequeno_almoco + calorias_almoco + calorias_lanche + calorias_jantar
parint('No dia ' + data_hoje + ' foram consumidas ' + str(total_calorias) + ' calorias. :)') 