# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:30:03 2017

@author: ZHAW
"""

import csv
import math
import sys

def punkt_eingabe():
    ''' Aufgabe: 
        - welche Fehler können entstehen?
        - Fangen Sie die Fehler mit try/except ab
        - Wertebereich: Lassen Sie nur Werte >= -1.
    '''
    x = int(input("x Koordinate: "))
    y = int(input("y Koordinate: "))
    return x, y


def weg_erfassen(weg):
    ''' Aufgabe:
        - Welche Fehler können entstehen?
    '''
    print("Koordinatenpunkte erfassen (abschliessen mit (-1,-1))")
    while True:
        punkt = punkt_eingabe()
        if punkt == (-1,-1):
            print("Danke für die Eingabe", weg)
            break
        else:
            weg.append(punkt)


def weg_laden(weg):
    ''' Aufgabe:
        - Erweitern Sie die Funktion mit einer Eingabe des Filenames
          Defaultwert: v10_B_weg.csv
        - Welche Fehler können entstehen?
        - Fangen Sie die Fehler mit try/except ab
    '''
    csv_weg = csv.reader(open('v10_B_weg.csv', newline=''),
                         delimiter=',', 
                         quotechar='"')
    ''' Aufgabe:
        - Welche Fehler können entstehen?
        - Fangen Sie die Fehler mit try/except ab
    '''
    for punkt in csv_weg:
        weg.append((int(punkt[0]), int(punkt[1])))


def weg_speichern(weg):
    # weg als comma-separated werte speichern
    ''' Aufgabe:
        - Erweitern Sie die Funktion mit einer Eingabe des Filenames
          Defaultwert: v10_B_weg.csv
        - Welche Fehler können entstehen?
        - Fangen Sie die Fehler mit try/except ab
    '''
    writer = csv.writer(open('v09_B_weg.csv', 'w', newline=''),
                        delimiter=',', 
                        quotechar='"', 
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerows(weg)


def weg_laenge(weg):
    ''' Aufgabe:
        - Welche Fehler können entstehen?
    '''
    laenge = 0.0
    for i in range(len(weg)-1):
        x1, y1 = weg[i]
        x2, y2 = weg[i+1]
        laenge += math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return laenge


def finde_naechster_punkt(weg, mein_punkt):
    ''' Aufgabe:
        - Welche Fehler können entstehen?
    '''
    x0, y0 = mein_punkt         # unpacking tuple
    min_abstand = 1e10          # Initialisierung mit grosser Zahl
    min_punkt = (-1, -1)        # Initialisierung mit (-1,-1)
    for xi, yi in weg:
        abstand = math.sqrt((x0-xi)**2 + (y0-yi)**2)
        if abstand < min_abstand:
            min_abstand = abstand
            min_punkt = (xi,yi) # packing tuple
    return min_punkt, min_abstand


def menu_wahl():
    ''' Aufgabe:
        - Welche Fehler können entstehen?
        - Fangen Sie die Fehler mit try/except ab
    '''
    print("\n\nWillkommen - Bitte wählen Sie eine Option")
    print("1) Einlesen einer Liste von Koordinaten ab Tastatur")
    print("2) Speichern der Liste in einer Datei")
    print("3) Laden einer Liste aus einer Datei")
    print("4) Berechnen des Weglänge zwischen den einzelnen Punkten")
    print("5) Bestimmen nächster Wegpunkt und Abstand")
    print("9) Program verlassen")
    die_wahl = 0
    while die_wahl not in [1,2,3,4,5,9]:
        die_wahl = int(input("Ihre Wahl: "))
    return die_wahl


def main():
    ''' Aufgabe:
        - Welche Fehler können entstehen?
    '''
    ein_weg = []
    ein_punkt = (200, 400)
    while (True):
        wahl = menu_wahl()
        if   wahl == 9:
            sys.exit()
        elif wahl == 1:
            weg_erfassen(ein_weg)
            print("Weg erfasst:", ein_weg)
        elif wahl == 2:
            weg_speichern(ein_weg)
            print("Weg gespeichert:", ein_weg)        
        elif wahl == 3:
            weg_laden(ein_weg)
            print("Weg geladen:", ein_weg)
        elif wahl == 4:
            print("Weg:", ein_weg)
            print("Weg Länge:", weg_laenge(ein_weg), "m")
        elif wahl == 5:
            p, d = finde_naechster_punkt(ein_weg, ein_punkt)
            print("Weg:", ein_weg)
            print("Nächster Punkt", p, "Distanz", d)

main()
