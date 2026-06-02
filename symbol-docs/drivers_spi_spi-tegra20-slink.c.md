# drivers/spi/spi-tegra20-slink.c

Subsystem: drivers/spi

## Functions (31)

### handle_cpu_based_xfer
- Return type: static irqreturn_t
- Signature: handle_cpu_based_xfer(struct tegra_slink_data * tspi)
- Line: 839

### handle_dma_based_xfer
- Return type: static irqreturn_t
- Signature: handle_dma_based_xfer(struct tegra_slink_data * tspi)
- Line: 879

### tegra_slink_calculate_curr_xfer_param
- Return type: static unsigned
- Signature: tegra_slink_calculate_curr_xfer_param(struct spi_device * spi,struct tegra_slink_data * tspi,struct spi_transfer * t)
- Line: 253

### tegra_slink_clear_status
- Return type: static void
- Signature: tegra_slink_clear_status(struct tegra_slink_data * tspi)
- Line: 225

### tegra_slink_copy_client_txbuf_to_spi_txbuf
- Return type: static void
- Signature: tegra_slink_copy_client_txbuf_to_spi_txbuf(struct tegra_slink_data * tspi,struct spi_transfer * t)
- Line: 363

### tegra_slink_copy_spi_rxbuf_to_client_rxbuf
- Return type: static void
- Signature: tegra_slink_copy_spi_rxbuf_to_client_rxbuf(struct tegra_slink_data * tspi,struct spi_transfer * t)
- Line: 394

### tegra_slink_deinit_dma_param
- Return type: static void
- Signature: tegra_slink_deinit_dma_param(struct tegra_slink_data * tspi,bool dma_to_memory)
- Line: 644

### tegra_slink_dma_complete
- Return type: static void
- Signature: tegra_slink_dma_complete(void * args)
- Line: 425

### tegra_slink_fill_tx_fifo_from_client_txbuf
- Return type: static unsigned
- Signature: tegra_slink_fill_tx_fifo_from_client_txbuf(struct tegra_slink_data * tspi,struct spi_transfer * t)
- Line: 288

### tegra_slink_get_packed_size
- Return type: static u32
- Signature: tegra_slink_get_packed_size(struct tegra_slink_data * tspi,struct spi_transfer * t)
- Line: 236

### tegra_slink_init_dma_param
- Return type: static int
- Signature: tegra_slink_init_dma_param(struct tegra_slink_data * tspi,bool dma_to_memory)
- Line: 592

### tegra_slink_isr
- Return type: static irqreturn_t
- Signature: tegra_slink_isr(int irq,void * context_data)
- Line: 968

### tegra_slink_isr_thread
- Return type: static irqreturn_t
- Signature: tegra_slink_isr_thread(int irq,void * context_data)
- Line: 959

### tegra_slink_prepare_message
- Return type: static int
- Signature: tegra_slink_prepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 771

### tegra_slink_probe
- Return type: static int
- Signature: tegra_slink_probe(struct platform_device * pdev)
- Line: 1000

### tegra_slink_read_rx_fifo_to_client_rxbuf
- Return type: static unsigned int
- Signature: tegra_slink_read_rx_fifo_to_client_rxbuf(struct tegra_slink_data * tspi,struct spi_transfer * t)
- Line: 330

### tegra_slink_readl
- Return type: static u32
- Signature: tegra_slink_readl(struct tegra_slink_data * tspi,unsigned long reg)
- Line: 209

### tegra_slink_remove
- Return type: static void
- Signature: tegra_slink_remove(struct platform_device * pdev)
- Line: 1129

### tegra_slink_resume
- Return type: static int
- Signature: tegra_slink_resume(struct device * dev)
- Line: 1155

### tegra_slink_runtime_resume
- Return type: static int __maybe_unused
- Signature: tegra_slink_runtime_resume(struct device * dev)
- Line: 1186

### tegra_slink_runtime_suspend
- Return type: static int __maybe_unused
- Signature: tegra_slink_runtime_suspend(struct device * dev)
- Line: 1174

### tegra_slink_setup
- Return type: static int
- Signature: tegra_slink_setup(struct spi_device * spi)
- Line: 731

### tegra_slink_start_cpu_based_transfer
- Return type: static int
- Signature: tegra_slink_start_cpu_based_transfer(struct tegra_slink_data * tspi,struct spi_transfer * t)
- Line: 555

### tegra_slink_start_dma_based_transfer
- Return type: static int
- Signature: tegra_slink_start_dma_based_transfer(struct tegra_slink_data * tspi,struct spi_transfer * t)
- Line: 470

### tegra_slink_start_rx_dma
- Return type: static int
- Signature: tegra_slink_start_rx_dma(struct tegra_slink_data * tspi,int len)
- Line: 451

### tegra_slink_start_transfer_one
- Return type: static int
- Signature: tegra_slink_start_transfer_one(struct spi_device * spi,struct spi_transfer * t)
- Line: 671

### tegra_slink_start_tx_dma
- Return type: static int
- Signature: tegra_slink_start_tx_dma(struct tegra_slink_data * tspi,int len)
- Line: 432

### tegra_slink_suspend
- Return type: static int
- Signature: tegra_slink_suspend(struct device * dev)
- Line: 1148

### tegra_slink_transfer_one
- Return type: static int
- Signature: tegra_slink_transfer_one(struct spi_controller * host,struct spi_device * spi,struct spi_transfer * xfer)
- Line: 797

### tegra_slink_unprepare_message
- Return type: static int
- Signature: tegra_slink_unprepare_message(struct spi_controller * host,struct spi_message * msg)
- Line: 828

### tegra_slink_writel
- Return type: static void
- Signature: tegra_slink_writel(struct tegra_slink_data * tspi,u32 val,unsigned long reg)
- Line: 215

## Structs (2)

### tegra_slink_chip_data
- Line: 149
- Members:
  - cs_hold_time: bool
  - dev: device *
  - host: spi_controller *
  - chip_data: const struct tegra_slink_chip_data *
  - lock: spinlock_t
  - clk: clk *
  - rst: reset_control *
  - base: void __iomem *
  - phys: phys_addr_t
  - irq: unsigned
  - cur_speed: u32
  - cur_spi: spi_device *
  - cur_pos: unsigned
  - cur_len: unsigned
  - words_per_32bit: unsigned
  - bytes_per_word: unsigned
  - curr_dma_words: unsigned
  - cur_direction: unsigned
  - cur_rx_pos: unsigned
  - cur_tx_pos: unsigned
  - dma_buf_size: unsigned
  - max_buf_size: unsigned
  - is_curr_dma_xfer: bool
  - rx_dma_complete: completion
  - tx_dma_complete: completion
  - tx_status: u32
  - rx_status: u32
  - status_reg: u32
  - is_packed: bool
  - packed_size: u32
  - command_reg: u32
  - command2_reg: u32
  - dma_control_reg: u32
  - def_command_reg: u32
  - def_command2_reg: u32
  - xfer_completion: completion
  - curr_xfer: spi_transfer *
  - rx_dma_chan: dma_chan *
  - rx_dma_buf: u32 *
  - rx_dma_phys: dma_addr_t
  - rx_dma_desc: dma_async_tx_descriptor *
  - tx_dma_chan: dma_chan *
  - tx_dma_buf: u32 *
  - tx_dma_phys: dma_addr_t
  - tx_dma_desc: dma_async_tx_descriptor *

### tegra_slink_data
- Line: 153
- Members:
  - cs_hold_time: bool
  - dev: device *
  - host: spi_controller *
  - chip_data: const struct tegra_slink_chip_data *
  - lock: spinlock_t
  - clk: clk *
  - rst: reset_control *
  - base: void __iomem *
  - phys: phys_addr_t
  - irq: unsigned
  - cur_speed: u32
  - cur_spi: spi_device *
  - cur_pos: unsigned
  - cur_len: unsigned
  - words_per_32bit: unsigned
  - bytes_per_word: unsigned
  - curr_dma_words: unsigned
  - cur_direction: unsigned
  - cur_rx_pos: unsigned
  - cur_tx_pos: unsigned
  - dma_buf_size: unsigned
  - max_buf_size: unsigned
  - is_curr_dma_xfer: bool
  - rx_dma_complete: completion
  - tx_dma_complete: completion
  - tx_status: u32
  - rx_status: u32
  - status_reg: u32
  - is_packed: bool
  - packed_size: u32
  - command_reg: u32
  - command2_reg: u32
  - dma_control_reg: u32
  - def_command_reg: u32
  - def_command2_reg: u32
  - xfer_completion: completion
  - curr_xfer: spi_transfer *
  - rx_dma_chan: dma_chan *
  - rx_dma_buf: u32 *
  - rx_dma_phys: dma_addr_t
  - rx_dma_desc: dma_async_tx_descriptor *
  - tx_dma_chan: dma_chan *
  - tx_dma_buf: u32 *
  - tx_dma_phys: dma_addr_t
  - tx_dma_desc: dma_async_tx_descriptor *

## Variables (5)

- static **slink_pm_ops** : const struct dev_pm_ops (line 1200)
- static **tegra20_spi_cdata** : const struct tegra_slink_chip_data (line 989)
- static **tegra30_spi_cdata** : const struct tegra_slink_chip_data (line 985)
- static **tegra_slink_driver** : platform_driver (line 1205)
- static **tegra_slink_of_match** : const struct of_device_id[] (line 993)

## Macros (104)

- **DATA_DIR_RX** (line 135)
- **DATA_DIR_TX** (line 134)
- **DEFAULT_SPI_DMA_BUF_LEN** (line 139)
- **MAX_CHIP_SELECT** (line 146)
- **RX_FIFO_FULL_COUNT_ZERO** (line 141)
- **SLINK_BIDIROE** (line 61)
- **SLINK_BIT_LENGTH**(x) (line 30)
- **SLINK_BLK_CNT**(val) (line 80)
- **SLINK_BOTH_EN** (line 32)
- **SLINK_BSY** (line 95)
- **SLINK_CK_SDA** (line 42)
- **SLINK_COMMAND** (line 29)
- **SLINK_COMMAND2** (line 57)
- **SLINK_COUNT**(val) (line 78)
- **SLINK_CS_ACTIVE_BETWEEN** (line 64)
- **SLINK_CS_POLARITY** (line 35)
- **SLINK_CS_POLARITY1** (line 41)
- **SLINK_CS_POLARITY2** (line 43)
- **SLINK_CS_POLARITY3** (line 44)
- **SLINK_CS_SW** (line 33)
- **SLINK_CS_VALUE** (line 34)
- **SLINK_DMA_BLOCK_SIZE**(x) (line 105)
- **SLINK_DMA_CTL** (line 104)
- **SLINK_DMA_EN** (line 124)
- **SLINK_DMA_TIMEOUT** (line 137)
- **SLINK_ENB** (line 53)
- **SLINK_ERR** (line 93)
- **SLINK_FIFO_DEPTH** (line 147)
- **SLINK_FIFO_EMPTY** (line 99)
- **SLINK_FIFO_ERROR** (line 96)
- **SLINK_FIFO_REFILLS_0** (line 67)
- **SLINK_FIFO_REFILLS_1** (line 68)
- **SLINK_FIFO_REFILLS_2** (line 69)
- **SLINK_FIFO_REFILLS_3** (line 70)
- **SLINK_FIFO_REFILLS_MASK** (line 71)
- **SLINK_GO** (line 52)
- **SLINK_IDLE_SCLK_DRIVE_HIGH** (line 46)
- **SLINK_IDLE_SCLK_DRIVE_LOW** (line 45)
- **SLINK_IDLE_SCLK_MASK** (line 49)
- **SLINK_IDLE_SCLK_PULL_HIGH** (line 48)
- **SLINK_IDLE_SCLK_PULL_LOW** (line 47)
- **SLINK_IDLE_SDA_DRIVE_HIGH** (line 37)
- **SLINK_IDLE_SDA_DRIVE_LOW** (line 36)
- **SLINK_IDLE_SDA_MASK** (line 40)
- **SLINK_IDLE_SDA_PULL_HIGH** (line 39)
- **SLINK_IDLE_SDA_PULL_LOW** (line 38)
- **SLINK_IE_RXC** (line 123)
- **SLINK_IE_TXC** (line 122)
- **SLINK_INT_SIZE**(x) (line 63)
- **SLINK_LSBFE** (line 58)
- **SLINK_MAS_DATA** (line 101)
- **SLINK_MODES** (line 55)
- **SLINK_MODF** (line 81)
- **SLINK_MODFEN** (line 62)
- **SLINK_M_S** (line 50)
- **SLINK_PACKED** (line 116)
- **SLINK_PACK_SIZE_16** (line 119)
- **SLINK_PACK_SIZE_32** (line 120)
- **SLINK_PACK_SIZE_4** (line 117)
- **SLINK_PACK_SIZE_8** (line 118)
- **SLINK_PACK_SIZE_MASK** (line 121)
- **SLINK_RDY** (line 94)
- **SLINK_RXEN** (line 75)
- **SLINK_RX_EMPTY** (line 87)
- **SLINK_RX_FIFO** (line 132)
- **SLINK_RX_FIFO_FULL_COUNT**(val) (line 128)
- **SLINK_RX_FLUSH** (line 91)
- **SLINK_RX_FULL** (line 86)
- **SLINK_RX_OVF** (line 89)
- **SLINK_RX_TRIG_1** (line 111)
- **SLINK_RX_TRIG_16** (line 114)
- **SLINK_RX_TRIG_4** (line 112)
- **SLINK_RX_TRIG_8** (line 113)
- **SLINK_RX_TRIG_MASK** (line 115)
- **SLINK_RX_UNF** (line 82)
- **SLINK_SCLK** (line 92)
- **SLINK_SLAVE_DATA** (line 102)
- **SLINK_SPC0** (line 73)
- **SLINK_SPIE** (line 60)
- **SLINK_SSOE** (line 59)
- **SLINK_SS_EN_CS**(x) (line 65)
- **SLINK_SS_HOLD_TIME**(val) (line 129)
- **SLINK_SS_SETUP**(x) (line 66)
- **SLINK_STATUS** (line 77)
- **SLINK_STATUS2** (line 126)
- **SLINK_STATUS2_RESET** (line 143)
- **SLINK_TXEN** (line 74)
- **SLINK_TX_EMPTY** (line 85)
- **SLINK_TX_FIFO** (line 131)
- **SLINK_TX_FIFO_EMPTY_COUNT**(val) (line 127)
- **SLINK_TX_FLUSH** (line 90)
- **SLINK_TX_FULL** (line 84)
- **SLINK_TX_OVF** (line 83)
- **SLINK_TX_TRIG_1** (line 106)
- **SLINK_TX_TRIG_16** (line 109)
- **SLINK_TX_TRIG_4** (line 107)
- **SLINK_TX_TRIG_8** (line 108)
- **SLINK_TX_TRIG_MASK** (line 110)
- **SLINK_TX_UNF** (line 88)
- **SLINK_WAIT** (line 51)
- **SLINK_WAIT_PACK_INT**(x) (line 72)
- **SLINK_WORD**(val) (line 79)
- **SLINK_WORD_SIZE**(x) (line 31)
- **TX_FIFO_EMPTY_COUNT_MAX** (line 140)
