from table import Table
from player import Player
import pandas as pd


# Main function to execute the game
def init_players():

    # Demander le nombre de joueurs
    while True:
        try:
            num_players = int(input("Combien de joueurs participeront à la partie ? "))
            if num_players <= 0:
                raise ValueError("Le nombre de joueurs doit être supérieur à 0.")
            break
        except ValueError as e:
            print(e)

    players = []

    # Recueillir les noms des joueurs
    for i in range(num_players):
        while True:
            player_name = input(f"Veuillez entrer le nom du Joueur {i + 1}: ").strip()
            if player_name:
                players.append(Player(name=player_name, chips=100))
                break
            else:
                print("Le nom du joueur ne peut pas être vide.")

    # Afficher un tableau des joueurs
    players_data = [{"Nom": player.name, "Jetons": player.chips} for player in players]
    df = pd.DataFrame(players_data)
    print("\n--- Tableau des joueurs ---")
    print(df.to_string(index=False))

    return players


def main():
    print("Bienvenue au Texas Hold'em Poker!")

    # Initialisation des joueurs
    players = init_players()

    # Initialisation de la table et du paquet de cartes
    table = Table()
    table.players = players

    # Boucle principale du jeu
    while not table.is_game_over():
        table.deck.shuffle()
        table.deal_to_players()
        table.community_cards = []
        table.reset_pot()

        # Ajouter les cartes communautaires progressivement
        while len(table.community_cards) < 5:
            if len(table.community_cards) == 0:
                # Flop: les 3 premières cartes
                table.community_cards.extend(table.deck.draw(3))
            else:
                # Turn et River: ajouter une carte à la fois
                table.community_cards.extend(table.deck.draw(1))

            # Effectuer les paris
            table.run_betting_round()

            # Déterminer le gagnant de la manche
            winners = table.has_best_hand()
            total_pot = table.pot  # La somme totale à distribuer
            if len(winners) == 1:
                # Cas d'un gagnant unique
                winner = winners[0]
                winner.chips += total_pot
                print(f"Le gagnant de la manche est {winner.name}, il remporte {total_pot} jetons!")
            else:
                # Cas de plusieurs gagnants (égalité)
                split_pot = total_pot // len(winners)  # Répartition équitable
                for winner in winners:
                    winner.chips += split_pot
                    print(f"{winner.name} partage la victoire et reçoit {split_pot} jetons.")
                remainder = total_pot % len(winners)
                if remainder > 0:
                    print(
                        f"Le reste de {remainder} jetons est conservé par la table.")

        # Éliminer les joueurs sans jetons
        table.remove_bankrupt_players()

    # Fin du jeu
    print("\n--- Résultats ---")
    winner = table.players[0]
    print(f"Le gagnant de la partie est {winner.name} avec {winner.chips} jetons!")


if __name__ == "__main__":
    main()
