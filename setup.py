from setuptools import setup

setup(
    name="electrum-server",
    version="0.9",
    scripts=['electrum_server.py','electrum-server'],
    install_requires=['plyvel'],
    py_modules=[
        'src.utils',
        'src.storage',
        'src.deserialize',
        'src.networks',
        'src.blockchain_processor',
        'src.processor',
        'src.version',
        'src.irc',
        'src.poller',
        'src.stratum_tcp',
        'src.stratum_http',
    ],
    description="Litecoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/pooler/electrum-ltc-server/",
    long_description="""Server for the Electrum Lightweight Litecoin Wallet"""
)


