from treys import Card
import random
from Table import Table
from Player import Player


# Les classes Card, Player, Table et Deck sont déjà implémentées.

# Main function to execute the game
def main():
    print("Bienvenue au Texas Hold'em Poker!")

    # Initialisation des joueurs
    players = [
        Player(name=f"Joueur {i + 1}", chips=100) for i in range(4)  # Exemple avec 4 joueurs
    ]

    # Initialisation de la table et du paquet de cartes
    table = Table()
    table.players = players
    table.deck.shuffle()

    # TODO le jeu

    # Détermination du gagnant
    print("\n--- Résultats ---")
    winner = table.determine_winner()
    if winner:
        print(f"Le gagnant est {winner.name} avec {winner.chips} jetons!")
    else:
        print("Pas de gagnant, erreur dans la détermination du vainqueur.")


if __name__ == "__main__":
    main()
