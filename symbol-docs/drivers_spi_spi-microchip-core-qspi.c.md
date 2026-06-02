# drivers/spi/spi-microchip-core-qspi.c

Subsystem: drivers/spi

## Functions (20)

### mchp_coreqspi_adjust_op_size
- Return type: static int
- Signature: mchp_coreqspi_adjust_op_size(struct spi_mem * mem,struct spi_mem_op * op)
- Line: 587

### mchp_coreqspi_config_op
- Return type: static void
- Signature: mchp_coreqspi_config_op(struct mchp_coreqspi * qspi,const struct spi_mem_op * op)
- Line: 422

### mchp_coreqspi_disable_ints
- Return type: static void
- Signature: mchp_coreqspi_disable_ints(struct mchp_coreqspi * qspi)
- Line: 354

### mchp_coreqspi_enable_ints
- Return type: static void
- Signature: mchp_coreqspi_enable_ints(struct mchp_coreqspi * qspi)
- Line: 345

### mchp_coreqspi_exec_op
- Return type: static int
- Signature: mchp_coreqspi_exec_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 486

### mchp_coreqspi_isr
- Return type: static irqreturn_t
- Signature: mchp_coreqspi_isr(int irq,void * dev_id)
- Line: 359

### mchp_coreqspi_prepare_message
- Return type: static int
- Signature: mchp_coreqspi_prepare_message(struct spi_controller * ctlr,struct spi_message * m)
- Line: 622

### mchp_coreqspi_probe
- Return type: static int
- Signature: mchp_coreqspi_probe(struct platform_device * pdev)
- Line: 720

### mchp_coreqspi_read_op
- Return type: static void
- Signature: mchp_coreqspi_read_op(struct mchp_coreqspi * qspi)
- Line: 200

### mchp_coreqspi_remove
- Return type: static void
- Signature: mchp_coreqspi_remove(struct platform_device * pdev)
- Line: 802

### mchp_coreqspi_set_cs
- Return type: static void
- Signature: mchp_coreqspi_set_cs(struct spi_device * spi,bool enable)
- Line: 168

### mchp_coreqspi_set_mode
- Return type: static int
- Signature: mchp_coreqspi_set_mode(struct mchp_coreqspi * qspi,const struct spi_mem_op * op)
- Line: 133

### mchp_coreqspi_setup
- Return type: static int
- Signature: mchp_coreqspi_setup(struct spi_device * spi)
- Line: 181

### mchp_coreqspi_setup_clock
- Return type: static int
- Signature: mchp_coreqspi_setup_clock(struct mchp_coreqspi * qspi,struct spi_device * spi,u32 max_freq)
- Line: 388

### mchp_coreqspi_supports_op
- Return type: static bool
- Signature: mchp_coreqspi_supports_op(struct spi_mem * mem,const struct spi_mem_op * op)
- Line: 560

### mchp_coreqspi_transfer_one
- Return type: static int
- Signature: mchp_coreqspi_transfer_one(struct spi_controller * ctlr,struct spi_device * spi,struct spi_transfer * t)
- Line: 689

### mchp_coreqspi_unprepare_message
- Return type: static int
- Signature: mchp_coreqspi_unprepare_message(struct spi_controller * ctlr,struct spi_message * m)
- Line: 607

### mchp_coreqspi_wait_for_ready
- Return type: static int
- Signature: mchp_coreqspi_wait_for_ready(struct mchp_coreqspi * qspi)
- Line: 477

### mchp_coreqspi_write_op
- Return type: static void
- Signature: mchp_coreqspi_write_op(struct mchp_coreqspi * qspi)
- Line: 236

### mchp_coreqspi_write_read_op
- Return type: static void
- Signature: mchp_coreqspi_write_read_op(struct mchp_coreqspi * qspi)
- Line: 264

## Structs (1)

### mchp_coreqspi
- Line: 121
- Members:
  - regs: void __iomem *
  - clk: clk *
  - data_completion: completion
  - op_lock: mutex
  - txbuf: u8 *
  - rxbuf: u8 *
  - irq: int
  - tx_len: int
  - rx_len: int

## Variables (4)

- static **mchp_coreqspi_driver** : platform_driver (line 822)
- static **mchp_coreqspi_mem_caps** : const struct spi_controller_mem_caps (line 603)
- static **mchp_coreqspi_mem_ops** : const struct spi_controller_mem_ops (line 597)
- static **mchp_coreqspi_of_match** : const struct of_device_id[] (line 816)

## Macros (57)

- **BYTESLOWER_MASK** (line 85)
- **BYTESUPPER_MASK** (line 84)
- **CONTROL_CLKIDLE** (line 31)
- **CONTROL_CLKRATE_MASK** (line 39)
- **CONTROL_CLKRATE_SHIFT** (line 40)
- **CONTROL_ENABLE** (line 27)
- **CONTROL_FLAGSX4** (line 38)
- **CONTROL_MASTER** (line 28)
- **CONTROL_MODE0** (line 33)
- **CONTROL_MODE12_EX_RO** (line 35)
- **CONTROL_MODE12_EX_RW** (line 36)
- **CONTROL_MODE12_FULL** (line 37)
- **CONTROL_MODE12_MASK** (line 34)
- **CONTROL_SAMPLE_MASK** (line 32)
- **CONTROL_XIP** (line 29)
- **CONTROL_XIPADDR** (line 30)
- **DIRECT_ACCESS_EN_SSEL** (line 80)
- **DIRECT_ACCESS_OP_SSEL** (line 81)
- **DIRECT_ACCESS_OP_SSEL_SHIFT** (line 82)
- **FRAMES_CMDBYTES_MASK** (line 46)
- **FRAMES_CMDBYTES_SHIFT** (line 47)
- **FRAMES_FLAGBYTE** (line 51)
- **FRAMES_FLAGWORD** (line 52)
- **FRAMES_IDLE_MASK** (line 49)
- **FRAMES_IDLE_SHIFT** (line 50)
- **FRAMES_SHIFT** (line 48)
- **FRAMES_TOTALBYTES_MASK** (line 45)
- **IEN_RXAVAILABLE** (line 59)
- **IEN_RXDONE** (line 58)
- **IEN_RXFIFOEMPTY** (line 61)
- **IEN_TXAVAILABLE** (line 60)
- **IEN_TXDONE** (line 57)
- **IEN_TXFIFOFULL** (line 62)
- **MAX_DATA_CMD_LEN** (line 89)
- **MAX_DIVIDER** (line 87)
- **MIN_DIVIDER** (line 88)
- **REG_CONTROL** (line 97)
- **REG_DIRECT_ACCESS** (line 101)
- **REG_FRAMES** (line 98)
- **REG_FRAMESUP** (line 107)
- **REG_IEN** (line 99)
- **REG_RX_DATA** (line 103)
- **REG_STATUS** (line 100)
- **REG_TX_DATA** (line 104)
- **REG_UPPER_ACCESS** (line 102)
- **REG_X4_RX_DATA** (line 105)
- **REG_X4_TX_DATA** (line 106)
- **STATUS_FLAGSX4** (line 74)
- **STATUS_MASK** (line 75)
- **STATUS_READY** (line 73)
- **STATUS_RXAVAILABLE** (line 69)
- **STATUS_RXDONE** (line 68)
- **STATUS_RXFIFOEMPTY** (line 71)
- **STATUS_TXAVAILABLE** (line 70)
- **STATUS_TXDONE** (line 67)
- **STATUS_TXFIFOFULL** (line 72)
- **TIMEOUT_MS** (line 92)
