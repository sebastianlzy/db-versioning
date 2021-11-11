"""insert data into Genre tables

Revision ID: 1c50a7eda8b9
Revises: ab99e753ee28
Create Date: 2021-10-01 14:54:58.146629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c50a7eda8b9'
down_revision = 'ab99e753ee28'
branch_labels = None
depends_on = None

def get_data(input_path):

    f = open(input_path, "r")
    data = f.read().splitlines()
    print(data)

    return [n.split(",") for n in data]

def insert_data(data, callback):
    for datum in data[1:]:
        sql = callback(datum)
        print(sql)
        op.execute(sql)

def genre_callback(datum):
    table_name = "\"Genre\""
    column_name = "\"Genre\""
    return "INSERT INTO {} ({}) VALUES ('{}')".format(table_name, column_name, datum[0])

def genre_cost_callback(datum):
    table_name = "\"GenreCost\""
    column_name = "\"GenreCost\",\"Genre\""
    return "INSERT INTO {} ({}) VALUES ({}, '{}')".format(table_name, column_name, datum[0], datum[1])

def genre_distance_callback(datum):
    table_name = "\"GenreDistance\""
    column_name = "\"GenreDistance\",\"Genre\""
    return "INSERT INTO {} ({}) VALUES ({}, '{}')".format(table_name, column_name, datum[0], datum[1])

def genre_insurance_callback(datum):
    table_name = "\"GenreInsurance\""
    column_name = "\"GenreInsurance\",\"Genre\""
    return "INSERT INTO {} ({}) VALUES ({}, '{}')".format(table_name, column_name, datum[0], datum[1])


def upgrade():

    insert_data(get_data("../data/Genre.csv"), genre_callback)
    insert_data(get_data("../data/GenreCost.csv"), genre_cost_callback)
    insert_data(get_data("../data/GenreDistance.csv"), genre_distance_callback)
    insert_data(get_data("../data/GenreInsurance.csv"), genre_insurance_callback)


def downgrade():
    op.execute("DELETE FROM \"Genre\"")
    op.execute("DELETE FROM \"GenreCost\"")
    op.execute("DELETE FROM \"GenreDistance\"")
    op.execute("DELETE FROM \"GenreInsurance\"")
