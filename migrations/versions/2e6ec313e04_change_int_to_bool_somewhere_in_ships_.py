"""Change int to bool somewhere in ships data

Revision ID: 2e6ec313e04
Revises: 1f4f8dd0a86
Create Date: 2015-10-24 18:23:40.694199

"""

# revision identifiers, used by Alembic.
revision = '2e6ec313e04'
down_revision = '1f4f8dd0a86'

from alembic import op


def upgrade():
    conn = op.get_bind()
    conn.execute("ALTER TABLE admiral_equipment ALTER COLUMN locked TYPE BOOLEAN USING CASE WHEN locked=0 THEN false ELSE true END;")


def downgrade():
    conn = op.get_bind()
    conn.execute("ALTER TABLE admiral_equipment ALTER COLUMN locked TYPE INTEGER USING CASE WHEN false THEN 0 ELSE 1 END;")
