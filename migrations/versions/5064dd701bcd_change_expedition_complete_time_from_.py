"""Change expedition complete time from BigInteger to Int

Revision ID: 5064dd701bcd
Revises: df0fd0bd9bed
Create Date: 2016-01-23 11:58:35.711978

"""

# revision identifiers, used by Alembic.
revision = '5064dd701bcd'
down_revision = 'df0fd0bd9bed'

from alembic import op
import sqlalchemy as sa


def upgrade():
    conn = op.get_bind()
    conn.execute("ALTER TABLE expedition ALTER COLUMN time_taken TYPE INT")


def downgrade():
    conn = op.get_bind()
    conn.execute("ALTER TABLE expedition ALTER COLUMN time_taken TYPE BIGINT")
