trabalho_terca = True
trabalho_quinta = True


tv50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv32 = trabalho_quinta != trabalho_terca
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Mais saudavel={}" .format(
    tv50, tv32, sorvete, mais_saudavel))
