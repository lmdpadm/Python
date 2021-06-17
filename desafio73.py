tabela = ('FLAMENGO', 'INTERNACIONAL', 'ATLÉTICO MG', 'SÃO PAULO',
          'FLUMINENSE', 'GRÊMIO', 'PALMEIRAS', 'SANTOS', 'ATHLÉTICO PR',
          'BRAGANTINO', 'CEARÁ', 'CORINTHIANS', 'ATLÉTICO GO', 'BAHIA',
          'SPORT', 'FORTALEZA', 'VASCO', 'GOIÁS', 'CORITIBA', 'BOTAFOGO')
print('\033[1;32m⚽⚽⚽\033[m CENTRAL DO BRASILEIRÃO 2020 \033[1;32m⚽⚽⚽\033[m')
print(f'TABELA DE TIMES: {tabela}')
print('\033[1;32m⚽\033[m' * 25)
print(f'CINCO PRIMEIROS COLOCADOS: {tabela[:5]}')
print('\033[1;32m⚽\033[m' * 25)
print(f'QUATRO ÚLTIMOS COLOCADOS: {tabela[-4:]}')
print('\033[1;32m⚽\033[m' * 25)
print(f'TABELA EM ORDEM ALFABÉTICA: {sorted(tabela)}')
print('\033[1;32m⚽\033[m' * 25)
print(f'O TIME SÃO PAULO TERMINOU NA {tabela.index("SÃO PAULO") + 1}ª COLOCAÇÃO.')
