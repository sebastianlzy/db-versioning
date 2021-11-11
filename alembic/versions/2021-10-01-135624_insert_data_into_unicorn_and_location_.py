"""insert_data_into_unicorn_and_location_tables

Revision ID: 4f48253b366b
Revises: 30c197edd88f
Create Date: 2021-10-01 13:56:24.109064

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '4f48253b366b'
down_revision = '30c197edd88f'
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

def location_callback(datum):
    table_name = "\"Location\""
    column_name = "\"Name\""
    return "INSERT INTO {} ({}) VALUES ('{}')".format(table_name, column_name, datum[0])

def unicorn_callback(datum):
    table_name = "\"Unicorn\""
    column_name = "\"Unicorn\""
    return "INSERT INTO {} ({}) VALUES ('{}')".format(table_name, column_name, datum[0])


def upgrade():
    insert_data(get_data("../data/Location.csv"), location_callback)
    insert_data(get_data("../data/Unicorn.csv"), unicorn_callback)


def downgrade():
    op.execute("DELETE FROM \"Location\"")
    op.execute("DELETE FROM \"Unicorn\"")
