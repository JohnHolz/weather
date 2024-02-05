from src.model import db
from src.create_app import create_app

if __name__ == "__main__":
    app = create_app()
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0",port=5011,debug=True)
    # app.run(host="0.0.0.0",port=5011)
    # app.run(host="0.0.0.0",debug=True)
    # app.run(host="0.0.0.0")
