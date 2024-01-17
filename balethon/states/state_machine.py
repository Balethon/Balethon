from sqlite3 import connect
from threading import local
from typing import Union

from .state import State
from ..conditions import at_state


class StateMachine:
    global_state_machine = None

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS user_states(user_id INTEGER PRIMARY KEY, user_state TEXT)"""
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

    def __init__(self, database: str = ":memory:", state_group=None):
        self.database = database
        self.local = local()
        self.state_group = state_group
        self.create_table()

    @property
    def connection(self):
        if not hasattr(self.local, "connection"):
            self.connection = connect(self.database)
        return self.local.connection

    @connection.setter
    def connection(self, connection):
        self.local.connection = connection

    def insert_user_state(self, user_id: Union[int, str], state: Union[State, str]):
        sql = """INSERT INTO user_states VALUES (?, ?)"""
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, (int(user_id), state))
        connection.commit()

    def update_user_state(self, user_id: Union[int, str], state: Union[State, str]):
        sql = """UPDATE user_states SET user_state = ? WHERE user_id = ?"""
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, (state, int(user_id)))
        connection.commit()

    def __setitem__(self, user_id: Union[int, str], state: Union[State, str]):
        if isinstance(state, State):
            state = str(state)
        if self[user_id] is None:
            self.insert_user_state(user_id, state)
        else:
            self.update_user_state(user_id, state)

    def select_user_state(self, user_id: Union[int, str]):
        sql = """SELECT user_state FROM user_states WHERE user_id = ?"""
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, (int(user_id),))
        return cursor.fetchone()

    def __getitem__(self, user_id: Union[int, str]):
        result = self.select_user_state(user_id)
        if result is None:
            return result
        elif self.state_group is not None and result[0] in self.state_group.get_state_dict():
            return getattr(self.state_group, result[0])
        else:
            return result[0]

    def delete_user_state(self, user_id: Union[int, str]):
        sql = """DELETE from user_states where user_id = ?"""
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, (int(user_id),))
        connection.commit()

    def __delitem__(self, user_id: Union[int, str]):
        if self[user_id] is None:
            raise KeyError("User does not exist")
        self.delete_user_state(user_id)

    def at(self, state: Union[State, str]):
        return at_state(state, self)

    def change_database(self, database: str = ":memory:"):
        connection = self.connection
        now_connection = connect(database)
        connection.backup(now_connection)
        self.connection = now_connection

    def get_all(self):
        sql = """SELECT * FROM user_states"""
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql)
        return dict(cursor.fetchall())


StateMachine.global_state_machine = StateMachine()
