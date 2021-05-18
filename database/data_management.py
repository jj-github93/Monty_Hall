from sqlalchemy import Float, String, Integer, Column, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

database = "sqlite:///users.db"


class User(Base):
    __tablename__ = "Users"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    username = Column("Username", String, unique=True)
    games = Column("Games", Integer, default=0)
    wins = Column("Wins", Integer, default=0)
    losses = Column("Losses", Integer, default=0)
    win_loss = Column("Win/Loss", Float, default=0.0)

    @staticmethod
    def session_maker(db):
        """
            Function to create a new session.
        """

        engine = create_engine(db)

        Base.metadata.create_all(bind=engine)

        Session = sessionmaker(bind=engine)

        session = Session()

        return session

    @staticmethod
    def add_user(db):
        """
            Function that gets a unique username from the user.
            Adds the new user to the db.
        """
        session = User.session_maker(db)

        new_user = User()
        while True:
            try:
                new_username = input("Enter a unique username: \n").upper()
                new_user.username = new_username
                session.add(new_user)
                session.commit()
            except IntegrityError:
                print("Username entered is already taken \n")
                session.rollback()
                session.close()
            else:
                session.close()

        return new_username

    @staticmethod
    def update_user(user_name, games, wins, losses, win_loss, db):
        """
            Function that searches for a user in the table by their username.
            Once found it updates their statistics with the parse in values.
        """

        # Creates a new session
        session = User.session_maker(db)

        # Searches table by unique username
        user = session.query(User).filter(User.username == user_name).with_for_update().one()

        # Updates the selected users details
        user.wins = wins
        user.games = games
        user.losses = losses
        user.win_loss = win_loss

        # commits session
        session.commit()
        session.close()

    @staticmethod
    def init_db(db):
        session = User.session_maker(db)
        session.commit()
        session.close()
