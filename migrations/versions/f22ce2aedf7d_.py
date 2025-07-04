"""empty message

Revision ID: f22ce2aedf7d
Revises: 31f3c645284e
Create Date: 2025-07-03 11:10:15.385112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f22ce2aedf7d'
down_revision = '31f3c645284e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.add_column(sa.Column('respondido', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contato', schema=None) as batch_op:
        batch_op.drop_column('respondido')

    # ### end Alembic commands ###
