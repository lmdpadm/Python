me = float(input("O total de metros é:"))
#c = me / 100
#mi = me / 1000
#print('O total de {} metros convertido em centímetros é {:.5f} \nEm milímetros é {:.5f}'.format(me, c, mi))
print('O total de {} metros convertido em: \nKM é {:.4f} \nHM é {:.3f} \nDAM é {:.2f} \nM é {} \nDM é {:.2f} \nCM é {:.2f} \nMM é {:.2f}'.format(me, (me / 1000), (me / 100), (me / 10), (me / 1), (me * 10), (me * 100), (me * 1000)))
