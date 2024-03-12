import sys


class Sudoku:
    def __init__(self, file_path):
        self.data = self.load_data_inline(file_path)
        self.is_valid = self.isValid()
        self.grid = self.formated_data()
        self.is_correct = self.isCorrect()
        self.print_grid()
        # TODO renvoyer la valeur dans un fichier text

    def load_data_inline(self, file_path):
        # importer les données en une seule ligne
        with open(file_path, "r") as file:
            contents = file.read()

        return contents.replace("\n", " ").split()

    def isValid(self):
        # Verifier le nombre de valeurs dans un tableau. 9*9 = 81 values
        if len(self.data) != 81:
            print("Entrée non-valide : Nombre de valeur n'est pas correcte.")
            return False

        is_valide = True
        for triple in self.data:
            if len(triple) == 3:
                x, y, z = map(int, tuple(triple))
                # validation de données [0-8][0-8][1-9]
                if not (0 <= x <= 8 and 0 <= y <= 8 and 1 <= z <= 9):
                    print(f"Entrée erronées #\t [{triple}]")
                    is_valide = False
            else:
                print(f"Format incorrect #\t [{triple}]")
                is_valide = False

        return is_valide

    def formated_data(self):
        # retourner les donnees dans une grille (matrice 9*9)
        if self.is_valid:
            grid = [[0] * 9 for _ in range(9)]

            for triple in self.data:
                x, y, z = map(int, tuple(triple))
                grid[x][y] = z

            return grid
        else:
            return None

    def square_3x3_list(self, i, j):
        # prendre un carré de ses coordonnes superieres gauche
        # retourner une liste
        row = []
        for sub_i in range(i, i + 3):
            for sub_j in range(j, j + 3):
                row.append(self.grid[sub_i][sub_j])
        return row

    def isCorrect(self):
        # verification ligne et colonne
        if not self.grid:
            return False

        for i in range(9):
            # ligne
            line = self.grid[i]
            if len(set(line)) != len(line):
                print(f"Sudoku - Faux : erreur ligne numero {i}.\n")
                return False

            # colonne
            col = [self.grid[j][i] for j in range(9)]
            if len(set(col)) != len(col):
                print(f"Sudoku - Faux : erreur colonne numero {i}.\n")
                return False

        # verification par carré
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # square = [self.grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                carre = self.square_3x3_list(i, j)
                if len(carre) != len(set(carre)):
                    print(f"Sudoku - Faux : erreur carre ({i},{j}).\n")
                    return False

        print("Sudoku - Juste.\n")
        return True

    def print_grid(self):
        x = "valides" if self.is_valid else "invalides"
        y = "correcte" if self.is_correct else "incorrecte"
        print(f"Données d'entrée sont {x} et le jeu est {y}.\n")

        if not self.is_valid:
            return None

        matrice = ""
        for i in range(9):
            row = ""
            for j in range(9):
                row += " " + str(self.grid[i][j])
                if not (j + 1) % 3 and j + 1 != 9:
                    row += " |"
            matrice += row + "\n"
            if not (i + 1) % 3 and i + 1 != 9:
                matrice += "-------+-------+-------\n"
        print(matrice)
        return matrice


if __name__ == '__main__':

    filepath = ""  # sys.argv[1]
    print(filepath)

    # s1 = Sudoku(filepath)
    s1 = Sudoku("./data/partie.txt")
    s2 = Sudoku("./data/partie2.txt")
    s3 = Sudoku("./data/partie3.txt")

