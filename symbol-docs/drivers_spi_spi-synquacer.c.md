# drivers/spi/spi-synquacer.c

Subsystem: drivers/spi

## Functions (13)

### read_fifo
- Return type: static int
- Signature: read_fifo(struct synquacer_spi * sspi)
- Line: 141

### sq_spi_rx_handler
- Return type: static irqreturn_t
- Signature: sq_spi_rx_handler(int irq,void * priv)
- Line: 562

### sq_spi_tx_handler
- Return type: static irqreturn_t
- Signature: sq_spi_tx_handler(int irq,void * priv)
- Line: 582

### synquacer_spi_config
- Return type: static int
- Signature: synquacer_spi_config(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 228

### synquacer_spi_enable
- Return type: static int
- Signature: synquacer_spi_enable(struct spi_controller * host)
- Line: 520

### synquacer_spi_probe
- Return type: static int
- Signature: synquacer_spi_probe(struct platform_device * pdev)
- Line: 601

### synquacer_spi_remove
- Return type: static void
- Signature: synquacer_spi_remove(struct platform_device * pdev)
- Line: 735

### synquacer_spi_resume
- Return type: static int __maybe_unused
- Signature: synquacer_spi_resume(struct device * dev)
- Line: 767

### synquacer_spi_set_cs
- Return type: static void
- Signature: synquacer_spi_set_cs(struct spi_device * spi,bool enable)
- Line: 483

### synquacer_spi_suspend
- Return type: static int __maybe_unused
- Signature: synquacer_spi_suspend(struct device * dev)
- Line: 751

### synquacer_spi_transfer_one
- Return type: static int
- Signature: synquacer_spi_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 353

### synquacer_spi_wait_status_update
- Return type: static int
- Signature: synquacer_spi_wait_status_update(struct synquacer_spi * sspi,bool enable)
- Line: 499

### write_fifo
- Return type: static int
- Signature: write_fifo(struct synquacer_spi * sspi)
- Line: 184

## Structs (1)

### synquacer_spi
- Line: 121
- Members:
  - dev: device *
  - transfer_done: completion
  - cs: unsigned int
  - bpw: unsigned int
  - mode: unsigned int
  - speed: unsigned int
  - aces: bool
  - rtm: bool
  - rx_buf: void *
  - tx_buf: const void *
  - clk: clk *
  - clk_src_type: int
  - regs: void __iomem *
  - rx_words: u32
  - tx_words: u32
  - bus_width: unsigned int
  - transfer_mode: unsigned int
  - rx_irq_name: char[]
  - tx_irq_name: char[]

## Variables (3)

- static **synquacer_hsspi_acpi_ids** : const struct acpi_device_id[] (line 809)
- static **synquacer_spi_driver** : platform_driver (line 816)
- static **synquacer_spi_of_match** : const struct of_device_id[] (line 802)

## Macros (80)

- **SYNQUACER_HSSPI_CLOCK_SRC_IHCLK** (line 115)
- **SYNQUACER_HSSPI_CLOCK_SRC_IPCLK** (line 116)
- **SYNQUACER_HSSPI_DMCFG_MSTARTEN** (line 78)
- **SYNQUACER_HSSPI_DMCFG_SSDC** (line 77)
- **SYNQUACER_HSSPI_DMPSEL_CS_MASK** (line 82)
- **SYNQUACER_HSSPI_DMPSEL_CS_SHIFT** (line 83)
- **SYNQUACER_HSSPI_DMSTART_START** (line 80)
- **SYNQUACER_HSSPI_DMSTATUS_RX_DATA_MASK** (line 91)
- **SYNQUACER_HSSPI_DMSTATUS_RX_DATA_SHIFT** (line 92)
- **SYNQUACER_HSSPI_DMSTATUS_TX_DATA_MASK** (line 93)
- **SYNQUACER_HSSPI_DMSTATUS_TX_DATA_SHIFT** (line 94)
- **SYNQUACER_HSSPI_DMSTOP_STOP** (line 81)
- **SYNQUACER_HSSPI_DMTRP_BUS_WIDTH_SHIFT** (line 84)
- **SYNQUACER_HSSPI_DMTRP_DATA_MASK** (line 85)
- **SYNQUACER_HSSPI_DMTRP_DATA_RX** (line 88)
- **SYNQUACER_HSSPI_DMTRP_DATA_SHIFT** (line 86)
- **SYNQUACER_HSSPI_DMTRP_DATA_TX** (line 89)
- **SYNQUACER_HSSPI_DMTRP_DATA_TXRX** (line 87)
- **SYNQUACER_HSSPI_ENABLE_TMOUT_MSEC** (line 113)
- **SYNQUACER_HSSPI_FIFOCFG_FIFO_WIDTH_MASK** (line 100)
- **SYNQUACER_HSSPI_FIFOCFG_FIFO_WIDTH_SHIFT** (line 101)
- **SYNQUACER_HSSPI_FIFOCFG_RX_FLUSH** (line 102)
- **SYNQUACER_HSSPI_FIFOCFG_RX_THRESHOLD_MASK** (line 96)
- **SYNQUACER_HSSPI_FIFOCFG_RX_THRESHOLD_SHIFT** (line 97)
- **SYNQUACER_HSSPI_FIFOCFG_TX_FLUSH** (line 103)
- **SYNQUACER_HSSPI_FIFOCFG_TX_THRESHOLD_MASK** (line 98)
- **SYNQUACER_HSSPI_FIFOCFG_TX_THRESHOLD_SHIFT** (line 99)
- **SYNQUACER_HSSPI_FIFO_DEPTH** (line 105)
- **SYNQUACER_HSSPI_FIFO_RX_THRESHOLD** (line 107)
- **SYNQUACER_HSSPI_FIFO_TX_THRESHOLD** (line 106)
- **SYNQUACER_HSSPI_IRQ_NAME_MAX** (line 119)
- **SYNQUACER_HSSPI_MCTRL_CDSS** (line 47)
- **SYNQUACER_HSSPI_MCTRL_COMMAND_SEQUENCE_EN** (line 46)
- **SYNQUACER_HSSPI_MCTRL_MEN** (line 45)
- **SYNQUACER_HSSPI_MCTRL_MES** (line 48)
- **SYNQUACER_HSSPI_MCTRL_SYNCON** (line 49)
- **SYNQUACER_HSSPI_NUM_CHIP_SELECT** (line 118)
- **SYNQUACER_HSSPI_PCC_ACES** (line 53)
- **SYNQUACER_HSSPI_PCC_CDRS_MASK** (line 60)
- **SYNQUACER_HSSPI_PCC_CDRS_SHIFT** (line 61)
- **SYNQUACER_HSSPI_PCC_CPHA** (line 51)
- **SYNQUACER_HSSPI_PCC_CPOL** (line 52)
- **SYNQUACER_HSSPI_PCC_RTM** (line 54)
- **SYNQUACER_HSSPI_PCC_SAFESYNC** (line 58)
- **SYNQUACER_HSSPI_PCC_SDIR** (line 56)
- **SYNQUACER_HSSPI_PCC_SENDIAN** (line 57)
- **SYNQUACER_HSSPI_PCC_SS2CD_SHIFT** (line 59)
- **SYNQUACER_HSSPI_PCC_SSPOL** (line 55)
- **SYNQUACER_HSSPI_REG_DMBCC** (line 37)
- **SYNQUACER_HSSPI_REG_DMCFG** (line 35)
- **SYNQUACER_HSSPI_REG_DMSTART** (line 36)
- **SYNQUACER_HSSPI_REG_DMSTATUS** (line 38)
- **SYNQUACER_HSSPI_REG_FAULTC** (line 34)
- **SYNQUACER_HSSPI_REG_FAULTF** (line 33)
- **SYNQUACER_HSSPI_REG_FIFOCFG** (line 39)
- **SYNQUACER_HSSPI_REG_MCTRL** (line 24)
- **SYNQUACER_HSSPI_REG_MID** (line 42)
- **SYNQUACER_HSSPI_REG_PCC**(n) (line 26)
- **SYNQUACER_HSSPI_REG_PCC0** (line 25)
- **SYNQUACER_HSSPI_REG_RXC** (line 32)
- **SYNQUACER_HSSPI_REG_RXE** (line 31)
- **SYNQUACER_HSSPI_REG_RXF** (line 30)
- **SYNQUACER_HSSPI_REG_RX_FIFO** (line 41)
- **SYNQUACER_HSSPI_REG_TXC** (line 29)
- **SYNQUACER_HSSPI_REG_TXE** (line 28)
- **SYNQUACER_HSSPI_REG_TXF** (line 27)
- **SYNQUACER_HSSPI_REG_TX_FIFO** (line 40)
- **SYNQUACER_HSSPI_RXE_FIFO_MORE_THAN_THRESHOLD** (line 74)
- **SYNQUACER_HSSPI_RXE_SLAVE_RELEASED** (line 75)
- **SYNQUACER_HSSPI_RXF_FIFO_MORE_THAN_THRESHOLD** (line 71)
- **SYNQUACER_HSSPI_RXF_SLAVE_RELEASED** (line 72)
- **SYNQUACER_HSSPI_TRANSFER_MODE_RX** (line 111)
- **SYNQUACER_HSSPI_TRANSFER_MODE_TX** (line 110)
- **SYNQUACER_HSSPI_TRANSFER_TMOUT_MSEC** (line 112)
- **SYNQUACER_HSSPI_TXE_FIFO_EMPTY** (line 68)
- **SYNQUACER_HSSPI_TXE_FIFO_FULL** (line 67)
- **SYNQUACER_HSSPI_TXE_SLAVE_RELEASED** (line 69)
- **SYNQUACER_HSSPI_TXF_FIFO_EMPTY** (line 64)
- **SYNQUACER_HSSPI_TXF_FIFO_FULL** (line 63)
- **SYNQUACER_HSSPI_TXF_SLAVE_RELEASED** (line 65)
