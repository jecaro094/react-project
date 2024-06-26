"""Add pokedex entry to pokemons table

Revision ID: 0170b214a1c3
Revises: 
Create Date: 2024-05-19 14:22:25.085186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0170b214a1c3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemons', sa.Column('pokedex', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pokemons', 'pokedex')
    # ### end Alembic commands ###
