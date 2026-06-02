# drivers/i2c/busses/i2c-pca-platform.c

Subsystem: drivers/i2c

## Functions (12)

### i2c_pca_pf_dummyreset
- Return type: static void
- Signature: i2c_pca_pf_dummyreset(void * pd)
- Line: 101

### i2c_pca_pf_handler
- Return type: static irqreturn_t
- Signature: i2c_pca_pf_handler(int this_irq,void * dev_id)
- Line: 117

### i2c_pca_pf_probe
- Return type: static int
- Signature: i2c_pca_pf_probe(struct platform_device * pdev)
- Line: 130

### i2c_pca_pf_readbyte16
- Return type: static int
- Signature: i2c_pca_pf_readbyte16(void * pd,int reg)
- Line: 45

### i2c_pca_pf_readbyte32
- Return type: static int
- Signature: i2c_pca_pf_readbyte32(void * pd,int reg)
- Line: 51

### i2c_pca_pf_readbyte8
- Return type: static int
- Signature: i2c_pca_pf_readbyte8(void * pd,int reg)
- Line: 39

### i2c_pca_pf_remove
- Return type: static void
- Signature: i2c_pca_pf_remove(struct platform_device * pdev)
- Line: 223

### i2c_pca_pf_resetchip
- Return type: static void
- Signature: i2c_pca_pf_resetchip(void * pd)
- Line: 108

### i2c_pca_pf_waitforcompletion
- Return type: static int
- Signature: i2c_pca_pf_waitforcompletion(void * pd)
- Line: 76

### i2c_pca_pf_writebyte16
- Return type: static void
- Signature: i2c_pca_pf_writebyte16(void * pd,int reg,int val)
- Line: 63

### i2c_pca_pf_writebyte32
- Return type: static void
- Signature: i2c_pca_pf_writebyte32(void * pd,int reg,int val)
- Line: 69

### i2c_pca_pf_writebyte8
- Return type: static void
- Signature: i2c_pca_pf_writebyte8(void * pd,int reg,int val)
- Line: 57

## Structs (1)

### i2c_pca_pf_data
- Line: 28
- Members:
  - reg_base: void __iomem *
  - irq: int
  - gpio: gpio_desc *
  - wait: wait_queue_head_t
  - adap: i2c_adapter
  - algo_data: i2c_algo_pca_data

## Variables (2)

- static **i2c_pca_of_match_table** : const struct of_device_id[] (line 231)
- static **i2c_pca_pf_driver** : platform_driver (line 239)
