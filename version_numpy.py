# projet version numpy
import os
import numpy as np


class Sudoku:
    def __init__(self, in_path, out_path) -> None:
        self.in_path = in_path
        self.out_path = out_path
        # self.error = None

        self.write_log(f"Sudoku # chemin du fichier [{in_path}]\n")

        self.vals = self.import_data(in_path)
        self.matrice = self.formated_data()

        # affichage, +resultat en fichier
        self.afficher_matrice()

    def is_valide(self):
        # Verifier le nombre de valeurs dans un tableau. 9*9 = 81 values
        valide = True
        if len(self.vals) != 81:
            self.write_log("Sudoku # Matrice sudoku introuvable ou/et Nombre de valeur est incorrecte.\n")
            valide = False

        for triple in self.vals:
            if len(triple) == 3:
                x, y, z = map(int, tuple(triple))
                # validation de données [0-8][0-8][1-9]
                if not (0 <= x <= 8 and 0 <= y <= 8 and 1 <= z <= 9):
                    self.write_log(f"Sudoku # [{triple}] \t-> Index erroné\n")
                    valide = False
            else:
                self.write_log(f"Sudoku # [{triple}] \t-> Format incorrect\n")
                valide = False

        return True if valide else False

    def import_data(self, path):
        # importer les données depuis un fichier
        # retourner un tableau de données
        try:
            with open(path, "r") as file:
                contents = file.read()
            # remplacer les retoure-ligne par des espaces
            # spliter en tableau, op(espace)
            return contents.strip().replace("\n", " ").split()
        except OSError as e:
            self.write_log("System # Fichier n'existe pas\n")
        return []

    def write_log(self, res):
        print(res)
        if res:
            with open(self.out_path, "a") as file:
                file.write(res)
            return True
        else:
            return False

    def formated_data(self):
        # initialiser une matrice 9x9
        matrice = np.zeros((9, 9), dtype=int)
        if self.is_valide():
            self.write_log(f"Sudoku # Données d'entree Sudoku valide\n")
            for val in self.vals:
                x, y, z = map(int, tuple(val))
                # verfier s'il n'y a pas une valeur pour le meme indice
                if matrice[x, y] != 0:
                    self.write_log(
                        f"Sudoku # position ({x},{y}) = {matrice[x, y]} & {z}\t-> Index erroné, valeur double\n")
                    break
                matrice[x, y] = z
            return matrice
        self.write_log(f"Sudoku # Données d'entree Sudoku invalide")
        return np.zeros((9, 9), dtype=int)

    def is_correct(self):
        # regles du jeux
        # verifier s'il y a bien une matrice remplie
        if not self.matrice.any():
            return False

        # verifier les colonnes et les lignes
        # si toutes leurs valeurs sont uniques
        for i in range(9):
            # verification que les colonnes et les lignes contiennent
            # des valeurs uniques
            if not len(np.unique(self.matrice[:, i])) == len(np.unique(self.matrice[i, :])) == 9:
                error_str = f"Sudoku # La ligne index[{i}] contient des valeurs doubles {self.matrice[i, :]}\n" if len(
                    np.unique(self.matrice[i, :])) != 9 else ""
                error_str += f"Sudoku # La colonne index[{i}] contient des valeurs doubles {self.matrice[:, i]}\n" if len(
                    np.unique(self.matrice[:, i])) != 9 else ""
                self.write_log(error_str)
                return False

        # verifier les carres
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sous_matrice_carre = self.matrice[i:i + 3, j:j + 3]
                if np.size(sous_matrice_carre) != len(np.unique(sous_matrice_carre)):
                    res = afficher_matrice_nxn(sous_matrice_carre)
                    self.write_log("Sudoku # carre contient des valeurs doubles\n" + res)
                    return False

        # si aucune des exceptions est aver return true
        return True

    def afficher_matrice(self):
        res = " "
        if self.matrice.any():
            for i in range(np.shape(self.matrice)[0]):
                if i % 3 == 0 and i != 0:
                    # imprimer un separateur de ligne, sauf premiere ligne
                    res = res + "-" * 21 + "\n "
                for j in range(np.shape(self.matrice)[0]):
                    # imprimer un separateur de colonne, sauf premiere colonne
                    if j % 3 == 0 and j != 0:
                        res = res + "| "
                    res = res + str(self.matrice[i, j]) + " "
                res = res + "\n "

            self.write_log(f"\nSudoku # => {'Jeu Gagnant' if self.is_correct() else 'Jeu Perdant'} <=\n")

        self.transpose_matrice()
        self.write_log(res + "\n\n"+"#"*33+"\n\n ")

    def transpose_matrice(self):
        """
            Calcule de tansposé, matrice sudoku
        """
        if self.matrice.any():
            t = self.matrice.transpose()
            self.write_log(f"Matrice transposé : \n{t}\n\n")


# affichage de n'importe quel matrice, ex : 3x3
def afficher_matrice_nxn(matrice):
    res = " "
    if matrice.any():
        for i in range(np.shape(matrice)[0]):
            if i % 3 == 0 and i != 0:
                res = res + "-" * 21 + "\n "
            for j in range(np.shape(matrice)[0]):
                if j % 3 == 0 and j != 0:
                    res = res + "| "
                res = res + str(matrice[i, j]) + " "
            res = res + "\n "
    return res


# main programme principal
sudoku1 = Sudoku("test1.txt", "log.txt")

print()
sudoku2 = Sudoku("test2.txt", "log.txt")

print()
sudoku3 = Sudoku("test3.txt", "log.txt")

print()
sudoku4 = Sudoku("test4.txt", "log.txt")

print()
sudoku5 = Sudoku("test5.txt", "log.txt")

print()
sudoku_empty = Sudoku("empty.txt", "log.txt")
