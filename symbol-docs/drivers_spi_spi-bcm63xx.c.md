# drivers/spi/spi-bcm63xx.c

Subsystem: drivers/spi

## Functions (12)

### bcm63xx_spi_interrupt
- Return type: static irqreturn_t
- Signature: bcm63xx_spi_interrupt(int irq,void * dev_id)
- Line: 410

### bcm63xx_spi_max_length
- Return type: static size_t
- Signature: bcm63xx_spi_max_length(struct spi_device * spi)
- Line: 428

### bcm63xx_spi_probe
- Return type: static int
- Signature: bcm63xx_spi_probe(struct platform_device * pdev)
- Line: 492

### bcm63xx_spi_remove
- Return type: static void
- Signature: bcm63xx_spi_remove(struct platform_device * pdev)
- Line: 623

### bcm63xx_spi_resume
- Return type: static int
- Signature: bcm63xx_spi_resume(struct device * dev)
- Line: 653

### bcm63xx_spi_setup_transfer
- Return type: static void
- Signature: bcm63xx_spi_setup_transfer(struct spi_device * spi,struct spi_transfer * t)
- Line: 186

### bcm63xx_spi_suspend
- Return type: static int
- Signature: bcm63xx_spi_suspend(struct device * dev)
- Line: 641

### bcm63xx_spi_transfer_one
- Return type: static int
- Signature: bcm63xx_spi_transfer_one(struct spi_controller * host,struct spi_message * m)
- Line: 329

### bcm63xx_txrx_bufs
- Return type: static int
- Signature: bcm63xx_txrx_bufs(struct spi_device * spi,struct spi_transfer * first,unsigned int num_transfers)
- Line: 217

### bcm_spi_readb
- Return type: static u8
- Signature: bcm_spi_readb(struct bcm63xx_spi * bs,unsigned int offset)
- Line: 154

### bcm_spi_writeb
- Return type: static void
- Signature: bcm_spi_writeb(struct bcm63xx_spi * bs,u8 value,unsigned int offset)
- Line: 160

### bcm_spi_writew
- Return type: static void
- Signature: bcm_spi_writew(struct bcm63xx_spi * bs,u16 value,unsigned int offset)
- Line: 166

## Structs (1)

### bcm63xx_spi
- Line: 134
- Members:
  - done: completion
  - regs: void __iomem *
  - irq: int
  - reg_offsets: const unsigned long *
  - fifo_size: unsigned int
  - msg_type_shift: unsigned int
  - msg_ctl_width: unsigned int
  - tx_io: u8 __iomem *
  - rx_io: const u8 __iomem *
  - clk: clk *
  - pdev: platform_device *

## Enums (1)

### bcm63xx_regs_spi
- Line: 111

## Variables (6)

- static **bcm6348_spi_reg_offsets** : const unsigned long[] (line 435)
- static **bcm6358_spi_reg_offsets** : const unsigned long[] (line 453)
- static **bcm63xx_spi_dev_match** : const struct platform_device_id[] (line 471)
- static **bcm63xx_spi_driver** : platform_driver (line 670)
- static **bcm63xx_spi_freq_table** : const unsigned int[][2] (line 176)
- static **bcm63xx_spi_of_match** : const struct of_device_id[] (line 485)

## Macros (76)

- **BCM63XX_SPI_BUS_NUM** (line 132)
- **BCM63XX_SPI_MAX_CS** (line 131)
- **BCM63XX_SPI_MAX_PREPEND** (line 129)
- **MODEBITS** (line 215)
- **SPI_6348_CLK_CFG** (line 30)
- **SPI_6348_CMD** (line 25)
- **SPI_6348_FILL_BYTE** (line 31)
- **SPI_6348_INT_MASK** (line 28)
- **SPI_6348_INT_MASK_ST** (line 27)
- **SPI_6348_INT_STATUS** (line 26)
- **SPI_6348_MSG_CTL** (line 34)
- **SPI_6348_MSG_CTL_WIDTH** (line 35)
- **SPI_6348_MSG_DATA** (line 36)
- **SPI_6348_MSG_DATA_SIZE** (line 37)
- **SPI_6348_MSG_TAIL** (line 32)
- **SPI_6348_MSG_TYPE_SHIFT** (line 66)
- **SPI_6348_RSET_SIZE** (line 24)
- **SPI_6348_RX_DATA** (line 38)
- **SPI_6348_RX_DATA_SIZE** (line 39)
- **SPI_6348_RX_TAIL** (line 33)
- **SPI_6348_ST** (line 29)
- **SPI_6358_CLK_CFG** (line 54)
- **SPI_6358_CMD** (line 49)
- **SPI_6358_FILL_BYTE** (line 55)
- **SPI_6358_INT_MASK** (line 52)
- **SPI_6358_INT_MASK_ST** (line 51)
- **SPI_6358_INT_STATUS** (line 50)
- **SPI_6358_MSG_CTL** (line 43)
- **SPI_6358_MSG_CTL_WIDTH** (line 44)
- **SPI_6358_MSG_DATA** (line 45)
- **SPI_6358_MSG_DATA_SIZE** (line 46)
- **SPI_6358_MSG_TAIL** (line 56)
- **SPI_6358_MSG_TYPE_SHIFT** (line 67)
- **SPI_6358_RSET_SIZE** (line 42)
- **SPI_6358_RX_DATA** (line 47)
- **SPI_6358_RX_DATA_SIZE** (line 48)
- **SPI_6358_RX_TAIL** (line 57)
- **SPI_6358_ST** (line 53)
- **SPI_BYTE_CNT_SHIFT** (line 65)
- **SPI_BYTE_SWAP** (line 109)
- **SPI_CLK_0_391MHZ** (line 100)
- **SPI_CLK_0_781MHZ** (line 101)
- **SPI_CLK_12_50MHZ** (line 105)
- **SPI_CLK_1_563MHZ** (line 102)
- **SPI_CLK_20MHZ** (line 99)
- **SPI_CLK_3_125MHZ** (line 103)
- **SPI_CLK_6_250MHZ** (line 104)
- **SPI_CLK_MASK** (line 106)
- **SPI_CMD_BUSY** (line 95)
- **SPI_CMD_COMMAND_MASK** (line 75)
- **SPI_CMD_COMMAND_SHIFT** (line 74)
- **SPI_CMD_DEVICE_ID_SHIFT** (line 76)
- **SPI_CMD_HARD_RESET** (line 72)
- **SPI_CMD_NOOP** (line 70)
- **SPI_CMD_ONE_BYTE_SHIFT** (line 78)
- **SPI_CMD_ONE_WIRE_SHIFT** (line 79)
- **SPI_CMD_PREPEND_BYTE_CNT_SHIFT** (line 77)
- **SPI_CMD_SOFT_RESET** (line 71)
- **SPI_CMD_START_IMMEDIATE** (line 73)
- **SPI_DEV_ID_0** (line 80)
- **SPI_DEV_ID_1** (line 81)
- **SPI_DEV_ID_2** (line 82)
- **SPI_DEV_ID_3** (line 83)
- **SPI_FD_RW** (line 62)
- **SPI_HD_R** (line 64)
- **SPI_HD_W** (line 63)
- **SPI_INTR_CLEAR_ALL** (line 91)
- **SPI_INTR_CMD_DONE** (line 86)
- **SPI_INTR_RX_OVERFLOW** (line 87)
- **SPI_INTR_RX_UNDERFLOW** (line 90)
- **SPI_INTR_TX_OVERFLOW** (line 89)
- **SPI_INTR_TX_UNDERFLOW** (line 88)
- **SPI_RX_EMPTY** (line 94)
- **SPI_SERIAL_BUSY** (line 96)
- **SPI_SSOFFTIME_MASK** (line 107)
- **SPI_SSOFFTIME_SHIFT** (line 108)
