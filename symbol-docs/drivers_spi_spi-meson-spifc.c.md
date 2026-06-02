# drivers/spi/spi-meson-spifc.c

Subsystem: drivers/spi

## Functions (13)

### meson_spifc_drain_buffer
- Return type: static void
- Signature: meson_spifc_drain_buffer(struct meson_spifc * spifc,u8 * buf,int len)
- Line: 115

### meson_spifc_fill_buffer
- Return type: static void
- Signature: meson_spifc_fill_buffer(struct meson_spifc * spifc,const u8 * buf,int len)
- Line: 141

### meson_spifc_hw_init
- Return type: static void
- Signature: meson_spifc_hw_init(struct meson_spifc * spifc)
- Line: 274

### meson_spifc_probe
- Return type: static int
- Signature: meson_spifc_probe(struct platform_device * pdev)
- Line: 285

### meson_spifc_remove
- Return type: static void
- Signature: meson_spifc_remove(struct platform_device * pdev)
- Line: 350

### meson_spifc_resume
- Return type: static int
- Signature: meson_spifc_resume(struct device * dev)
- Line: 373

### meson_spifc_runtime_resume
- Return type: static int
- Signature: meson_spifc_runtime_resume(struct device * dev)
- Line: 406

### meson_spifc_runtime_suspend
- Return type: static int
- Signature: meson_spifc_runtime_suspend(struct device * dev)
- Line: 396

### meson_spifc_setup_speed
- Return type: static void
- Signature: meson_spifc_setup_speed(struct meson_spifc * spifc,u32 speed)
- Line: 165

### meson_spifc_suspend
- Return type: static int
- Signature: meson_spifc_suspend(struct device * dev)
- Line: 357

### meson_spifc_transfer_one
- Return type: static int
- Signature: meson_spifc_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 245

### meson_spifc_txrx
- Return type: static int
- Signature: meson_spifc_txrx(struct meson_spifc * spifc,struct spi_transfer * xfer,int offset,int len,bool last_xfer,bool last_chunk)
- Line: 194

### meson_spifc_wait_ready
- Return type: static int
- Signature: meson_spifc_wait_ready(struct meson_spifc * spifc)
- Line: 94

## Structs (1)

### meson_spifc
- Line: 75
- Members:
  - host: spi_controller *
  - regmap: regmap *
  - clk: clk *
  - dev: device *

## Variables (4)

- static **meson_spifc_driver** : platform_driver (line 429)
- static **meson_spifc_dt_match** : const struct of_device_id[] (line 422)
- static **meson_spifc_pm_ops** : const struct dev_pm_ops (line 415)
- static **spifc_regmap_config** : const struct regmap_config (line 82)

## Macros (42)

- **CLOCK_CNT_HIGH_MASK** (line 49)
- **CLOCK_CNT_HIGH_SHIFT** (line 48)
- **CLOCK_CNT_LOW_MASK** (line 51)
- **CLOCK_CNT_LOW_SHIFT** (line 50)
- **CLOCK_DIV_MASK** (line 47)
- **CLOCK_DIV_SHIFT** (line 46)
- **CLOCK_SOURCE** (line 45)
- **CMD_USER** (line 43)
- **CTRL_ENABLE_AHB** (line 44)
- **REG_ADDR** (line 23)
- **REG_B8** (line 39)
- **REG_C0** (line 38)
- **REG_CLOCK** (line 28)
- **REG_CMD** (line 22)
- **REG_CTRL** (line 24)
- **REG_CTRL1** (line 25)
- **REG_CTRL2** (line 27)
- **REG_MAX** (line 40)
- **REG_SLAVE** (line 34)
- **REG_SLAVE1** (line 35)
- **REG_SLAVE2** (line 36)
- **REG_SLAVE3** (line 37)
- **REG_STATUS** (line 26)
- **REG_USER** (line 29)
- **REG_USER1** (line 30)
- **REG_USER2** (line 31)
- **REG_USER3** (line 32)
- **REG_USER4** (line 33)
- **SLAVE_OP_MODE** (line 63)
- **SLAVE_SW_RST** (line 64)
- **SLAVE_TRST_DONE** (line 62)
- **SPIFC_BUFFER_SIZE** (line 66)
- **USER1_BN_UC_DIN_MASK** (line 60)
- **USER1_BN_UC_DIN_SHIFT** (line 59)
- **USER1_BN_UC_DOUT_MASK** (line 58)
- **USER1_BN_UC_DOUT_SHIFT** (line 57)
- **USER4_CS_ACT** (line 61)
- **USER_CMP_MODE** (line 53)
- **USER_DIN_EN_MS** (line 52)
- **USER_UC_DIN_SEL** (line 55)
- **USER_UC_DOUT_SEL** (line 54)
- **USER_UC_MASK** (line 56)
