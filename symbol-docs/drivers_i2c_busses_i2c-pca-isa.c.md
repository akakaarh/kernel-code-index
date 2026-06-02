# drivers/i2c/busses/i2c-pca-isa.c

Subsystem: drivers/i2c

## Functions (8)

### pca_handler
- Return type: static irqreturn_t
- Signature: pca_handler(int this_irq,void * dev_id)
- Line: 89

### pca_isa_match
- Return type: static int
- Signature: pca_isa_match(struct device * dev,unsigned int id)
- Line: 109

### pca_isa_probe
- Return type: static int
- Signature: pca_isa_probe(struct device * dev,unsigned int id)
- Line: 122

### pca_isa_readbyte
- Return type: static int
- Signature: pca_isa_readbyte(void * pd,int reg)
- Line: 47

### pca_isa_remove
- Return type: static void
- Signature: pca_isa_remove(struct device * dev,unsigned int id)
- Line: 164

### pca_isa_resetchip
- Return type: static void
- Signature: pca_isa_resetchip(void * pd)
- Line: 83

### pca_isa_waitforcompletion
- Return type: static int
- Signature: pca_isa_waitforcompletion(void * pd)
- Line: 59

### pca_isa_writebyte
- Return type: static void
- Signature: pca_isa_writebyte(void * pd,int reg,int val)
- Line: 37

## Variables (8)

- static **base** : unsigned long (line 27)
- static **clock** : int (line 32)
- static **irq** : int (line 28)
- static **pca_isa_data** : i2c_algo_pca_data (line 94)
- static **pca_isa_driver** : isa_driver (line 175)
- static **pca_isa_ops** : i2c_adapter (line 102)
- static **pca_isa_ops** : i2c_adapter (line 34)
- static **pca_wait** : wait_queue_head_t (line 35)

## Macros (2)

- **DRIVER** (line 24)
- **IO_SIZE** (line 25)
