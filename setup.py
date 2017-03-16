from setuptools import setup

setup(
    name="electrum-wdc-server",
    version="1.0",
    scripts=['run_electrum_wdc_server.py','electrum-wdc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumwdcserver':'src'
        },
    py_modules=[
        'electrumwdcserver.__init__',
        'electrumwdcserver.utils',
        'electrumwdcserver.storage',
        'electrumwdcserver.deserialize',
        'electrumwdcserver.networks',
        'electrumwdcserver.blockchain_processor',
        'electrumwdcserver.server_processor',
        'electrumwdcserver.processor',
        'electrumwdcserver.version',
        'electrumwdcserver.ircthread',
        'electrumwdcserver.stratum_tcp'
    ],
    description="Litecoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/woodcoin-core/electrum-wdc-server/",
    long_description="""Server for the Electrum Lightweight Woodcoin Wallet"""
)
