"""Insert data into blessing and distance tables

Revision ID: 28fcce130abd
Revises: 01fb63a7faec
Create Date: 2021-10-01 15:18:53.772779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28fcce130abd'
down_revision = '01fb63a7faec'
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

def blessings_callback(datum):
    table_name = "\"Blessings\""
    column_name = "\"Title\",\"Genres\",\"Price\",\"Unicorn\""
    return "INSERT INTO {} ({}) VALUES ('{}','{}', {}, '{}')".format(table_name, column_name, datum[0], datum[1], datum[2], datum[3])

def distance_callback(datum):
    table_name = "\"Distance\""
    column_name = "\"Distance\",\"LocationStart\", \"LocationEnd\""
    return "INSERT INTO {} ({}) VALUES ({}, '{}', '{}')".format(table_name, column_name, datum[0], datum[1], datum[2])


def upgrade():
    insert_data(get_data("../data/Blessings.csv"), blessings_callback)
    insert_data(get_data("../data/Distance.csv"), distance_callback)


def downgrade():
    op.execute("DELETE FROM \"Blessings\"")
    op.execute("DELETE FROM \"Distance\"")
