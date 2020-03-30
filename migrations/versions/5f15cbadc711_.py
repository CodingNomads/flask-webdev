"""Unique slugs

Revision ID: 5f15cbadc711
Revises: f4bed1492264
Create Date: 2020-03-18 22:56:27.864403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f15cbadc711'
down_revision = 'f4bed1492264'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'compositions', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'compositions', type_='unique')
    # ### end Alembic commands ###