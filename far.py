#!/bin/user/python

# module

import os,sys,time,subprocess

# menu
def perkalian(a,b):
    return a*b
def pembagian (a,b):
    return a/b
def pertambahan (a,b):
    return a+b
def pengurangan (a,b):
    return a-b

# daftar
os.system("clear")
os.system("figlet kalkulator")
print("      by mr virus spm")
print("++++++++++++++++++++++++++++++")
print("1). perkalian")
print("2). pembagian")
print("3). pertambahan")
print("4). pengurangan")
print("++++++++++++++++++++++++++++++")
mull=input("masukan pilihan => ")

gas1 = int(input("angka pertama => "))
gas2 = int(input("angka kedua => "))

# masukan data
if mull =="1":
   print(gas1,"*",gas2,"=",perkalian(gas1,gas2))
