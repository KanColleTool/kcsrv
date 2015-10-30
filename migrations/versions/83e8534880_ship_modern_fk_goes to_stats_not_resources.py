"""ship modern fk goes to stats not resources

Revision ID: 83e8534880
Revises: 2e6ec313e04
Create Date: 2015-10-24 22:02:05.517352

"""

# revision identifiers, used by Alembic.
revision = '83e8534880'
down_revision = '2e6ec313e04'

from alembic import op
import sqlalchemy as sa


def upgrade():
### commands auto generated by Alembic - please adjust! ###
    op.add_column('ship', sa.Column('modern_stats_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_ship_modern_stats_id'), 'ship', ['modern_stats_id'], unique=False)
    op.drop_index('ix_ship_modern_resources_id', table_name='ship')
    op.drop_constraint('ship_modern_resources_id_fkey', 'ship', type_='foreignkey')
    op.create_foreign_key(None, 'ship', 'stats', ['modern_stats_id'], ['id'])
    op.drop_column('ship', 'modern_resources_id')
    ### end Alembic commands ###


def downgrade():
### commands auto generated by Alembic - please adjust! ###
    op.add_column('ship', sa.Column('modern_resources_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'ship', type_='foreignkey')
    op.create_foreign_key('ship_modern_resources_id_fkey', 'ship', 'resources', ['modern_resources_id'], ['id'])
    op.create_index('ix_ship_modern_resources_id', 'ship', ['modern_resources_id'], unique=False)
    op.drop_index(op.f('ix_ship_modern_stats_id'), table_name='ship')
    op.drop_column('ship', 'modern_stats_id')
    ### end Alembic commands ###