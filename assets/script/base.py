from random import randint
from time import sleep

#Força= Hércules   Vel= Hermes  Per= Artemis  Sab= Atena

listra=str(("-="*15))
linha=("--"*20)

##################################################################################################################################################

poçãozoera_produtos=("poção de riso","poção lingua roxa","poção-não-me-esqueça","poção-me-esqueça")
poçãozoera_preços=(5, 7, 20, 40)
sacolao_produtos=str("tomate batata cenoura maçã").split()
sacolao_precos=(3, 3, 4, 5)
pronomes=("os tomates","as batatas","as cenouras","as maçãs")

poção_produtos1=("poção de cura 1","poção de força 1","poção de sabedoria 1","poção de velocidade 1","poção de percepção 1")
poção_produtos2=("poção de cura 1","poção de cura 2","poção de força 1","poção de força 2","poção de sabedoria 1","poção de sabedoria 2","poção de velocidade 1","poção de velocidade 2","poção de percepção 1","poção de percepção 2")
poção_produtos3=("poção de cura 1","poção de cura 2","poção de cura 3","poção de força 1","poção de força 2","força de hécules","poção de sabedoria 1","poção de sabedoria 2","sabedoria de atena","poção de velocidade 1","poção de velocidade 2","velocidade de hermes","poção de percepção 1","poção de percepção 2","percepção de artémis")

poção_produtos1_plural=("poções de cura 1","poções de força 1","poções de sabedoria 1","poções de velocidade 1","poções de percepção 1")
poção_produtos2_plural=("poções de cura 1","poções de cura 2","poções de força 1","poções de força 2","poções de sabedoria 1","poções de sabedoria 2","poções de velocidade 1","poções de velocidade 2","poções de percepção 1","poções de percepção 2")
poção_produtos3_plural=("poções de cura 1","poções de cura 2","poções de cura 3","poções de força 1","poções de força 2","força de hécules","poções de sabedoria 1","poções de sabedoria 2","sabedoria de atena","poções de velocidade 1","poções de velocidade 2","velocidade de hermes","poções de percepção 1","poções de percepção 2","percepção de artémis")

poção_preços1=(20,15,15,10,10)
poção_preços2_semajuda=(20,50,15,30,15,30,10,20,10,20)
poção_preços2_comajuda=(15,35,10,20,10,20,5,10,5,10)
poção_preços3_semajuda=(20,50,150,15,30,80,15,30,80,10,20,50,10,20,50)
poção_preços3_comajuda=(15,35,60,10,20,30,10,20,30,5,10,15,5,10,15)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

loja_m1="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura       1 ---> $20\n{}\n[ 2 ] Poção de força      1 ---> $15\n{}\n[ 3 ] Poção de sabedoria  1 ---> $15\n{}\n[ 4 ] Poção de velocidade 1 ---> $10\n{}\n[ 5 ] Poção de percepção  1 ---> $10\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)

loja_m2_semajuda_comum="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura       1 ---> $20\n{}\n[ 2 ] Poção de força      1 ---> $15\n{}\n[ 3 ] Poção de sabedoria  1 ---> $15\n{}\n[ 4 ] Poção de velocidade 1 ---> $10\n{}\n[ 5 ] Poção de percepção  1 ---> $10\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)
loja_m2_semajuda_premium="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura       2 ---> $50\n{}\n[ 2 ] Poção de força      2 ---> $30\n{}\n[ 3 ] Poção de sabedoria  2 ---> $30\n{}\n[ 4 ] Poção de velocidade 2 ---> $20\n{}\n[ 5 ] Poção de percepção 2 ---> $20\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)
loja_m2_comajuda_comum="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura       1 ---> $15\n{}\n[ 2 ] Poção de força      1 ---> $10\n{}\n[ 3 ] Poção de sabedoria  1 ---> $10\n{}\n[ 4 ] Poção de velocidade 1 ---> $5\n{}\n[ 5 ] Poção de percepção  1 ---> $5\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)
loja_m2_comajuda_premium="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura       2 ---> $35\n{}\n[ 2 ] Poção de força      2 ---> $20\n{}\n[ 3 ] Poção de sabedoria  2 ---> $20\n{}\n[ 4 ] Poção de velocidade 2 ---> $10\n{}\n[ 5 ] Poção de percepção 2 ---> $10\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)

loja_m3_semajuda_comum="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura       1 ---> $20\n{}\n[ 2 ] Poção de força      1 ---> $15\n{}\n[ 3 ] Poção de sabedoria  1 ---> $15\n{}\n[ 4 ] Poção de velocidade 1 ---> $10\n{}\n[ 5 ] Poção de percepção  1 ---> $10\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)
loja_m3_semajuda_premium="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura       2 ---> $50\n{}\n[ 2 ] Poção de força      2 ---> $30\n{}\n[ 3 ] Poção de sabedoria  2 ---> $30\n{}\n[ 4 ] Poção de velocidade 2 ---> $20\n{}\n[ 5 ] Poção de percepção 2 ---> $20\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)
loja_m3_comajuda_comum="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura       1 ---> $15\n{}\n[ 2 ] Poção de força      1 ---> $10\n{}\n[ 3 ] Poção de sabedoria  1 ---> $10\n{}\n[ 4 ] Poção de velocidade 1 ---> $5\n{}\n[ 5 ] Poção de percepção  1 ---> $5\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)
loja_m3_comajuda_premium="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura       2 ---> $35\n{}\n[ 2 ] Poção de força      2 ---> $20\n{}\n[ 3 ] Poção de sabedoria  2 ---> $20\n{}\n[ 4 ] Poção de velocidade 2 ---> $10\n{}\n[ 5 ] Poção de percepção  2 ---> $10\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)
loja_m3_semajuda_divina="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura         3 ---> $150\n{}\n[ 2 ] Força de Hércules       ---> $60\n{}\n[ 3 ] Sabedoria de Atena      ---> $60\n{}\n[ 4 ] Velocidade de Hermes   ---> $50\n{}\n[ 5 ] Percepção de Artémis   ---> $50\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)
loja_m3_commajuda_divina="=-=-=-=-=-=-= < Produtos > =-=-=-=-=-=-=\n\n{}\n[ 1 ] Poção de cura         3 ---> $60\n{}\n[ 2 ] Força de Hércules       ---> $30\n{}\n[ 3 ] Sabedoria de Atena      ---> $30\n{}\n[ 4 ] Velocidade de Hermes   ---> $15\n{}\n[ 5 ] Percepção de Artémis   ---> $15\n{}\n".format(linha, linha, linha, linha, linha,linha,listra)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


####################################################################################################################################################################

ganancia=0
#ouro=(randint(0,10))
ouro=300000
xp=0

#statuses= hp,atk,vel,per,sab,cons
#jooj


poção_ajuda=False
ajudinha=0
loja_de_poções_niveis=0
xp_da_loja_de_poção=0
loja_de_poçõesnvl1=False
loja_de_poçõesnvl2=False
loja_de_poçõesnvl3=False
finaldejogo=0
final=False
menu_loja=False
mundo_aberto= False
loja_dentro=False

while final is False:
	leva_dano=0

	umd=randint(5,7)


	reinos_aleatorio=randint(0,4)
	reinos_elfo=("Alqualondë Avallonè Brithombar Eldamar Ithilien").split()
	reinos_ciclope=("Glúkdra Mashshag Tandra Ugarg Gashbad").split()
	reinos_humano=("Vermênia Estátira Divinópolis Anauroch Warkatopia").split()
	reino=(reinos_humano, reinos_elfo, reinos_ciclope)
	
	inventário= {"quanto" : [], "item" : []}

	
	print("{}Bem vindo ao RPG EXTREMAMENTE experimental do Jhony{}\n".format(listra,listra))
	raças=("Humano","Elfo","Ciclope")
	print('''Raças disponíveis:
		[ 1 ] Humano
		[ 2 ] Elfo
		[ 3 ] Ciclope''')
	raça_escolha=int(input("Qual é a sua escolha? "))
	raça_escolhida=(raças[raça_escolha-1])

	nome=str(input("\nQual é o seu nome? ")).capitalize()
	print(listra)
	reino_raça=(reino[raça_escolha-1])
	reino_nasc=(reino_raça[reinos_aleatorio])
	print(f"\nSeu nome é {nome}, um {raça_escolhida.lower()} nascido e criado no reino de {reino_nasc}. Você tem {ouro} de ouro e {xp} de XP\n\n{listra}")


	if raça_escolha==1:
		player_atk= randint(1,8)
		player_vel= randint(1,8)
		player_per= randint(1,8)
		player_sab= randint(1,8)
		player_cons=randint(1,8)
		player_hp=((randint(1,8)+player_cons)*2)
		inventário=inventário+("1x Espada")

	elif raça_escolha==2:
		player_atk= (randint(1,6)-3)
		player_vel= (randint(2,7)+4)
		player_per= (randint(2,7)+1)
		player_sab= (randint(4,9)+3)
		player_cons=(randint(1,7)-1)
		player_hp=((umd*2)-1)
		inventário=inventário+("1x Cajado")

	elif raça_escolha==3:
		player_atk= (randint(4,9)+2)
		player_vel= (randint(1,5)-3)
		player_per= (randint(2,6)-4)
		player_sab= (randint(1,6)-3)
		player_cons=(randint(3,10))
		player_hp=((randint(3,9)+player_cons+3)*3)
		inventário['item'].append('Porrete')
		inventário['quanto'].append(1)
	stat_list=("""
	Seus atributos são:
	HP: {}
	ATAQUE: {}
	VELOCIDADE: {}
	PERCEPÇÃO: {}
	SABEDORIA: {}
	CONSTITUIÇÃO: {}""".format(player_hp,player_atk,player_vel,player_per,player_sab,player_cons))
	print(stat_list)
	print('\n',listra,'\n')
	invent=[inventário['quanto']]


	bichins=("goblin diabrete duende").split()
	bichins_hp=randint(30,50)
	inimigo_bixin=(bichins[randint(0,2)])


	fim=False

	while mundo_aberto is not True:
		while fim is not True:
			if raça_escolhida==3:
				dano_magico=randint(1,4)
				dano_fisico=randint(1,7)+player_atk
			elif raça_escolhida==2:
				dano_magico=randint(1,7)+player_sab
				dano_fisico=randint(1,4)
			else:
				dano_magico=randint(1,6)+player_sab
				dano_fisico=randint(1,6)+player_atk

			danos=(dano_fisico, dano_magico)


			print("dm {}".format(dano_magico))
			print("df {}".format(dano_fisico))
			print("\n")

			print("Seu HP: {}".format(player_hp))
			print("Tem um {} te atacando, mete a porrada nesse merda!!".format(inimigo_bixin))
			print("HP do {}: {}".format(inimigo_bixin, bichins_hp))
			print("Tipos de dano:\n[ 1 ] Dano físico (ATAQUE)\n[ 2 ] Dano mágico (SABEDORIA)")
			escolhadedano=int(input("Qual é a sua escolha, fi? "))


#========================================================================================================================================
#========================================================================================================================================
			dano_causado=danos[escolhadedano-1]
			if dano_causado<0:
				dano_causado=0

			bichins_hp=bichins_hp-dano_causado
			if bichins_hp<=0:
				print("\n{}{}\n\nVocê causou {} de dano no {}. Deixando ele com 0 de vida\n\n{}{}".format(listra,listra,dano_causado, inimigo_bixin,listra,listra))
				print("Aeee, tu matou o {}!\n{}{}".format(inimigo_bixin,listra,listra))
				adicional=(randint(50, 80))
				xp_adicional=(randint(100, 130))
				print("\n")
				print(listra)
				ouro+=adicional
				xp+=xp_adicional
				print("Você ganhou {} de ouro e {} de XP. Agora você tem {} de ouro e {} de XP".format(adicional,xp_adicional, ouro, xp))
				print(listra)
				print("\n")

				fim=True

			elif bichins_hp>0:
				print("\n{}{}\n\nVocê causou {} de dano no {}. Deixando ele com {} de vida\n\n{}{}".format(listra,listra,dano_causado, inimigo_bixin, bichins_hp,listra,listra))
			if bichins_hp>=0:
				leva_dano=(randint(3,6))
				player_hp=player_hp-leva_dano
				
			if bichins_hp>=0 and player_hp>=0:
				print("\nAgora ele te ataca, causando {} de dano, te deixando com {} de vida\n\n{}{}".format(leva_dano, player_hp,listra,listra))
			if player_hp<=0 and bichins_hp>=0:
				print("Agora ele te ataca, causando {} de dano, te deixando com 0 de vida".format(leva_dano))
				print(listra)
				print("GAME OVER")
#========================================================================================================================================
#========================================================================================================================================

				fim=True
				while finaldejogo==0:
					game_over=str(input("Você perdeu, deseja jogar novamente? [S/N] ")).strip().upper()[0]
					if game_over=='S':
						final=False
						finaldejogo=1
					elif game_over=='N':
						finaldejogo=1
						final=True
						print(listra)
					else:
						print("Escolha invalida")
	




		loja_dentro=False
		tio=randint(5,10)
		print("Você está na rua, o que quer fazer?\n[ 1 ] Ir para o sacolão do seu zé\n[ 2 ] Ir para a loja de poções\n[ 3 ] Ir para a loja de armas\n[ 4 ] Checar ouro e XP\n[ 5 ] Checar inventário")
		escolha=int(input())
	#SACOLÃO
		if escolha==1:
			while ganancia==0: #FAZ UMA VEZ SÓ BOBÃO-------------------------------------
				print("{}\nA caminho do sacolão, você acaba esbarrando com seu tio, e ele te dá {} moedas de ouro!\n{}".format(listra, tio, listra))
				ouro=ouro+tio
				ganancia=ganancia+1
			while loja_dentro is not True:
				menu_loja=False
				print("Você tá no sacolão, o que pretende fazer?\n[ 1 ] Comprar\n[ 2 ] Checar ouro e XP\n[ 3 ] Sair")
				sescolha=int(input())
				if sescolha==1:
					while menu_loja is not True:
						print("Produtos\n[ 1 ] Tomate ----> $3\n[ 2 ] Batata ----> $3\n[ 3 ] Cenoura ---> $4\n[ 4 ] Maçã ------> $5\n[ 5 ] Sair")
						produto=int(input())
						quantidade=int(input("Quer comprar quant{}? ".format(pronomes[produto-1])))
						preço_total=(sacolao_precos[produto-1])*quantidade
						print("Ao todo isso vai custar ${}, você tem ${} deseja continuar? [S/N]".format(preço_total, ouro))
						simnao=str(input()).upper()[0]
						if simnao=='S':
							if ouro<preço_total:
									print("{}\nVocê não tem dinheiro o suficiente. Faltam ${} pra poder comprar isso\n{}\n".format(listra, preço_total-ouro, listra))
							if quantidade>1 and ouro>preço_total:
								ouro=ouro-(sacolao_precos[produto-1])*quantidade
								print("Você comprou {} {}s e agora tem ${}".format(quantidade,sacolao_produtos[produto-1], ouro))
								menu_loja=True
							elif quantidade==1 and ouro>preço_total:
								ouro=ouro-(sacolao_precos[produto-1])*quantidade
								print("Você comprou 1 {} e agora tem ${}".format(sacolao_produtos[produto-1], ouro))
							'''inventário=inventário+"\n"+str(quantidade)+"x"+(sacolao_produtos[produto-1].capitalize())'''
							menu_loja=True
						elif simnao=='N':
							menu_loja=True

				elif sescolha==2:
					print("{}\nSeu ouro e xp são: ${} XP {}\n{}\n".format(listra,ouro, xp, listra))
				elif sescolha==3:
					loja_dentro=True


		elif escolha==2:
			while loja_dentro is not True:
				menu_loja=False
				if xp_da_loja_de_poção<2500:
					print("Você entra na loja de poções e se depara com vários frascos com liquídos de diferentes cores\nO que pretende fazer?\n[ 1 ] Comprar\n[ 2 ] Checar ouro e XP\n[ 3 ] Seu inventário\n[ 4 ] Ler placa\n[ 5 ] Sair")
				elif xp_da_loja_de_poção>=2500 and xp_da_loja_de_poção<7000:
					print("Você entra na loja de poções e se depara com vários frascos com liquídos de diferentes cores\nO que pretende fazer?\n[ 1 ] Comprar sessão comum\n[ 2 ] Comprar sessão premium\n[ 3 ] Checar ouro e XP\n[ 4 ] Sair")
				elif xp_da_loja_de_poção>=7000:
					print("Você entra na loja de poções e se depara com vários frascos com liquídos de diferentes cores\nO que pretende fazer?\n[ 1 ] Comprar sessão comum\n[ 2 ] Comprar sessão premium\n[ 3 ] Comprar na sessão divina\n[ 4 ] Checar ouro e XP\n[ 5 ] Sair")
				sescolha=int(input())
				if sescolha==1:
						while menu_loja is not True:
								if xp_da_loja_de_poção<2500:
									print(loja_m1)
									produto=int(input())
									quantidade=int(input("Quer comprar quantas {}? ".format(poção_produtos1_plural[produto-1])))
									preço_total=(poção_preços1[produto-1])*quantidade
								
								elif xp_da_loja_de_poção>=7000 and poção_ajuda==True:
									quantidade=int(input("Quer comprar quantas {}? ".format(poção_produtos3_plural[produto-1])))
									preço_total=(poção_preços3_comajuda[produto-1])*quantidade
									#
									#
								
								elif xp_da_loja_de_poção>7000:
									quantidade=int(input("Quer comprar quantas {}? ".format(poção_produtos3_plural[produto-1])))
									preço_total=(poção_preços3_semajuda[produto-1])*quantidade
								print("Ao todo isso vai custar ${}, você tem ${} deseja continuar? [S/N]".format(preço_total, ouro))
								simnao=str(input()).upper()[0]
								if simnao=='S':
									if ouro<preço_total:
											print("{}\nVocê não tem dinheiro o suficiente. Faltam ${} pra poder comprar isso\n{}\n".format(listra, preço_total-ouro, listra))
									if quantidade>1 and ouro>preço_total:
										ouro=ouro-(poção_preços1[produto-1])*quantidade
										print("Você comprou {} {}s e agora tem ${}".format(quantidade,poção_produtos1_plural[produto-1], ouro))

									elif quantidade==1 and ouro>preço_total:
										ouro=ouro-(poção_preços1[produto-1])*quantidade
										print("Você comprou 1 {} e agora tem ${}".format(poção_produtos1[produto-1], ouro))
									menu_loja=True
									xp_da_loja_de_poção=xp_da_loja_de_poção+preço_total

								elif simnao=='N':
									menu_loja=True
				elif sescolha==2:
					if xp_da_loja_de_poção<2500:
						print("{}\nSeu ouro e xp são: ${}\n{}\n".format(listra,ouro, listra))
					elif xp_da_loja_de_poção>=2500 and xp_da_loja_de_poção <7000 and poção_ajuda==True:
						while menu_loja is not True:
								print(loja_m2_comajuda_premium)
								quantidade=int(input("Quer comprar quantas {}? ".format(poção_produtos2_plural[produto-1])))
								preço_total=(poção_preços2_comajuda[produto-1])*quantidade
						print("Ao todo isso vai custar ${}, você tem ${} deseja continuar? [S/N]".format(preço_total, ouro))
						simnao=str(input()).upper()[0]
						if simnao=='S':
								if ouro<preço_total:
									print("{}\nVocê não tem dinheiro o suficiente. Faltam ${} pra poder comprar isso\n{}\n".format(listra, preço_total-ouro, listra))
								if quantidade>1 and ouro>preço_total:
									ouro=ouro-(poção_preços1[produto-1])*quantidade
									print("Você comprou {} {}s e agora tem ${}".format(quantidade,poção_produtos1_plural[produto-1], ouro))


								elif quantidade==1 and ouro>preço_total:
									ouro=ouro-(poção_preços1[produto-1])*quantidade
									print("Você comprou 1 {} e agora tem ${}".format(poção_produtos1[produto-1], ouro))
								menu_loja=True
								xp_da_loja_de_poção=xp_da_loja_de_poção+preço_total


					elif xp_da_loja_de_poção>2500 and xp_da_loja_de_poção <7000:
						print(loja_m2_semajuda_premium)
						quantidade=int(input("Quer comprar quantas {}? ".format(poção_produtos2_plural[produto-1])))
						preço_total=(poção_preços2_semajuda[produto-1])*quantidade

				elif sescolha==3:
					print(f"\n{listra}\nSeu inventário contém:\n{inventário}\n.")
				elif sescolha==4:
					while menu_loja is not True:
						print(ajudinha)
						print('Você se aproxima de uma placa encima de uma caixa e lê: "Por favor, nos doe algumas moedas para expandirmos nossa loja"')
						simnao=str(input("Deseja doar? [S/N]")).upper()[0]
						if simnao=="S":
							migalha=int(input("Quanto deseja doar? Você tem ${} ".format(ouro)))
							print("Você coloca {} moedas na caixa, e agora você tem ${}".format(migalha,ouro-migalha))
							menu_loja=True
							ouro=ouro-migalha
							ajudinha=ajudinha+migalha
							xp_da_loja_de_poção=xp_da_loja_de_poção+migalha
						elif simnao=="N":
							menu_loja=True
				elif sescolha==5:
					loja_dentro=True



		elif escolha==4:
			print("{}\nSeu ouro e xp são: ${} XP {}\n{}\n".format(listra,ouro, xp, listra))
		elif escolha==5:
			print(f"\n{listra}\nSeu inventário contém:\n{invent}\n{listra}\n")

