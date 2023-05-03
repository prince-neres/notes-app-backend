"""empty message

Revision ID: 475ff0a2f307
Revises: a40a9305aa71
Create Date: 2023-05-02 22:06:34.321760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '475ff0a2f307'
down_revision = 'a40a9305aa71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('notes_id_seq'::regclass)"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('notes_id_seq'::regclass)"))

    # ### end Alembic commands ###
