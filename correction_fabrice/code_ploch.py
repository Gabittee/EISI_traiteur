import csv
import argparse

def afficher_tableau_de_bord():
    print("Tableau de bord")
    print('-' * 57)
    print("Chambres       Moy Min Max")

def lire_fichier_csv(fichier_csv):
    chambres = {}
    # Ouverture du fichier de données
    with open(fichier_csv) as fichier:
        lecteur_csv = csv.reader(fichier, delimiter=';')
        next(lecteur_csv)
        # Parcours des données du fichier
        for champ in lecteur_csv:
            try:
                chambre = champ[2]
                temperature = float(champ[3].replace(',', '.'))
                if chambre not in chambres:
                    chambres[chambre] = []
                chambres[chambre].append(temperature)
            except (ValueError, IndexError):
                print(f"Champ skippé: {champ}")
    return chambres

def afficher_statistiques(fichier_csv):
    chambres = lire_fichier_csv(fichier_csv)
    # Calcul moyenne, minimum et maximum température de chaque chambres
    for chambre, temperatures in chambres.items():
        if temperatures:
            moyenne = sum(temperatures) / len(temperatures)
            mini = min(temperatures)
            maxi = max(temperatures)
            print(f"{chambre} {round(moyenne, 1)} {mini} {maxi}")
        else:
            print(f"{chambre} Pas de valeur trouvée")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyse des températures des chambres à partir d\'un fichier CSV.')
    parser.add_argument('fichier_csv', type=str, help='Chemin vers le fichier CSV à analyser')
    args = parser.parse_args()

    afficher_tableau_de_bord()
    afficher_statistiques(args.fichier_csv)