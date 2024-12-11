from Table import Table
from Player import Player


# Les classes Card, Player, Table et Deck sont déjà implémentées.

# Main function to execute the game
def main():
    print("Bienvenue au Texas Hold'em Poker!")

    # Initialisation des joueurs
    players = [
        Player(name=f"Joueur {i + 1}", chips=100) for i in range(3)  # Exemple avec 4 joueurs
    ]

    # Demander nom du joueur et l'ajouter à l'array

    # Initialisation de la table et du paquet de cartes
    table = Table()
    table.players = players
    table.deck.shuffle()

    # TODO le jeu
    # Afficher son jeu et la mise en cours (si pas premier tour pour la mise)
    # Placer 3 cartes en milieu puis commencez les paris
    # Le premier joueur peut soit parier soit au dodo
    # Les joueurs suivant peuvent soient s'aligner soit au dodo
    # Affichage de la première carte
    # Et de meme jusqua la fin
    # La boucle s'arrete lorsque il ne reste que un joueur en jeu ou si toutes les cartes sont révélés et que tt le monde a parié





    # Détermination du gagnant
    print("\n--- Résultats ---")
    winner = table.determine_winner()
    if winner:
        print(f"Le gagnant est {winner.name} avec {winner.chips} jetons!")
    else:
        print("Pas de gagnant, erreur dans la détermination du vainqueur.")


if __name__ == "__main__":
    main()
