# drivers/spi/spi-tegra114.c

Subsystem: drivers/spi

## Functions (35)

### handle_cpu_based_xfer
- Return type: static irqreturn_t
- Signature: handle_cpu_based_xfer(struct tegra_spi_data * tspi)
- Line: 1122

### handle_dma_based_xfer
- Return type: static irqreturn_t
- Signature: handle_dma_based_xfer(struct tegra_spi_data * tspi)
- Line: 1163

### tegra_spi_calculate_curr_xfer_param
- Return type: static unsigned
- Signature: tegra_spi_calculate_curr_xfer_param(struct spi_device * spi,struct tegra_spi_data * tspi,struct spi_transfer * t)
- Line: 257

### tegra_spi_cleanup
- Return type: static void
- Signature: tegra_spi_cleanup(struct spi_device * spi)
- Line: 934

### tegra_spi_clear_status
- Return type: static void
- Signature: tegra_spi_clear_status(struct tegra_spi_data * tspi)
- Line: 242

### tegra_spi_copy_client_txbuf_to_spi_txbuf
- Return type: static void
- Signature: tegra_spi_copy_client_txbuf_to_spi_txbuf(struct tegra_spi_data * tspi,struct spi_transfer * t)
- Line: 387

### tegra_spi_copy_spi_rxbuf_to_client_rxbuf
- Return type: static void
- Signature: tegra_spi_copy_spi_rxbuf_to_client_rxbuf(struct tegra_spi_data * tspi,struct spi_transfer * t)
- Line: 426

### tegra_spi_deinit_dma_param
- Return type: static void
- Signature: tegra_spi_deinit_dma_param(struct tegra_spi_data * tspi,bool dma_to_memory)
- Line: 692

### tegra_spi_dma_complete
- Return type: static void
- Signature: tegra_spi_dma_complete(void * args)
- Line: 465

### tegra_spi_dump_regs
- Return type: static void
- Signature: tegra_spi_dump_regs(struct tegra_spi_data * tspi)
- Line: 1017

### tegra_spi_fill_tx_fifo_from_client_txbuf
- Return type: static unsigned
- Signature: tegra_spi_fill_tx_fifo_from_client_txbuf(struct tegra_spi_data * tspi,struct spi_transfer * t)
- Line: 291

### tegra_spi_flush_fifos
- Return type: static int
- Signature: tegra_spi_flush_fifos(struct tegra_spi_data * tspi)
- Line: 510

### tegra_spi_init_dma_param
- Return type: static int
- Signature: tegra_spi_init_dma_param(struct tegra_spi_data * tspi,bool dma_to_memory)
- Line: 660

### tegra_spi_isr
- Return type: static irqreturn_t
- Signature: tegra_spi_isr(int irq,void * context_data)
- Line: 1253

### tegra_spi_isr_thread
- Return type: static irqreturn_t
- Signature: tegra_spi_isr_thread(int irq,void * context_data)
- Line: 1244

### tegra_spi_parse_cdata_dt
- Return type: static tegra_spi_client_data *
- Signature: tegra_spi_parse_cdata_dt(struct spi_device * spi)
- Line: 912

### tegra_spi_probe
- Return type: static int
- Signature: tegra_spi_probe(struct platform_device * pdev)
- Line: 1297

### tegra_spi_read_rx_fifo_to_client_rxbuf
- Return type: static unsigned int
- Signature: tegra_spi_read_rx_fifo_to_client_rxbuf(struct tegra_spi_data * tspi,struct spi_transfer * t)
- Line: 343

### tegra_spi_readl
- Return type: static u32
- Signature: tegra_spi_readl(struct tegra_spi_data * tspi,unsigned long reg)
- Line: 226

### tegra_spi_remove
- Return type: static void
- Signature: tegra_spi_remove(struct platform_device * pdev)
- Line: 1439

### tegra_spi_resume
- Return type: static int
- Signature: tegra_spi_resume(struct device * dev)
- Line: 1471

### tegra_spi_runtime_resume
- Return type: static int
- Signature: tegra_spi_runtime_resume(struct device * dev)
- Line: 1503

### tegra_spi_runtime_suspend
- Return type: static int
- Signature: tegra_spi_runtime_suspend(struct device * dev)
- Line: 1491

### tegra_spi_set_hw_cs_timing
- Return type: static int
- Signature: tegra_spi_set_hw_cs_timing(struct spi_device * spi)
- Line: 719

### tegra_spi_setup
- Return type: static int
- Signature: tegra_spi_setup(struct spi_device * spi)
- Line: 943

### tegra_spi_setup_transfer_one
- Return type: static u32
- Signature: tegra_spi_setup_transfer_one(struct spi_device * spi,struct spi_transfer * t,bool is_first_of_msg,bool is_single_xfer)
- Line: 770

### tegra_spi_start_cpu_based_transfer
- Return type: static int
- Signature: tegra_spi_start_cpu_based_transfer(struct tegra_spi_data * tspi,struct spi_transfer * t)
- Line: 628

### tegra_spi_start_dma_based_transfer
- Return type: static int
- Signature: tegra_spi_start_dma_based_transfer(struct tegra_spi_data * tspi,struct spi_transfer * t)
- Line: 534

### tegra_spi_start_rx_dma
- Return type: static int
- Signature: tegra_spi_start_rx_dma(struct tegra_spi_data * tspi,int len)
- Line: 491

### tegra_spi_start_transfer_one
- Return type: static int
- Signature: tegra_spi_start_transfer_one(struct spi_device * spi,struct spi_transfer * t,u32 command1)
- Line: 865

### tegra_spi_start_tx_dma
- Return type: static int
- Signature: tegra_spi_start_tx_dma(struct tegra_spi_data * tspi,int len)
- Line: 472

### tegra_spi_suspend
- Return type: static int
- Signature: tegra_spi_suspend(struct device * dev)
- Line: 1464

### tegra_spi_transfer_end
- Return type: static void
- Signature: tegra_spi_transfer_end(struct spi_device * spi)
- Line: 997

### tegra_spi_transfer_one_message
- Return type: static int
- Signature: tegra_spi_transfer_one_message(struct spi_controller * host,struct spi_message * msg)
- Line: 1031

### tegra_spi_writel
- Return type: static void
- Signature: tegra_spi_writel(struct tegra_spi_data * tspi,u32 val,unsigned long reg)
- Line: 232

## Structs (3)

### tegra_spi_client_data
- Line: 160
- Members:
  - has_intr_mask_reg: bool
  - tx_clk_tap_delay: int
  - rx_clk_tap_delay: int
  - dev: device *
  - host: spi_controller *
  - lock: spinlock_t
  - clk: clk *
  - rst: reset_control *
  - base: void __iomem *
  - phys: phys_addr_t
  - irq: unsigned
  - cur_speed: u32
  - cur_spi: spi_device *
  - cs_control: spi_device *
  - cur_pos: unsigned
  - words_per_32bit: unsigned
  - bytes_per_word: unsigned
  - curr_dma_words: unsigned
  - cur_direction: unsigned
  - cur_rx_pos: unsigned
  - cur_tx_pos: unsigned
  - dma_buf_size: unsigned
  - max_buf_size: unsigned
  - is_curr_dma_xfer: bool
  - use_hw_based_cs: bool
  - rx_dma_complete: completion
  - tx_dma_complete: completion
  - tx_status: u32
  - rx_status: u32
  - status_reg: u32
  - is_packed: bool
  - command1_reg: u32
  - dma_control_reg: u32
  - def_command1_reg: u32
  - def_command2_reg: u32
  - spi_cs_timing1: u32
  - spi_cs_timing2: u32
  - last_used_cs: u8
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
  - soc_data: const struct tegra_spi_soc_data *

### tegra_spi_data
- Line: 165
- Members:
  - has_intr_mask_reg: bool
  - tx_clk_tap_delay: int
  - rx_clk_tap_delay: int
  - dev: device *
  - host: spi_controller *
  - lock: spinlock_t
  - clk: clk *
  - rst: reset_control *
  - base: void __iomem *
  - phys: phys_addr_t
  - irq: unsigned
  - cur_speed: u32
  - cur_spi: spi_device *
  - cs_control: spi_device *
  - cur_pos: unsigned
  - words_per_32bit: unsigned
  - bytes_per_word: unsigned
  - curr_dma_words: unsigned
  - cur_direction: unsigned
  - cur_rx_pos: unsigned
  - cur_tx_pos: unsigned
  - dma_buf_size: unsigned
  - max_buf_size: unsigned
  - is_curr_dma_xfer: bool
  - use_hw_based_cs: bool
  - rx_dma_complete: completion
  - tx_dma_complete: completion
  - tx_status: u32
  - rx_status: u32
  - status_reg: u32
  - is_packed: bool
  - command1_reg: u32
  - dma_control_reg: u32
  - def_command1_reg: u32
  - def_command2_reg: u32
  - spi_cs_timing1: u32
  - spi_cs_timing2: u32
  - last_used_cs: u8
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
  - soc_data: const struct tegra_spi_soc_data *

### tegra_spi_soc_data
- Line: 156
- Members:
  - has_intr_mask_reg: bool
  - tx_clk_tap_delay: int
  - rx_clk_tap_delay: int
  - dev: device *
  - host: spi_controller *
  - lock: spinlock_t
  - clk: clk *
  - rst: reset_control *
  - base: void __iomem *
  - phys: phys_addr_t
  - irq: unsigned
  - cur_speed: u32
  - cur_spi: spi_device *
  - cs_control: spi_device *
  - cur_pos: unsigned
  - words_per_32bit: unsigned
  - bytes_per_word: unsigned
  - curr_dma_words: unsigned
  - cur_direction: unsigned
  - cur_rx_pos: unsigned
  - cur_tx_pos: unsigned
  - dma_buf_size: unsigned
  - max_buf_size: unsigned
  - is_curr_dma_xfer: bool
  - use_hw_based_cs: bool
  - rx_dma_complete: completion
  - tx_dma_complete: completion
  - tx_status: u32
  - rx_status: u32
  - status_reg: u32
  - is_packed: bool
  - command1_reg: u32
  - dma_control_reg: u32
  - def_command1_reg: u32
  - def_command2_reg: u32
  - spi_cs_timing1: u32
  - spi_cs_timing2: u32
  - last_used_cs: u8
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
  - soc_data: const struct tegra_spi_soc_data *

## Variables (6)

- static **tegra114_spi_soc_data** : tegra_spi_soc_data (line 1270)
- static **tegra124_spi_soc_data** : tegra_spi_soc_data (line 1274)
- static **tegra210_spi_soc_data** : tegra_spi_soc_data (line 1278)
- static **tegra_spi_driver** : platform_driver (line 1522)
- static **tegra_spi_of_match** : const struct of_device_id[] (line 1282)
- static **tegra_spi_pm_ops** : const struct dev_pm_ops (line 1517)

## Macros (108)

- **CS_ACTIVE_BETWEEN_PACKETS_0** (line 75)
- **CS_ACTIVE_BETWEEN_PACKETS_1** (line 77)
- **CS_ACTIVE_BETWEEN_PACKETS_2** (line 79)
- **CS_ACTIVE_BETWEEN_PACKETS_3** (line 81)
- **CYCLES_BETWEEN_PACKETS_0**(x) (line 74)
- **CYCLES_BETWEEN_PACKETS_1**(x) (line 76)
- **CYCLES_BETWEEN_PACKETS_2**(x) (line 78)
- **CYCLES_BETWEEN_PACKETS_3**(x) (line 80)
- **DATA_DIR_RX** (line 147)
- **DATA_DIR_TX** (line 146)
- **DEFAULT_SPI_DMA_BUF_LEN** (line 150)
- **MAX_CHIP_SELECT** (line 144)
- **MAX_HOLD_CYCLES** (line 153)
- **MAX_INACTIVE_CYCLES** (line 89)
- **MAX_SETUP_HOLD_CYCLES** (line 88)
- **RX_FIFO_FULL_COUNT_ZERO** (line 152)
- **SPI_BIDIROE** (line 35)
- **SPI_BIT_LENGTH**(x) (line 27)
- **SPI_BLK_CNT**(val) (line 92)
- **SPI_BOTH_EN_BIT** (line 32)
- **SPI_BOTH_EN_BYTE** (line 31)
- **SPI_COMMAND1** (line 26)
- **SPI_COMMAND2** (line 63)
- **SPI_CONT** (line 133)
- **SPI_CONTROL_MODE_0** (line 54)
- **SPI_CONTROL_MODE_1** (line 55)
- **SPI_CONTROL_MODE_2** (line 56)
- **SPI_CONTROL_MODE_3** (line 57)
- **SPI_CONTROL_MODE_MASK** (line 58)
- **SPI_CS_INACTIVE** (line 111)
- **SPI_CS_POL_INACTIVE**(n) (line 45)
- **SPI_CS_POL_INACTIVE_MASK** (line 46)
- **SPI_CS_SEL**(x) (line 53)
- **SPI_CS_SEL_0** (line 48)
- **SPI_CS_SEL_1** (line 49)
- **SPI_CS_SEL_2** (line 50)
- **SPI_CS_SEL_3** (line 51)
- **SPI_CS_SEL_MASK** (line 52)
- **SPI_CS_SETUP_HOLD**(reg,cs,val) (line 69)
- **SPI_CS_SW_HW** (line 42)
- **SPI_CS_SW_VAL** (line 41)
- **SPI_CS_TIMING1** (line 67)
- **SPI_CS_TIMING2** (line 73)
- **SPI_DEFAULT_SPEED** (line 154)
- **SPI_DMA** (line 134)
- **SPI_DMA_BLK** (line 137)
- **SPI_DMA_BLK_SET**(x) (line 138)
- **SPI_DMA_CTL** (line 120)
- **SPI_DMA_EN** (line 135)
- **SPI_DMA_TIMEOUT** (line 149)
- **SPI_ERR** (line 105)
- **SPI_FIFO_DEPTH** (line 145)
- **SPI_FIFO_EMPTY** (line 115)
- **SPI_FIFO_ERROR** (line 113)
- **SPI_FIFO_STATUS** (line 96)
- **SPI_FRAME_END** (line 110)
- **SPI_IDLE_SDA_DRIVE_HIGH** (line 37)
- **SPI_IDLE_SDA_DRIVE_LOW** (line 36)
- **SPI_IDLE_SDA_MASK** (line 40)
- **SPI_IDLE_SDA_PULL_HIGH** (line 39)
- **SPI_IDLE_SDA_PULL_LOW** (line 38)
- **SPI_IE_RX** (line 132)
- **SPI_IE_TX** (line 131)
- **SPI_INTR_ALL_MASK** (line 143)
- **SPI_INTR_MASK** (line 142)
- **SPI_LSBIT_FE** (line 34)
- **SPI_LSBYTE_FE** (line 33)
- **SPI_MODE_SEL**(x) (line 59)
- **SPI_M_S** (line 60)
- **SPI_PACKED** (line 28)
- **SPI_PIO** (line 61)
- **SPI_RDY** (line 94)
- **SPI_RX_DATA** (line 118)
- **SPI_RX_EN** (line 30)
- **SPI_RX_FIFO** (line 141)
- **SPI_RX_FIFO_EMPTY** (line 97)
- **SPI_RX_FIFO_FLUSH** (line 107)
- **SPI_RX_FIFO_FULL** (line 98)
- **SPI_RX_FIFO_FULL_COUNT**(val) (line 109)
- **SPI_RX_FIFO_OVF** (line 102)
- **SPI_RX_FIFO_UNF** (line 101)
- **SPI_RX_TAP_DELAY**(x) (line 65)
- **SPI_RX_TRIG_1** (line 126)
- **SPI_RX_TRIG_16** (line 129)
- **SPI_RX_TRIG_4** (line 127)
- **SPI_RX_TRIG_8** (line 128)
- **SPI_RX_TRIG_MASK** (line 130)
- **SPI_SETUP_HOLD**(setup,hold) (line 68)
- **SPI_SET_CS_ACTIVE_BETWEEN_PACKETS**(reg,cs,val) (line 82)
- **SPI_SET_CYCLES_BETWEEN_PACKETS**(reg,cs,val) (line 85)
- **SPI_SLV_IDLE_COUNT**(val) (line 93)
- **SPI_TRANS_STATUS** (line 91)
- **SPI_TX_DATA** (line 117)
- **SPI_TX_EN** (line 29)
- **SPI_TX_FIFO** (line 140)
- **SPI_TX_FIFO_EMPTY** (line 99)
- **SPI_TX_FIFO_EMPTY_COUNT**(val) (line 108)
- **SPI_TX_FIFO_FLUSH** (line 106)
- **SPI_TX_FIFO_FULL** (line 100)
- **SPI_TX_FIFO_OVF** (line 104)
- **SPI_TX_FIFO_UNF** (line 103)
- **SPI_TX_TAP_DELAY**(x) (line 64)
- **SPI_TX_TRIG_1** (line 121)
- **SPI_TX_TRIG_16** (line 124)
- **SPI_TX_TRIG_4** (line 122)
- **SPI_TX_TRIG_8** (line 123)
- **SPI_TX_TRIG_MASK** (line 125)
- **TX_FIFO_EMPTY_COUNT_MAX** (line 151)
