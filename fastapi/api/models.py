from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import relationship
from .database import Base

community_association=Table(
    'workout_routine',Base.metadata,
    Column('community_id',Integer,ForeignKey('communitys.id')),
    Column('routine_id',Integer,ForeignKey('routines.id')),
    )

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String ,unique=True,index=True)
    hashed_password=Column(String)

class Workout(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    name=Column(String, index=True)
    description=Column(String,index=True)
    routines=relationship('Routine',secondary=community_association,back_populates='workouts')

class Routine(Base):
    __tablename__='routines'
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    name=Column(String,index=True)
    description=Column(String,index=True)
    workouts=relationship('Workout',secondary=community_association,back_populates='routines')
Workout.routines=relationship('Routine',secondary=community_association,back_populates='workouts')
     


