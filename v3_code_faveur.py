import csv

def lire_donnees_csv(fichier_csv, chambre_id):

    temperatures = []
    with open(fichier_csv) as csv_file:
        contenu_csv = csv.reader(csv_file, delimiter=';')
        for ligne in contenu_csv:
            if ligne[2] == chambre_id:
                temperature = float(ligne[3].replace(',', '.'))
                temperatures.append(temperature)
    return temperatures

def calculer_statistiques(temperatures):

    if not temperatures:
        return 0, 0, 0
    moyenne = sum(temperatures) / len(temperatures)
    minimum = min(temperatures)
    maximum = max(temperatures)
    return moyenne, minimum, maximum

def afficher_resultats(nb_chambres, fichier_csv):

    print("Affichage des mesures de température d'une chambre froide")
    print('-' * 57)
    print("                       Moy  Min  Max")

    for i in range(nb_chambres):
        chambre_id = f'chambrefroide0{i + 1}'
        print(chambre_id, end=' ')

        temperatures = lire_donnees_csv(fichier_csv, chambre_id)
        moyenne, minimum, maximum = calculer_statistiques(temperatures)

        print(f"{round(moyenne, 1):>10} {minimum:>4} {maximum:>4}")
    
# Exécution du programme
if __name__ == "__main__":
    afficher_resultats(nb_chambres=3, fichier_csv='traiteur.csv')
