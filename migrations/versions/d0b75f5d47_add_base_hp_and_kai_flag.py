"""Add base_hp and kai flag

Revision ID: d0b75f5d47
Revises: 2f8220972dc
Create Date: 2015-05-07 21:43:01.703895

"""

# revision identifiers, used by Alembic.
revision = 'd0b75f5d47'
down_revision = '2f8220972dc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ship', sa.Column('hp_base', sa.Integer(), nullable=True))
    op.add_column('ship', sa.Column('kai', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ship', 'kai')
    op.drop_column('ship', 'hp_base')
    ### end Alembic commands ###