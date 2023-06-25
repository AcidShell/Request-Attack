# Request-Attack
Envios de requisições. Verifique o código do script.

Este é um script em Python que utiliza a biblioteca aiohttp para enviar um grande número de requisições HTTP para um determinado site. O objetivo do script é testar a capacidade de resposta e estabilidade do servidor em relação a um grande fluxo de tráfego. O código define uma URL como alvo para as requisições, um número máximo de requisições a serem feitas e o tamanho do pool de envios. O script utiliza programação assíncrona para permitir que múltiplas requisições sejam feitas simultaneamente e tempos de resposta mais rápidos. O tempo total de execução é medido e exibido no final do script.

A configuração recomendada (100) me deu uma taxa de 1000 envios em 4 segundos.

Dentro do codigo do script você podera configurar:

url = " " # ALVO
num_requisicoes =  # MAXIMO QUE SERÁ ENVIADO
pool_size = 100 # ENVIOS ( recomendado - 100 )
