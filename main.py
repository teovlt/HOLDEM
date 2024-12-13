from Table import Table
from Player import Player


# Main function to execute the game
def initPlayers():
    players = [
        Player(name=f"Joueur {i + 1}", chips=100) for i in range(3)
    ]

    # Demander nom du joueur et l'ajouter à l'array
    name = input("Veuillez entrer votre nom: ")
    main_player = Player(name=name, chips=100)
    players.append(main_player)
    return players


def main():
    print("Bienvenue au Texas Hold'em Poker!")

    # Initialisation des joueurs
    players = initPlayers()

    # Initialisation de la table et du paquet de cartes
    table = Table()
    table.players = players
    table.deck.shuffle()

    # Distribuer les cartes à chaque jouer
    table.deal_to_players()

    # Plus grosse boucle qui attend que tout le monde n'ai plus de jetons

    # TODO boucle du jeu
    # Placer 3 cartes en milieu puis commencez les paris
    # Sélectionner un premier joueur au hasard
    # Le premier joueur peut soit parier soit au dodo
    # Les joueurs suivant peuvent soient s'aligner soit au dodo

    # TOUR DU JOUEUR(si pas premier) : proposez 2 choix, s'aligner, se coucher et
    # Afficher ses cartes en gros au dessus
    # Si aligner, joueur suivant, sinon attendre la fin du tour

    # A la fin du tour

    # Affichage des cartes, méthode en affichant 3 puis 1 puis 1
    # Et de meme jusqua la fin
    # La boucle s'arrete lorsque il ne reste que un joueur en jeu ou si toutes les cartes sont révélés et que tt le monde a parié
    # Dans ce cas la somme va a celui qui a la meilleure combinaison

    # Détermination du gagnant
    print("\n--- Résultats ---")
    winner = table.determine_winner()
    if winner:
        print(f"Le gagnant est {winner.name} avec {winner.chips} jetons!")
    else:
        print("Pas de gagnant, erreur dans la détermination du vainqueur.")


if __name__ == "__main__":
    main()
