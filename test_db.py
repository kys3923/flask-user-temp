from models import db, User

# ================== create users
users = [
  User(
    name="Steve Peters",
    email="stpets@bigdaddy.com",
    bio="Cranky but cool and caring"
  )
]
# ========================= option 1
users.append(User(
  name="Miek Schull",
  email="mikey.boi@prettyokay.dev",
  bio="The reddest raddest dev"
))

# ========================== option 2

bb = User(
  name="Brandi butler",
  email="brandi@butler.com",
  bio="Cats and computers are my jam"
)
users.append(bb)

db.session.add_all(users)
db.session.commit()