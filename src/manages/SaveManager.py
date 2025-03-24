import sqlite3
from typing import Dict

from src.Entities.ImposingWarriorAlly import ImposingWarriorAlly
from src.Entities.Player import Player
from src.Entities.RapierWarriorAlly import RapierWarriorAlly


class SaveManager:
    def __init__(self, db_name="save_data.db"):
        """ Inicializa o gerenciador de saves e cria a tabela se não existir. """
        self.db_name = db_name
        self._initialize_database()

    def save(self, player: Player, last_level: int):
        """ Salva os dados do jogador no banco. """
        player_query = """
        INSERT INTO player (id, gold, level, skill_level, last_level_completed)
        VALUES (1, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            gold = excluded.gold,
            level = excluded.level,
            skill_level = excluded.skill_level,
            last_level_completed = excluded.last_level_completed;
        """
        self._execute_query(player_query, (player.gold, player.level, player.skill_level, last_level))

        for ally in player.allies:
            ally_query = """
                    INSERT INTO ally (player_id, identity, level)
                    VALUES (1, ?, ?)
                    ON CONFLICT(player_id, identity) DO UPDATE SET
                        level = excluded.level;
                    """
            self._execute_query(ally_query, (ally.identity, ally.level))


    def load(self) -> Dict[str, Player | int]:
        """ Carrega os dados do jogador do banco. Retorna (gold, level, skill_level, last_level_completed). """
        player_query = "SELECT gold, level, skill_level, last_level_completed FROM player WHERE id = 1;"
        player_return = self._execute_query(player_query)
        player_data = player_return[0] if len(player_return) == 1 else None

        allies_query = "SELECT identity, level FROM ally WHERE player_id = 1;"
        allies_return = self._execute_query(allies_query)
        allies_data = allies_return if len(allies_return) == 1 else []

        allies = []

        for ally_data in allies_data:
            if ally_data[0] == ImposingWarriorAlly().identity:
                allies.append(ImposingWarriorAlly(ally_data[1]))
                continue
            if ally_data[0] == RapierWarriorAlly().identity:
                allies.append(RapierWarriorAlly(ally_data[1]))
                continue


        if player_data:
            player = Player(player_data[0], player_data[1], player_data[2], allies)
        else:
            player = Player()


        return {'player': player, 'last_level': player_data[3] if player_data else 1}

    def _initialize_database(self):
        """ Cria a tabela se ainda não existir. """
        queries = [
            """
            CREATE TABLE IF NOT EXISTS player (
                id INTEGER PRIMARY KEY,
                gold INTEGER DEFAULT 0,
                level INTEGER DEFAULT 1,
                skill_level INTEGER DEFAULT 0,
                last_level_completed INTEGER DEFAULT 0
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS ally (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id INTEGER NOT NULL,
                identity TEXT NOT NULL,
                level INTEGER DEFAULT 1,
                FOREIGN KEY (player_id) REFERENCES player(id) ON DELETE CASCADE,
                UNIQUE(player_id, identity)
            );
            """
        ]

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            for query in queries:
                cursor.execute(query)
            conn.commit()

    def _execute_query(self, query, params=()):
        """ Executa uma query no banco e gerencia a conexão automaticamente. """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()