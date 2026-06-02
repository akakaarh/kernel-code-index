# drivers/spi/spi-tegra210-quad.c

Subsystem: drivers/spi

## Functions (45)

### handle_cpu_based_xfer
- Return type: static irqreturn_t
- Signature: handle_cpu_based_xfer(struct tegra_qspi * tqspi)
- Line: 1454

### handle_dma_based_xfer
- Return type: static irqreturn_t
- Signature: handle_dma_based_xfer(struct tegra_qspi * tqspi)
- Line: 1494

### tegra_qspi_addr_config
- Return type: static u32
- Signature: tegra_qspi_addr_config(bool is_ddr,u8 bus_width,u8 len)
- Line: 1113

### tegra_qspi_calculate_curr_xfer_param
- Return type: static unsigned int
- Signature: tegra_qspi_calculate_curr_xfer_param(struct tegra_qspi * tqspi,struct spi_transfer * t)
- Line: 276

### tegra_qspi_cmd_config
- Return type: static u32
- Signature: tegra_qspi_cmd_config(bool is_ddr,u8 bus_width,u8 len)
- Line: 1097

### tegra_qspi_combined_seq_xfer
- Return type: static int
- Signature: tegra_qspi_combined_seq_xfer(struct tegra_qspi * tqspi,struct spi_message * msg)
- Line: 1152

### tegra_qspi_copy_client_txbuf_to_qspi_txbuf
- Return type: static void
- Signature: tegra_qspi_copy_client_txbuf_to_qspi_txbuf(struct tegra_qspi * tqspi,struct spi_transfer * t)
- Line: 408

### tegra_qspi_copy_qspi_rxbuf_to_client_rxbuf
- Return type: static void
- Signature: tegra_qspi_copy_qspi_rxbuf_to_client_rxbuf(struct tegra_qspi * tqspi,struct spi_transfer * t)
- Line: 445

### tegra_qspi_deinit_dma
- Return type: static void
- Signature: tegra_qspi_deinit_dma(struct tegra_qspi * tqspi)
- Line: 745

### tegra_qspi_dma_complete
- Return type: static void
- Signature: tegra_qspi_dma_complete(void * args)
- Line: 474

### tegra_qspi_dma_map_xfer
- Return type: static int
- Signature: tegra_qspi_dma_map_xfer(struct tegra_qspi * tqspi,struct spi_transfer * t)
- Line: 568

### tegra_qspi_dma_stop
- Return type: static void
- Signature: tegra_qspi_dma_stop(struct tegra_qspi * tqspi)
- Line: 1128

### tegra_qspi_dma_unmap_xfer
- Return type: static void
- Signature: tegra_qspi_dma_unmap_xfer(struct tegra_qspi * tqspi,struct spi_transfer * t)
- Line: 593

### tegra_qspi_dump_regs
- Return type: static void
- Signature: tegra_qspi_dump_regs(struct tegra_qspi * tqspi)
- Line: 1008

### tegra_qspi_fill_tx_fifo_from_client_txbuf
- Return type: static unsigned int
- Signature: tegra_qspi_fill_tx_fifo_from_client_txbuf(struct tegra_qspi * tqspi,struct spi_transfer * t)
- Line: 315

### tegra_qspi_flush_fifos
- Return type: static int
- Signature: tegra_qspi_flush_fifos(struct tegra_qspi * tqspi,bool atomic)
- Line: 537

### tegra_qspi_handle_error
- Return type: static void
- Signature: tegra_qspi_handle_error(struct tegra_qspi * tqspi)
- Line: 1033

### tegra_qspi_handle_timeout
- Return type: static int
- Signature: tegra_qspi_handle_timeout(struct tegra_qspi * tqspi)
- Line: 1067

### tegra_qspi_init_dma
- Return type: static int
- Signature: tegra_qspi_init_dma(struct tegra_qspi * tqspi)
- Line: 770

### tegra_qspi_isr_thread
- Return type: static irqreturn_t
- Signature: tegra_qspi_isr_thread(int irq,void * context_data)
- Line: 1577

### tegra_qspi_mask_clear_irq
- Return type: static void
- Signature: tegra_qspi_mask_clear_irq(struct tegra_qspi * tqspi)
- Line: 255

### tegra_qspi_non_combined_seq_xfer
- Return type: static int
- Signature: tegra_qspi_non_combined_seq_xfer(struct tegra_qspi * tqspi,struct spi_message * msg)
- Line: 1285

### tegra_qspi_parse_cdata_dt
- Return type: static tegra_qspi_client_data *
- Signature: tegra_qspi_parse_cdata_dt(struct spi_device * spi)
- Line: 953

### tegra_qspi_pio_stop
- Return type: static void
- Signature: tegra_qspi_pio_stop(struct tegra_qspi * tqspi)
- Line: 1143

### tegra_qspi_probe
- Return type: static int
- Signature: tegra_qspi_probe(struct platform_device * pdev)
- Line: 1702

### tegra_qspi_read_rx_fifo_to_client_rxbuf
- Return type: static unsigned int
- Signature: tegra_qspi_read_rx_fifo_to_client_rxbuf(struct tegra_qspi * tqspi,struct spi_transfer * t)
- Line: 364

### tegra_qspi_readl
- Return type: static u32
- Signature: tegra_qspi_readl(struct tegra_qspi * tqspi,unsigned long offset)
- Line: 241

### tegra_qspi_remove
- Return type: static void
- Signature: tegra_qspi_remove(struct platform_device * pdev)
- Line: 1821

### tegra_qspi_reset
- Return type: static void
- Signature: tegra_qspi_reset(struct tegra_qspi * tqspi)
- Line: 1025

### tegra_qspi_resume
- Return type: static int __maybe_unused
- Signature: tegra_qspi_resume(struct device * dev)
- Line: 1840

### tegra_qspi_runtime_resume
- Return type: static int __maybe_unused
- Signature: tegra_qspi_runtime_resume(struct device * dev)
- Line: 1875

### tegra_qspi_runtime_suspend
- Return type: static int __maybe_unused
- Signature: tegra_qspi_runtime_suspend(struct device * dev)
- Line: 1859

### tegra_qspi_setup
- Return type: static int
- Signature: tegra_qspi_setup(struct spi_device * spi)
- Line: 970

### tegra_qspi_setup_transfer_one
- Return type: static u32
- Signature: tegra_qspi_setup_transfer_one(struct spi_device * spi,struct spi_transfer * t,bool is_first_of_msg)
- Line: 834

### tegra_qspi_start_cpu_based_transfer
- Return type: static int
- Signature: tegra_qspi_start_cpu_based_transfer(struct tegra_qspi * qspi,struct spi_transfer * t)
- Line: 722

### tegra_qspi_start_dma_based_transfer
- Return type: static int
- Signature: tegra_qspi_start_dma_based_transfer(struct tegra_qspi * tqspi,struct spi_transfer * t)
- Line: 605

### tegra_qspi_start_rx_dma
- Return type: static int
- Signature: tegra_qspi_start_rx_dma(struct tegra_qspi * tqspi,struct spi_transfer * t,int len)
- Line: 509

### tegra_qspi_start_transfer_one
- Return type: static int
- Signature: tegra_qspi_start_transfer_one(struct spi_device * spi,struct spi_transfer * t,u32 command1)
- Line: 898

### tegra_qspi_start_tx_dma
- Return type: static int
- Signature: tegra_qspi_start_tx_dma(struct tegra_qspi * tqspi,struct spi_transfer * t,int len)
- Line: 481

### tegra_qspi_suspend
- Return type: static int __maybe_unused
- Signature: tegra_qspi_suspend(struct device * dev)
- Line: 1833

### tegra_qspi_transfer_end
- Return type: static void
- Signature: tegra_qspi_transfer_end(struct spi_device * spi)
- Line: 1041

### tegra_qspi_transfer_one_message
- Return type: static int
- Signature: tegra_qspi_transfer_one_message(struct spi_controller * host,struct spi_message * msg)
- Line: 1438

### tegra_qspi_unmask_irq
- Return type: static void
- Signature: tegra_qspi_unmask_irq(struct tegra_qspi * tqspi)
- Line: 559

### tegra_qspi_validate_cmb_seq
- Return type: static bool
- Signature: tegra_qspi_validate_cmb_seq(struct tegra_qspi * tqspi,struct spi_message * msg)
- Line: 1404

### tegra_qspi_writel
- Return type: static void
- Signature: tegra_qspi_writel(struct tegra_qspi * tqspi,u32 value,unsigned long offset)
- Line: 246

## Structs (3)

### tegra_qspi
- Line: 184
- Members:
  - cmb_xfer_capable: bool
  - supports_tpm: bool
  - has_ext_dma: bool
  - cs_count: unsigned int
  - tx_clk_tap_delay: int
  - rx_clk_tap_delay: int
  - dev: device *
  - host: spi_controller *
  - lock: spinlock_t
  - clk: clk *
  - base: void __iomem *
  - phys: phys_addr_t
  - irq: unsigned int
  - cur_speed: u32
  - cur_pos: unsigned int
  - words_per_32bit: unsigned int
  - bytes_per_word: unsigned int
  - curr_dma_words: unsigned int
  - cur_direction: unsigned int
  - cur_rx_pos: unsigned int
  - cur_tx_pos: unsigned int
  - dma_buf_size: unsigned int
  - max_buf_size: unsigned int
  - is_curr_dma_xfer: bool
  - rx_dma_complete: completion
  - tx_dma_complete: completion
  - tx_status: u32
  - rx_status: u32
  - status_reg: u32
  - is_packed: bool
  - use_dma: bool
  - command1_reg: u32
  - dma_control_reg: u32
  - def_command1_reg: u32
  - def_command2_reg: u32
  - spi_cs_timing1: u32
  - spi_cs_timing2: u32
  - dummy_cycles: u8
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
  - soc_data: const struct tegra_qspi_soc_data *

### tegra_qspi_client_data
- Line: 179
- Members:
  - cmb_xfer_capable: bool
  - supports_tpm: bool
  - has_ext_dma: bool
  - cs_count: unsigned int
  - tx_clk_tap_delay: int
  - rx_clk_tap_delay: int
  - dev: device *
  - host: spi_controller *
  - lock: spinlock_t
  - clk: clk *
  - base: void __iomem *
  - phys: phys_addr_t
  - irq: unsigned int
  - cur_speed: u32
  - cur_pos: unsigned int
  - words_per_32bit: unsigned int
  - bytes_per_word: unsigned int
  - curr_dma_words: unsigned int
  - cur_direction: unsigned int
  - cur_rx_pos: unsigned int
  - cur_tx_pos: unsigned int
  - dma_buf_size: unsigned int
  - max_buf_size: unsigned int
  - is_curr_dma_xfer: bool
  - rx_dma_complete: completion
  - tx_dma_complete: completion
  - tx_status: u32
  - rx_status: u32
  - status_reg: u32
  - is_packed: bool
  - use_dma: bool
  - command1_reg: u32
  - dma_control_reg: u32
  - def_command1_reg: u32
  - def_command2_reg: u32
  - spi_cs_timing1: u32
  - spi_cs_timing2: u32
  - dummy_cycles: u8
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
  - soc_data: const struct tegra_qspi_soc_data *

### tegra_qspi_soc_data
- Line: 172
- Members:
  - cmb_xfer_capable: bool
  - supports_tpm: bool
  - has_ext_dma: bool
  - cs_count: unsigned int
  - tx_clk_tap_delay: int
  - rx_clk_tap_delay: int
  - dev: device *
  - host: spi_controller *
  - lock: spinlock_t
  - clk: clk *
  - base: void __iomem *
  - phys: phys_addr_t
  - irq: unsigned int
  - cur_speed: u32
  - cur_pos: unsigned int
  - words_per_32bit: unsigned int
  - bytes_per_word: unsigned int
  - curr_dma_words: unsigned int
  - cur_direction: unsigned int
  - cur_rx_pos: unsigned int
  - cur_tx_pos: unsigned int
  - dma_buf_size: unsigned int
  - max_buf_size: unsigned int
  - is_curr_dma_xfer: bool
  - rx_dma_complete: completion
  - tx_dma_complete: completion
  - tx_status: u32
  - rx_status: u32
  - status_reg: u32
  - is_packed: bool
  - use_dma: bool
  - command1_reg: u32
  - dma_control_reg: u32
  - def_command1_reg: u32
  - def_command2_reg: u32
  - spi_cs_timing1: u32
  - spi_cs_timing2: u32
  - dummy_cycles: u8
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
  - soc_data: const struct tegra_qspi_soc_data *

## Enums (1)

### tegra_qspi_transfer_type
- Line: 165

## Variables (8)

- static **tegra186_qspi_soc_data** : tegra_qspi_soc_data (line 1638)
- static **tegra210_qspi_soc_data** : tegra_qspi_soc_data (line 1631)
- static **tegra234_qspi_soc_data** : tegra_qspi_soc_data (line 1645)
- static **tegra241_qspi_soc_data** : tegra_qspi_soc_data (line 1652)
- static **tegra_qspi_acpi_match** : const struct acpi_device_id[] (line 1682)
- static **tegra_qspi_driver** : platform_driver (line 1896)
- static **tegra_qspi_of_match** : const struct of_device_id[] (line 1659)
- static **tegra_qspi_pm_ops** : const struct dev_pm_ops (line 1891)

## Macros (105)

- **CS_ACTIVE_BETWEEN_PACKETS_0** (line 65)
- **CYCLES_BETWEEN_PACKETS_0**(x) (line 64)
- **DATA_DIR_RX** (line 160)
- **DATA_DIR_TX** (line 159)
- **DEFAULT_QSPI_DMA_BUF_LEN** (line 163)
- **QSPI_ADDRESS_SDR_DDR** (line 156)
- **QSPI_ADDRESS_SIZE_SET**(x) (line 157)
- **QSPI_ADDRESS_VALUE_SET**(X) (line 151)
- **QSPI_ADDRESS_X1_X2_X4**(x) (line 154)
- **QSPI_ADDRESS_X1_X2_X4_MASK** (line 155)
- **QSPI_BIT_LENGTH**(x) (line 28)
- **QSPI_BLK_CNT**(val) (line 68)
- **QSPI_CMB_SEQ_ADDR** (line 150)
- **QSPI_CMB_SEQ_ADDR_CFG** (line 153)
- **QSPI_CMB_SEQ_CMD** (line 137)
- **QSPI_CMB_SEQ_CMD_CFG** (line 140)
- **QSPI_CMB_SEQ_EN** (line 147)
- **QSPI_COMMAND1** (line 27)
- **QSPI_COMMAND2** (line 56)
- **QSPI_COMMAND_SDR_DDR** (line 143)
- **QSPI_COMMAND_SIZE_SET**(x) (line 144)
- **QSPI_COMMAND_VALUE_SET**(X) (line 138)
- **QSPI_COMMAND_X1_X2_X4**(x) (line 141)
- **QSPI_COMMAND_X1_X2_X4_MASK** (line 142)
- **QSPI_CONTROL_MODE_0** (line 50)
- **QSPI_CONTROL_MODE_3** (line 51)
- **QSPI_CONTROL_MODE_MASK** (line 52)
- **QSPI_CS_POL_INACTIVE**(n) (line 41)
- **QSPI_CS_POL_INACTIVE_MASK** (line 42)
- **QSPI_CS_SEL**(x) (line 48)
- **QSPI_CS_SEL_0** (line 43)
- **QSPI_CS_SEL_1** (line 44)
- **QSPI_CS_SEL_2** (line 45)
- **QSPI_CS_SEL_3** (line 46)
- **QSPI_CS_SEL_MASK** (line 47)
- **QSPI_CS_SW_HW** (line 39)
- **QSPI_CS_SW_VAL** (line 38)
- **QSPI_CS_TIMING1** (line 60)
- **QSPI_CS_TIMING2** (line 63)
- **QSPI_DMA_BLK** (line 111)
- **QSPI_DMA_BLK_SET**(x) (line 112)
- **QSPI_DMA_CTL** (line 96)
- **QSPI_DMA_EN** (line 109)
- **QSPI_DMA_HI_ADDRESS** (line 115)
- **QSPI_DMA_MEM_ADDRESS** (line 114)
- **QSPI_DMA_TIMEOUT** (line 162)
- **QSPI_DUMMY_CYCLES_MAX** (line 135)
- **QSPI_ERR** (line 80)
- **QSPI_FIFO_DEPTH** (line 120)
- **QSPI_FIFO_EMPTY** (line 90)
- **QSPI_FIFO_ERROR** (line 86)
- **QSPI_FIFO_STATUS** (line 71)
- **QSPI_GLOBAL_CONFIG** (line 146)
- **QSPI_INTERFACE_WIDTH**(x) (line 31)
- **QSPI_INTERFACE_WIDTH_DUAL** (line 33)
- **QSPI_INTERFACE_WIDTH_MASK** (line 30)
- **QSPI_INTERFACE_WIDTH_QUAD** (line 34)
- **QSPI_INTERFACE_WIDTH_SINGLE** (line 32)
- **QSPI_INTR_MASK** (line 122)
- **QSPI_INTR_RDY_MASK** (line 127)
- **QSPI_INTR_RX_FIFO_OVF_MASK** (line 124)
- **QSPI_INTR_RX_FIFO_UNF_MASK** (line 123)
- **QSPI_INTR_RX_TX_FIFO_ERR** (line 128)
- **QSPI_INTR_TX_FIFO_OVF_MASK** (line 126)
- **QSPI_INTR_TX_FIFO_UNF_MASK** (line 125)
- **QSPI_MISC_REG** (line 133)
- **QSPI_M_S** (line 53)
- **QSPI_NUM_DUMMY_CYCLE**(x) (line 134)
- **QSPI_PACKED** (line 29)
- **QSPI_PIO** (line 54)
- **QSPI_RDY** (line 69)
- **QSPI_RX_DATA** (line 94)
- **QSPI_RX_EN** (line 37)
- **QSPI_RX_FIFO** (line 118)
- **QSPI_RX_FIFO_EMPTY** (line 72)
- **QSPI_RX_FIFO_FLUSH** (line 82)
- **QSPI_RX_FIFO_FULL** (line 73)
- **QSPI_RX_FIFO_FULL_COUNT**(val) (line 84)
- **QSPI_RX_FIFO_OVF** (line 77)
- **QSPI_RX_FIFO_UNF** (line 76)
- **QSPI_RX_TAP_DELAY**(x) (line 58)
- **QSPI_RX_TRIG**(n) (line 103)
- **QSPI_RX_TRIG_1** (line 104)
- **QSPI_RX_TRIG_16** (line 107)
- **QSPI_RX_TRIG_4** (line 105)
- **QSPI_RX_TRIG_8** (line 106)
- **QSPI_SDR_DDR_SEL** (line 35)
- **QSPI_SETUP_HOLD**(setup,hold) (line 61)
- **QSPI_TPM_WAIT_POLL_EN** (line 148)
- **QSPI_TRANS_STATUS** (line 67)
- **QSPI_TX_DATA** (line 93)
- **QSPI_TX_EN** (line 36)
- **QSPI_TX_FIFO** (line 117)
- **QSPI_TX_FIFO_EMPTY** (line 74)
- **QSPI_TX_FIFO_EMPTY_COUNT**(val) (line 83)
- **QSPI_TX_FIFO_FLUSH** (line 81)
- **QSPI_TX_FIFO_FULL** (line 75)
- **QSPI_TX_FIFO_OVF** (line 79)
- **QSPI_TX_FIFO_UNF** (line 78)
- **QSPI_TX_TAP_DELAY**(x) (line 57)
- **QSPI_TX_TRIG**(n) (line 97)
- **QSPI_TX_TRIG_1** (line 98)
- **QSPI_TX_TRIG_16** (line 101)
- **QSPI_TX_TRIG_4** (line 99)
- **QSPI_TX_TRIG_8** (line 100)
