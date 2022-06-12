from aiopg.sa import create_engine
import sqlalchemy as sa

from settings import get_dsn

# tables metadata object
metadata_obj = sa.MetaData()

# table definitions
wallets = sa.Table('wallets', metadata_obj,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('balance', sa.Float(asdecimal=True)))

courses = sa.Table('courses', metadata_obj,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255)))

tasks = sa.Table('tasks', metadata_obj,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255)),
        sa.Column('description', sa.Text),
        sa.Column('done', sa.Boolean),
        sa.Column('price', sa.Float(asdecimal=True)))

students = sa.Table('students', metadata_obj,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(255)),
        sa.Column('email', sa.String(255)),
        sa.Column('wallet_id', sa.Integer, sa.ForeignKey('wallets.id', ondelete='CASCADE')))

students_courses = sa.Table('students_courses', metadata_obj,
        sa.Column('student_id', sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.ForeignKey('courses.id'), primary_key=True),
        sa.Column('progress', sa.Float(asdecimal=True)))

students_tasks = sa.Table('students_tasks', metadata_obj,
        sa.Column('student_id', sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('task_id', sa.ForeignKey('tasks.id'), primary_key=True))


async def pg_context(app):
    dsn = get_dsn()
    engine = await create_engine(dsn=dsn)
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()

