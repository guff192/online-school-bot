from sqlalchemy import create_engine, MetaData
from db import wallets, courses, tasks, students, students_courses, students_tasks
from settings import get_dsn


ADMIN_DB_URL = get_dsn()
admin_engine = create_engine(ADMIN_DB_URL)


def create_tables(engine=admin_engine):
    meta = MetaData(bind=engine)
    meta.create_all(bind=engine, tables=[wallets, courses, tasks, students, students_courses, students_tasks], checkfirst=True)


if __name__ == '__main__':
    create_tables(admin_engine)
