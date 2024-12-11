from treys import Evaluator, Card
import random
import Player
import Table

# Les classes Card, Player, Table et Deck sont déjà implémentées.

# Main function to execute the game
def main():
    print("Bienvenue au Texas Hold'em Poker!")

    # Initialisation des joueurs
    players = [
        Player(name=f"Joueur {i+1}", chips=100) for i in range(4)  # Exemple avec 4 joueurs
    ]

    # Initialisation de la table et du paquet de cartes
    table = Table()
    table.players = players
    table.deck.shuffle()

    # Distribution des cartes aux joueurs
    table.deal_to_players()

    # Phase pré-flop
    print("\n--- Pré-flop ---")
    table.collect_bets()
    afficher_etat_joueurs(players)

    # Flop : 3 cartes communes
    flop = table.deck.draw(3)
    table.add_community_cards(flop)
    print("Cartes du flop :", afficher_cartes(table.community_cards))
    table.collect_bets()
    afficher_etat_joueurs(players)

    # Turn : 1 carte commune
    turn = table.deck.draw(1)
    table.add_community_cards(turn)
    print("Carte du turn :", afficher_cartes(table.community_cards))
    table.collect_bets()
    afficher_etat_joueurs(players)

    # River : 1 carte commune
    river = table.deck.draw(1)
    table.add_community_cards(river)
    print("Carte de la river :", afficher_cartes(table.community_cards))
    table.collect_bets()
    afficher_etat_joueurs(players)

    # Détermination du gagnant
    print("\n--- Résultats ---")
    gagnant = table.determine_winner()
    if gagnant:
        print(f"Le gagnant est {gagnant.name} avec {gagnant.chips} jetons!")
    else:
        print("Pas de gagnant, erreur dans la détermination du vainqueur.")

# Fonction pour afficher l'état des joueurs
def afficher_etat_joueurs(players):
    for player in players:
        if player.is_active:
            print(f"{player.name} - Jetons: {player.chips}, Main: {afficher_cartes(player.hand)}")
        else:
            print(f"{player.name} est couché.")

# Fonction pour afficher une liste de cartes
def afficher_cartes(cards):
    return ", ".join(str(card) for card in cards)

if __name__ == "__main__":
    main()
