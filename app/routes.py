from flask import Flask, request, jsonify
from app.models import User, Quest, ActionLog
from datetime import datetime

from app import db

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db.init_app(app)



def index():
    return "hhello world"

#@app.route('/users', methods=['POST'])
def create_user():
    #add some data to db
    user1 = User(
        wallet_address='0xab5801a7d398351b8be11c439e05c5b3259aec9b',
        experience=432,
        level=7,
        nickname='vitalik',
        avatar_url='avatar_url_228',
        skill_general_xp=33,
        skill_dex_xp=65,
        skill_nft_xp=11
    )
    
    db.session.add(user1)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

#@app.route('/users/<int:user_id>', methods=['GET'])
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

#@app.route('/quests', methods=['POST'])
def create_quest():
    new_quest = Quest(
        name='A DEX maxi thread',
        topic='DEX',        
        description='This will motivate you to start using decentralized exchanges',
        text="""Are you tired of the restrictions and limitations of centralized exchanges? Are you looking for a more secure, transparent, and decentralized way to trade cryptocurrencies? Look no further than decentralized exchanges, or DEXs, the future of crypto trading!

With a DEX, you can trade cryptocurrencies peer-to-peer, without the need for intermediaries or central authorities. This means that you have complete control over your assets, and you can be sure that your trades are executed fairly and transparently.

But that's not all! DEXs also offer a wide range of advantages over centralized exchanges. For starters, they are more secure, since they do not store your private keys or personal information on their servers. This makes them less vulnerable to hacks and data breaches, which are unfortunately common in the world of centralized exchanges.

Moreover, DEXs offer a higher degree of privacy and anonymity, since you don't have to provide personal information or go through lengthy KYC procedures to start trading. This means that you can maintain your privacy while still enjoying the benefits of trading cryptocurrencies.

And let's not forget about the gamification aspect of our education platform - with DEXs, you can participate in various challenges and competitions to showcase your trading skills and knowledge of the crypto market. So what are you waiting for? Join the decentralized revolution today and start trading on DEXs like Uniswap, Sushiswap, or Pancakeswap!""",
        image_url='pic123',
        experience_reward = 7,
        skill_reward = 5

    )
    db.session.add(new_quest)
    db.session.commit()
    return jsonify({'message': 'Quest created successfully'}), 201

#@app.route('/quests/<int:quest_id>', methods=['GET'])
def get_quest(quest_id):
    quest = Quest.query.get(quest_id)
    if not quest:
        return jsonify({'message': 'Quest not found'}), 404
    return jsonify({
        'id': quest.id,
        'name': quest.name,
        'topic': quest.topic,
        'description': quest.description,
        'text': quest.text,
        'image_url': quest.image_url,
        'experience_reward': quest.experience_reward,
        'skill_reward': quest.skill_reward
    })
'''
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
'''