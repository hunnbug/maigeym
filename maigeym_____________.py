# -*- coding: cp1251 -*-
import random
from time import sleep
import os

def resumegame(game):
    print("������ �������� ���?\n1 - ��\n2 - ���")
    a = int(input())
    if(a == 1):
        #if(game == 1):
           # sloti777()
        if(game == 2):
            Roulette.stavka()
    if(a == 2):
        return 0

#def sloti777():
    #elem = ["�����", "���������", "����� ����", "�����", "����", "�����"]
    #result = []
    #for i in range(3):
       # r = random.randint(0,5)
        #result.append(elem[r])
       # resumegame(1)
    #return 0 #����� 23:03, �������� ��������, ���� ���������� �����, ����� ��������, ����� �������� ��������

            
class Roulette:
    stavka_cv = ""
    result = ""
    def stavka():
        print("�� ��� �������?: \n1.������\n2.�������\n3.����")
        a = int(input())
        match a:
            case 1:
                Roulette.stavka_cv = "������ ������"
            case 2:
                Roulette.stavka_cv = "������� ������"
            case 3:
                Roulette.stavka_cv = "����"
        Roulette.roulette()
    def roulette():
        stavka = Roulette.stavka_cv
        result = Roulette.result
        r = random.randint(0, 100)
        if r <= 49:
            result = "������ ������"
        if 49 < r <= 98:
            result = "������� ������"
        if 98 < r <= 100:
            result = "����"
            
        print("������� ��������")
        sleep(0.5)
        print("1")
        sleep(0.5)
        print("2")
        sleep(0.5)
        print("3")
        sleep(0.5)
        
        match result:
            case "������ ������":
                print("��� ������ ������ ������")
            case "������� ������":
                print("��� ������ ������� ������")
            case "����":
                print("��� ������ ����")
        if result == stavka:
            print("�� ��������")
        else:
            print("�� ���������")
        resumegame(2)
        return 0

class Blackjack:
    koloda = ["�������� ������", "�������� ������", "������ ����", "��������� ������",
                "�������� ����", "�������� ����", "���� ����", "��������� ����",
                "�������� �����", "�������� �����", "����� ����", "��������� �����",
                "�������� ���", "�������� ���", "��� ����", "��������� ���",
                "2 ����", "2 �����", "2 ������", "2 ����",
                "3 ����", "3 �����", "3 ������", "3 ����",
                "4 ����", "4 �����", "4 ������", "4 ����",
                "5 ����", "5 �����", "5 ������", "5 ����",
                "6 ����", "6 �����", "6 ������", "6 ����",
                "7 ����", "7 �����", "7 ������", "7 ����",
                "8 ����", "8 �����", "8 ������", "8 ����",
                "9 ����", "9 �����", "9 ������", "9 ����",
                "10 ����", "10 �����", "10 ������", "10 ����",]
    cost = 0
    ruka = []
    dealerCost = 0
    dealerRuka = []
    def dealer():
        for i in range(2):
            r = random.randint(0,51)
            if r <= 15:
                Blackjack.dealerCost += 10
            if 15 < r <= 19:
                Blackjack.dealerCost += 2
            if 19 < r <= 23:
                Blackjack.dealerCost += 3
            if 23 < r <= 27:
                Blackjack.dealerCost += 4
            if 27 < r <= 31:
                Blackjack.dealerCost += 5
            if 31 < r <= 35:
                Blackjack.dealerCost += 6
            if 35 < r <= 39:
                Blackjack.dealerCost += 7
            if 39 < r <= 43:
                Blackjack.dealerCost += 8
            if 43 < r <= 47:
                Blackjack.dealerCost += 9
            if 47 < r <= 51:
                Blackjack.dealerCost += 10
            Blackjack.dealerRuka.append(Blackjack.koloda[r])
        
    def gameworks():
        print("����� ���� ������� �������� ����, �� ��� ������ � ��������\n1. ��������������\n2. ����")
        a = int(input())
        if a == 1:
            Blackjack.game(1)
        if a == 2:
            os.system('cls')
            return 0
    def game(new):
        if new == 1:
            Blackjack.cost = 0
            Blackjack.dealerCost = 0
            Blackjack.ruka.clear()
            Blackjack.dealerRuka.clear()
        if new == 0:
            new = 0
        r = random.randint(0,51)
        if r <= 11:
            Blackjack.cost += 10
        if 11 < r <= 15:
            Blackjack.cost += 11
        if 15 < r <= 19:
            Blackjack.cost += 2
        if 19 < r <= 23:
            Blackjack.cost += 3
        if 23 < r <= 27:
            Blackjack.cost += 4
        if 27 < r <= 31:
            Blackjack.cost += 5
        if 31 < r <= 35:
            Blackjack.cost += 6
        if 35 < r <= 39:
            Blackjack.cost += 7
        if 39 < r <= 43:
            Blackjack.cost += 8
        if 43 < r <= 47:
            Blackjack.cost += 9
        if 47 < r <= 51:
            Blackjack.cost += 10
        Blackjack.ruka.append(Blackjack.koloda[r])
            
        print("���� ����: ", end = "")
        for i in range(len(Blackjack.ruka)):
            print(Blackjack.ruka[i], end = " | ")
        print ("\n���� ����: " + str(Blackjack.cost))
        
        if Blackjack.cost == 21:
            print("\n�� ��������\n")
            Blackjack.gameworks()
            return 0
        if Blackjack.cost > 21:
            print("\n�� ���������\n")
            Blackjack.gameworks()
        
        print("1. ��������\n2. ���")
        a = int(input())
        if(a == 1):
            Blackjack.game(0)
        if(a == 2):
            Blackjack.dealer()
                
            print("���� ���� ������: " + str(Blackjack.dealerCost))
            if(Blackjack.cost > Blackjack.dealerCost):
                print("\n�� ��������!\n")
                Blackjack.gameworks()
                return 0
            if(Blackjack.cost < Blackjack.dealerCost):
                print("\n�� ���������\n")
                Blackjack.gameworks()
                return 0    
            if(Blackjack.cost == Blackjack.dealerCost):
                print("\n�����\n")
                Blackjack.gameworks()
                return 0 
                
        print("�� ���������")
        return 0       

print("������� v f.01\n\n")
print("�", end = "")
sleep(0.1)
print("a", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print(": ", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print(": ", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�", end = "")
sleep(0.1)
print("�")
sleep(2)

print("�� ������ � ����� � ������, ������ ���� ����������� ��� ����� ���������� �����")
print("1. ����� � ������")
print("2. ����������� ������� ����� � ������ �� �����")
print("����� ������� �������� �������� �����, ��� ���������������")
a = int(input())

match a:
    case 1:
        print("�� ������� � ������, ������ ������ ������� ������������ �����", end = "")
    case 2:
        exit()
print(".", end = "")
sleep(0.1)
print(".", end = "")
sleep(0.1)
print(".")
print("����� � ������ �� ��������� ����������� ���� � ��, ��������, ������������ ���������� ������� ���������")
print("�� ����� ��� �������� ��������� ���� ������, ������, ��� �������� �� ����� ����� �������� � � ��������� � ��� ��� ����� ��� �����")
input("������� ����� ������ ��� �����������")
os.system('cls')
print("�� �� ����� ���������� �����, ����� ������")
sleep(1)
print("�� � �� ��� ������ ���")
sleep(2)
os.system('cls')

print("����� ������ � ������ �� �������� �������� ���������� ������, �������� ������ � ������ �������� ��� ������ �����������")
def vibor():
    print("�����:\n1. ����� �������� � ��������\n2. ������� ��� ���������� � ����� ������ � ������(� ����������)\n3. ����� ������ � �����(� ����������)\n4. ����� ������ � �������(� ����������")
    a = int(input())
    if a != 1:
        vibor()
    if a == 1:
        Blackjack.gameworks()
vibor()
#��� ��������� � ����������, �������� ��������, � �������� �������� ��� ������, ����� ����� ����, � ����������
#� �������� ���������� � ���� � ������� ������ � ���� ������ �� �����, � ��������
