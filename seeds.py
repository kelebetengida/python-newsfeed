from app.models import User
from app.db import Session, Base, engine
from app.models import User, Post
from app.models import User, Post, Comment
from app.models import User, Post, Comment, Vote
# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
  User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
  User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
  User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])
db.commit()

# insert posts
db.add_all([
  Post(title='Our tech problems have become more complex. What do you think?', post_url='https://www.nytimes.com/2022/11/02/insider/personal-tech-brian-chen.html', user_id=1),
  Post(title='You wonder, when did this conversation become so hilarious? What am I missing?', post_url='https://www.npr.org/2020/09/25/916997530/laughter-the-best-medicine', user_id=1),
  Post(title='Small business owners - how they live, how they work, what influences them', post_url='https://www.beyondthetodolist.com/tara-mcmullin-on-changing-your-approach-to-goal-setting/', user_id=2),
  Post(title='The ban on semiconductor', post_url='https://www.vox.com/world/2022/11/5/23440525/biden-administration-semiconductor-export-ban-china', user_id=3),
  Post(title='Following successful completion of Artemis I recovery operations', post_url='https://www.nasa.gov/feature/i-am-artemis-christine-st-germain', user_id=4)
])


db.commit()
# insert comments
db.add_all([
  Comment(comment_text='I love this convo! Laughter is the best treatment!', user_id=1, post_id=2),
  Comment(comment_text='Tara is the host of What Works, a great podcast!', user_id=1, post_id=3),
  Comment(comment_text='Teach companies are dominating all sectors and I think that creates more jobs but it also makes us to dependent.', user_id=2, post_id=1),
  Comment(comment_text='What a great Podcast!', user_id=2, post_id=3),
  Comment(comment_text='Here work was fetured on The Huffington Post, you go Tara!', user_id=3, post_id=3)
])

db.commit()
# insert votes
db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=1, post_id=4),
  Vote(user_id=2, post_id=4),
  Vote(user_id=3, post_id=4),
  Vote(user_id=4, post_id=2)
])

db.commit()
db.close()