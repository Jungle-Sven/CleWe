from flask import Flask, request, jsonify
from app.models import db, db_uri, User, Quest, Action
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        wallet_address=data['wallet_address'],
        experience=data.get('experience', 0),
        level=data.get('level', 1),
        nickname=data['nickname'],
        avatar_url=data['avatar_url'],
        skill_general_xp=data.get('skill_general_xp', 0),
        skill_dex_xp=data.get('skill_dex_xp', 0),
        skill_nft_xp=data.get('skill_nft_xp', 0)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({
        'id': user.id,
        'wallet_address': user.wallet_address,
        'experience': user.experience,
        'level': user.level,
        'nickname': user.nickname,
        'avatar_url': user.avatar_url,
        'skill_general_xp': user.skill_general_xp,
        'skill_dex_xp': user.skill_dex_xp,
        'skill_nft_xp': user.skill_nft_xp
    })

@app.route('/quests', methods=['POST'])
def create_quest():
    data = request.json
    new_quest = Quest(
        name=data['name'],
        topic=data['topic'],
        text=data['text']
    )
    db.session.add(new_quest)
    db.session.commit()
    return jsonify({'message': 'Quest created successfully'}), 201

@app.route('/quests/<int:quest_id>', methods=['GET'])
def get_quest(quest_id):
    quest = Quest.query.get(quest_id)
    if not quest:
        return jsonify({'message': 'Quest not found'}), 404
    return jsonify({
        'id': quest.id,
        'name': quest.name,
        'topic': quest.topic,
        'text': quest.text
    })

@app.route('/actions', methods=['POST'])
def create_action():
    data = request.json
    new_action = Action(
        user_wallet=data['user_wallet'],
        action=data['action'],
        xp_reward=data.get('xp_reward', 0),
        timestamp=datetime.utcnow()
    )
    db.session.add(new_action)
    db.session.commit()
    return jsonify({'message': 'Action created successfully'}), 201

@app.route('/users/<int:user_id>/actions', methods=['GET'])
def get_user_actions(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    actions = Action.query.filter_by(user_wallet=user.wallet_address).all()
    return jsonify([{
        'id': action.id,
        'user_wallet': action.user_wallet,
        'timestamp': action.timestamp,
        'action': action.action,
        'xp_reward': action.xp_reward
    } for action in actions])

if __name__ == '__main__':
    app.run(debug=True)
