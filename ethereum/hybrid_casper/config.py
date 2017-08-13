import copy
from ethereum import utils, config

config_casper = dict(
    # The Casper-specific config declaration
    HOMESTEAD_FORK_BLKNUM=0,
    ANTI_DOS_FORK_BLKNUM=0,
    CLEARING_FORK_BLKNUM=0,
    CONSENSUS_STRATEGY='hybrid_casper',
    EPOCH_LENGTH=25,
    CASPER_ADDRESS=utils.mk_contract_address(utils.privtoaddr(utils.sha3("null_sender")), 4),
    NULL_SENDER=utils.sha3("null_sender")
)

config.config_casper = {**config.default_config, **config_casper}
