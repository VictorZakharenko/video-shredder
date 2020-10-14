from app import create_app
from app import db
from app.models import User, Role
import click

app = create_app()

@app.cli.command()
def give_admin_role_to_new_user():
    #create user
    user = User.query.filter_by(email='cider1@sweet.ru').first()
    if not user:
        user = User(email='cider1@sweet.ru', active=True)
        user.set_password('91Afr1caShredder1!')
        db.session.add(user)
        db.session.commit() 
    admin_role = Role.query.filter_by(name='admin').first()
    app.logger.info(admin_role)
    if not admin_role:
        app.logger.info('Создаю админскую роль')
        # create admin role
        new_admin_role = Role(name='admin', description='Admin', users=[user])
        db.session.add(new_admin_role)
        db.session.commit()
        app.logger.info('Готово! Роль создана и присвоена')
    else:
        if admin_role not in user.roles:
            user.roles.append(admin_role)
            app.logger.info(user.roles)
            db.session.commit()

        app.logger.info('Готово! Роль присвоена')
