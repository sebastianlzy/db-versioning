"""create_unicorn_and_location_tables

Revision ID: 30c197edd88f
Revises:
Create Date: 2021-10-01 13:53:43.781599

"""
from alembic import op
from sqlalchemy import Column, Integer, String, ForeignKey


# revision identifiers, used by Alembic.
revision = '30c197edd88f'
down_revision = None
branch_labels = None
depends_on = None


def setup_location_table():
    op.create_table(
        'Location',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('Name', String, unique=True),
    )

def setup_unicorn_table():
    op.create_table(
        'Unicorn',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('Unicorn', String, unique=True),
    )


def setup_unicorn_location_table():
    op.create_table(
       'UnicornLocation',
       Column('id', Integer, primary_key=True, autoincrement=True),
       Column('Location', String, ForeignKey('Location.Name', ondelete="CASCADE")),
       Column('Unicorn', String, ForeignKey('Unicorn.Unicorn', ondelete="CASCADE")),
    )


def upgrade():
    setup_location_table()
    setup_unicorn_table()
    setup_unicorn_location_table()

def downgrade():
    op.execute('''drop table "UnicornLocation" cascade;
                drop table "Location" cascade;
                drop table "Unicorn" cascade;''')