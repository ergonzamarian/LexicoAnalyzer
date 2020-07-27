#!/usr/bin/python3
# -*- coding: utf-8 -*-

# NOME: ERGON ZAMARIAN LIMA
# RA: 167776
import sys

# ABRIR

programa_fonte = open('programa_fonte.txt', 'r')

# LENDO

leitura_prog_fonte = programa_fonte.read()
leitura_banco_linguagem = ['program','simb_program','begin','simb_begin','end','simb_end','var','simb_var','real','simb_tipo','integer','simb_tipo','float','simb_tipo',',','simb_v','procedure','simb_procedure',';','simb_pv','else','simb_else','read','simb_read','write','simb_write','while','simb_while','if','simb_if','then','simb_then','=','simb_igual','>=','simb_maior_igual','<=','simb_menor_igual','>','simb_maior','<','simb_menor','+','simb_mais','-','simb_menos','*','simb_vezes','/','simb_barra',')','simb_fecha_parenteses','(','simb_abre_parenteses','{','simb_abre_chaves','}','simb_fecha_chaves','.','simb_ponto',':','simb_dp',':=','simb_atrib']


# LISTAS AUXILIARES

programa_aux = leitura_prog_fonte.split('\n')

# TRATATIVAS DE PALAVRAS DA LIGUAGEM
leitura_prog_fonte = leitura_prog_fonte.replace(","," , ")
leitura_prog_fonte = leitura_prog_fonte.replace(";"," ; ")
leitura_prog_fonte = leitura_prog_fonte.replace("{"," { ")
leitura_prog_fonte = leitura_prog_fonte.replace("}"," } ")
leitura_prog_fonte = leitura_prog_fonte.replace(">"," > ")
leitura_prog_fonte = leitura_prog_fonte.replace("<"," < ")
leitura_prog_fonte = leitura_prog_fonte.replace("+"," + ")
leitura_prog_fonte = leitura_prog_fonte.replace("-"," - ")
leitura_prog_fonte = leitura_prog_fonte.replace("*"," * ")
leitura_prog_fonte = leitura_prog_fonte.replace("/"," / ")
leitura_prog_fonte = leitura_prog_fonte.replace("("," ( ")
leitura_prog_fonte = leitura_prog_fonte.replace(")"," ) ")
leitura_prog_fonte = leitura_prog_fonte.replace("."," . ")
leitura_prog_fonte = leitura_prog_fonte.replace(":"," : ")
leitura_prog_fonte = leitura_prog_fonte.replace("="," = ")


# TRANSFORMANDO A STRING EM VETOR JA ADEQUADA AS LINGUAGENS

leitura_prog_fonte = leitura_prog_fonte.split()

# NOMEANDO VETOR

prog_fonte_vetor = leitura_prog_fonte
banco_linguagem_vetor = leitura_banco_linguagem

# IMPRIMINDO NO FORMATO DO ANALISADOR

cont_comentario = 0
linha = '-' * 70
bd = '|'
num = 'num'
print ('')
print ('')
print ('')
print (linha)
print ('RESULTADO ANALISADOR'.center(60))
print (linha)


# lista_final_PB = ARMAZENA TODAS AS PALAVRAS DO PROGRAMA, BANCO E NÚMEROS SEM OS ERROS
# lista_resultado_lexico = INSERE O RESULTADO NA ORDEM EM QUE APARECE NO CÓDIGO FONTE
lista_final_PB = []
lista_resultado_lexico = []
i = 0
while i < len(prog_fonte_vetor):
    
    # PALAVRAS E SIMBOLOS DA LINGUAGEM
    j = 0
    while j < len(banco_linguagem_vetor):

        if prog_fonte_vetor[i] == banco_linguagem_vetor[j]:
            # TRATATIVAS ESPECIAIS
            if prog_fonte_vetor[i] == ':' and prog_fonte_vetor[i+1] == '=':
                print (':='.center(20), bd.center(20), 'simb_atrib'.center(10))
                print (linha)
                lista_final_PB.insert(i,prog_fonte_vetor[i])
                lista_resultado_lexico.insert(i,'simb_atrib')
                i+=1
            elif prog_fonte_vetor[i] == '>' and prog_fonte_vetor[i+1] == '=':
                print ('>='.center(20), bd.center(20), 'simb_maior_igual'.center(10))
                print (linha)
                lista_final_PB.insert(i,prog_fonte_vetor[i])
                lista_resultado_lexico.insert(i,'simb_maior_igual')
                i+=1
            elif prog_fonte_vetor[i] == '<' and prog_fonte_vetor[i+1] == '=':
                print ('<='.center(20), bd.center(20), 'simb_menor_igual'.center(10))
                print (linha)
                lista_resultado_lexico.insert(i,'simb_menor_igual')
                lista_final_PB.insert(i,prog_fonte_vetor[i])
                i+=1 
            else:
                if prog_fonte_vetor[i] == '{':
                    lista_final_PB.insert(i,'{')
                    # VERIFICAÇÃO DE EXCLUSÃO
                    k = i
                    exclui = False
                    while k < len(prog_fonte_vetor):
                        if prog_fonte_vetor[k]=='}':
                            exclui = True
                        k+=1
                    s=0
                    if exclui:
                        
                        cont_comentario +=1 
                        lista_final_PB.insert(i,'}')
                        while prog_fonte_vetor[i] != '}':
                            lista_final_PB.insert(i,prog_fonte_vetor[i])
                            i+=1
                        if prog_fonte_vetor[i] == '}':
                            i+=1
                        if s==0:
                            print (prog_fonte_vetor[i].center(20), bd.center(20), banco_linguagem_vetor[banco_linguagem_vetor.index(prog_fonte_vetor[i])+1].center(10))
                            print (linha)
                            lista_final_PB.insert(i,prog_fonte_vetor[i])
                            lista_resultado_lexico.insert(i,banco_linguagem_vetor[banco_linguagem_vetor.index(prog_fonte_vetor[i])+1])
                            
                        else:
                            print (prog_fonte_vetor[i].center(20), bd.center(20), banco_linguagem_vetor[j+1].center(10))
                            print (linha)
                            lista_final_PB.insert(i,prog_fonte_vetor[i])
                            lista_resultado_lexico.insert(i,banco_linguagem_vetor[j+1])
                        s+=1
                    else: 
                        print (prog_fonte_vetor[i].center(20), bd.center(20), banco_linguagem_vetor[j+1].center(10))
                        print (linha)
                        lista_final_PB.insert(i,prog_fonte_vetor[i])
                        lista_resultado_lexico.insert(i,banco_linguagem_vetor[j+1])
                else:
                    print (prog_fonte_vetor[i].center(20), bd.center(20), banco_linguagem_vetor[j+1].center(10))
                    print (linha)
                    lista_final_PB.insert(i,prog_fonte_vetor[i])
                    lista_resultado_lexico.insert(i,banco_linguagem_vetor[j+1])

                    if '=' in prog_fonte_vetor:
                        lista_final_PB.insert(i,'=')
        j+=1
    
    # NÚMEROS
    if prog_fonte_vetor[i].isdigit(): 
        if prog_fonte_vetor[i+1] == '.' and prog_fonte_vetor[i+2].isdigit():
            num_aux = prog_fonte_vetor[i] + '.' + prog_fonte_vetor[i + 2]
            print (num_aux.center(20), bd.center(20), num.center(10))
            print (linha)
            lista_final_PB.insert(i,prog_fonte_vetor[i])
            lista_final_PB.insert(i,prog_fonte_vetor[i+1])
            lista_final_PB.insert(i,prog_fonte_vetor[i+2])
            lista_resultado_lexico.insert(i,num_aux)
            i+=2
        else:
            print (prog_fonte_vetor[i].center(20), bd.center(20), num.center(10))
            print (linha)
            lista_final_PB.insert(i,prog_fonte_vetor[i])
            lista_resultado_lexico.insert(i,num)
    # ID
    elif (prog_fonte_vetor[i] not in banco_linguagem_vetor and prog_fonte_vetor[i][0] not in '_' and  prog_fonte_vetor[i][0].isdigit() == False):

        j = 1
        condicao = True
        while j < len(prog_fonte_vetor[i]):
            if (prog_fonte_vetor[i][j] in '_') or (prog_fonte_vetor[i][j].isdigit()) or (prog_fonte_vetor[i][j].isupper()) or (prog_fonte_vetor[i][j].islower()):
                condicao
            else:
                condicao = False
            j+=1
        if condicao:
                    print (prog_fonte_vetor[i].center(20), bd.center(20), 'ident'.center(10))
                    print (linha)
                    lista_final_PB.insert(i,prog_fonte_vetor[i])
                    lista_resultado_lexico.insert(i,'ident')
    i+=1

# ERROS

cont_erro = 0
print('\n')
print ('#'* 70)
print('\n')
print (linha)
i = 0

print ('ERRO(S) LÉXICO(S)'.center(60))

while i < len(prog_fonte_vetor):

    if prog_fonte_vetor[i] not in lista_final_PB:
        cont_erro +=1
        j=0
        while j < len(programa_aux):
            if prog_fonte_vetor[i] in programa_aux[j]: 
                print (linha)
                print (prog_fonte_vetor[i].center(20), bd.center(20), 'ERRO LÉXICO LINHA: '.center(10),j + 1)
                lista_resultado_lexico.insert(i,'ERRO LÉXICO')
            j+=1
    i+=1
if cont_erro == 0:
    print (linha)
    print(' NÃO HÁ ERROS LÉXICOS')
    print(' A SOLICITAÇÃO FOI RECEBIDA COM SUCESSO')
    print (linha)
    print('\n')
    print ('#'* 70)
    print('\n')
    print (linha)
    print('DADOS DO PROGRAMA'.center(60))
else:
    print (linha)
    print('\n')
    print ('#'* 70)
    print('\n')
    print (linha)
    print('DADOS DO PROGRAMA'.center(60))
    print (linha)
    print (' QUANTIDADE DE ERROS LÉXICOS: ', cont_erro)

print (linha)
print (' QUANTIDADE DE COMENTARIOS FEITOS: ', cont_comentario)
print (linha)
print('\n'*3)

op = input('Deseja imprimir resultado (sim ou nao) ? ')

if op =='sim':
    print('\n')
    print ('#'* 70)
    print('\n')
    print(lista_resultado_lexico)
    print('\n')
    print ('#'* 70)
    print('\n')
    print(' Até a próxima!!')
else:
    print('\n')
    print ('#'* 70)
    print('\n')
    print(' Até a próxima!!')