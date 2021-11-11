"""Add Genre tables

Revision ID: ab99e753ee28
Revises: 4f48253b366b
Create Date: 2021-10-01 14:49:50.634308

"""
from alembic import op
from sqlalchemy import Column, Integer, String, ForeignKey

# revision identifiers, used by Alembic.
revision = 'ab99e753ee28'
down_revision = '4f48253b366b'
branch_labels = None
depends_on = None


def setup_genre_table():
    op.create_table(
        'Genre',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('Genre', String, unique=True),
    )


def setup_genre_cost_table():
    op.create_table(
        'GenreCost',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('GenreCost', Integer),
        Column('Genre', String, ForeignKey('Genre.Genre', ondelete="CASCADE")),
    )


def setup_genre_distance_table():
    op.create_table(
        'GenreDistance',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('GenreDistance', Integer),
        Column('Genre', String, ForeignKey('Genre.Genre', ondelete="CASCADE")),
    )


def setup_genre_insurance_table():
    op.create_table(
        'GenreInsurance',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('GenreInsurance', Integer),
        Column('Genre', String, ForeignKey('Genre.Genre', ondelete="CASCADE")),
    )


def upgrade():
    setup_genre_table()
    setup_genre_cost_table()
    setup_genre_distance_table()
    setup_genre_insurance_table()


def downgrade():
    op.execute('''
        drop table "Genre" cascade;
        drop table "GenreCost" cascade;
        drop table "GenreDistance" cascade;
        drop table "GenreInsurance" cascade;
    ''')
