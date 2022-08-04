"""add remaining columns to posts table

Revision ID: 317daa8e0f65
Revises: 983b1ed11e06
Create Date: 2022-08-03 19:59:53.163467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '317daa8e0f65'
down_revision = '983b1ed11e06'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), server_default='True', nullable=False))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
