import time
import random
import emoji
import playsound
escolha = input(str("Escreva pedra,papel ou tesoura: "))
escolha = escolha.strip().lower().rstrip()
permissao = 1
emo = 0
emo1 = 0
if escolha == 'papel':
    vaiprojogo = "papel"
    emo = emoji.emojize(" :page_facing_up:", use_aliases=True)
elif escolha == 'pedra':
    vaiprojogo = 'pedra'
    emo = emoji.emojize(" :chestnut:", use_aliases=True)
elif escolha == 'tesoura':
    vaiprojogo = 'tesoura'
    emo = emoji.emojize(" :scissors:", use_aliases=True)

else:
    print('\n' * 100)
    print("Escolha não encontrada, verifique a ortografia")
    permissao = 0
if permissao == 1:
    print('\n' * 100)
    print("Você escolheu {} {} {} {}".format(vaiprojogo, emo, emo, emo))
    time.sleep(3)
    print('\n' * 100)
    print("É a vez do adversario..")
    time.sleep(3)
    print('\n' * 100)
    escolhaadv = random.randrange(0, 3)
    if escolhaadv == 0:
        escolhaadv = "papel"
        emo1 = emoji.emojize(" :page_facing_up:", use_aliases=True)
    elif escolhaadv == 1:
        escolhaadv = "pedra"
        emo1 = emoji.emojize(" :chestnut:", use_aliases=True)
    elif escolhaadv == 2:
        escolhaadv = 'tesoura'
        emo1 = emoji.emojize(" :scissors:", use_aliases=True)
    else:
        print("erro no random")
    print("o adversario escolheu {} {} {} {}".format(escolhaadv, emo1, emo1, emo1))
    time.sleep(3)
    print('\n' * 100)
    print("comparando escolhas..")
    time.sleep(3)
    print('\n' * 100)
    time.sleep(1)
    if (vaiprojogo == 'tesoura' and escolhaadv == 'papel'):
        print("A tesoura corta o papel\n\033[34mVOCÊ VENCEU!")
        playsound.playsound('mariovitoria.mp3')
    elif (vaiprojogo == 'pedra' and escolhaadv == 'tesoura'):
        print("A pedra quebra a tesoura\n\033[34VOCÊ VENCEU!")
        playsound.playsound('mariovitoria.mp3')
    elif (vaiprojogo == 'papel' and escolhaadv == 'pedra'):
        print("O papel embrulha a pedra\n\033[34mVOCÊ VENCEU!")
        playsound.playsound('mariovitoria.mp3')
    elif (escolhaadv == 'tesoura' and vaiprojogo == 'papel'):
        print("A tesoura corta o papel\n\033[31mVOCÊ PERDEU!")
        playsound.playsound('marioderrota.mp3')
    elif (escolhaadv == 'pedra' and vaiprojogo == 'tesoura'):
        print("A pedra quebra a tesoura\n\033[31mVOCÊ PERDEU!")
        playsound.playsound('marioderrota.mp3')
    elif (escolhaadv == 'papel' and vaiprojogo == 'pedra'):
        print("O papel embrulha a pedra\n\033[31mVOCÊ PERDEU!")
        playsound.playsound('marioderrota.mp3')
    elif escolhaadv == vaiprojogo:
        print("Mesmas escolhas\nEMPATE!\nescuta musica do got ai entao fodase")
        playsound.playsound('somgot.mp3')
    else:
        print("houve algum erro")
