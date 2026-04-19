from flask_frozen import Freezer
from app import create_app

app = create_app()
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

# 👇 ADD THIS HERE
@freezer.register_generator
def static_pages():
    yield 'page.privacy', {}
    yield 'page.terms', {}

if __name__ == '__main__':
    freezer.freeze()