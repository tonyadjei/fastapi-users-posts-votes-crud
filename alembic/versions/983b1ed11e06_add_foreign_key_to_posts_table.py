"""add foreign key to posts table

Revision ID: 983b1ed11e06
Revises: 28e0cf8edf4a
Create Date: 2022-08-03 19:51:25.515596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '983b1ed11e06'
down_revision = '28e0cf8edf4a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_users_fkey', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fkey", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
