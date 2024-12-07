import heapq

def dijkstra(graphe, debut, fin, debug=False):
    if debut not in graphe or fin not in graphe:
        raise ValueError("Les sommets de départ ou d'arrivée ne sont pas dans le graphe.")

    # Initialiser les distances à l'infini pour tous les sommets
    distances = {sommet: float('inf') for sommet in graphe}
    distances[debut] = 0

    # Initialiser les prédécesseurs à None pour tous les sommets
    precedents = {sommet: None for sommet in graphe}

    # Créer une file de priorité avec le sommet de départ
    file_priorite = [(0, debut)]

    while file_priorite:
        # Affiche la file de priorité avant extraction
        if debug:
            print("File de priorité avant extraction :", file_priorite)

        distance_actuelle, sommet_actuel = heapq.heappop(file_priorite)

        if debug:
            print(f"Traitement du sommet: {sommet_actuel}, distance: {distance_actuelle}")

        if distance_actuelle > distances[sommet_actuel]:
            continue

        for voisin, poids in graphe[sommet_actuel].items():
            nouvelle_distance = distance_actuelle + poids

            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                precedents[voisin] = sommet_actuel

                # Ajouter le voisin dans la file de priorité
                heapq.heappush(file_priorite, (nouvelle_distance, voisin))

                # Affiche la file après ajout
                if debug:
                    print(f"Ajout du sommet : ({nouvelle_distance}, {voisin})")
                    print("File de priorité après ajout :", file_priorite)

    if distances[fin] == float('inf'):
        return None, float('inf')

    # Reconstruction du chemin le plus court
    chemin = []
    sommet_actuel = fin
    while sommet_actuel:
        chemin.insert(0, sommet_actuel)
        sommet_actuel = precedents[sommet_actuel]

    return chemin, distances[fin]

# Exemple d'utilisation
graphe = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'D': 2, 'F': 3},
    'C': {'A': 2, 'D': 3, 'E': 4},
    'D': {'B': 2, 'C': 3, 'F': 3, 'G': 3, 'E': 2},
    'E': {'C': 4, 'D': 2, 'G': 5},
    'F': {'B': 3, 'D': 3, 'G': 4},
    'G': {'F': 4, 'D': 3, 'E': 5}
}

sommet_depart = 'A'
sommet_fin = 'G'

plus_court_chemin, distance = dijkstra(graphe, sommet_depart, sommet_fin, debug=True)

if plus_court_chemin:
    print("Plus court chemin:", plus_court_chemin)
    print("Distance:", distance)
else:
    print("Aucun chemin trouvé entre", sommet_depart, "et", sommet_fin)
