from app import db
from datetime import datetime

def slugify(s):
	patern = r'[^\w+]'
	return re.sub(patern, '-', s)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title= db.Column(db.String(140))
	slug = db.Column(db.String(140), unique=True)# slug = url for napolneniya stranici
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())
	def __init__(self , *args, **kwargs):
		super(Post , self).__init__(*args,**kwargs)
		self.generate_slug()

	def generate_slug(self):
		if self.title:
			self.slug = slugify(self.title)
	def __repr__(self):
		return '<Post id: {}, title: {}>'.format(self.id, self.title)

	 # * eto spisok, ** - eto slovar kw-imenovaniye parametri' ronstruktor v nem posicionnie argumenti i imenovanie


