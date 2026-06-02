# drivers/spi/spi-iproc-qspi.c

Subsystem: drivers/spi

## Functions (5)

### bcm_iproc_probe
- Return type: static int
- Signature: bcm_iproc_probe(struct platform_device * pdev)
- Line: 92

### bcm_iproc_qspi_get_l2_int_status
- Return type: static u32
- Signature: bcm_iproc_qspi_get_l2_int_status(struct bcm_qspi_soc_intc * soc_intc)
- Line: 29

### bcm_iproc_qspi_int_ack
- Return type: static void
- Signature: bcm_iproc_qspi_int_ack(struct bcm_qspi_soc_intc * soc_intc,int type)
- Line: 54

### bcm_iproc_qspi_int_set
- Return type: static void
- Signature: bcm_iproc_qspi_int_set(struct bcm_qspi_soc_intc * soc_intc,int type,bool en)
- Line: 68

### bcm_iproc_remove
- Return type: static void
- Signature: bcm_iproc_remove(struct platform_device * pdev)
- Line: 127

## Structs (1)

### bcm_iproc_intc
- Line: 20
- Members:
  - soc_intc: bcm_qspi_soc_intc
  - pdev: platform_device *
  - int_reg: void __iomem *
  - int_status_reg: void __iomem *
  - soclock: spinlock_t
  - big_endian: bool

## Variables (2)

- static **bcm_iproc_driver** : platform_driver (line 139)
- static **bcm_iproc_of_match** : const struct of_device_id[] (line 132)

## Macros (2)

- **INTR_BASE_BIT_SHIFT** (line 17)
- **INTR_COUNT** (line 18)
