from sqlalchemy import Float, String, Integer, Column, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    username = Column("Username", String, unique=True)
    games = Column("Games", Integer, default=0)
    wins = Column("Wins", Integer, default=0)
    losses = Column("Losses", Integer, default=0)
    win_loss = Column("Win/Loss", Float, default=0.0)


engine = create_engine("sqlite:///users.db", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()


def add_user():
    new_user = User()

    try:
        new_user.username = input("Enter a unique username: \n")
        session.add(new_user)
        session.commit()
    except IntegrityError:
        print("Username entered is already taken \n")
        session.rollback()

    finally:
        session.close()


add_user()

session.close()
