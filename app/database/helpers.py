from sqlalchemy.orm.session import Session
def save(db:Session,object):
  db.add(object)
  db.commit()
  db.refresh(object)
  return object