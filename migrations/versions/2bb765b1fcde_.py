"""empty message

Revision ID: 2bb765b1fcde
Revises: 62abce5e6660
Create Date: 2021-04-08 02:52:47.521563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bb765b1fcde'
down_revision = '62abce5e6660'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('birth_year', sa.Integer(), nullable=False))
    op.add_column('character', sa.Column('eye_color', sa.Integer(), nullable=False))
    op.add_column('character', sa.Column('gender', sa.String(length=250), nullable=False))
    op.add_column('character', sa.Column('hair_color', sa.Integer(), nullable=False))
    op.add_column('character', sa.Column('height', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('character', 'height')
    op.drop_column('character', 'hair_color')
    op.drop_column('character', 'gender')
    op.drop_column('character', 'eye_color')
    op.drop_column('character', 'birth_year')
    # ### end Alembic commands ###
