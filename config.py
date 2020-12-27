import os


def get_config():
    env = os.getenv('env') or os.getenv('ENV')

    if env and env.lower() == 'production':
        config = {
            'SITEURL': 'http://mohanad.kaleia.io',
            'SITENAME': 'Mohanad Kaleia',
        }
    else:
        config = {
            'SITEURL': 'http://localhost:5000',
            'SITENAME': 'Mohanad Kaleia',
        }
    
    return config