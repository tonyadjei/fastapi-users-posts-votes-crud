"""add content column to post table

Revision ID: a869730917ce
Revises: 821ad3690269
Create Date: 2022-08-03 19:23:08.178207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a869730917ce'
down_revision = '821ad3690269'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
