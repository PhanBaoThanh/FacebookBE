"""upgrade

Revision ID: 2d1d3c753cce
Revises: 671818ebf392
Create Date: 2023-04-13 15:40:36.405709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d1d3c753cce'
down_revision = '671818ebf392'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Admin',
    sa.Column('AdminId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=128), nullable=True),
    sa.Column('DateOfBirth', sa.DateTime(), nullable=True),
    sa.Column('Account', sa.String(length=128), nullable=True),
    sa.Column('Password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('AdminId')
    )
    op.create_table('Client',
    sa.Column('ClientId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=128), nullable=True),
    sa.Column('PhoneNumber', sa.String(length=128), nullable=True),
    sa.Column('Email', sa.String(length=128), nullable=True),
    sa.Column('Account', sa.String(length=128), nullable=True),
    sa.Column('Password', sa.String(length=128), nullable=True),
    sa.Column('Sex', sa.Boolean(), nullable=True),
    sa.Column('DayOfBirth', sa.DateTime(), nullable=True),
    sa.Column('Avatar', sa.String(length=500), nullable=True),
    sa.Column('BackgroundImg', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('ClientId')
    )
    op.create_table('Groups',
    sa.Column('GroupId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=128), nullable=True),
    sa.Column('CreatedAt', sa.DateTime(), nullable=True),
    sa.Column('BackgroundImg', sa.String(length=500), nullable=True),
    sa.Column('IsPrivate', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('GroupId')
    )
    op.create_table('Chat',
    sa.Column('ChatId', sa.Integer(), nullable=False),
    sa.Column('ClientId1', sa.Integer(), nullable=True),
    sa.Column('ClientId2', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ClientId1'], ['Client.ClientId'], ),
    sa.ForeignKeyConstraint(['ClientId2'], ['Client.ClientId'], ),
    sa.PrimaryKeyConstraint('ChatId')
    )
    op.create_table('Friend',
    sa.Column('FriendId', sa.Integer(), nullable=False),
    sa.Column('ClientId1', sa.Integer(), nullable=True),
    sa.Column('ClientId2', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ClientId1'], ['Client.ClientId'], ),
    sa.ForeignKeyConstraint(['ClientId2'], ['Client.ClientId'], ),
    sa.PrimaryKeyConstraint('FriendId')
    )
    op.create_table('FriendRequest',
    sa.Column('FriendRequestId', sa.Integer(), nullable=False),
    sa.Column('SenderId', sa.Integer(), nullable=True),
    sa.Column('ReceiverId', sa.Integer(), nullable=True),
    sa.Column('CreatedAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ReceiverId'], ['Client.ClientId'], ),
    sa.ForeignKeyConstraint(['SenderId'], ['Client.ClientId'], ),
    sa.PrimaryKeyConstraint('FriendRequestId')
    )
    op.create_table('GroupMember',
    sa.Column('GroupMemberId', sa.Integer(), nullable=False),
    sa.Column('GroupId', sa.Integer(), nullable=True),
    sa.Column('ClientId', sa.Integer(), nullable=True),
    sa.Column('IsAdmin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['ClientId'], ['Client.ClientId'], ),
    sa.ForeignKeyConstraint(['GroupId'], ['Groups.GroupId'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('GroupMemberId')
    )
    op.create_table('GroupRequest',
    sa.Column('GroupRequestId', sa.Integer(), nullable=False),
    sa.Column('GroupId', sa.Integer(), nullable=True),
    sa.Column('ClientId', sa.Integer(), nullable=True),
    sa.Column('CreatedAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ClientId'], ['Client.ClientId'], ),
    sa.ForeignKeyConstraint(['GroupId'], ['Groups.GroupId'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('GroupRequestId')
    )
    op.create_table('Post',
    sa.Column('PostId', sa.Integer(), nullable=False),
    sa.Column('GroupId', sa.Integer(), nullable=True),
    sa.Column('ClientId', sa.Integer(), nullable=True),
    sa.Column('CreatedAt', sa.DateTime(), nullable=True),
    sa.Column('Content', sa.String(length=500), nullable=True),
    sa.Column('Img', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ClientId'], ['Client.ClientId'], ),
    sa.ForeignKeyConstraint(['GroupId'], ['Groups.GroupId'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('PostId')
    )
    op.create_table('PostConfirm',
    sa.Column('PostConfirmId', sa.Integer(), nullable=False),
    sa.Column('GroupId', sa.Integer(), nullable=True),
    sa.Column('ClientId', sa.Integer(), nullable=True),
    sa.Column('CreatedAt', sa.DateTime(), nullable=True),
    sa.Column('Content', sa.String(length=500), nullable=True),
    sa.Column('Img', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ClientId'], ['Client.ClientId'], ),
    sa.ForeignKeyConstraint(['GroupId'], ['Groups.GroupId'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('PostConfirmId')
    )
    op.create_table('Comment',
    sa.Column('CommentId', sa.Integer(), nullable=False),
    sa.Column('PostId', sa.Integer(), nullable=True),
    sa.Column('ClientId', sa.Integer(), nullable=True),
    sa.Column('Content', sa.String(length=500), nullable=True),
    sa.Column('CreatedAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ClientId'], ['Client.ClientId'], ),
    sa.ForeignKeyConstraint(['PostId'], ['Post.PostId'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('CommentId')
    )
    op.create_table('Message',
    sa.Column('MessageId', sa.Integer(), nullable=False),
    sa.Column('ChatId', sa.Integer(), nullable=True),
    sa.Column('SenderId', sa.Integer(), nullable=True),
    sa.Column('Content', sa.String(length=500), nullable=True),
    sa.Column('CreatedAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ChatId'], ['Chat.ChatId'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['SenderId'], ['Client.ClientId'], ),
    sa.PrimaryKeyConstraint('MessageId')
    )
    op.create_table('Reaction',
    sa.Column('ReactionId', sa.Integer(), nullable=False),
    sa.Column('PostId', sa.Integer(), nullable=True),
    sa.Column('ClientId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ClientId'], ['Client.ClientId'], ),
    sa.ForeignKeyConstraint(['PostId'], ['Post.PostId'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ReactionId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Reaction')
    op.drop_table('Message')
    op.drop_table('Comment')
    op.drop_table('PostConfirm')
    op.drop_table('Post')
    op.drop_table('GroupRequest')
    op.drop_table('GroupMember')
    op.drop_table('FriendRequest')
    op.drop_table('Friend')
    op.drop_table('Chat')
    op.drop_table('Groups')
    op.drop_table('Client')
    op.drop_table('Admin')
    # ### end Alembic commands ###
