from sqlite3 import connect

from .state import State
from ..conditions import at_state


class StateMachine:

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS user_states(user_id INTEGER PRIMARY KEY, user_state TEXT)"""
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()

    def __init__(self, database=":memory:", state_group=None):
        self.connection = connect(database)
        self.state_group = state_group
        self.create_table()

    def insert_user_state(self, user_id, state):
        sql = """INSERT INTO user_states VALUES (?, ?)"""
        cursor = self.connection.cursor()
        cursor.execute(sql, (int(user_id), state))
        self.connection.commit()

    def update_user_state(self, user_id, state):
        sql = """UPDATE user_states SET user_state = ? WHERE user_id = ?"""
        cursor = self.connection.cursor()
        cursor.execute(sql, (state, int(user_id)))
        self.connection.commit()

    def __setitem__(self, user_id, state):
        if isinstance(state, State):
            state = str(state)
        if self[user_id] is None:
            self.insert_user_state(user_id, state)
        else:
            self.update_user_state(user_id, state)

    def select_user_state(self, user_id):
        sql = """SELECT user_state FROM user_states WHERE user_id = ?"""
        cursor = self.connection.cursor()
        cursor.execute(sql, (int(user_id),))
        return cursor.fetchone()

    def __getitem__(self, user_id):
        result = self.select_user_state(user_id)
        if result is None:
            return result
        elif self.state_group is not None and result[0] in self.state_group.get_state_dict():
            return getattr(self.state_group, result[0])
        else:
            return result[0]

    def delete_user_state(self, user_id):
        sql = """DELETE from user_states where user_id = ?"""
        cursor = self.connection.cursor()
        cursor.execute(sql, (int(user_id),))
        self.connection.commit()

    def __delitem__(self, user_id):
        if self[user_id] is None:
            raise KeyError("User does not exist")
        self.delete_user_state(user_id)

    def at(self, state):
        return at_state(state, self)
