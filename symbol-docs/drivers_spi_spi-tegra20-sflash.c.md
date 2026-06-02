# drivers/spi/spi-tegra20-sflash.c

Subsystem: drivers/spi

## Functions (17)

### handle_cpu_based_xfer
- Return type: static irqreturn_t
- Signature: handle_cpu_based_xfer(struct tegra_sflash_data * tsd)
- Line: 358

### tegra_sflash_calculate_curr_xfer_param
- Return type: static unsigned
- Signature: tegra_sflash_calculate_curr_xfer_param(struct spi_device * spi,struct tegra_sflash_data * tsd,struct spi_transfer * t)
- Line: 157

### tegra_sflash_clear_status
- Return type: static void
- Signature: tegra_sflash_clear_status(struct tegra_sflash_data * tsd)
- Line: 151

### tegra_sflash_fill_tx_fifo_from_client_txbuf
- Return type: static unsigned
- Signature: tegra_sflash_fill_tx_fifo_from_client_txbuf(struct tegra_sflash_data * tsd,struct spi_transfer * t)
- Line: 172

### tegra_sflash_isr
- Return type: static irqreturn_t
- Signature: tegra_sflash_isr(int irq,void * context_data)
- Line: 396

### tegra_sflash_probe
- Return type: static int
- Signature: tegra_sflash_probe(struct platform_device * pdev)
- Line: 417

### tegra_sflash_read_rx_fifo_to_client_rxbuf
- Return type: static int
- Signature: tegra_sflash_read_rx_fifo_to_client_rxbuf(struct tegra_sflash_data * tsd,struct spi_transfer * t)
- Line: 202

### tegra_sflash_readl
- Return type: static u32
- Signature: tegra_sflash_readl(struct tegra_sflash_data * tsd,unsigned long reg)
- Line: 139

### tegra_sflash_remove
- Return type: static void
- Signature: tegra_sflash_remove(struct platform_device * pdev)
- Line: 526

### tegra_sflash_resume
- Return type: static int
- Signature: tegra_sflash_resume(struct device * dev)
- Line: 552

### tegra_sflash_runtime_resume
- Return type: static int
- Signature: tegra_sflash_runtime_resume(struct device * dev)
- Line: 582

### tegra_sflash_runtime_suspend
- Return type: static int
- Signature: tegra_sflash_runtime_suspend(struct device * dev)
- Line: 570

### tegra_sflash_start_cpu_based_transfer
- Return type: static int
- Signature: tegra_sflash_start_cpu_based_transfer(struct tegra_sflash_data * tsd,struct spi_transfer * t)
- Line: 223

### tegra_sflash_start_transfer_one
- Return type: static int
- Signature: tegra_sflash_start_transfer_one(struct spi_device * spi,struct spi_transfer * t,bool is_first_of_msg,bool is_single_xfer)
- Line: 250

### tegra_sflash_suspend
- Return type: static int
- Signature: tegra_sflash_suspend(struct device * dev)
- Line: 545

### tegra_sflash_transfer_one_message
- Return type: static int
- Signature: tegra_sflash_transfer_one_message(struct spi_controller * host,struct spi_message * msg)
- Line: 306

### tegra_sflash_writel
- Return type: static void
- Signature: tegra_sflash_writel(struct tegra_sflash_data * tsd,u32 val,unsigned long reg)
- Line: 145

## Structs (1)

### tegra_sflash_data
- Line: 103
- Members:
  - dev: device *
  - host: spi_controller *
  - lock: spinlock_t
  - clk: clk *
  - rst: reset_control *
  - base: void __iomem *
  - irq: unsigned
  - cur_speed: u32
  - cur_spi: spi_device *
  - cur_pos: unsigned
  - cur_len: unsigned
  - bytes_per_word: unsigned
  - cur_direction: unsigned
  - curr_xfer_words: unsigned
  - cur_rx_pos: unsigned
  - cur_tx_pos: unsigned
  - tx_status: u32
  - rx_status: u32
  - status_reg: u32
  - def_command_reg: u32
  - command_reg: u32
  - dma_control_reg: u32
  - xfer_completion: completion
  - curr_xfer: spi_transfer *

## Variables (3)

- static **slink_pm_ops** : const struct dev_pm_ops (line 596)
- static **tegra_sflash_driver** : platform_driver (line 601)
- static **tegra_sflash_of_match** : const struct of_device_id[] (line 411)

## Macros (65)

- **DATA_DIR_RX** (line 97)
- **DATA_DIR_TX** (line 96)
- **MAX_CHIP_SELECT** (line 99)
- **SPI_ACTIVE_SCLK_DRIVE_HIGH** (line 31)
- **SPI_ACTIVE_SCLK_DRIVE_LOW** (line 30)
- **SPI_ACTIVE_SCLK_MASK** (line 29)
- **SPI_ACTIVE_SCLK_PULL_HIGH** (line 33)
- **SPI_ACTIVE_SCLK_PULL_LOW** (line 32)
- **SPI_ACTIVE_SDA** (line 38)
- **SPI_ACTIVE_SDA_DRIVE_HIGH** (line 40)
- **SPI_ACTIVE_SDA_DRIVE_LOW** (line 39)
- **SPI_ACTIVE_SDA_PULL_HIGH** (line 42)
- **SPI_ACTIVE_SDA_PULL_LOW** (line 41)
- **SPI_BIT_LENGTH**(x) (line 59)
- **SPI_BLK_CNT**(count) (line 74)
- **SPI_BSY** (line 64)
- **SPI_CK_SDA_FALLING** (line 35)
- **SPI_CK_SDA_MASK** (line 37)
- **SPI_CK_SDA_RISING** (line 36)
- **SPI_COMMAND** (line 26)
- **SPI_CS0_EN** (line 55)
- **SPI_CS1_EN** (line 54)
- **SPI_CS2_EN** (line 53)
- **SPI_CS3_EN** (line 52)
- **SPI_CS_DELAY_MASK** (line 51)
- **SPI_CS_HW** (line 50)
- **SPI_CS_MASK** (line 57)
- **SPI_CS_POL_INVERT** (line 44)
- **SPI_CS_SW** (line 49)
- **SPI_CS_VAL_HIGH** (line 47)
- **SPI_CS_VAL_LOW** (line 48)
- **SPI_DMA_BLK_COUNT**(count) (line 91)
- **SPI_DMA_CTL** (line 80)
- **SPI_DMA_EN** (line 81)
- **SPI_DMA_TIMEOUT** (line 101)
- **SPI_FIFO_DEPTH** (line 100)
- **SPI_FIFO_EMPTY** (line 77)
- **SPI_FIFO_ERROR** (line 76)
- **SPI_GO** (line 27)
- **SPI_IE_RXC** (line 82)
- **SPI_IE_TXC** (line 83)
- **SPI_MODES** (line 61)
- **SPI_M_S** (line 28)
- **SPI_PACKED** (line 84)
- **SPI_RDY** (line 65)
- **SPI_RXF_EMPTY** (line 70)
- **SPI_RXF_FLUSH** (line 67)
- **SPI_RXF_FULL** (line 71)
- **SPI_RX_CMP** (line 79)
- **SPI_RX_EN** (line 46)
- **SPI_RX_FIFO** (line 94)
- **SPI_RX_TRIG_1W** (line 86)
- **SPI_RX_TRIG_4W** (line 87)
- **SPI_RX_TRIG_MASK** (line 85)
- **SPI_RX_UNF** (line 68)
- **SPI_STATUS** (line 63)
- **SPI_TXF_EMPTY** (line 72)
- **SPI_TXF_FLUSH** (line 66)
- **SPI_TXF_FULL** (line 73)
- **SPI_TX_EN** (line 45)
- **SPI_TX_FIFO** (line 93)
- **SPI_TX_OVF** (line 69)
- **SPI_TX_TRIG_1W** (line 89)
- **SPI_TX_TRIG_4W** (line 90)
- **SPI_TX_TRIG_MASK** (line 88)
