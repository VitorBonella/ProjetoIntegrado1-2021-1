"""Username

Revision ID: f3a4d7834f2e
Revises: 205b0d125f24
Create Date: 2021-09-23 13:29:53.927180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3a4d7834f2e'
down_revision = '205b0d125f24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('post_username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'post_username')
    # ### end Alembic commands ###