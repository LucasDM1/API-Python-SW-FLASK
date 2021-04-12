"""empty message

Revision ID: cdb0e616ca83
Revises: 4f684f2a3014
Create Date: 2021-04-09 23:37:01.969086

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cdb0e616ca83'
down_revision = '4f684f2a3014'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fav_planets')
    op.drop_table('fav_chars')
    op.add_column('users', sa.Column('character_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('planet_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'characters', ['character_id'], ['id'])
    op.create_foreign_key(None, 'users', 'planets', ['planet_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'planet_id')
    op.drop_column('users', 'character_id')
    op.create_table('fav_chars',
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('char_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['char_id'], ['characters.id'], name='fav_chars_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fav_chars_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('fav_planets',
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('plan_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['plan_id'], ['planets.id'], name='fav_planets_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fav_planets_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###