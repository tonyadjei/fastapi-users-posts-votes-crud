"""create posts table

Revision ID: 821ad3690269
Revises: 
Create Date: 2022-08-03 19:04:26.437183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '821ad3690269'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id',sa.Integer(), nullable=False, primary_key=True)
    , sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
