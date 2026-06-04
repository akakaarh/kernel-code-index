# drivers/mmc/host/cqhci-crypto.c

Subsystem: drivers/mmc

## Functions (7)

### cqhci_crypto_clear_keyslot
- Return type: static int
- Signature: cqhci_crypto_clear_keyslot(struct cqhci_host * cq_host,int slot)
- Line: 100

### cqhci_crypto_init
- Return type: int
- Signature: cqhci_crypto_init(struct cqhci_host * cq_host)
- Line: 161

### cqhci_crypto_keyslot_evict
- Return type: static int
- Signature: cqhci_crypto_keyslot_evict(struct blk_crypto_profile * profile,const struct blk_crypto_key * key,unsigned int slot)
- Line: 112

### cqhci_crypto_keyslot_program
- Return type: static int
- Signature: cqhci_crypto_keyslot_program(struct blk_crypto_profile * profile,const struct blk_crypto_key * key,unsigned int slot)
- Line: 54

### cqhci_crypto_program_key
- Return type: static void
- Signature: cqhci_crypto_program_key(struct cqhci_host * cq_host,const union cqhci_crypto_cfg_entry * cfg,int slot)
- Line: 31

### cqhci_find_blk_crypto_mode
- Return type: static blk_crypto_mode_num
- Signature: cqhci_find_blk_crypto_mode(union cqhci_crypto_cap_entry cap)
- Line: 135

### cqhci_host_from_crypto_profile
- Return type: static cqhci_host *
- Signature: cqhci_host_from_crypto_profile(struct blk_crypto_profile * profile)
- Line: 26

## Structs (1)

### cqhci_crypto_alg_entry
- Line: 15
- Members:
  - alg: cqhci_crypto_alg
  - key_size: cqhci_crypto_key_size

## Variables (2)

- **cqhci_crypto_algs** : const struct cqhci_crypto_alg_entry[] (line 18)
- static **cqhci_crypto_ops** : const struct blk_crypto_ll_ops (line 129)
