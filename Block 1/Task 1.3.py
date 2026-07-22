from enum import Enum


class Position(Enum):
    FORWARD = "FORWARD"
    MIDFIELDER = "MIDFIELDER"
    DEFENDER = "DEFENDER"
    GOALKEEPER = "GOALKEEPER"


class EventType(Enum):
    GOAL = "GOAL"
    SUBSTITUTION = "SUBSTITUTION"
    HALF_TIME = "HALF_TIME"
    FULL_TIME = "FULL_TIME"


class MatchPhase(Enum):
    REGULATION = "REGULATION"
    FINISHED = "FINISHED"


class Player:
    def __init__(self, name, position, base_attack, base_defense, stamina=100):
        self.name = name
        self.position = position  # Enum
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.stamina = stamina

    def deplete_stamina(self, rate):
        self.stamina = max(self.stamina - rate, 10)

    def get_effective_attack(self):
        return self.base_attack * (self.stamina / 100.0)

    def get_effective_defense(self):
        return self.base_defense * (self.stamina / 100.0)


class Team:
    def __init__(self, country_name, roster, active_lineup):
        self.country_name = country_name
        self.roster = roster
        self.active_lineup = active_lineup
        self.bench = [player for player in roster if player not in active_lineup]
        self.substitutions_remaining = 5

    def get_aggregate_attack(self):
        attackers = [
            p for p in self.active_lineup if p.position in [Position.FORWARD, Position.MIDFIELDER]
        ]
        if not attackers:
            return 0.0
        total_attack = sum(p.get_effective_attack() for p in attackers)
        return total_attack / len(attackers)

    def get_aggregate_defense(self):
        defenders = [
            p for p in self.active_lineup if p.position in [Position.DEFENDER, Position.GOALKEEPER]
        ]
        if not defenders:
            return 0.0
        total_defense = sum(p.get_effective_defense() for p in defenders)
        return total_defense / len(defenders)

    def execute_substitution(self, player_out, player_in):
        if (
            self.substitutions_remaining > 0
            and player_out in self.active_lineup
            and player_in in self.bench
        ):

            self.active_lineup.remove(player_out)
            self.bench.append(player_out)

            self.bench.remove(player_in)
            self.active_lineup.append(player_in)

            self.substitutions_remaining -= 1
            return True
        return False


class MatchEvent:
    _id_counter = 1

    def __init__(self, event_type, minute, team=None, player=None, outcome_text=""):
        self._event_id = MatchEvent._id_counter
        MatchEvent._id_counter += 1
        self._event_type = event_type  # Enum
        self._minute = minute
        self._team = team
        self._player = player
        self._outcome_text = outcome_text

    @property
    def event_id(self):
        return self._event_id

    @property
    def event_type(self):
        return self._event_type

    @property
    def minute(self):
        return self._minute

    @property
    def team(self):
        return self._team

    @property
    def player(self):
        return self._player

    @property
    def outcome_text(self):
        return self._outcome_text

    def to_string(self):
        team_str = self.team.country_name if self.team else "N/A"
        player_str = self.player.name if self.player else "N/A"
        return f"[{self.minute}'] {self.event_type.value} | Team: {team_str} | Player: {player_str} -> {self.outcome_text}"


class Match:
    def __init__(self, home_team, away_team, seed=42):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = 0
        self.away_score = 0
        self.current_minute = 0
        self.timeline = []
        self.phase = MatchPhase.REGULATION

        self._seed = seed

    def _custom_random(self):
        self._seed = (self._seed * 1103515245 + 12345) & 0x7FFFFFFF
        return self._seed / 2147483647.0

    def run_minute_tick(self):
        if self.phase == MatchPhase.FINISHED:
            return

        self.current_minute += 1
        all_active = self.home_team.active_lineup + self.away_team.active_lineup
        for player in all_active:
            player.deplete_stamina(0.5)

        self.process_goal_attempt(self.home_team, self.away_team)
        self.process_goal_attempt(self.away_team, self.home_team)

        if self.current_minute == 45:
            self.timeline.append(
                MatchEvent(
                    event_type=EventType.HALF_TIME,
                    minute=45,
                    outcome_text=f"Half Time! Score: {self.home_team.country_name} {self.home_score} - {self.away_score} {self.away_team.country_name}",
                )
            )

        if self.current_minute >= 90:
            self.phase = MatchPhase.FINISHED
            self.timeline.append(
                MatchEvent(
                    event_type=EventType.FULL_TIME,
                    minute=90,
                    outcome_text=f"Full Time! Final Score: {self.home_team.country_name} {self.home_score} - {self.away_score} {self.away_team.country_name}",
                )
            )

    def process_goal_attempt(self, attacking_team, defending_team):
        if self._custom_random() <= 0.05:
            attack = attacking_team.get_aggregate_attack()
            defense = defending_team.get_aggregate_defense()

            # Dynamic Margin Threshold: Attack > (Defense * 1.3)
            if attack > defense :
                if attacking_team == self.home_team:
                    self.home_score += 1
                else:
                    self.away_score += 1

                forwards = [
                    p
                    for p in attacking_team.active_lineup
                    if p.position == Position.FORWARD
                ]
                if forwards:
                    idx = int(self._custom_random() * len(forwards))
                    scorer = forwards[idx]
                else:
                    scorer = attacking_team.active_lineup[0]

                event = MatchEvent(
                    event_type=EventType.GOAL,
                    minute=self.current_minute,
                    team=attacking_team,
                    player=scorer,
                    outcome_text=f"GOAL! {scorer.name} scored a fantastic goal!",
                )
                self.timeline.append(event)

    def run_full_simulation(self):
        while self.phase != MatchPhase.FINISHED:
            self.run_minute_tick()


if __name__ == "__main__":
    egypt_lineup = [
        Player("El Shenawy", Position.GOALKEEPER, 40, 70),
        Player("Hegazi", Position.DEFENDER, 30, 70),
        Player("Abdelmonem", Position.DEFENDER, 30, 72),
        Player("Hany", Position.DEFENDER, 30, 68),
        Player("Hamdy", Position.DEFENDER, 30, 68),
        Player("Elneny", Position.MIDFIELDER, 85, 50),
        Player("Attia", Position.MIDFIELDER, 80, 50),
        Player("Zizo", Position.MIDFIELDER, 90, 40),
        Player("Mo Salah", Position.FORWARD, 99, 30),
        Player("Marmoush", Position.FORWARD, 95, 30),
        Player("Mostafa Mohamed", Position.FORWARD, 92, 30),
    ]

    egypt_bench = [Player("Trezeguet", Position.FORWARD, 88, 30)]
    egypt_roster = egypt_lineup + egypt_bench

    senegal_lineup = [
        Player("Mendy", Position.GOALKEEPER, 40, 72),
        Player("Koulibaly", Position.DEFENDER, 30, 72),
        Player("Diallo", Position.DEFENDER, 30, 68),
        Player("Sabaly", Position.DEFENDER, 30, 68),
        Player("Jakobs", Position.DEFENDER, 30, 65),
        Player("Gana Gueye", Position.MIDFIELDER, 82, 50),
        Player("Ciss", Position.MIDFIELDER, 80, 50),
        Player("N. Mendy", Position.MIDFIELDER, 80, 50),
        Player("Sadio Mane", Position.FORWARD, 98, 30),
        Player("Sarr", Position.FORWARD, 92, 30),
        Player("Jackson", Position.FORWARD, 90, 30),
    ]

    senegal_bench = [Player("Dia", Position.FORWARD, 85, 30)]
    senegal_roster = senegal_lineup + senegal_bench

    team_egypt = Team("Egypt", egypt_roster, egypt_lineup)
    team_senegal = Team("Senegal", senegal_roster, senegal_lineup)

    match = Match(team_egypt, team_senegal, seed=77)
    match.run_full_simulation()

    print("=== RECORDED TIMELINE ===")
    for event in match.timeline:
        print(event.to_string())
