frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('Oi')
print(""""Aqui estão os loucos. Os desajustados. Os rebeldes. Os criadores de caso. 
Os pinos redondos nos buracos quadrados. Aqueles que vêem as coisas de forma diferente. 
Eles não curtem regras. E não respeitam o status quo. Você pode citá-los, discordar deles, glorificá-los ou caluniá-los. 
Mas a única coisa que você não pode fazer é ignorá-los. Porque eles mudam as coisas. Empurram a raça humana para a frente. 
E, enquanto alguns os vêem como loucos, nós os vemos como geniais. 
Porque as pessoas loucas o bastante para acreditar que podem mudar o mundo, são as que o mudam""")
print(frase.count('o'))
print(frase.count('O'))
print(frase.count('eo'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(len(frase.lstrip()))
print(len(frase.rstrip()))
print(frase.replace('Python', 'Android'))
print(frase[0])

frase = frase.replace('Python', 'Android')
print(frase)

print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('python'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[1])
print(dividido[2])
print(dividido[3])
print(dividido[2][3])

