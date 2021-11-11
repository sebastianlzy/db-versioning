"""Create blessings and distance tables

Revision ID: 01fb63a7faec
Revises: 1c50a7eda8b9
Create Date: 2021-10-01 15:14:18.188278

"""
from alembic import op
from sqlalchemy import Column, Integer, String, ForeignKey


# revision identifiers, used by Alembic.
revision = '01fb63a7faec'
down_revision = '1c50a7eda8b9'
branch_labels = None
depends_on = None



def setup_blessing_table():
    op.create_table(
        'Blessings',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('Title', String, unique=True),
        Column('Genres', String, ForeignKey('Genre.Genre', ondelete="CASCADE")),
        Column('Price', Integer),
        Column('Unicorn', String, ForeignKey('Unicorn.Unicorn', ondelete="CASCADE")),
    )


def setup_distance_table():
    op.create_table(
        'Distance',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('Distance', Integer),
        Column('LocationStart', String, ForeignKey('Location.Name', ondelete="CASCADE")),
        Column('LocationEnd', String, ForeignKey('Location.Name', ondelete="CASCADE")),
    )



def upgrade():
   setup_distance_table()
   setup_blessing_table()


def downgrade():
    op.execute('''
        drop table "Distance" cascade;
        drop table "Blessings" cascade;
    ''')