Review code Sacha Knoplock.

- Le code est fonctionnel et parvient à extraire et à traiter les températures pour la 1re chambre froide, mais pas les autres.
- Cependant, il manque une gestion des erreurs, par exemple si le fichier CSV est introuvable ou buguer.
- Il n'y a pas de gestion de chambre froides supplémentaire.
- Les colonnes ne sont pas vérifiées, ce qui peut entraîner des erreurs si la structure du CSV est incorrecte.
- Les noms des variables pourraient être plus explicites pour améliorer la lisibilité.
- L'affichage est mélangé avec le calcul des valeurs.
- Le format de sortie est clair et lisible, ce qui est un bon point pour l'expérience utilisateur.
- Le code ne gère pas les fichiers CSV contenant des en-têtes, ce qui pourrait provoquer des erreurs si le fichier est modifié pour en inclure.
- Le code n'a aucune sécurité
- Il manque une gestion des exceptions pour les conversions de chaînes en flottants, ce qui pourrait causer des plantages si les données sont corrompues.