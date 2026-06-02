# drivers/spi/spi-realtek-rtl-snand.c

Subsystem: drivers/spi

## Functions (11)

### rtl_snand_dma_op
- Return type: static bool
- Signature: rtl_snand_dma_op(const struct spi_mem_op * op)
- Line: 315

### rtl_snand_dma_xfer
- Return type: static int
- Signature: rtl_snand_dma_xfer(struct rtl_snand * snand,int cs,const struct spi_mem_op * op)
- Line: 232

### rtl_snand_exec_op
- Return type: static int
- Signature: rtl_snand_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 326

### rtl_snand_irq
- Return type: static irqreturn_t
- Signature: rtl_snand_irq(int irq,void * data)
- Line: 38

### rtl_snand_probe
- Return type: static int
- Signature: rtl_snand_probe(struct platform_device * pdev)
- Line: 357

### rtl_snand_set_cs
- Return type: static void
- Signature: rtl_snand_set_cs(struct rtl_snand * snand,int cs,bool active)
- Line: 63

### rtl_snand_supports_op
- Return type: static bool
- Signature: rtl_snand_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 53

### rtl_snand_wait_ready
- Return type: static int
- Signature: rtl_snand_wait_ready(struct rtl_snand * snand)
- Line: 75

### rtl_snand_xfer
- Return type: static int
- Signature: rtl_snand_xfer(struct rtl_snand * snand,int cs,const struct spi_mem_op * op)
- Line: 156

### rtl_snand_xfer_head
- Return type: static int
- Signature: rtl_snand_xfer_head(struct rtl_snand * snand,int cs,const struct spi_mem_op * op)
- Line: 83

### rtl_snand_xfer_tail
- Return type: static void
- Signature: rtl_snand_xfer_tail(struct rtl_snand * snand,int cs)
- Line: 151

## Structs (1)

### rtl_snand
- Line: 32
- Members:
  - dev: device *
  - regmap: regmap *
  - comp: completion

## Variables (3)

- static **rtl_snand_driver** : platform_driver (line 407)
- static **rtl_snand_match** : const struct of_device_id[] (line 348)
- static **rtl_snand_mem_ops** : const struct spi_controller_mem_ops (line 343)

## Macros (18)

- **CMR_LEN**(len) (line 29)
- **CMR_WID**(width) (line 30)
- **SNAFCCR** (line 14)
- **SNAFCFR** (line 12)
- **SNAFCFR_DMA_IE** (line 13)
- **SNAFDIR** (line 21)
- **SNAFDIR_DMA_IP** (line 22)
- **SNAFDLR** (line 23)
- **SNAFDRSAR** (line 20)
- **SNAFDTR** (line 19)
- **SNAFRCMR** (line 16)
- **SNAFRDR** (line 17)
- **SNAFSR** (line 24)
- **SNAFSR_NFCOS** (line 25)
- **SNAFSR_NFDRS** (line 26)
- **SNAFSR_NFDWS** (line 27)
- **SNAFWCMR** (line 15)
- **SNAFWDR** (line 18)
